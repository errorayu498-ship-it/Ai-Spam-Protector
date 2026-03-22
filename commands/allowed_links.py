import discord
from discord import app_commands
import json

class AllowedLinks(discord.app_commands.Group):

    def __init__(self):
        super().__init__(name="allowed_links", description="Manage allowed links")

    @app_commands.command(name="add", description="Allow a new link")
    async def add(self, interaction: discord.Interaction, link: str):

        with open("data/links.json", "r") as f:
            data = json.load(f)

        link_id = str(len(data["allowed"]) + 100)

        data["allowed"][link_id] = link

        with open("data/links.json", "w") as f:
            json.dump(data, f, indent=4)

        await interaction.response.send_message(
            f"Allowed link added\nID: `{link_id}`\nLink: `{link}`"
        )
