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

class bott(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @nextcord.slash_command(name="bot", description="Shows information about the bot")
    async def bot(self, interaction: nextcord.Interaction):
        em = Embed(title="Soptikon", description="A Discord bot developed by Soptikon.")
        em.add_field(name="Author", value="Soptikon")
        em.add_field(name="Version", value="1.0.0")
        em.set_thumbnail(url=self.bot.user.avatar.url)
        em.set_footer(text="Made with ❤️ by https://github.com/Soptikon")
        await interaction.response.send_message(embed=em)

        
def setup(bot):
    bot.add_cog(bott(bot))        