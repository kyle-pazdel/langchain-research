from dotenv import load_dotenv, find_dotenv
import openai
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from prettyprinter import pprint

load_dotenv(find_dotenv())

# llm = OpenAI()

# llm.invoke(input="Tell me a joke")

# result = llm.generate(["Tell me a joke about cows", "Tell me a joke about parrots"])
# print(result)

# result.llm_output


llm = ChatOpenAI()

# Single Call Example

result = llm.invoke(input="Tell me a joke")
print(result)

# Messages Example
messages = [
  SystemMessage(content="You are a helpful assistant specialized in providing information about BellaVista Restaurant"),
  HumanMessage(content="What's on the menu?"),
  AIMessage(content="BellaVista offers a variety of Italian dishes including pasta, pizza, and seafood."),
  HumanMessage(content="Do you have vegan options?")
]

llm_result = llm.invoke(input=messages)
pprint(llm_result)

# Batch Messages Example
batch_messages = [
  [
    SystemMessage(content="You area helpful assistant that translates English to German."),
    HumanMessage(content="Do you have vegan options?"),
  ],
  [
    SystemMessage(content="You area helpful assistant that translates English to Spanish."),
    HumanMessage(content="Do you have vegan options?"),
  ],
]

batch_result = llm.generate(batch_messages)

translations = [generation[0].text for generation in batch_result.generations]
pprint(translations)