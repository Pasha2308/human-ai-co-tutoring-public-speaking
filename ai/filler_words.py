FILLER_WORDS = {
    "um",
    "uh",
    "like",
    "you know",
    "actually"
}


def filler_ratio(transcript: str) -> float:
    """
    Calculates the ratio of filler words in a transcript.
    """
    words = transcript.lower().split()

    if not words:
        return 1.0

    filler_count = sum(1 for word in words if word in FILLER_WORDS)
    return filler_count / len(words)


def filler_score(ratio: float) -> int:
    """
    Scores filler word usage.
    """
    if ratio <= 0.03:
        return 95
    elif ratio <= 0.06:
        return 80
    else:
        return 60
