import os
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f"Conectado como {client.user}")


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("!hola"):
    await message.channel.send("¡Hola! Bot activo y funcionando en la nube.")


token = os.environ.get("DISCORD_TOKEN")
client.run(token)
