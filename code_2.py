from dotenv import load_dotenv, find_dotenv
import openai
from langchain_openai import OpenAI, ChatOpenAI

load_dotenv(find_dotenv())

llm = OpenAI()

llm.invoke(input="Tell me a joke")

result = llm.generate(["Tell me a joke about cows", "Tell me a joke about parrots"])
print(result)

result.llm_output


llm = ChatOpenAI()

result = llm.invoke(input="Tell me a joke")
print(result)