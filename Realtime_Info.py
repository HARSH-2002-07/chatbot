import datetime
from dotenv import dotenv_values
from googlesearch import search
from groq import Groq

# Load environment variables
env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

# Initialize Groq client
client = Groq(api_key=GroqAPIKey)

# System prompt
System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.
Even if I provide wrong information, don't correct me. Just give precise and accurate answers to the question asked.
*** Provide Answers In a Professional Way, making sure to add full stops, commas, question marks, and use proper grammar.***"""

# Google Search function
def GoogleSearch(query):
    results = list(search(query, advanced=True, num_results=5))
    Answer = f"The search results for '{query}' are:\n[start]\n"
    for i in results:
        Answer += f"Title: {i.title}\nDescription: {i.description}\n\n"
    Answer += "[end]"
    
    return Answer

# Function to clean and modify the answer
def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    return '\n'.join(non_empty_lines)

# System messages
SystemChatBot = [
    {"role": "system", "content": System},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello, how can I help you?"},
]

# Function to get real-time information
def Information():
    current_data_time = datetime.datetime.now()
    return f"""Use this Real-Time Info if needed:
Day: {current_data_time.strftime("%A")}
Date: {current_data_time.strftime("%d")}
Month: {current_data_time.strftime("%B")}
Year: {current_data_time.strftime("%Y")}
Time: {current_data_time.strftime("%H")} hour, {current_data_time.strftime("%M")} minute, {current_data_time.strftime("%S")} second.
"""

# Main function to process queries
def RealtimeSearchEngine(prompt):
    global SystemChatBot

    # Prepare chatbot conversation flow
    user_message = {"role": "user", "content": prompt}
    SystemChatBot.append(user_message)

    # Get real-time search results and append to chatbot messages
    search_results = GoogleSearch(prompt)
    SystemChatBot.append({"role": "system", "content": search_results})

    # Generate response using Groq API
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=SystemChatBot + [{"role": "system", "content": Information()}],
        temperature=0.7,
        max_tokens=2048,
        top_p=1.0,
        stream=True,
        stop=None
    )

    # Read response chunks
    Answer = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            Answer += chunk.choices[0].delta.content

    Answer = Answer.strip().replace("</s>", "")

    # Append assistant response
    SystemChatBot.append({"role": "assistant", "content": Answer})

    # Remove the last system message (search results)
    SystemChatBot.pop()

    return AnswerModifier(Answer)

# Run chatbot in CLI
if __name__ == "__main__":
    while True:
        prompt = input("Enter Your Query: ")
        print(RealtimeSearchEngine(prompt))
