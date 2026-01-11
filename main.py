import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega variáveis no arquivo .env, nesse caso a chave da API do Gemini
load_dotenv()
api_key = os.getenv("MY_AI_API_KEY")

genai.configure(api_key=api_key)

# Configurando a IA Generativa
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite",
    system_instruction="Seu papel é desempenhar a função de chatbot.",
)
chat = model.start_chat()

response = ""
message = input("You: ")
while message != "quit":
    response = chat.send_message(message)
    print("ChatBot: " + response.text)
    message = input("You: ")