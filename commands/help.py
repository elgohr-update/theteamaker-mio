from discord.ext import commands
import discord

def setup(bot):
    bot.add_cog(Help(bot))

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        """this command!"""
        embed = discord.Embed(title="Help")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        for command in self.bot.commands:
            embed.add_field(name=command.name, value=command.help, inline=False)
        
        await ctx.send(embed=embed)