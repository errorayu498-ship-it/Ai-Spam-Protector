import discord
from discord import app_commands
import json

class ShowInfo(discord.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="show_info", description="Show bot info")
    async def show_info(self, interaction: discord.Interaction):

        with open("data/links.json", "r") as f:
            data = json.load(f)

        allowed = "\n".join(
            [f"{i} → {v}" for i, v in data["allowed"].items()]
        )

        blocked = "\n".join(
            [f"{i} → {v}" for i, v in data["blocked"].items()]
        )

        embed = discord.Embed(
            title="SARAIKI Ai Guard Bot Info",
            color=discord.Color.green()
        )

        embed.add_field(name="Allowed Links", value=allowed or "None", inline=False)
        embed.add_field(name="Blocked Links", value=blocked or "None", inline=False)

        embed.set_footer(text="AI Moderation System Active")

        await interaction.response.send_message(embed=embed)
