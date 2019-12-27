import discord
from discord.ext import commands
from settings import PREFIX, TOKEN, PRIVATE_SERVER_ID, GENERAL_CHANNEL_ID, DEFAULT_ROLES

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
    if member.guild.id == PRIVATE_SERVER_ID:
        for role in to_add:
            try:
                await member.add_roles(member.guild.get_role(role), atomic=True)
            except:
                pass
        
        image = discord.File('hi.jpg', filename='hi.jpg', spoiler=False)
        await member.guild.get_channel(GENERAL_CHANNEL_ID).send(file=image)

bot.run(TOKEN)