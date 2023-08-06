def underscore_to_word(string: str) -> str:
    return " ".join([x.capitalize() for x in string.split("_")])