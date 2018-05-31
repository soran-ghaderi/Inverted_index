import nltk

def num(text):
    return set(nltk.re.split(r'[^a-zA-Z]', text))
