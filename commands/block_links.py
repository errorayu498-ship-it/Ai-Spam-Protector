import discord
from discord import app_commands
import json

class BlockLinks(discord.app_commands.Group):

    def __init__(self):
        super().__init__(name="block_link", description="Block links")

    @app_commands.command(name="add", description="Block a link")
    async def add(self, interaction: discord.Interaction, link: str):

        with open("data/links.json", "r") as f:
            data = json.load(f)

        link_id = str(len(data["blocked"]) + 500)

        data["blocked"][link_id] = link

        with open("data/links.json", "w") as f:
            json.dump(data, f, indent=4)

        await interaction.response.send_message(
            f"🚫 Blocked link added\nID: `{link_id}`\nLink: `{link}`"
        )
