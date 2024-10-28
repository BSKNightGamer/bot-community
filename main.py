import os
import discord
from discord.ext import commands
from discord import app_commands
import time

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

start_time = time.time()

# //////////////////// Bot Event /////////////////////////
# คำสั่ง bot พร้อมใช้งานแล้ว
@bot.event
async def on_ready():
    print("Bot Online!")
    print("555")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")




# แจ้งคนเข้า -ออกเซิฟเวอร์

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1300087037906387017) # IDห้อง
    text = f"Welcome to the server, {member.mention}!"

    emmbed = discord.Embed(title = 'Welcome to the server!',
                           description = text,
                           color = 0x66FFFF)

    await channel.send(text) # ส่งข้อความไปที่ห้องนี้
    await channel.send(embed = emmbed)  # ส่ง Embed ไปที่ห้องนี้
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัวของ member


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1300087037906387017)  # IDห้อง
    text = f"{member.name} has left the server!"
    await channel.send(text)  # ส่งข้อความไปที่ห้องนี้



# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'hello':
        await message.channel.send("Hello It's me") # ส่งกลับไปที่ห้องนั่น

    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)
    # ทำคำสั่ง event แล้วไปทำคำสั่ง bot command ต่อ




# ///////////////////// Commands /////////////////////
# กำหนดคำสั่งให้บอท

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}!")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


# Slash Commands
@bot.tree.command(name='hellobot', description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message("Hello It's me BOT DISCORD")


@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")

@bot.tree.command(name='uptime')
async def uptimecommand(interaction):

    current_time = time.time()
    uptime_seconds = int(current_time - start_time)
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    embed = discord.Embed(title="💮 𝗪𝗘𝗡𝗗𝗬 𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬",
                        description=f"> **บอทออนไลน์มากี่ชั่วโมงแล้ว**\n\n> `✅ {hours} ชั่วโมง | {minutes} นาที | {seconds} วินาที`",
                        colour=0xff00ff)

    embed.set_footer(text="💮 𝗪𝗘𝗡𝗗𝗬 𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬")

    await interaction.response.send_message(embed = embed)

# Embeds

@bot.tree.command(name='help', description='Bot Commands')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='Help Me! - Bot Commands',
                           description='Bot Commands',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())


    # ใส่ข้อมูล
    emmbed.add_field(name='/hello1', value='Hello Commmand', inline=True)
    emmbed.add_field(name='/hello2', value='Hello Commmand', inline=True)
    emmbed.add_field(name='/hello3', value='Hello Commmand', inline=False)

    emmbed.set_author(name='Author', url='https://www.youtube.com/@maoloop01/channels', icon_url='https://yt3.googleusercontent.com/0qFq3tGT6LVyfLtZc-WCXcV9YyEFQ0M9U5W8qDe36j2xBTN34CJ20dZYQHmBz6aXASmttHI=s900-c-k-c0x00ffffff-no-rj')

    # ใส่รูปเล็ก-ใหญ่
    emmbed.set_thumbnail(url='https://yt3.googleusercontent.com/0qFq3tGT6LVyfLtZc-WCXcV9YyEFQ0M9U5W8qDe36j2xBTN34CJ20dZYQHmBz6aXASmttHI=s900-c-k-c0x00ffffff-no-rj')
    emmbed.set_image(url='https://i.ytimg.com/vi/KZRa9DQzUpQ/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCfWDgiBYjFJtrUasd5yxmQZJG_cg')

    # Footer เนื้อหาส่วนท้าย
    emmbed.set_footer(text='Footer', icon_url='https://yt3.googleusercontent.com/0qFq3tGT6LVyfLtZc-WCXcV9YyEFQ0M9U5W8qDe36j2xBTN34CJ20dZYQHmBz6aXASmttHI=s900-c-k-c0x00ffffff-no-rj')

    await interaction.response.send_message(embed = emmbed)


server_on()

# os.getenv('TOKEN')

bot.run(os.getenv('TOKEN'))
