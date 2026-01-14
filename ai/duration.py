import wave


def get_duration_seconds(audio_path: str) -> float:
    """
    Returns the duration of an audio file in seconds.
    """
    with wave.open(audio_path, 'rb') as audio:
        frames = audio.getnframes()
        rate = audio.getframerate()
        duration = frames / float(rate)
    return duration


def duration_score(actual_seconds: float, target_seconds: float) -> int:
    """
    Scores speech duration based on deviation from target duration.
    """
    deviation = abs(actual_seconds - target_seconds) / target_seconds

    if deviation <= 0.10:
        return 100
    elif deviation <= 0.20:
        return 80
    else:
        return 60
