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


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cr7 = RonaldoHimself()
        self.leveler = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("level stats cog ready")


    @commands.slash_command(name="level", description="Shows your level stats")
    async def level(self, ctx):
        embed = discord.Embed(color=0x00ff00)
        embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
        embed.set_author(name=ctx.author.name, icon_url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
        level = self.leveler.get_progress(ctx.author.id)
        embed.description = f"you are level {level[2]} with {level[0]}/{level[1]} xp to the next level"
        await ctx.respond(embed=embed)
    
    
            
    

def setup(bot):
    bot.add_cog(Levels(bot))
