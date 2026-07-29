import streamlit as st
import requests

st.set_page_config(
    page_title="Popular Movies",
    page_icon="🔥",
    layout="wide"
)

API_KEY = st.secrets["OMDB_API_KEY"]

st.title("🔥 Popular Movies")

movies = [
    "Avengers: Endgame",
    "Avatar",
    "Titanic",
    "Spider-Man: No Way Home",
    "Joker",
    "Barbie",
    "Oppenheimer",
    "Dune",
    "Deadpool",
    "Mission: Impossible - Fallout"
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