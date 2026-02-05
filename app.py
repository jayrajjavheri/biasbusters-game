import streamlit as st
import pandas as pd
from PIL import Image
from gtts import gTTS
import os

st.set_page_config(page_title="BiasBusters", layout="centered")

st.title("🎮 BiasBusters – Behavioural Finance Game")
st.subheader("Mentor: SuperStar R 😎")

df = pd.read_csv("data/scenarios.csv")
row = df.iloc[0]

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.answered = False

st.markdown("### Level 1: Herd Mentality")
st.write(row["question"])

# Function to create voice
def speak(text):
    tts = gTTS(text=text)
    tts.save("voice.mp3")
    st.audio("voice.mp3",autoplay=True)

# Buttons
if st.button(row["option1"]):
    st.session_state.answered = True
    st.session_state.result = "bias"

if st.button(row["option2"]):
    st.session_state.answered = True
    st.session_state.result = "good"

if st.button(row["option3"]):
    st.session_state.answered = True
    st.session_state.result = "good"

# Result
if st.session_state.answered:
    if st.session_state.result == "bias":
        img = Image.open("images/angry.jpg")
        st.image(img, width=250)
        msg = "Crowd is loud, but your brain should be louder!"
        st.error("🤦 Bias Detected: Herd Mentality")
        st.write("SuperStar R:", msg)
        speak(msg)
    else:
        img = Image.open("images/happy.jpg")
        st.image(img, width=250)
        msg = "Smart move! Research always wins."
        st.success("✅ Good Decision!")
        st.write("SuperStar R:", msg)
        speak(msg)
        st.session_state.score += 10

st.markdown("---")
st.subheader(f"Your Score: {st.session_state.score}")
