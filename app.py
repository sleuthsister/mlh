import os
import random
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="ZenChoice • Decision Assistant",
    page_icon="🪷",
    layout="centered",
)

st.title("🪷 ZenChoice")
st.write("Breathe in clarity. Make your decisions gently.")

if "options" not in st.session_state:
    st.session_state.options = ["", ""]
if "verdict" not in st.session_state:
    st.session_state.verdict = None

st.subheader("Enter choices:")
for i in range(len(st.session_state.options)):
    st.session_state.options[i] = st.text_input(f"Option {i+1}", value=st.session_state.options[i], key=f"opt_{i}")

if st.button("➕ Add Option"):
    st.session_state.options.append("")
    st.rerun()

if st.button("🎋 Decide"):
    opts = [o for o in st.session_state.options if o.strip()]
    if len(opts) >= 2:
        st.session_state.verdict = random.choice(opts)
        st.success(f"Chosen: {st.session_state.verdict}")
    else:
        st.warning("Please enter at least two options.")
