import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta  # For handling months and years

def classify_query(query):
    # Define temporal keywords for "new"
    temporal_keywords = ["current", "latest", "present", "trending"]
    reference_date = datetime(2023, 11, 1)  # November 2023

    # Check for temporal keywords
    if any(keyword in query.lower() for keyword in temporal_keywords):
        return "New"

    # Check for relative time phrases like "2 months ago"
    relative_pattern = r'(\d+)\s*(weeks?|months?|years?)\s*ago'
    relative_match = re.search(relative_pattern, query.lower())
    if relative_match:
        quantity = int(relative_match.group(1))  # Extract the quantity
        unit = relative_match.group(2)  # Extract the unit

        # Calculate the date based on the relative time
        if "week" in unit:
            calculated_date = datetime.now() - timedelta(weeks=quantity)
        elif "month" in unit:
            calculated_date = datetime.now() - relativedelta(months=quantity)
        elif "year" in unit:
            calculated_date = datetime.now() - relativedelta(years=quantity)
        
        # Compare the calculated date to the reference date
        if calculated_date < reference_date:
            return "Old"
        else:
            return "New"

    # Check for specific dates in the query
    date_pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4})\b'
    dates = re.findall(date_pattern, query)

    if dates:
        for date in dates:
            try:
                if "-" in date or "/" in date:
                    parsed_date = datetime.strptime(date, "%d-%m-%Y") if "-" in date else datetime.strptime(date, "%d/%m/%Y")
                else:
                    parsed_date = datetime(int(date), 1, 1)
                if parsed_date < reference_date:
                    return "Old"
                else:
                    return "New"
            except ValueError:
                continue  # Skip invalid date formats

    # Default to "New" if no temporal keyword, relative time, or valid date is found
    return "New"

# Test the function
queries = [
    "Who is the current prime minister of India?",
    "Who was the president of the USA in 2005?",
    "Who is the president of the USA?",
    "Who is the CEO of stock market?",
    "Who was the president of India in 1999?",
    "Tell me the most trending news about addverb",
    "What happened two months ago?",
    "Who was the prime minister 2 year ago?",
    "Tell me about the president 4 weeks ago."
]

for query in queries:
    print(f"Query: {query}\nClassification: {classify_query(query)}\n")
