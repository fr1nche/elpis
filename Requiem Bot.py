import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    description="🤖 Я крутой Discord бот!" 
)

@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.do_not_disturb,
        activity=discord.Game("GTA 5 RP | Murrieta") 
    )

    print(f"Бот {bot.user} запущен!")

bot.run("Ваш токен")