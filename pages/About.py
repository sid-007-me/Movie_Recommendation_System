import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("""
## 🎬 Movie Recommendation System

This project recommends movies based on their similarity using a content-based recommendation approach.

### ✨ Features

- Recommend similar movies
- Movie posters
- IMDb ratings
- Release year
- Genre
- Movie overview

### 🛠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- CountVectorizer
- Cosine Similarity
- OMDb API

### 📂 Dataset

TMDB 5000 Movie Dataset

---

This project was developed as a portfolio project for learning Machine Learning and Streamlit.
""")