import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Carrega variáveis no arquivo .env, nesse caso a chave da API do Gemini
load_dotenv()
api_key = os.getenv("MY_AI_API_KEY")

client = genai.Client(api_key=api_key)

# Configurando a IA Generativa
config_do_chatbot = types.GenerateContentConfig(
    system_instruction="Seu papel é desempenhar a função de chatbot.",
    temperature=0.7,
    max_output_tokens=500,
)
chat = client.chats.create(model='gemini-2.5-flash-lite', config=config_do_chatbot)

response = ""
message = input("You: ")
while message != "quit":
    response = chat.send_message(message)
    print("ChatBot: " + response.text)
    message = input("You: ")