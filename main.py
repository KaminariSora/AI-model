# import ollama

# response = ollama.chat(
#     model='thewindmom/llama3-med42-8b:latest',
#     messages=[
#         {'role': 'system', 'content': 'You are a friendly AI who talks like a human.'},
#         {'role': 'user', 'content': 'สวัสดี'}
#     ]
# )

# print(response['message']['content'])

# user_input = input("Enter question: ")

import chromadb 
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(".env")
load_dotenv(dotenv_path=env_path)
chroma_api_key = os.getenv("CHROMA_API_KEY")

client = chromadb.CloudClient(
  api_key=chroma_api_key,
  tenant='f69a80c1-ef1c-467e-be0a-4295c55b5ffb',
  database='model-memory'
)

collection = client.create_collection(name="model_memory")

def memory_insert(text, id):
    collection.add(
        documents=[text],
        ids=[id]
    )

memory_insert("testing", "1")

result= collection.get()
print(result)