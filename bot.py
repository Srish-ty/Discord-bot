import asyncio
import os
from itertools import cycle
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix=["/", "<@!994664955305533602> ",
                                   "<@994664955305533602> "], case_insensitive=True, intents=intents,
                   owner_ids=[773902563476897812])


@bot.event
async def on_ready():
    print("Bot is ready")
    guild = bot.get_guild(GUILD)
    print(guild.members)
    mem = len(guild.members)
    statuses = cycle([f"{mem} Members!", "h!help"])
    while not bot.is_closed():
        status = next(statuses)
        activity = discord.Activity(
            type=discord.ActivityType.watching, name=status)
        await bot.change_presence(status=discord.Status.dnd, activity=activity)
        await asyncio.sleep(20)


bot.remove_command("help")
bot.start_time = int(time.time())


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded {filename}")
            except commands.ExtensionAlreadyLoaded:
                pass
            except Exception as e:
                print(e)


async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


asyncio.run(main())
