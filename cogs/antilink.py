import os
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Color


links = [
    ".com", ".org", ".net", ".info", ".biz", ".mobi", ".name", ".pro",
    ".coop", ".aero", ".museum", ".travel", ".jobs", ".cz", ".us", ".uk",
    ".de", ".fr", ".jp", ".ru", ".cn", ".br", ".au", ".gov", ".edu", ".mil",
    ".int", ".eu", ".io", ".tv", ".gg", ".je", ".app", ".blog", ".guru",
    ".shop", ".music", ".design", ".tech", "https://", "mc.", "http://",
    "www.", ".me", ".aternos", ".co", "play.", ".gg", ".dev", ".rip", ".io", ".xyz", 
]

class AntiLink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user or message.author.bot:
            return
        

        if message.author.guild_permissions.administrator:
            return
        

        if any(link in message.content.lower() for link in links):
            await message.delete()
            em = Embed(title="Link Detected", description=f"You can't send links here {message.author.mention}!", color=Color.red())
            await message.channel.send(embed=em)

def setup(bot):
    bot.add_cog(AntiLink(bot))
  