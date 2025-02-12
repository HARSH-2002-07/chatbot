import wikipediaapi

def fetch_wikipedia_summary(topic, lang='en'):
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='my-wikipedia-bot/1.0', language=lang)
    page = wiki_wiki.page(topic)
    
    if not page.exists():
        return f"The page '{topic}' does not exist on Wikipedia."
    
    return page.summary

if __name__ == "__main__":
    topic = input("Enter a Wikipedia topic: ")
    summary = fetch_wikipedia_summary(topic)
    print("\nSummary:\n", summary)