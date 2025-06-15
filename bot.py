# bot.py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to milliseconds
    await ctx.send(f"Pong! Latency is {latency:.2f} ms")

import os
bot.run(os.getenv("DISCORD_TOKEN"))
