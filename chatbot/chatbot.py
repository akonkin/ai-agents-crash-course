import chainlit as cl
import dotenv

from agents import Runner, SQLiteSession, trace
from nutrition_agent import nutrition_agent

dotenv.load_dotenv()

@cl.on_message
async def on_message(message: cl.Message):
    await cl.Message(content=f"Received: {message.content}").send()