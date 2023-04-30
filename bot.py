# discord-gpt
# ethan.hamilton798@gmail.com
# this is a discord bot that let's you interact with GPT-4

# import libraries
import discord
import openai
import requests
import json
from dotenv import load_dotenv
import os
import asyncio

# load env variables
load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = openai_api_key
discord_bot_token = os.environ.get("DISCORD_BOT_TOKEN")

# set up discord bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# chat function
async def chat(messages):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, _sync_chat, messages)
    return response

def _sync_chat(messages):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages,
        temperature=0.5,
        max_tokens=200,
    )
    response = response.choices[0].message['content']
    return response


# init message
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

messages = []
# messaging logic
@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    elif message.content.startswith("$gpt"):
        print("Message received:", message.content)
        user_message = message.content[5:].strip()
        messages.append({"role": "user", "content": user_message})
        print("Sending messages to GPT:", messages)
        response = await chat(messages)
        print("GPT response:", response)
        if response:
            await message.channel.send(response)
            messages.append({"role": "assistant", "content": response})

client.run(discord_bot_token)
