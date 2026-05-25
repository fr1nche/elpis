import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.do_not_disturb,
        activity=discord.Game("Работаю...")
    )

    print(f"Бот {bot.user} запущен!")

# Приветствие новых участников
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel

    if channel:
        await channel.send(
            f"👋 Добро пожаловать на сервер, {member.mention}!"
        )

# Команда:
# !send Текст сообщения
# + прикреплённая картинка

@bot.command()
async def send(ctx, *, message):

    # Проверяем, прикреплено ли изображение
    if ctx.message.attachments:

        attachment = ctx.message.attachments[0]

        # Скачиваем файл
        file = await attachment.to_file()

        # Отправляем текст + изображение
        await ctx.send(
            content=message,
            file=file
        )

    else:
        # Если картинки нет — отправляем только текст
        await ctx.send(message)

bot.run("ВАШ ТОКЕН")