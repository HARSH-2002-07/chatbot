import wikipedia
import re

def extract_keywords(query):
    """Extracts key terms from the user query."""
    keywords = []
    if "current president" in query.lower():
        keywords.append("current president")
    if "US" in query or "America" in query:
        keywords.append("US president")
    return keywords

def get_wikipedia_summary(topic):
    """Fetches a Wikipedia summary of the given topic."""
    try:
        return wikipedia.summary(topic, sentences=10)  # Fetching 10 sentences
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=10)
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for the topic."

def filter_relevant_info(summary, keywords):
    """Filters the summary to extract only relevant sentences."""
    sentences = summary.split(". ")
    relevant_sentences = [s for s in sentences if any(k in s for k in keywords)]
    return ". ".join(relevant_sentences) if relevant_sentences else "No relevant information found."

# Example Query
query = "Who is the current president of the US?"

# Step 1: Extract keywords from query
keywords = extract_keywords(query)

# Step 2: Get Wikipedia data
summary = get_wikipedia_summary("President of the United States")

# Step 3: Filter out relevant information
result = filter_relevant_info(summary, keywords)

print(query, "1")
print(keywords, "2")
print(summary, "3")
print(result)
