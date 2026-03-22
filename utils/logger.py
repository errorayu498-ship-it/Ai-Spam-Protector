import discord
from config import CONFIG

async def log_action(bot, guild, message):

    channel = guild.get_channel(CONFIG["log_channel"])

    if not channel:
        return

    embed = discord.Embed(
        title="Moderation Log",
        description=message,
        color=discord.Color.red()
    )

    await channel.send(embed=embed)
