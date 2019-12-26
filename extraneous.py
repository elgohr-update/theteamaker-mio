from discord.ext import commands

# Commands to generate pleasantry and hakase images!

class Pleasantry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pleasantry(self, ctx, *, arg):
        await ctx.send("https://cdn.discordapp.com/attachments/659498703173845003/659498920619278360/28129Mai.jpg")

class Hakase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hakase(self, ctx, *, arg):
        await ctx.send("https://cdn.discordapp.com/attachments/659498703173845003/659580391975419915/s7OJm5d.jpg")


# say hi
class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hi(self, ctx):
        await ctx.send(f"hi, {ctx.author.nick}!")
