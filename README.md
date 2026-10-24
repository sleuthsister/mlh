# 🪷 ZenChoice — The Indecisive Oracle

A fun, calming, zen-styled Streamlit application powered by **Gemma** open models to help indecisive users break free from analysis paralysis!

---

## ✨ Features

- **🧘 Zen Interface**: Calming sage-green aesthetics, smooth breathing pulses, and clean typography.
- **⚡ Multiple Choices**: Enter 2 or more options with dynamic add/remove, plus one-click preset dilemmas (Pizza vs Sushi, Sleep vs Gym, etc.).
- **🔮 Gemma-Powered Decision Oracle**: Uses Gemma (`gemma-2-9b-it`, `gemma-2-27b-it`) or Gemini via Google AI Studio.
- **🎭 Customizable Personas**: Choose between *Zen Master*, *Cosmic Oracle*, *Chaos Goblin*, or *Ruthless Pragmatist*.
- **🍵 The Verdict Card**: Delivers an undeniable final decision, philosophical wisdom, gentle roast / reality check, and a 10-second micro-ritual.
- **🎈 Built-in Demo Mode**: If no API key is set yet, it runs smoothly in demo mode so you can preview the vibe immediately!

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your Google Gemini API Key
You have two ways to add your API key:
- **Option A**: Create a `.env` file from `.env.example`:
  ```bash
  copy .env.example .env
  ```
  Then paste your API key:
  ```env
  GEMINI_API_KEY=AIzaSy...
  ```
- **Option B**: Enter it directly in the sidebar inside the running app!

### 3. Run the App
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.
