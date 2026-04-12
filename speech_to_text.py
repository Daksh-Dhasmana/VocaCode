# speech_to_text.py
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from streamlit_mic_recorder import mic_recorder

load_dotenv()
def get_voice(duration=None):
    audio = mic_recorder(
        start_prompt="🎤 Start Speaking",
        stop_prompt="⏹️ Stop",
        format="wav",
        key="mic"
    )

    if audio and 'bytes' in audio:
        st.success("✅ Audio captured!")

        try:
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                st.error("Missing GROQ_API_KEY")
                return None

            client = Groq(api_key=api_key)

            with st.spinner("Transcribing..."):
                transcription = client.audio.transcriptions.create(
                    file=("audio.wav", audio['bytes']),
                    model="whisper-large-v3-turbo",
                    response_format="text"
                )

            return transcription.lower()

        except Exception as e:
            st.error(f"Error: {e}")
            return None

    return None