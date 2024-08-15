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

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="ping", description="Shows ping of the bot")
    async def ping(self, interaction: nextcord.Interaction):
        em = Embed(title="Pong!", description=f"Latency: {round(self.bot.latency * 1000)}ms")
        em.set_footer(text=f"Requested by {interaction.user.name}")
        em.set_author(name="Soptikon", icon_url=self.bot.user.display_avatar.url, url="https://github.com/Soptikon")
        await interaction.response.send_message(embed=em)



def setup(bot):
    bot.add_cog(ping(bot))        