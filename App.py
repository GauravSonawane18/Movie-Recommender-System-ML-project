import streamlit as st
import pickle
import requests

# Style sheet for Streamlit UI
st.markdown(
    """
    <style>
    .block-container {
        max-width: 90%; /* Adjust width */
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Load both pickle files
movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list = movies['title'].values

# Streamlit UI
st.header("🎬 Movie Recommender System")
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

# Fallback poster if no image found
FALLBACK_POSTER = "https://via.placeholder.com/500x750.png?text=No+Image"

def fetch_movie_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=1d3ee1c379b02e85c4d4c7b772e1a1d0&language=en-US"
    try:
        response = requests.get(url)
        data = response.json()
    
        # Check if the poster path exists
        if 'poster_path' in data and data['poster_path']:
            return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
        else:
            return FALLBACK_POSTER
    except:
        return FALLBACK_POSTER

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    recommend_movie=[]
    recommend_poster = []
    
    for i in distance[1:6]:
        movie_id=movies.iloc[i[0]]['id']
        recommend_movie.append(movies.iloc[i[0]]['title'])
        recommend_poster.append(fetch_movie_poster(movie_id))
    return recommend_movie, recommend_poster

# Display recommendations
if st.button("Show Recommendation"):
    recommend_movie, recommend_poster = recommend(selectvalue)

    cols = st.columns(5)
    for col, title, poster in zip(cols, recommend_movie, recommend_poster):
        with col:
            st.text(title)
            st.image(poster, width=250)

    # # Either For loop or This one by one
    # with col1:
    #     st.text(recommend_movie[0])
    #     st.image(recommend_poster[0], width=250)
    # with col2:
    #     st.text(recommend_movie[1])
    #     st.image(recommend_poster[1],  width=250)
    # with col3:
    #     st.text(recommend_movie[2])
    #     st.image(recommend_poster[2], width=250)
    # with col4:
    #     st.text(recommend_movie[3])
    #     st.image(recommend_poster[3], width=250)
    # with col5:
    #     st.text(recommend_movie[4])
    #     st.image(recommend_poster[4], width=250)

