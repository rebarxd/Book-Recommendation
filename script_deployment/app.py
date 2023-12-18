from flask import Flask, request, jsonify
import pickle
import numpy as np

popular_df = pickle.load(open('model/popular.pkl', 'rb'))
pt = pickle.load(open('model/pt.pkl', 'rb'))
books = pickle.load(open('model/books.pkl', 'rb'))
similarity_scores = pickle.load(open('model/similarity_scores.pkl', 'rb'))

app = Flask(__name__)

def convert_to_python_types(data):
    if isinstance(data, np.int64):
        return int(data)
    elif isinstance(data, np.generic):
        return data.item()
    elif isinstance(data, list):
        return [convert_to_python_types(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_to_python_types(value) for key, value in data.items()}
    else:
        return data

@app.route('/')
def index():
    return jsonify({
        "book_name": convert_to_python_types(list(popular_df['Book-Title'].values)),
        "author": convert_to_python_types(list(popular_df['Book-Author'].values)),
        "votes": convert_to_python_types(list(popular_df['num_ratings'].values)),
        "rating": convert_to_python_types(list(popular_df['avg_rating'].values))
    })

@app.route('/recommend_books', methods=['GET'])
def recommend():
    user_input = request.args.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = {}
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item["book_title"] = convert_to_python_types(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item["author"] = convert_to_python_types(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))

        data.append(item)

    return jsonify({"data": convert_to_python_types(data)})


if __name__ == '__main__':
    app.run()
