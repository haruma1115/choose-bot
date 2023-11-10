import discord
from discord.ext import commands
import random

# 創建 Discord intents，啟用所有意向，但停用 typing 和 presences 意向
intents = discord.Intents.all()
intents.typing = False
intents.presences = False

# 創建機器人實例，指定指令前綴為 'd!'，並傳遞 intents
bot = commands.Bot(command_prefix='!', intents=intents)

# 預先設定的三個選項
predefined_options = ["選項1", "選項2", "選項3"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def choose(ctx, *additional_options):
    # 將預先設定的選項和使用者提供的額外選項合併成一個列表
    options = predefined_options + list(additional_options)
    
    # 如果選項數量小於 2，回應提示訊息
    if len(options) < 2:
        await ctx.send("請提供至少兩個選項！")
    else:
        # 從選項中隨機選擇一個，並回應到同一頻道
        chosen_option = random.choice(options)
        await ctx.send(f'{chosen_option}')

# 使用你的機器人令牌啟動機器人
bot.run('token')
