from flask import Flask, render_template, request, jsonify  # Import jsonify
import pickle
import numpy as np

popular_df = pickle.load(open('./data/popular.pkl','rb'))
pt = pickle.load(open('./data/pt.pkl','rb'))
books = pickle.load(open('./data/books.pkl','rb'))
similarity_scores = pickle.load(open('./data/similarity_scores.pkl','rb'))

# Your existing code...
app = Flask(__name__)
@app.route('/recommend_books_json', methods=['POST'])  # Change route name
def recommend_json():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = {}
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item['title'] = temp_df['Book-Title'].values[0]
        item['author'] = temp_df['Book-Author'].values[0]
        item['image_url'] = temp_df['Image-URL-S'].values[0]

        data.append(item)

    return jsonify(data)  # Return JSON response

# Your existing code...

if __name__ == '__main__':
    app.run(debug=True)
