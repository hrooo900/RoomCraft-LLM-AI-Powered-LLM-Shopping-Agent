################################ MODEL ###################################
import os
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


if not os.environ.get("MISTRAL_API_KEY"):
    os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")

model = ChatMistralAI(model = 'mistral-large-latest')