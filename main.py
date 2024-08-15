# Made with ❤️ by https://github.com/Soptikon
import os
import nextcord
from nextcord.ext import commands
from datetime import timedelta
from nextcord import Embed, Color
from nextcord.ui import Button, View, Modal, TextInput
import aiohttp
import aiosqlite
import random
import asyncio
import time


intents = nextcord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='D!', intents=intents)

@bot.event
async def on_ready():
    print("________________________________")
    print(f"{bot.user} is ready and online!")
    print("If you need help please visit:")
    print("  https://github.com/Soptikon  ")
    print("         Version: 1.0.0        ")
    print("________________________________")


def load_cogs(bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            bot.load_extension(f'cogs.{filename[:-3]}')


if __name__ == "__main__":
    load_cogs(bot)
    bot.run("Your_Discord_Bot_Token")
    pass

asyncio.run(main())

