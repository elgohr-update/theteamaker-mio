import discord
from discord.ext import commands
from settings import PREFIX, TOKEN
import dataset

bot = commands.Bot(command_prefix=PREFIX)

@bot.command()
@commands.is_owner()
async def give_all(ctx, *, arg):
    for role in ctx.guild.roles:
        if role.name == arg:
            to_add = role
            break
    
    try:
        for member in ctx.guild.members:
            if member.id != guild.owner_id:
                try:
                    await member.add_roles(to_add, atomic=True)
                except Exception as e:
                    print(e)
        await ctx.send(f"All users have successfully been given the **{arg}** role!")
    except:
        await ctx.send("Something went wrong! Let eva know.")

# two very cool images #

@bot.command()
async def pleasantry(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/659498703173845003/659498920619278360/28129Mai.jpg")

@bot.command()
async def hakase(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/659498703173845003/659580391975419915/s7OJm5d.jpg")

@bot.command()
async def hi(ctx):
    await ctx.send("hi")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

bot.run(TOKEN)