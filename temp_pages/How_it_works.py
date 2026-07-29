import streamlit as st

st.set_page_config(
    page_title="How It Works",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ How the Recommendation System Works")

st.markdown("""
## 📌 Content-Based Recommendation System

This project uses a **Content-Based Filtering** approach.

Instead of using user ratings, it recommends movies based on their content such as:

- 🎭 Genres
- 🎬 Cast
- 🎥 Director
- 🔑 Keywords
- 📝 Movie Overview

---

## 🔄 Workflow

### 1️⃣ Data Collection
The TMDB 5000 Movies Dataset is loaded and cleaned.

### 2️⃣ Feature Engineering
Important movie information is combined into a single **Tags** column.

Example:

Action Adventure TomCruise ChristopherMcQuarrie Mission Impossible Spy

### 3️⃣ Text Vectorization
The tags are converted into numerical vectors using **CountVectorizer**.

### 4️⃣ Similarity Calculation
Cosine Similarity is used to compare movies.

Movies with higher similarity scores are considered more alike.

### 5️⃣ Recommendation
When a user selects a movie:

- The similarity scores are calculated.
- The top 5 most similar movies are returned.
- Posters and movie details are fetched using the OMDb API.
""")

st.success("✅ Recommendation Technique: Content-Based Filtering")