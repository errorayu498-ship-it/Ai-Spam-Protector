import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from link_detector import extract_links, is_allowed
from ai_filter import check_message
from warning_system import add_warning
from config import CONFIG
from commands.show_info import ShowInfo

@bot.event
async def setup_hook():
    await bot.add_cog(ShowInfo(bot))


load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    links = extract_links(message.content)

    blocked = False

    for link in links:

        if not is_allowed(link):
            blocked = True

    ai_result = await check_message(message.content)

    if blocked or "BLOCK" in ai_result:

        await message.delete()

        warn = await add_warning(message.author)

        timeout = CONFIG["timeout_levels"].get(warn)

        if timeout:
            await message.author.timeout(
                discord.utils.utcnow() + discord.timedelta(seconds=timeout)
            )

        try:
            await message.author.send(
                f"You received warning {warn}/3 for posting prohibited content."
            )
        except:
            pass

    await bot.process_commands(message)

bot.run(os.getenv("BOT_TOKEN"))
