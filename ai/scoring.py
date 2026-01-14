def weighted_score(scores: dict, weights: dict) -> float:
    """
    Computes a weighted average score.
    """
    total = 0.0
    weight_sum = 0.0

    for key, score in scores.items():
        weight = weights.get(key, 0)
        total += score * weight
        weight_sum += weight

    return total / weight_sum if weight_sum > 0 else 0.0
