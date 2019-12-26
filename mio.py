import discord
from discord.ext import commands
from settings import PREFIX, TOKEN

# cog importing #
from give_all import Give_All
from extraneous import Hakase, Pleasantry, Hi
from pet_database import Add_Pet, Gen_Pet, Delete_Pet, List_Pet, Custom_Pet

bot = commands.Bot(command_prefix=PREFIX)

cogs = [
    Give_All(bot),
    Hakase(bot),
    Pleasantry(bot),
    Hi(bot),
    Add_Pet(bot),
    Gen_Pet(bot),
    Delete_Pet(bot),
    List_Pet(bot),
    Custom_Pet(bot)
    ]

def setup(bot):
    for cog in cogs:
        bot.add_cog(cog)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

setup(bot)
bot.run(TOKEN)