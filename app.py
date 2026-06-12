import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["grok_api_key"])

st.title("AI Interview Prep Tool ohh jandaa eee")
st.write("Get personalized interview questions for any role")

role = st.text_input("What role are you preparing for?")
interview_type = st.selectbox(
    "Interview type",
    ["Technical", "HR", "Both"]
)

if st.button("Generate Questions"):
    if role:
        with st.spinner("Generating questions..."):
            prompt = f"""
            You are an expert interviewer. Generate 10 {interview_type} 
            interview questions for a {role} position. For each question 
            provide a strong sample answer. Format clearly with the 
            question as a header and answer below it.
            """
            chat = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            st.write(chat.choices[0].message.content)
    else:
        st.warning("Please enter a role first")