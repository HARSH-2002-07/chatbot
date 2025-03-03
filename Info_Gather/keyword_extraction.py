import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def extract_keywords(text):
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return Counter(words).most_common(10)  # Get top 10 keywords

text = """Who is the current president of the US?"""
keywords = extract_keywords(text)

print("Top Keywords:", keywords)
