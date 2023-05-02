# This example requires the 'members' privileged intent to use the Member converter.

import os
import discord
import config
from utils.leveling import LevelerDB


intents = discord.Intents.all()
intents.members = True

bot = discord.Bot(intents=intents)
leveler = LevelerDB()

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")
# bot.load_extension("cogs.levels")
# bot.load_extension("cogs.SIUCOG")
# bot.load_extension("cogs.info")

siucog = bot.get_cog("SIU")
siucog.leveler = leveler
levels = bot.get_cog("Levels")
levels.leveler = leveler

# for x in bot.cogs:
#     print(x)

# siucog = bot.get_cog("SIU")
# siucog.leveler = leveler
# levels = bot.get_cog("Levels")
# levels.leveler = leveler

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(f"Bot ID: {bot.user.id}")

@bot.slash_command()
async def joined(ctx: discord.ApplicationContext, member: discord.Member = None):
    # Setting a default value for the member parameter makes it optional ^
    user = member or ctx.author
    await ctx.respond(
        f"{user.name} joined at {discord.utils.format_dt(user.joined_at)}"
    )

@bot.slash_command()
async def bot_joined(ctx: discord.ApplicationContext):
    await ctx.respond(
        f"I joined at {discord.utils.format_dt(bot.user.joined_at)}"
    )

# To learn how to add descriptions and choices to options, check slash_options.py
bot.run(config.client_discord_token)