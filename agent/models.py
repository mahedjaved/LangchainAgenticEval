import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables from .env
load_dotenv()

model = init_chat_model(
    model="nvidia/nemotron-3.5-lightning:free",  # Use ":free" if utilizing the free tier
    model_provider="openai",
    base_url="https://ai-gateway.kilo.ai/api/v1",
    api_key=os.getenv("KILO_API_KEY"),
)

response = model.invoke("Tell me a joke on Hideo Kojima.")

print(response.content)

