def human_validate() -> bool:
    """
    Final human decision for mastery validation.
    Returns True if approved, False otherwise.
    """
    decision = input("Approve mastery? (y/n): ").strip().lower()
    return decision == "y"
