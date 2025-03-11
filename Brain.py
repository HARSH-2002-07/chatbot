from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

SystemChatBot = [
    {"role": "system", "content": System}
]

def RealTimeInformation():
  current_data_time = datetime.datetime.now()
  day = current_data_time.strftime("%A")
  date = current_data_time.strftime("%d")
  month = current_data_time.strftime("%B")
  year = current_data_time.strftime("%Y")
  hour = current_data_time.strftime("%H")
  minute = current_data_time.strftime("%M")
  second = current_data_time.strftime("%S")

  data = f"please use this realtime information if needed, \n"
  data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
  data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"
  return data

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    return '\n'.join(non_empty_lines)

def ChatBot(Query):
  SystemChatBot.append({"role": "user", "content": Query})

  completion = client.chat.completions.create(
      model="llama3-70b-8192",
      messages=SystemChatBot + [{"role": "system", "content": RealTimeInformation()}],
      max_tokens=1024,
      temperature=0.7,
      top_p=1,
      stream=True,
      stop=None
   )

  Answer = ""

  for chunk in completion:
    if chunk.choices[0].delta.content:
      Answer += chunk.choices[0].delta.content

  Answer = Answer.replace("</s>", "")

  SystemChatBot.append({"role": "assistant", "content": Answer.strip()})

  return AnswerModifier(Answer)

if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Query: ")
        print(ChatBot(user_input))