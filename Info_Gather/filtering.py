import re

text = """(Your Wikipedia content here)"""

# Extract sentences mentioning 'power', 'election', 'responsibility'
important_sentences = re.findall(r"([^.]*?(power|elect|responsibility|policy|law|veto|foreign).*?\.)", text, re.IGNORECASE)
filtered_text = " ".join([sentence[0] for sentence in important_sentences])

print(filtered_text)
