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

class cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @nextcord.slash_command(name="cat", description="Shows a random cat image")
    async def cat(self, interaction: nextcord.Interaction):
        em = Embed(title="Cat")
        em.set_image(url="https://cataas.com/cat")
        await interaction.response.send_message(embed=em)

def setup(bot):
    bot.add_cog(cat(bot))        