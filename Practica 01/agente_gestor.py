import discord
from discord.ext import commands
import gestor_comando
import os
from dotenv import load_dotenv


load_dotenv()


# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Cuando el bot inicia
@bot.event
async def on_ready():
    print(f"Bot conectado correctamente como {bot.user}")


# Comando ayuda
@bot.command()
async def ayuda(ctx):
    respuesta = gestor_comando.analizar_comando("!ayuda")
    await ctx.send(respuesta)


# Comando hora
@bot.command()
async def hora(ctx):
    respuesta = gestor_comando.analizar_comando("!hora")
    await ctx.send(respuesta)


# Comando definir
@bot.command()
async def definir(ctx, *, termino):
    respuesta = gestor_comando.analizar_comando(f"!definir {termino}")
    await ctx.send(respuesta)


# Comando validar
@bot.command()
async def validar(ctx, *, nombre):
    respuesta = gestor_comando.analizar_comando(f"!validar {nombre}")
    await ctx.send(respuesta)


# Evita que ignore mensajes
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    await bot.process_commands(message)


# Iniciar bot
bot.run(os.getenv("DISCORD_TOKEN"))