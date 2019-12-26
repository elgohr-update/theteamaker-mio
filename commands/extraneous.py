from discord.ext import commands

def setup(bot):
    bot.add_cog(Pleasantry(bot))
    bot.add_cog(Hakase(bot))
    bot.add_cog(Hi(bot))
    bot.add_cog(Give_All(bot))

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

class Give_All(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def give_all(self, ctx, *, arg):
        for role in ctx.guild.roles:
            if role.name == arg:
                to_add = role
                break
    
        try:
            for member in ctx.guild.members:
                if member.id != ctx.guild.owner_id:
                    try:
                        await member.add_roles(to_add, atomic=True)
                    except Exception as e:
                        print(e)
            await ctx.send(f"All users have successfully been given the **{arg}** role!")
        except Exception as e:
            await ctx.send("Something went wrong! Let eva know.")
            raise e
