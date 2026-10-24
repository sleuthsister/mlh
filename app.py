import os
import random
import streamlit as st
from dotenv import load_dotenv

# Load environment variables if present
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="ZenChoice • Gemma Oracle",
    page_icon="🪷",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Zen Styling
ZEN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap');

html, body, [class*="css"], [data-testid="stAppViewContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ECFDF5;
}

/* Background & serene ambient dark gradient */
.stApp, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 15% 15%, #132A22 0%, #0C1613 55%, #070D0B 100%) !important;
    color: #ECFDF5 !important;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #0A120F !important;
    border-right: 1px solid rgba(110, 231, 183, 0.12) !important;
}

[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3, 
[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] label, 
[data-testid="stSidebar"] span {
    color: #E2E8F0 !important;
}

/* Zen Header */
.zen-header {
    text-align: center;
    padding: 2.2rem 1rem 1.2rem 1rem;
    margin-bottom: 1.2rem;
}
.zen-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 600;
    background: linear-gradient(135deg, #ECFDF5 30%, #6EE7B7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3rem;
    letter-spacing: -0.5px;
}
.zen-subtitle {
    font-size: 1.05rem;
    color: #A7F3D0 !important;
    font-weight: 400;
}

/* Headings and markdown labels */
h1, h2, h3, h4, h5, h6, label, .stMarkdown p {
    color: #ECFDF5 !important;
}

/* Input boxes & textareas */
input[type="text"], input[type="password"], textarea, .stTextInput input {
    background-color: rgba(19, 42, 34, 0.75) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(110, 231, 183, 0.3) !important;
    border-radius: 10px !important;
}
input[type="text"]:focus, .stTextInput input:focus {
    border-color: #10B981 !important;
    box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.3) !important;
}

/* Card styles */
.zen-card {
    background: rgba(19, 42, 34, 0.8) !important;
    backdrop-filter: blur(16px);
    border: 1px solid rgba(110, 231, 183, 0.25) !important;
    border-radius: 20px;
    padding: 1.8rem;
    margin-top: 1.5rem;
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.5);
    animation: fadeIn 0.6s ease-in-out;
}

.verdict-header {
    text-align: center;
    margin-bottom: 1.2rem;
}

.verdict-badge {
    background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
    color: #FFFFFF !important;
    font-size: 1.45rem;
    font-weight: 700;
    padding: 0.75rem 2rem;
    border-radius: 999px;
    display: inline-block;
    box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
    margin-top: 0.5rem;
    letter-spacing: 0.3px;
}

.section-label {
    font-weight: 600;
    color: #6EE7B7 !important;
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-top: 1.1rem;
    margin-bottom: 0.3rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.zen-text {
    color: #E2E8F0 !important;
    line-height: 1.65;
    font-size: 1.05rem;
}

.ritual-box {
    background: rgba(6, 78, 59, 0.45) !important;
    border-left: 4px solid #10B981 !important;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-top: 1.3rem;
    font-size: 0.98rem;
    color: #D1FAE5 !important;
}

/* Breathe animation indicator */
@keyframes pulseBreathe {
    0% { transform: scale(1); opacity: 0.7; box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.6); }
    50% { transform: scale(1.15); opacity: 1; box-shadow: 0 0 12px 4px rgba(52, 211, 153, 0.4); }
    100% { transform: scale(1); opacity: 0.7; box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.6); }
}

.breathe-dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    background-color: #34D399;
    border-radius: 50%;
    margin-right: 8px;
    animation: pulseBreathe 3s infinite ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Buttons */
div.stButton > button {
    background: rgba(22, 48, 38, 0.85) !important;
    color: #ECFDF5 !important;
    font-weight: 600 !important;
    border: 1px solid rgba(110, 231, 183, 0.25) !important;
    border-radius: 12px !important;
    padding: 0.65rem 1.4rem !important;
    transition: all 0.2s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    background: rgba(30, 68, 54, 0.95) !important;
    border-color: #34D399 !important;
    box-shadow: 0 6px 16px rgba(16, 185, 129, 0.25) !important;
    color: #FFFFFF !important;
}

/* Primary CTA button (Let Gemma Decide) */
.decide-btn div.stButton > button {
    background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
    color: #FFFFFF !important;
    font-size: 1.12rem !important;
    padding: 0.85rem 1.8rem !important;
    box-shadow: 0 6px 22px rgba(16, 185, 129, 0.4) !important;
    border: none !important;
}

.decide-btn div.stButton > button:hover {
    background: linear-gradient(135deg, #34D399 0%, #059669 100%) !important;
    box-shadow: 0 8px 26px rgba(16, 185, 129, 0.55) !important;
}
</style>
"""

st.markdown(ZEN_CSS, unsafe_allow_html=True)

# ----------------- SESSION STATE -----------------
if "options" not in st.session_state:
    st.session_state.options = ["", ""]
if "verdict" not in st.session_state:
    st.session_state.verdict = None
if "context" not in st.session_state:
    st.session_state.context = ""

# ----------------- SIDEBAR CONFIG -----------------
with st.sidebar:
    st.markdown("### 🧘 Zen Settings")
    api_key_env = os.getenv("GEMINI_API_KEY", "")
    api_key = st.text_input(
        "Google Gemini API Key",
        value=api_key_env,
        type="password",
        help="Enter your Google AI Studio / Gemini API key. If left blank, demo mode will be used.",
    )

    model_choice = st.selectbox(
        "Model",
        options=[
            "gemini-3.5-flash-lite (Speedy & Recommended)",
            "gemini-3.1-flash-lite (Ultra Fast)",
            "gemini-3.5-flash (Standard)",
            "gemma-4-31b-it (Gemma 4 - 31B Open Model)",
            "gemma-4-26b-a4b-it (Gemma 4 - 26B Open Model)",
        ],
        index=0,
        help="Select the AI model to consult. If a model encounters high demand, an automatic fallback is used.",
    )

    persona = st.selectbox(
        "Oracle Persona",
        options=[
            "🧘 Zen Master (Mindful & Serene)",
            "🔮 Cosmic Oracle (Mystical & Poetic)",
            "⚡ Chaos Goblin (Spicy, spontaneous & bold)",
            "🎯 Ruthless Pragmatist (Ultra-logical & decisive)",
        ],
        index=0,
    )

    st.markdown("---")
    st.markdown(
        "<small style='color: #94A3B8;'>✨ Powered by Gemma open models via Google AI Studio.<br>"
        "Designed to eliminate analysis paralysis gently.</small>",
        unsafe_allow_html=True,
    )
    if st.button("🍃 Reset / Clear"):
        st.session_state.options = ["", ""]
        st.session_state.verdict = None
        st.session_state.context = ""
        st.rerun()

# ----------------- MAIN UI -----------------
st.markdown(
    """
    <div class="zen-header">
        <div class="zen-title">🪷 ZenChoice</div>
        <div class="zen-subtitle"><span class="breathe-dot"></span> Breathe in clarity. Let Gemma resolve your dilemma.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Preset inspirations
st.markdown("<p style='font-size:0.92rem; color:#A7F3D0; font-weight: 500; margin-bottom: 0.4rem;'>💡 Need inspiration? Try a preset:</p>", unsafe_allow_html=True)
col_p1, col_p2, col_p3, col_p4 = st.columns(4)

if col_p1.button("🍕 vs 🍣", use_container_width=True, help="Pizza vs Sushi"):
    st.session_state.options = ["Order cheesy woodfired Pizza", "Get fresh gourmet Sushi"]
    st.session_state.context = "It's dinner time and I'm craving comfort food"
    st.rerun()

if col_p2.button("😴 vs 🏋️", use_container_width=True, help="Sleep in vs Gym"):
    st.session_state.options = ["Sleep in for another cozy hour", "Get up and crush a gym workout"]
    st.session_state.context = "It's morning, feel slightly sleepy but want to stay fit"
    st.rerun()

if col_p3.button("📚 vs 🎮", use_container_width=True, help="Read Book vs Play Games"):
    st.session_state.options = ["Read that intriguing chapter", "Play video games with the squad"]
    st.session_state.context = "Free evening to unwind"
    st.rerun()

if col_p4.button("☕ vs 🍵", use_container_width=True, help="Coffee vs Matcha"):
    st.session_state.options = ["Rich Espresso Coffee", "Earthy Ceremonial Matcha"]
    st.session_state.context = "Midday slump, need clean energy"
    st.rerun()

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# Option inputs
st.markdown("#### ⚖️ Enter the choices you're torn between:")

# Dynamic options management
num_options = len(st.session_state.options)
for i in range(num_options):
    col_input, col_del = st.columns([0.88, 0.12])
    with col_input:
        st.session_state.options[i] = st.text_input(
            f"Option {i+1}",
            value=st.session_state.options[i],
            placeholder=f"e.g., {'Go for a refreshing walk' if i==0 else 'Finish writing that draft'}",
            key=f"option_input_{i}",
            label_visibility="collapsed",
        )
    with col_del:
        if num_options > 2:
            if st.button("🗑️", key=f"del_{i}", help="Remove this option"):
                st.session_state.options.pop(i)
                st.rerun()

col_add, _ = st.columns([0.4, 0.6])
with col_add:
    if num_options < 6:
        if st.button("➕ Add Another Choice", use_container_width=True):
            st.session_state.options.append("")
            st.rerun()

# Optional context
st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
st.session_state.context = st.text_input(
    "🍃 Extra context or mood (optional):",
    value=st.session_state.context,
    placeholder="e.g. 'I only have 30 minutes', 'Low budget', 'Rainy afternoon'",
)


# ----------------- GEMMA DECISION LOGIC -----------------
def generate_decision(options_list, context_text, chosen_persona, chosen_model, api_key_val):
    clean_options = [opt.strip() for opt in options_list if opt.strip()]
    if len(clean_options) < 2:
        return None, "Please provide at least 2 distinct choices."

    prompt = f"""You are the ultimate decision oracle for indecisive humans.
Your persona: {chosen_persona}.

The user is painfully stuck and cannot decide between these choices:
{chr(10).join(f"- {opt}" for opt in clean_options)}

Additional context/vibe: {context_text if context_text else "None provided. Rely on cosmic intuition."}

Your task:
1. Make a firm, unequivocal, 100% committed DECISION for them. No "it depends", no hedging!
2. Provide a playful, wise, or funny justification in character.
3. Provide a 10-second fun micro-ritual to do right this moment.

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:
VERDICT: [Name the single chosen option here, exactly or cleanly]
WISDOM: [2-3 sentences explaining why this path brings harmony/success/peace]
REALITY_CHECK: [1-2 witty or gentle sentences teasing the rejected options or calling out human overthinking]
RITUAL: [A simple, fun 10-second physical action, e.g., 'Take a slow sip of water, unclench your jaw, and never look back.']
"""

    # If API key is available, call Google Generative AI (SDK or direct REST API)
    if api_key_val:
        # Strategy 1: Try google.generativeai SDK
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key_val)
            model = genai.GenerativeModel(chosen_model)
            response = model.generate_content(prompt)
            return parse_oracle_response(response.text, clean_options), None
        except ImportError:
            pass
        except Exception as e:
            return None, f"Gemma invocation error: {str(e)}"

        # Strategy 2: Try modern google.genai SDK
        try:
            from google import genai
            client = genai.Client(api_key=api_key_val)
            response = client.models.generate_content(model=chosen_model, contents=prompt)
            return parse_oracle_response(response.text, clean_options), None
        except ImportError:
            pass
        except Exception as e:
            return None, f"Gemma invocation error: {str(e)}"

        # Strategy 3: Direct REST API via requests (zero extra SDK required!)
        try:
            import requests

            # Clean model name and define fallback sequence
            primary_model = chosen_model.split(" ")[0].replace("models/", "").strip()
            fallback_candidates = [
                primary_model,
                "gemini-3.5-flash-lite",
                "gemini-3.1-flash-lite",
                "gemini-3.5-flash",
                "gemma-4-31b-it",
            ]
            models_to_try = []
            for m in fallback_candidates:
                if m not in models_to_try:
                    models_to_try.append(m)

            last_error = None
            headers = {"Content-Type": "application/json"}
            payload = {
                "contents": [
                    {
                        "parts": [
                            {"text": prompt}
                        ]
                    }
                ]
            }

            for model_id in models_to_try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent?key={api_key_val}"
                try:
                    res = requests.post(url, headers=headers, json=payload, timeout=20)
                    if res.status_code == 200:
                        data = res.json()
                        candidates = data.get("candidates", [])
                        if candidates and "content" in candidates[0]:
                            parts = candidates[0]["content"].get("parts", [])
                            if parts and "text" in parts[0]:
                                parsed = parse_oracle_response(parts[0]["text"], clean_options)
                                # If fallback was used, add gentle note
                                if model_id != primary_model:
                                    parsed["wisdom"] += f" *(Consulted {model_id} via auto-fallback)*"
                                return parsed, None
                    else:
                        err_data = res.json().get("error", {})
                        last_error = f"API Error ({res.status_code}): {err_data.get('message', res.text)}"
                        # Try next fallback model if 404, 503, or 500
                        continue
                except requests.exceptions.Timeout:
                    last_error = f"Request timed out for {model_id}."
                    continue
                except Exception as ex:
                    last_error = str(ex)
                    continue

            return None, last_error or "Unable to reach oracle models right now."
        except Exception as e:
            return None, f"Connection error: {str(e)}"
    else:
        # Fun fallback demo mode if user hasn't added their key yet
        chosen = random.choice(clean_options)
        demo_response = f"""VERDICT: {chosen}
WISDOM: The universe smiles upon this choice. Analysis paralysis is just fear disguised as logic; your instinct already whispered this answer before you opened this app.
REALITY_CHECK: The alternative choices were just elaborate illusions keeping you trapped in the limbo of 'what if'.
RITUAL: Breathe in deeply for 4 seconds, exhale all doubts, smile, and execute with zero hesitation. (Note: Demo Mode - Add your Gemini API key in sidebar for live Gemma intelligence!)"""
        return parse_oracle_response(demo_response, clean_options), None


def parse_oracle_response(text, options):
    result = {
        "verdict": options[0],
        "wisdom": "Follow your true compass.",
        "reality_check": "Stop overthinking and start moving.",
        "ritual": "Take three deep mindful breaths.",
    }

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("VERDICT:"):
            result["verdict"] = line.replace("VERDICT:", "").strip()
        elif line.startswith("WISDOM:"):
            result["wisdom"] = line.replace("WISDOM:", "").strip()
        elif line.startswith("REALITY_CHECK:"):
            result["reality_check"] = line.replace("REALITY_CHECK:", "").strip()
        elif line.startswith("RITUAL:"):
            result["ritual"] = line.replace("RITUAL:", "").strip()

    # Fallback if raw text wasn't formatted cleanly
    if result["verdict"] == options[0] and "VERDICT:" not in text:
        result["wisdom"] = text

    return result


# ----------------- ACTION BUTTON -----------------
st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
col_btn, _ = st.columns([0.5, 0.5])
with col_btn:
    st.markdown('<div class="decide-btn">', unsafe_allow_html=True)
    decide_clicked = st.button("🎋 Let Gemma Decide", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

if decide_clicked:
    active_options = [opt for opt in st.session_state.options if opt.strip()]
    if len(active_options) < 2:
        st.warning("🌿 Please enter at least two choices to let the oracle weigh them.")
    else:
        zen_messages = [
            "🌬️ Consulting the gentle winds of wisdom...",
            "🪷 Aligning cosmic probabilities in Gemma...",
            "🍵 Brewing the ideal outcome...",
            "🧘 Quieting the mind and cutting through the noise...",
        ]
        with st.spinner(random.choice(zen_messages)):
            parsed, err = generate_decision(
                st.session_state.options,
                st.session_state.context,
                persona,
                model_choice,
                api_key,
            )
            if err:
                st.error(err)
            else:
                st.session_state.verdict = parsed
                st.balloons()

# ----------------- VERDICT DISPLAY -----------------
if st.session_state.verdict:
    v = st.session_state.verdict
    st.markdown(
        f"""
        <div class="zen-card">
            <div class="verdict-header">
                <div style="font-size: 0.95rem; color: #A7F3D0; font-weight: 600; text-transform: uppercase; letter-spacing: 1.2px;">✨ The Oracle Has Spoken ✨</div>
                <div class="verdict-badge">✨ {v['verdict']}</div>
            </div>
            
            <div class="section-label">🌿 Zen Wisdom</div>
            <div class="zen-text">{v['wisdom']}</div>
            
            <div class="section-label">🔮 Reality Check</div>
            <div class="zen-text">{v['reality_check']}</div>
            
            <div class="ritual-box">
                <strong>🍵 Your 10-Second Micro-Ritual:</strong><br>
                {v['ritual']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    col_again, col_flip = st.columns(2)
    with col_again:
        if st.button("🎲 I'm Still Hesitant, Roll Again"):
            st.session_state.verdict = None
            st.rerun()
    with col_flip:
        if st.button("✨ Make Another Choice"):
            st.session_state.options = ["", ""]
            st.session_state.verdict = None
            st.session_state.context = ""
            st.rerun()
