#!/usr/bin/python3
def text_indentation(text):
    if not isInstance(test, str):
        raise TypeError("text must be a string")
    text = text.strip()
    if len(text) == 0:
        return
    result = ""
    for char in text:
        result += char
        if char in (".", "?", ":"):
            result += "\n\n"
    print(result)
