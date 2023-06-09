from datetime import timedelta
import datetime
import time
import discord
from discord.ext import commands
from discord import option
from discord.ui import View, button
from utils.SIU import RonaldoHimself
from discord.utils import get
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
    @option("username", description="Enter the username of the user you want to stalk", required=False, type=discord.User)
    async def level(self, ctx, username):
        if username != None:
            embed = discord.Embed(color=0x00ff00)
            embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
            level = await self.leveler.get_progress(username.id)
            rank = await self.leveler.get_rank(username.id)
            embed.set_author(name=username.name+f" rank #{rank[0]} siu rank #{rank[1]}", icon_url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
            if level == False:
                await ctx.respond("0 messages sent")
                return
            siu_ratio = [(level[3]/level[5]),level[3],level[5]]
            embed.description = f"@{username.name} is level {level[2]} with {level[0]}/{level[1]} xp to the next level"
            embed.add_field(name=f"SIU ratio: {siu_ratio[0]:0.2f}%", value=f"times SUIed: {siu_ratio[1]}, total messages: {siu_ratio[2]}", inline=False)
            await ctx.respond(embed=embed)

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
        
    @commands.slash_command(name="leaderboard", description="Shows the top 10 players")
    async def leaderboard(self, ctx):
        embed = discord.Embed(color=0x00ff00)
        embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
        guild = ctx.guild
        leaderboard = self.leveler.get_leaderboard()  # Assuming this retrieves the global leaderboard
        member_list = guild.members
        member_names = []
        for member in member_list:
            member_names.append(member.name)
        filtered_leaderboard = []
        for x in leaderboard:
            if x[0] in member_names:
                filtered_leaderboard.append(x)
        description = ""
        for i in range(len(filtered_leaderboard)):
            description += f"{i+1}. {filtered_leaderboard[i][0]} - Level {filtered_leaderboard[i][1]}\n"
        
        embed.description = description
        await ctx.respond(embed=embed)

    @commands.slash_command(name="siu_leaders", description="Shows the top 10 players")
    async def siu_leaderboard(self, ctx):
        embed = discord.Embed(color=0x00ff00)
        embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
        guild = ctx.guild
        leaderboard = self.leveler.get_leaderboard_siu()  # Assuming this retrieves the global leaderboard
        member_list = guild.members
        member_names = []
        for member in member_list:
            member_names.append(member.name)
        filtered_leaderboard = []
        for x in leaderboard:
            if x[0] in member_names:
                filtered_leaderboard.append(x)
        description = ""
        for i in range(len(filtered_leaderboard)):
            description += f"{i+1}. {filtered_leaderboard[i][0]} - SIU count: {filtered_leaderboard[i][1]}\n"
        embed.description = description
        await ctx.respond(embed=embed)
        return


    @commands.slash_command(name="global_leaders", description="Global leaderboards")
    async def g_leaderboard(self, ctx):
        embed = discord.Embed(color=0x00ff00)
        embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
        leaderboard = self.leveler.get_leaderboard()
        description = ""
        for i in range(len(leaderboard)):
            description += f"{i+1}. {leaderboard[i][0]} - Level {leaderboard[i][1]}\n"
        embed.description = description
        await ctx.respond(embed=embed)


    # @commands.slash_command(name="levels_test", description="Shows the top 10 players")
    # async def levels_test(self, ctx):
    #     pass
    
            
    

def setup(bot):
    bot.add_cog(Levels(bot))
