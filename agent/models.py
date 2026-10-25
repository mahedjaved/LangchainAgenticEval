from dotenv import dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
model = init_chat_model("")
