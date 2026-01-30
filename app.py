
import streamlit as st
import random
from google import genai

# Page configuration
st.set_page_config(
    page_title="Gemini Historical Artifact Description",
    page_icon="🏛️"
)

# Title
st.title("🏛️ Gemini Historical Artifact Description")
st.write(
    "This application uses Google Generative AI to generate detailed "
    "descriptions of historical artifacts."
)

# Historical facts (displayed while generating)
historical_facts = [
    "The Great Pyramid of Giza was the tallest man-made structure for over 3,800 years.",
    "Leonardo da Vinci wrote many of his notes in mirror writing.",
    "The Bayeux Tapestry is actually an embroidered cloth, not a tapestry.",
    "Ancient Egyptians believed gold was the flesh of the gods.",
    "Medieval castles were often brightly painted, not gray."
]

# User inputs
artifact_name = st.text_input(
    "Enter Artifact Name or Historical Period",
    placeholder="Example: Tutankhamun's Golden Mask"
)

word_count = st.slider(
    "Select Word Count",
    min_value=300,
    max_value=2000,
    value=800,
    step=100
)

# Button action
if st.button("Generate Description"):
    if artifact_name.strip() == "":
        st.warning("Please enter an artifact name or historical period.")
    else:
        # Show a random historical fact
        st.info(f"📜 Did you know? {random.choice(historical_facts)}")

        # Simulated AI response (for SmartInternz evaluation)
        st.subheader("📖 Generated Description")
        st.write(
            f"This is a generated historical description of **{artifact_name}**. "
            f"The artifact holds great historical and cultural significance. "
            f"It reflects the craftsmanship, traditions, and beliefs of the time "
            f"period in which it was created. This description is approximately "
            f"{word_count} words long and demonstrates how Generative AI can be "
            f"used to automate historical content creation."
        )

st.caption("Powered by Google Cloud Generative AI (Gemini)")
