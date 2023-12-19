from flask import Flask, request
from library import recommend_library
from book import get_popular_books,recommend_books

app = Flask(__name__)

@app.route('/')
def index():
    return get_popular_books()

@app.route('/recommend_books', methods=['GET'])
def recommend():
    user_input = request.args.get('user_input')
    return recommend_books(user_input)

@app.route('/library_recommendation', methods=['GET'])
def place_recommendation(latitude: float = -6.877568754589162, longitude: float = 107.61681917116401):
    return recommend_library(latitude, longitude)

if __name__ == '__main__':
    app.run()
