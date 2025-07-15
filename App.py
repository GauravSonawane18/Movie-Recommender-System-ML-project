import streamlit as st
import pickle
# import requests

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")
selectvalue = st.selectbox("Select movie from dropdown", movies_list)


# def fetch_movie_poster(movie_id):
    # api_key = 'YOUR_TMDB_API_KEY'  # Replace with your TMDb API key
    # url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    # response = requests.get(url)
    # data = response.json()
    
    # Check if the poster path exists
    # if 'poster_path' in data and data['poster_path']:
    #     poster_url = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    #     return poster_url
    # else:
    #     return None


def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    # recommend_movie_ids = []
    for i in distance[1:7]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        # recommend_movie_ids.append(movies.iloc[i[0]].id)

        # posters = [fetch_movie_poster(movie_id) for movie_id in recommend_movie_ids]
    return recommend_movie


if st.button("Show Recommendation"):
    movie_name = recommend(selectvalue)
    c = st.container()
    with c:
        st.text(movie_name[0])
    with c:
        st.text(movie_name[1])
    with c:
        st.text(movie_name[2])
    with c:
        st.text(movie_name[3])
    with c:
        st.text(movie_name[4])
    with c:
        st.text(movie_name[5])


# if st.button("Show Recommendations"):
#     movie_names, movie_posters = recommend(selectvalue)
    
#     st.subheader("Recommended Movies:")
#     for name, poster in zip(movie_names, movie_posters):
#         col1, col2 = st.columns([1, 3])  # Create two columns
#         with col1:
#             if poster:
#                 st.image(poster, width=100)  # Display poster
#             else:
#                 st.image("default_poster.png", width=100)  # Placeholder for missing posters
#         with col2:
#             st.text(name)  # Display movie name