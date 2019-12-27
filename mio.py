import discord
from discord.ext import commands
from settings import PREFIX, TOKEN

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command('help')

COGS = ['extraneous', 'pet_database', 'help']

for cog in COGS:
    bot.load_extension(f"commands.{cog}")

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

bot.run(TOKEN)