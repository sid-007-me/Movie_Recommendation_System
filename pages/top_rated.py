import streamlit as st
import requests

st.set_page_config(
    page_title="Top Rated Movies",
    page_icon="🏆",
    layout="wide"
)

API_KEY = st.secrets["OMDB_API_KEY"]

st.title("🏆 Top Rated Movies")

movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "The Lord of the Rings: The Return of the King",
    "Forrest Gump",
    "Fight Club",
    "Inception",
    "Interstellar",
    "The Matrix",
    "Parasite"
]

def fetch_movie(movie):
    url = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
    return requests.get(url).json()

cols = st.columns(5)

for i, movie in enumerate(movies):

    data = fetch_movie(movie)

    with cols[i % 5]:

        if data.get("Poster") != "N/A":
            st.image(data["Poster"], use_container_width=True)

        st.markdown(f"**{movie}**")
        st.write(f"⭐ {data.get('imdbRating')}")
        st.write(f"📅 {data.get('Year')}")