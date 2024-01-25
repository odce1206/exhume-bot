from typing import Final
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from exhume import chargen
from modelos.char import Char
import dice

# STEP 0:
conf = load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running')


@bot.command()
async def exchar(ctx):
    personaje: Char = chargen()
    embed = discord.Embed(title=f"{personaje.charName}, {personaje.titulo}", colour=10038562)
    embed.add_field(name="Puntos de Vida: ", value=personaje.hp, inline=False)
    embed.add_field(name="Clase: ", value=personaje.tipo, inline=False)
    embed.add_field(name="Habilidad Especial: ", value=personaje.habEsp, inline=False)
    embed.add_field(name=":crossed_swords:  Fuerza: ", value=personaje.fuerza, inline=True)
    embed.add_field(name="\U0001F3C3 Destreza: ", value=personaje.destreza, inline=True)
    embed.add_field(name="\U0001F9D9 Voluntad: ", value=personaje.voluntad, inline=True)
    embed.set_thumbnail(url="https://img.itch.zone/aW1nLzk2ODg0NjIuanBn/original/0mcSPG.jpg")
    embed.set_author(name= "🎲 Exhume ", url = "https://rolepersecond.itch.io/exhume-esp-micro-fantasy-rpg")
    embed.set_footer(text="Bot Generador de PJs por: sudojar | Exhume por: Irvin Morales", icon_url="https://www.iconsdb.com/icons/preview/white/wizard-xxl.png")
    await ctx.send(embed=embed)


@bot.command()
async def roll(ctx, roll: str):
    await ctx.send(dice.roll(roll))

def main() -> None:
    # client.add_command(exchar)
    bot.run(token = TOKEN)
