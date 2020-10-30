import discord
import image

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$start'):
        image_name = image.generate_image()
        await message.channel.send(file=discord.File('./assets/generated/' + image_name + '.png'))

@client.event
async def on_reaction_add(reaction, user):
    if str(reaction) == '➡️':
        image_name = image.move_token('right')
        await reaction.message.channel.send(file=discord.File('./assets/generated/' + image_name + '.png'))

client.run('😪')