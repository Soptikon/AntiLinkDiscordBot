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

class dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @nextcord.slash_command(name="dog", description="Sends a random dog picture")
    async def dog(self, interaction: nextcord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                if resp.status != 200:
                    em = Embed(title="Dog", description="Could not retrieve a random dog picture.")
                    return await interaction.response.send_message("Could not retrieve a random dog picture.", ephemeral=True)

                data = await resp.json()

                em = Embed(title="Dog")
                em.set_image(url=data["message"])
                await interaction.response.send_message(embed=em)

def setup(bot):
    bot.add_cog(dog(bot))        