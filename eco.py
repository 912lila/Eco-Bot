import discord
import random
import os
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

tipo_meme = ["programacion", "musica", "famosos"]    

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
    
    hi = ["https://tenor.com/view/hello-hi-minion-gif-13004117825953885603",
          "https://tenor.com/view/kermit-kermit-the-frog-hello-hello-everyone-muppets-gif-6287263276957406125",
          "https://tenor.com/view/jim-carrey-derp-hello-tape-gif-3190819386124687142",
          "https://tenor.com/view/mandalorian-baby-yoda-hello-gif-17841283562417351200"]
    await ctx.send(random.choice(hi))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def calculadora(ctx, operacion = "", num1 = 0, num2 = 0):
    if operacion  == "suma":
        resultado = num1 + num2

    elif operacion  == "resta":
        resultado = num1 - num2  

    elif operacion  == "multiplicacion" or operacion == "multiplicación":
        resultado = num1 * num2

    elif operacion  == "division" or operacion == "división":
        if num2 != 0:   
            resultado = num1 / num2

    else: 
        await ctx.send("Esta calculadora es de matemáticas básicas: + - x ÷")
        return

    await ctx.send(f"El resultado de tu {operacion} es: {resultado}")      

@bot.command()
async def moneda(ctx, flip = ""):
    flip = random.randint(0,2)
    if flip == 0:
        await ctx.send("CARA!!")
    else:
        await ctx.send("CRUZ!!") 

@bot.command()
async def frases_motivadoras(ctx):
    frases = [
                "No tengas miedo de fallar, ten miedo de no intentarlo",
                "Cree en ti mismo, el mundo necesita tu luz",
                "El éxito no es definitivo; el fracaso no es fatal. Lo que realmente cuenta es tener valor para continuar",
                "Ganar es difícil, pero nunca imposible",
                "Si creo y confío en mí mismo, podré conseguir todos mis objetivos",
                "No importa lo lento que vayas, siempre y cuando no te detengas",
                "La vida nos enseña muchas leciones depende de nosotros aprenderlas",
                "Haz de cada día una obra maestra",
                "Deséalo, espéralo, suéñalo, pero por todos los medios… ¡Hazlo!",
                "Si siempre te concentras en lo que te falta, nunca tendrás lo suficiente",
                "Hasta que no te valores a ti mismo, no valorarás tu tiempo. Hasta que no valores tu tiempo, no harás nada con él"]    
    await ctx.send(random.choice(frases))


@bot.command()
async def meme(ctx,*,tipo:str):
    lista = os.listdir("img")
    

    imgenviar = random.choice(lista)

    with open(f"img/{imgenviar}", "rb") as f:

        imagen = discord.File(f)

    await ctx.send(file = imagen)    

@bot.command()
async def bye(ctx):
    await ctx.send("https://tenor.com/view/bai-see-you-later-bye-adios-got-to-go-gif-21054483")   

@bot.command()
async def musica(ctx):
    await ctx.send("https://youtu.be/6Mgqbai3fKo?si=8vLmsuFmB5I6hdEE")     

@bot.command()
async def ayuda(ctx):
    comandos = """Comandos: 
    -hello: Saludo👋 del bot
    -heh: El bot🤖 te dira "he" repetido el número de veces que indiques
    -calculadora: Realiza operaciones matematicas basicas + - x ÷
    -moneda: Lanza una moneda (cara o cruz)
    -frases_motivadoras: El bot🤖 te envia una frase motivacional 
    -meme: El bot🤖 te envia un meme"""
    await ctx.send(comandos)

bot.run("TOKEN") 
