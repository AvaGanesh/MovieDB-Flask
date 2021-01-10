from flask import Flask, render_template 
import requests


baseUrl = 'https://api.themoviedb.org/3'
imageBaseUrl = 'https://image.tmdb.org/t/p/w138_and_h175_face/'
v4key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTg0ZjU2YjgwMTZhYmI4ZmYxYmI5YmVjMTNjYjkxZSIsInN1YiI6IjVmYmY2Y2FmMjcxY2E1MDA0MTU2MTliZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VDkK3bjOM2F-C7vIElqleildA7cM2Llqfke9NKYiTRs'
v3key ='1984f56b8016abb8ff1bb9bec13cb91e'
endpoint = '1984f56b8016abb8ff1bb9bec13cb91e&language=en-US&page=';
coverImage = 'https://image.tmdb.org/t/p/w1920_and_h800_multi_faces/'


app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html') # Return index.html 


@app.route('/movie/genres/')
def get_movie_genres():
    receive = requests.get(baseUrl + '/genre/movie/list?api_key=' + v3key);
    return receive.json();

@app.route('/movie/popular/<page_no>')
def get_popular_movies(page_no):
    receive = requests.get(baseUrl + '/movie/popular?api_key='+ endpoint + page_no);
    return receive.json();

@app.route('/movie/top-rated/<page_no>')
def get_top_rated_movie(page_no): 
    recieve = requests.get(baseUrl + '/movie/top_rated?api_key='+ endpoint + page_no);
    return recieve.json();


@app.route('/movie/upcoming/<page_no>') 
def get_upcoming_movies(page_no):
    receive = requests.get(baseUrl+ '/movie/upcoming/?api_key=' + endpoint + page_no);
    return receive.json();


@app.route('/tv/popular-tv/<page_no>')
def get_popular_tv(page_no):
    receive = requests.get(baseUrl + '/tv/top_rated?api_key=' + endpoint + page_no);
    return receive.json();

@app.route('/tv/top-rated/<page_no>')
def get_top_rated_tv(page_no):
    receive = requests.get(baseUrl + '/tv/top_rated?api_key=' + endpoint + page_no);
    return receive.json();

@app.route('/tv/latest-tv/<page_no>')
def get_latest_tv(page_no):
    receive = requests.get(baseUrl + '/tv/latest?api_key=' + endpoint + page_no);
    return receive.json();

@app.route('/movie/details/<movie_id>')
def get_movie_details(movie_id):
    receive = requests.get(baseUrl + '/movie/'+ movie_id + '?api_key='+ v3key + '&language=en-US');
    return receive.json();


@app.route('/tv/details/<id>')
def get_tv_details(id):
    receive = requests.get(baseUrl + '/tv/' + id + '?api_key=' + v3key + '&language=en-US');
    return receive.json();

if __name__=="__main__":
    app.run()

