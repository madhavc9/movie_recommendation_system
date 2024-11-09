import streamlit as st
import pickle
import pandas as pd
import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4Njg5M2Y4ZDI5MDQ4MzAzZTEwMmYyZDJmNzFjODljYyIsInN1YiI6IjY0YTk0ZThjYjY4NmI5MDBlZGY4ZTI0OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hyyMVyPgfuEsCrP5SE6VrjLP4hR53SKxA2b28Ok9goU"
}
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
    data = requests.get(url, headers=headers)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    # full_path = "https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg"
    return full_path 

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    # recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        # recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.set_page_config(layout='wide')

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown?',
    movies['title'].values
)
if st.button('Recommend'):
    names = recommend(selected_movie_name)
    posters = [
        "https://t3.ftcdn.net/jpg/04/38/03/50/360_F_438035062_bxhey1N5fbRvjgPY0O7SqOnq3VzlrrSJ.jpg",
        "https://img.freepik.com/premium-photo/dark-blue-navy-color-scheme-photo-background-picture-day-background_136558-4027.jpg",
        "https://img.freepik.com/free-photo/green-gradient-abstract-background-empty-room-with-space-your-text-picture_1258-54428.jpg?size=626&ext=jpg&ga=GA1.1.1224184972.1714694400&semt=ais",
        "https://img.freepik.com/free-photo/orange-background_23-2147674307.jpg",
        "https://media.istockphoto.com/id/540533738/photo/blue-background.jpg?s=612x612&w=0&k=20&c=X3doabKNqbK6hBhq7vq5c8zQOYwycVFubOkxZC9NMoc="
    ]
    col1,col2,col3 = st.columns(3)

    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    
    col4, col5 = st.columns(2)
    
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])