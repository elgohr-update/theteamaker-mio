import discord
from discord.ext import commands
from settings import PREFIX, TOKEN, PRIVATE_SERVER_ID, GENERAL_CHANNEL_ID, DEFAULT_ROLES, BOT_ROLE

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
        if member.bot is False:
            for role in DEFAULT_ROLES:
                try:
                    await member.add_roles(member.guild.get_role(role), atomic=True)
                except:
                    pass

            image = discord.File('hi.jpg', filename='hi.jpg', spoiler=False)
            await member.guild.get_channel(GENERAL_CHANNEL_ID).send(file=image)
        
        elif member.bot is True:
            try:
                await member.add_roles(member.guild.get_role(BOT_ROLE), atomic=True)
            except:
                pass

bot.run(TOKEN)