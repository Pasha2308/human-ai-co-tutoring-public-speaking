import speech_recognition as sr


def transcribe_audio(audio_path: str) -> str:
    """
    Transcribes speech audio to text using a basic ASR engine.
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
