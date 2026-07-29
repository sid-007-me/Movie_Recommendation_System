import streamlit as st

st.set_page_config(
    page_title="Feedback",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Feedback")

st.write("We'd love to hear your thoughts about this Movie Recommendation System!")

with st.form("feedback_form"):

    name = st.text_input("Your Name")

    rating = st.slider(
        "Rate this project",
        min_value=1,
        max_value=5,
        value=5
    )

    feedback = st.text_area(
        "Your Feedback"
    )

    submit = st.form_submit_button("Submit")

    if submit:
        st.success("🎉 Thank you for your feedback!")
        st.balloons()

        st.write("**Name:**", name)
        st.write("**Rating:** ⭐" * rating)
        st.write("**Feedback:**")
        st.info(feedback)