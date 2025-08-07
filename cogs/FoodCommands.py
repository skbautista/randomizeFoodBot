import discord
from discord import app_commands
from discord.ext import commands
import dbhandler as db

class FoodCommands(commands.Cog):
    def __init__(self, bot):
        self.database = db.database('Food.db')
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} cog is ready.")

    @app_commands.command(name="addresto", description="Add a restaurant to the collection")
    async def addresto(self, interaction: discord.Interaction, resto: str, rType: str | None):
        self.database.addFood(resto, rType)
        embedMsg = discord.Embed(title="Added a restaurant!")
        embedMsg.add_field(name="",
                           value="",
                           inline=True)
        await interaction.response.send_message(embedMsg)

    @app_commands.command(name="getresto", description='The bot will pick a food spot for you')
    async def getresto(self, interaction: discord.Interaction, rtype: str | None):
        restos = self.database.pickResto(rtype)
        if len(restos) == 0:
            embedMsg = discord.Embed(title=f"There are no '{rtype} restaurants.'")
            embedMsg.add_field(name=f"Types of restaurants available:", value=f"{self.database.getAllTypes()}")
            await interaction.response.send_message(embed=embedMsg)
        else:
            await interaction.response.send_message(f"Eat at '{restos}' !")

async def setup(bot):
    await bot.add_cog(FoodCommands(bot))

