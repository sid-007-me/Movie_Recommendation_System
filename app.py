import streamlit as st
import pickle
import requests
import random
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


# --------------------------------------------------
# API Key
# --------------------------------------------------
API_KEY = st.secrets["OMDB_API_KEY"]

# --------------------------------------------------
# Load Data
# --------------------------------------------------
movies = pickle.load(open("movie_dict.pkl", "rb"))
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pickle.load(open("movie_dict.pkl", "rb"))

cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(movies["tags"]).toarray()

similarity = cosine_similarity(vectors)

with st.sidebar:
    st.image("Assets/banner.jpeg", width=120)

    #st.title("🎬 Movie Recommender")

    st.success("Machine Learning Project")

    st.divider()

    st.markdown("### 📊 Project Information")
    st.write(f"🎥 Movies: {len(movies)}")
    st.write("🤖 Algorithm: Content-Based Filtering")
    st.write("📚 Dataset: TMDB 5000")
    st.write("⚙️ Built with Streamlit")

    st.divider()

    st.markdown("### 👨‍💻 Developer")
    st.write("**Siddhant Singh**")

    st.divider()

    st.caption("Version 1.0")

#banner
with st.sidebar:
    st.image("Assets/banner.jpeg", width=120)
    st.title("🎬 Movie Recommender")

# --------------------------------------------------
# Recommendation Function
# --------------------------------------------------
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# --------------------------------------------------
# Fetch Movie Details
# --------------------------------------------------
def fetch_movie_details(movie_name):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    return {
        "poster": data.get("Poster"),
        "rating": data.get("imdbRating"),
        "year": data.get("Year"),
        "genre": data.get("Genre"),
        "plot": data.get("Plot")
    }


# --------------------------------------------------
# Hero Section
# --------------------------------------------------
st.markdown("""
<div style="text-align:center;padding:25px;">

<h1 style="color:#E50914;font-size:55px;">
🎬 Movie Recommendation System
</h1>

<h3 style="color:white;">
Discover your next favorite movie 🍿
</h3>

<p style="font-size:18px;color:#CFCFCF;">
Get personalized movie recommendations based on content similarity.
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Statistics
# --------------------------------------------------
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎥 Movies", len(movies))

with col2:
    st.metric("🤖 Algorithm", "Content-Based")

with col3:
    st.metric("⭐ Recommendations", "Top 5")

st.divider()

# --------------------------------------------------
# Welcome
# --------------------------------------------------
st.info("""
### 👋 Welcome!

Select your favorite movie below and click **Get Recommendations**.

The recommendation engine analyzes:

- 🎭 Genre
- 🎬 Cast
- 🎥 Director
- 🔑 Keywords
- 📝 Overview
""")

# --------------------------------------------------
# Featured Movie
# --------------------------------------------------
st.subheader("🌟 Featured Movie")

featured_movie = random.choice(movies["title"].values)
featured = fetch_movie_details(featured_movie)

col1, col2 = st.columns([1, 2])

with col1:
    if featured["poster"] and featured["poster"] != "N/A":
        st.image(featured["poster"], use_container_width=True)

with col2:
    st.markdown(f"## {featured_movie}")
    st.write(f"⭐ IMDb: {featured['rating']}")
    st.write(f"📅 Year: {featured['year']}")
    st.write(f"🎭 Genre: {featured['genre']}")

    if featured["plot"] and featured["plot"] != "N/A":
        st.write(featured["plot"])

st.divider()

# --------------------------------------------------
# Movie Selection
# --------------------------------------------------
selected_movie = st.selectbox(
    "🔍 Search Movie",
    movies["title"].values,
    index=None,
    placeholder="Start typing a movie..."
)

# --------------------------------------------------
# Recommendation Button
# --------------------------------------------------
if st.button("🚀 Get Recommendations", use_container_width=True):

    if selected_movie is None:
        st.warning("Please select a movie first.")

    else:

        with st.spinner("Finding similar movies... 🍿"):

            recommendations = recommend(selected_movie)

            st.markdown("## 🎯 Recommended Movies")

            for movie in recommendations:

                details = fetch_movie_details(movie)

                col1, col2 = st.columns([1, 2])

                with col1:

                    if details["poster"] and details["poster"] != "N/A":
                        st.image(details["poster"], use_container_width=True)
                    else:
                        st.write("No Poster Available")

                with col2:

                    st.subheader(movie)

                    st.write(f"⭐ **IMDb:** {details['rating']}")
                    st.write(f"📅 **Year:** {details['year']}")
                    st.write(f"🎭 **Genre:** {details['genre']}")

                    if details["plot"] and details["plot"] != "N/A":
                        st.write(details["plot"])

                st.divider()

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:gray; padding:10px;'>
        Made with ❤️ by <b>Siddhant Singh</b><br>
        Movie Recommendation System | Streamlit | Scikit-learn
    </div>
    """,
    unsafe_allow_html=True
)                