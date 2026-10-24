import os
import random
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

st.set_page_config(page_title="ZenChoice • Gemma Oracle", page_icon="🪷", layout="centered")

st.title("🪷 ZenChoice")
st.write("Breathe in clarity. Let Gemma resolve your dilemma.")

api_key = os.getenv("GEMINI_API_KEY", "")

with st.sidebar:
    st.header("Settings")
    api_key_input = st.text_input("Gemini API Key", value=api_key, type="password")
    persona = st.selectbox("Persona", ["Zen Master", "Cosmic Oracle", "Chaos Goblin", "Ruthless Pragmatist"])

if "options" not in st.session_state:
    st.session_state.options = ["", ""]
if "verdict" not in st.session_state:
    st.session_state.verdict = None

for i in range(len(st.session_state.options)):
    st.session_state.options[i] = st.text_input(f"Option {i+1}", value=st.session_state.options[i], key=f"opt_{i}")

if st.button("➕ Add Option"):
    st.session_state.options.append("")
    st.rerun()

if st.button("🎋 Let Gemma Decide"):
    clean_opts = [o.strip() for o in st.session_state.options if o.strip()]
    if len(clean_opts) >= 2:
        key = api_key_input or api_key
        if key:
            genai.configure(api_key=key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Persona: {persona}. Choose definitively between: {clean_opts}."
            res = model.generate_content(prompt)
            st.session_state.verdict = res.text
            st.success(res.text)
        else:
            st.session_state.verdict = random.choice(clean_opts)
            st.info(f"Demo Verdict: {st.session_state.verdict}")
