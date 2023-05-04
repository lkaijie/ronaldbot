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


    @commands.slash_command(name="rank", description="Shows your level stats")
    @option("username", description="Enter the username of the user you want to stalk", required=False)
    async def level(self, ctx):
        if ctx.options != None:
            pass
        else:
            embed = discord.Embed(color=0x00ff00)
            embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
            level = await self.leveler.get_progress(ctx.author.id)
            rank = await self.leveler.get_rank(ctx.author.id)
            embed.set_author(name=ctx.author.name+f" rank #{rank[0]} siu rank #{rank[1]}", icon_url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
            if level == False:
                await ctx.respond("0 messages sent")
                return
            siu_ratio = [(level[3]/level[5]),level[3],level[5]]
            embed.description = f"you are level {level[2]} with {level[0]}/{level[1]} xp to the next level"
            embed.add_field(name=f"SIU ratio: {siu_ratio[0]:0.2f}%", value=f"times SUIed: {siu_ratio[1]}, total messages: {siu_ratio[2]}", inline=False)
            await ctx.respond(embed=embed)
        
    # @commands.slash_command(name="leaderboard", description="Shows the top 10 players")
    # async def leaderboard(self, ctx):
    #     embed = discord.Embed(color=0x00ff00)
    #     embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
    #     embed.set_author(name=ctx.author.name, icon_url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
    #     leaderboard = self.leveler.get_leaderboard()
    #     description = ""
    #     for i in range(10):
    #         description += f"{i+1}. {leaderboard[i][0]} - Level {leaderboard[i][1]}\n"
    #     embed.description = description
    #     await ctx.respond(embed=embed)



    # @commands.slash_command(name="stalk", description="Shows the level stats of a user")
    # @option("username", description="Enter the username of the user you want to stalk", required=True)
    # @commands.guild_only()
    # async def stalk(self, ctx, username):
    #     embed = discord.Embed(color=0x00ff00)
    #     embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
    #     embed.set_author(name=ctx.author.name, icon_url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
    #     user = await self.bot.fetch_user(username)
    #     level = self.leveler.get_progress(user)
    #     embed.description = f"{user} is level {level[2]} with {level[0]}/{level[1]} xp to the next level"
    #     await ctx.respond(embed=embed)

    
    
            
    

def setup(bot):
    bot.add_cog(Levels(bot))
