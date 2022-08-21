import streamlit as st
import pickle
import pandas as pd
import requests

def get_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=103765e8dd7ac4eb1ddf5f68cfb27b88&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in distances:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(get_poster(movie_id))

    return recommended_movies, recommended_movies_poster


similarity = pickle.load(open('similarity.pkl', 'rb'))

# st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender system')
#List of Movies
selectedMovie = st.selectbox(
    'Select your favourite movie',
    (movies['title'].values))

#Button
if st.button('Recommend Movie'):
    names,poster = recommend(selectedMovie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])
