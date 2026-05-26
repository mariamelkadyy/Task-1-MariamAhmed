import string

def clean_input(text):

    text = text.lower()
    text = text.strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join(text.split())

    return text