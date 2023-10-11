from discord.ext import commands
import discord
import requests

BOT_TOKEN = PERSONAL
CHANNEL_ID = PERSONAL
CHANNEL_ID = PERSONAL


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Hello! Shiyoko desu!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Shiyoko desu!")
    
@bot.command()
async def card(ctx, *names):
    api_url = "https://api.scryfall.com/cards/named?fuzzy="
    for i in range(len(names)):
        if i == len(names)-1:
            api_url += names[i]
        else:
            api_url += names[i]
            api_url += "+"
    response = requests.get(api_url)
    response = response.json()
    
    name = response["name"]
    tcgplayer_link = response["purchase_uris"]["tcgplayer"]
    price_usd = response["prices"]["usd"]
    colors = response["color_identity"]
    if colors == []:
        colors = 'Colorless'
    cmc = response["mana_cost"]
    spell_type = response["type_line"]
    oracle_text = response["oracle_text"]
    image = response["image_uris"]["large"]
    
    embed=discord.Embed()
    
    embed.set_thumbnail(url=image)
    embed.add_field(name=f"**{name}**", value="", inline=False)
    embed.add_field(name="**TCGPlayer**", value=f"{tcgplayer_link}", inline=False)
    embed.add_field(name="**Price**", value=f"${price_usd}", inline=False)
    embed.add_field(name="**Colors**", value=f"{colors}", inline=False)
    embed.add_field(name="**CMC**", value=f"{cmc}", inline=False)
    embed.add_field(name="**Spell Type**", value=f"{spell_type}", inline=False)
    embed.add_field(name="**Text**", value=f"{oracle_text}", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.event
async def on_message(message):
    if "[" and "]" in message.content:
        start = message.content.find('[')+1
        end = message.content.find(']', start)
        names = message.content[start:end]
        names = names.split()
        
        api_url = "https://api.scryfall.com/cards/named?fuzzy="
        for i in range(len(names)):
            if i == len(names)-1:
                api_url += names[i]
            else:
                api_url += names[i]
                api_url += "+"
        response = requests.get(api_url)
        response = response.json()
        
        name = response["name"]
        tcgplayer_link = response["purchase_uris"]["tcgplayer"]
        price_usd = response["prices"]["usd"]
        colors = response["color_identity"]
        if colors == []:
            colors = 'Colorless'
        cmc = response["mana_cost"]
        spell_type = response["type_line"]
        oracle_text = response["oracle_text"]
        image = response["image_uris"]["large"]
        
        embed=discord.Embed()
        
        embed.set_thumbnail(url=image)
        embed.add_field(name=f"**{name}**", value="", inline=False)
        embed.add_field(name="**TCGPlayer**", value=f"{tcgplayer_link}", inline=False)
        embed.add_field(name="**Price**", value=f"${price_usd}", inline=False)
        embed.add_field(name="**Colors**", value=f"{colors}", inline=False)
        embed.add_field(name="**CMC**", value=f"{cmc}", inline=False)
        embed.add_field(name="**Spell Type**", value=f"{spell_type}", inline=False)
        embed.add_field(name="**Text**", value=f"{oracle_text}", inline=False)
        
        await message.channel.send(embed=embed)
        
    await bot.process_commands(message)
        
bot.run(BOT_TOKEN)