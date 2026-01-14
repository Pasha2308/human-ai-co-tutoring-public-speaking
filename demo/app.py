import streamlit as st
import tempfile
import sys
import os

# Add project root to Python path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)


from ai.duration import get_duration_seconds, duration_score
from ai.asr import transcribe_audio
from ai.filler_words import filler_ratio, filler_score

st.title("Human–AI Co-Tutoring Demo: Public Speaking")

st.write(
    "This demo shows an AI-only practice loop with final human validation."
)

uploaded_file = st.file_uploader(
    "Upload a speech audio file (.wav)", type=["wav"]
)

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        audio_path = tmp.name

    st.audio(audio_path)

    # --- AI Evaluation ---
    duration = get_duration_seconds(audio_path)
    transcript = transcribe_audio(audio_path)
    filler_r = filler_ratio(transcript)

    duration_sc = duration_score(duration, 60)
    filler_sc = filler_score(filler_r)

    st.subheader("AI Evaluation Results")
    st.write(f"Speech duration: {duration:.2f} seconds")
    st.write(f"Filler word ratio: {filler_r:.2%}")
    st.write(f"Duration score: {durationation_sc if False else duration_sc}")
    st.write(f"Filler score: {filler_sc}")

    avg_score = (duration_sc + filler_sc) / 2

    st.write(f"Average AI score: {avg_score:.1f}")

    # --- AI-only loop decision ---
    if avg_score < 80:
        st.warning("AI recommends retry. Please revise and resubmit.")
    else:
        st.success("AI recommends mastery")

        st.subheader("Final Human Validation")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("✅ Approve"):
                st.success("Mastery APPROVED by human validator")

        with col2:
            if st.button("❌ Reject"):
                st.error("Mastery REJECTED — return to AI practice loop")
