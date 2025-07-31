import discord
from discord import app_commands
from discord.ext import commands

class FoodCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} cog is ready.")

    @app_commands.command(name="addfood", description="Add food to the bot's colleciton.")
    async def addfood(self, interaction: discord.Interaction, restaurant: str, type: str=None):
        await interaction.response.send_message("testing")

async def setup(bot):
    await bot.add_cog(FoodCommands(bot))

