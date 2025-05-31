# app.py
import chainlit as cl
from problem_solver import get_ai_response

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    response = await get_ai_response(user_input)
    await cl.Message(content=response).send()