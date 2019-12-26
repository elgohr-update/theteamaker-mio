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

# meant to auto-assign roles on my private server
@bot.event
async def on_member_join(member):
    PRIVATE_SERVER_ID = 656309437648338975
    GENERAL_CHANNEL_ID = 656309437648338978
    to_add = [
        659570001090576391, # DJ
        657786333959290880, # cool people
    ]

    if member.guild.id == PRIVATE_SERVER_ID:
        for role in to_add:
            await member.add_roles(member.guild.get_role(role), atomic=True)
    
        image = discord.File('hi.jpg', filename='hi.jpg', spoiler=False)
        await member.guild.get_channel(GENERAL_CHANNEL_ID).send(file=image)

setup(bot)
bot.run(TOKEN)