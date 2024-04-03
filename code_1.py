from dotenv import load_dotenv, find_dotenv
import openai
from prettyprinter import pprint

load_dotenv(find_dotenv())

# Test OpenAI Chat Completion
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant specialized in providing information about BellaVista Italian Restaurant."},
        {"role": "user", "content": "What's on the menu?"},
        {"role": "assistant", "content": "BellaVista offers a variety of Italian dishes including pasta, pizza, and seafood."},
        {"role": "user", "content": "Do you have vegan options?"}
    ]
)

pprint(response.choices[0].message.content)