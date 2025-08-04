import streamlit as st
from dialect_utils import normalize_input
from emotion_utils import detect_emotion
from ollama_utils import query_ollama
import json

st.set_page_config(page_title="Emotion-Aware Chatbot", layout="centered")
st.title("🧠 Emotion-Aware Chatbot for Regional Dialects")

user_input = st.text_input("🗣️ Talk to me in your dialect:")

if user_input:
    normalized = normalize_input(user_input)
    emotion = detect_emotion(normalized)
    
    prompt = f"User said: '{normalized}' with emotion: {emotion}. Respond empathetically."
    response = query_ollama(prompt)

    st.markdown(f"### 🤖 Response:\n{response}")
    st.markdown(f"**Detected Emotion:** `{emotion}`")

    # Optional feedback
    feedback = st.radio("Was this response helpful?", ["👍 Yes", "👎 No"])
    if st.button("Submit Feedback"):
        with open("feedback_store.json", "a") as f:
            f.write(json.dumps({
                "input": user_input,
                "normalized": normalized,
                "emotion": emotion,
                "response": response,
                "feedback": feedback
            }) + "\n")
        st.success("✅ Feedback saved!")
