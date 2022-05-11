import nextcord

client = nextcord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.author, message.content)        
    if 'candice' in message.content.lower():
        await message.channel.send('Can dis nuts fit in your mouth')
    elif 'fitness' in message.content.lower():
        await message.channel.send('fit this dick')
    elif 'parody' in message.content.lower():
        await message.channel.send('pair of deez nuts')
    elif 'parodies' in message.content.lower():
        await message.channel.send('pair of deez nuts')
    elif 'sea of thieves' in message.content.lower():
        await message.channel.send('see if theese nuts fit in your mouth')
    elif 'plant' in message.content.lower():
        await message.channel.send('plant deez nuts')
    elif 'e10' in message.content.lower():
        await message.channel.send('eatin these nuts')
    elif 'ukelele' in message.content.lower():
        await message.channel.send('you can lay these nuts')
    elif 'dn' in message.content.lower():
        await message.channel.send('Deez Nuts')
    elif 'decide' in message.content.lower():
        await message.channel.send('dis side of this dick')
    elif 'dragon' in message.content.lower():
        await message.channel.send('dragin deez nuts')
    elif 'goblin' in message.content.lower():
        await message.channel.send('goblin deez nuts')
    elif 'pudding' in message.content.lower():
        await message.channel.send('pudding deez nuts')
    elif 'milo' in message.content.lower():
        await message.channel.send(' my load in your mouth')
    elif 'omelette' in message.content.lower():
        await message.channel.send('oma let deez nuts in your mouth')
    elif 'kombucha' in message.content.lower():
        await message.channel.send('come put cha mouth on deez nuts')
    elif 'candies' in message.content.lower():
        await message.channel.send('can these nuts fit in your mouth')
    elif 'bofa' in message.content.lower():
        await message.channel.send('bofa deez nuts')
        
client.run('')
diagnostics and repair 
