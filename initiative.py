import random
from discord.ext import commands

class Initiative(commands.Cog):
    def __init__(self, bot, players):
        self.bot = bot
        self.players = players
    
    @commands.command()
    async def initiative(self, ctx):
        await ctx.send('Rolling...')
        for i in range(len(self.players)):
            x = random.randint(1,20)
            name = self.players[i].name
            await ctx.send(f'{name} rolled {x}')

        