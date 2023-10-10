from discord.ext import commands
import discord
import requests

BOT_TOKEN = 'MTE1OTU2OTcyMTA3OTg5NDAzNw.GH3NfZ.EwAdAGY9KT96d3vXL41d_w-8BY229fQsTyec_E'
CHANNEL_ID = 1161395079156609206
#CHANNEL_ID = 1063696820657737769

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

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
    if colors == '':
        colors = 'Colorless'
    cmc = response["mana_cost"]
    spell_type = response["type_line"]
    oracle_text = response["oracle_text"]
    image = response["image_uris"]["large"]
    
    
    await ctx.send(f"**{name}**")
    await ctx.send(f"**TCGPLAYER:**\n{tcgplayer_link}")
    await ctx.send(f"**Price: **${price_usd}")
    await ctx.send(f"**Colors: **{colors}")
    await ctx.send(f"**CMC: **{cmc}")
    await ctx.send(f"**Spell Type: **{spell_type}")
    await ctx.send(f"**Text: **{oracle_text}")
    await ctx.send(f"{image}")
    
bot.run(BOT_TOKEN)