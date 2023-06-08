# This example demonstrates a standalone cog file with the bot instance in a separate file.

from datetime import timedelta
import datetime
import time
import discord
from discord.ext import commands
from discord import option
from discord.ui import View, button

startTime = time.time()

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Info cog loaded!")

    @commands.slash_command(name="help",description="Displays all avaliable commands")  
    async def help(self, ctx: discord.ApplicationContext):# 0x3083e3 is the color of the embed
        embed = discord.Embed(title="siu?", color=0xf1c232, 
            description="""
                `/help`: Shows this message.
                `/rank`: Shows yours or another users level stats.
                `/leaderboard`: Shows the top 10 players in the current server.
                `/siu_rank`: Shows your siu rank.
                `/siu_leaders`: Shows the top 10 siuers.
                `/global_leaders`: Shows the top 10 global players.
            """)
        embed.set_author(name="CR7", icon_url=self.bot.user.avatar.url)
        embed.add_field(name="SIUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU", 
            value="""
                **=-**
            """, inline=False)
        await ctx.respond(embed=embed)
    # @commands.slash_command(name="stats", description="Displays stats")
    # async def stats(self, ctx):
    #     # guess get total artits tracked and also unique artist tracked
    #     pass

def setup(bot):
    bot.add_cog(Info(bot))
