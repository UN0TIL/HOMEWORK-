def popular_words(text, words):
    text_cult = {}

    text = text.lower().split()

    for word in text:
        if word in words:
            text_cult[word] = text_cult.get(word, 0) + 1

    for word in words:
        if word not in text_cult:
            text_cult[word] = 0

    return text_cult


assert popular_words(
    """When I was One I had just begun When I was Two I was nearly new """,
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test1"
print("OK")
