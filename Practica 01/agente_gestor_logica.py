import discord
from discord.ext import commands
import agente_logica
import os
from dotenv import load_dotenv


load_dotenv()


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Bot conectado correctamente como {bot.user}")


@bot.command()
async def ayuda(ctx):
    respuesta = agente_logica.analizar_comando("!ayuda")
    await ctx.send(respuesta)


@bot.command()
async def definir(ctx, *, termino):
    respuesta = agente_logica.analizar_comando(f"!definir {termino}")
    await ctx.send(respuesta)


@bot.command()
async def validar(ctx, *, nombre):
    respuesta = agente_logica.analizar_comando(f"!validar {nombre}")
    await ctx.send(respuesta)


@bot.command()
async def hora(ctx):
    respuesta = agente_logica.analizar_comando("!hora")
    await ctx.send(respuesta)


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    await bot.process_commands(message)


bot.run(os.getenv("DISCORD_TOKEN"))