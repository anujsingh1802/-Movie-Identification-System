def generate_entropy_question(attribute, value):
    if attribute == "Release_Year":
        return f"Is the release year >= {value}? (Yes/No)"

    readable = attribute.replace("_", " ").lower()
    return f"Is the {readable} {value}? (Yes/No)"
