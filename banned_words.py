banned_words = {
    "kill", "stab", "murder", "attack", "shoot", "violence",
    "weapon", "bomb", "explosion", "rape", "sexual", "abuse"
}

def contains_banned_words(text):
    """Checks if a text contains banned words."""
    return any(word in text.lower() for word in banned_words)
