import discord
import settings

from discord.ext import commands
from music import Music
from initiative import Initiative
from models.player import Player

settings = settings.get_settings()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='The DMBot')

all_players = []
# Set up players
with open('players.txt', 'r') as players:
    for player in players:
        player_attributes = player.split(':')
        player = Player()
        player.name = player_attributes[0]
        player.class_name = player_attributes[1]
        all_players.append(player)


@bot.event
async def on_ready():
    print('😎powering up portals online😎')

bot.add_cog(Music(bot))
bot.add_cog(Initiative(bot, all_players))
bot.run(settings['discord_token'])