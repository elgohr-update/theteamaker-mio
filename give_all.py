from discord.ext import commands

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