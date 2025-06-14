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
        def create_embed(user, level, rank, siu_ratio)-> discord.Embed:
            embed = discord.Embed(color=0x00ff00)
            gif_url = "https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif"
            embed.set_thumbnail(url=gif_url)
            embed.set_author(name=user.name+f" rank #{rank[0]} siu rank #{rank[1]}", icon_url=gif_url)
            if level == False:
                embed.description = "0 messages sent"
                return False
            siu_ratio = [(level[3]/level[5]),level[3],level[5]]
            embed.description = f"@{user.name} is level {level[2]} with {level[0]}/{level[1]} xp to the next level"
            embed.add_field(name=f"SIU ratio: {siu_ratio[0]:0.2f}%", value=f"times SUIed: {siu_ratio[1]}, total messages: {siu_ratio[2]}", inline=False)
            return embed
        
        if username != None:
            level = await self.leveler.get_progress(username.id)
            rank = await self.leveler.get_rank(username.id)
            embed = create_embed(username, level, rank, None)
            if not embed:
                await ctx.respond("0 messages sent")
                return
            else:
                await ctx.respond(embed=embed)
        else:
            level = await self.leveler.get_progress(ctx.author.id)
            rank = await self.leveler.get_rank(ctx.author.id)
            embed = create_embed(ctx.author, level, rank, None)
            if not embed:
                await ctx.respond("0 messages sent")
                return
            else:
                await ctx.respond(embed=embed)
        return

    def generate_leaderboard_embed(self, title, color, thumbnail_url, guild, leaderboard, field_name):
        embed = discord.Embed(title=title, color=color)
        embed.set_thumbnail(url=thumbnail_url)
        member_ids = []
        for member in guild.members:
            member_ids.append(int(member.id))
        filtered_leaderboard = []
        
        for leader in leaderboard:
            if int(leader[0]) in member_ids:
                filtered_leaderboard.append((guild.get_member(int(leader[0])).display_name, leader[1]))
        description = ""
        for i, (name, value) in enumerate(filtered_leaderboard):
            description += f"{i+1}. {name} - {field_name} {value}\n"
        embed.description = description
        return embed
        
    @commands.slash_command(name="leaderboard", description="Shows the top 10 players")
    async def leaderboard(self, ctx):
        guild = ctx.guild
        leaderboard = self.leveler.get_leaderboard()  # Assuming this retrieves the global leaderboard
        embed = self.generate_leaderboard_embed("Global Leaderboard", 0x00ff00, "https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif", guild, leaderboard, "Level")
        await ctx.respond(embed=embed)
        return 

    @commands.slash_command(name="siu_leaders", description="Shows the top 10 players")
    async def siu_leaderboard(self, ctx):
        guild = ctx.guild
        leaderboard = self.leveler.get_leaderboard_siu()  # Assuming this retrieves the global leaderboard
        embed = self.generate_leaderboard_embed("Global SIU Leaderboard", 0x00ff00, "https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif", guild, leaderboard, "SIU count")
        await ctx.respond(embed=embed)
        return
    
    @commands.slash_command(name="global_leaders", description="Global leaderboards")
    async def g_leaderboard(self, ctx):
        embed = discord.Embed(color=0x00ff00)
        embed.set_thumbnail(url="https://media.tenor.com/nDP41DutB9QAAAAS/cr7-siu.gif")
        leaderboard = self.leveler.get_leaderboard()
        description = ""
        for i in range(len(leaderboard)):
            description += f"{i+1}. {self.bot.get_user(int(leaderboard[i][0])).name.split('#')[0]} - Level {leaderboard[i][1]}\n"
        embed.description = description
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Levels(bot))
