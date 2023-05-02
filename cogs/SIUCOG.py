# This example demonstrates a standalone cog file with the bot instance in a separate file.

from datetime import timedelta
import datetime
import time
import discord
from discord.ext import commands
from discord import option
from discord.ui import View, button
from utils.SIU import RonaldoHimself
import asyncio
# from utils.leveling import LevelerDB

startTime = time.time()

class SIU(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cr7 = RonaldoHimself()
        self.leveler = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("SIUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.startswith("http"):
            return
        # print(f"{message.author.name} said: {message.content}")
        SIUED = await self.cr7.SIUUUUUUUUU(str(message.content))
        # print("message content: " + str(message.content))
        if SIUED[0]:
            crossout_text = ''.join(['~~{}~~'.format(c) if c.islower() else c for c in SIUED[2]])
            embed = discord.Embed(color=0x00ff00)
            embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
            # embed.set_author(name=message.author.name, icon_url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
            embed.description = f"you said SIUUUUUUUUU in your sentence: {crossout_text}"
            await self.leveler.add_xp(message.author.id, 1, SIUUUUUUUUU=True, player_name=message.author.name)
            await message.channel.send(embed=embed)
        else:
            await self.leveler.add_xp(message.author.id, 1, SIUUUUUUUUU=False, player_name=message.author.name)
            


def setup(bot):
    bot.add_cog(SIU(bot))
