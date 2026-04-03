from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os


load_dotenv()

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")
DASHSCOPE_MODEL = os.getenv("DASHSCOPE_MODEL")

class MyChatModel:
    def create_model_dashscope(self):
        return ChatOpenAI(
            model=DASHSCOPE_MODEL,
            api_key=DASHSCOPE_API_KEY,
            base_url=DASHSCOPE_BASE_URL
        )
