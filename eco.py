import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "/", intents = intents)

@bot.event
async  def on_ready():
    print(f"Se inicio como {bot.user}")

ideas = ["1.Usa botellas de plástico vacías, latas🥫 o cajas de cartón📦 para hacer macetas🌱", "2.Haz papel📄 reciclado♻ a partir de periódicos📰 viejos o hojas usadas📃", "3.Usa cajas📦 de cereales🥣 o cajas📦 de zapatos👞 para hacer organizadores de escritorio o estantes pequeños", "4. Convierte frascos de vidrio en lámparas decorativas colocando una luz💡 LED dentro ", "5.Reúne palitos de helado🍦 limpios y pégalos para formar marcos de fotos🎞"]

reciclables = ["botella de plastico", "papel","carton"]
basura = ["empaques de papitas", "copitos","jeringas"]

frases = ["Separa tus desechos y recicla♻ siempre que puedas.", "Usa bombillas💡 LED, son más eficientes y duran más que las incandescentes.", "Crea un jardín🌱, cultiva tus propias plantas🌷 o verduras🍅.", "Anima a otros a usar bicicletas🚲 para desplazamientos cortos.","Informa a otros sobre la importancia de cuidar el medio ambiente🌎.", "Reduce el consumo de energía⚡, desconecta los dispositivos📱 que no estés usando"]

materiales = ["papel", "vidrio", "bolsa de plastico", "botella de plastico", "pilas", "chicle", "poliestireno", "lata", "globo"]
tiempo = ["2 a 5 meses", "indefinido(puede tardar 4.000 años o más)", "150 a 500 años", "100 a 1,000 años", "500 a 1,000 años", "5 años", "Más de 1,000 años", "10 a 100 años", "6 meses (látex) hasta varios años (plástico)"]

comandos = """Comandos: 
-manualidades: El bot🤖 te dira ideas de manualidades con materiables reciclables♻
-clasificar: Clasifica objetos como reciclables♻ o no🚫 reciclables♻
-descomposicion: El bot🤖 te dira el tiempo🕑 de descomposicion de ciertos materiales
-consejos: El bot🤖 te dira un consejo para ayudar al medio ambiente🌎"""

@bot.command()
async def manualidades(ctx):
    await ctx.send(random.choice(ideas))

@bot.command()
async def clasificar(ctx,*,objeto:str):

    if objeto in reciclables:
        await ctx.send(f"El objeto {objeto} es reciclable♻")

    elif objeto in basura:
        await ctx.send(f"El objeto {objeto} no🚫 es reciclable♻")

    else:
        await ctx.send("Aun no estoy entrenado para identificar el objeto")

@bot.command()
async def descomposicion(ctx,*,material:str):
    material = material.lower()
    found = False

    for i in range(len(materiales)):
        if materiales[i] == material:
            await ctx.send(f"El tiempo de descomposición de {material} es: {tiempo[i]}.")
            found = True
            break

    if not found:
        await ctx.send("No tengo información sobre este material.")   

@bot.command()
async def consejos(ctx):
    await ctx.send(random.choice(frases))

@bot.command()
async def ayuda(ctx):
    await ctx.send(comandos)

    

bot.run("TOKEN")    

