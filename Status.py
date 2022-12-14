from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_prince():
    async with app:
            while True:
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_prince = f"π ππππ π½ππ πππΌπππ\n\n**π¬ {CHANNEL_OR_GROUP_TYPE}**: {CHANNEL_OR_GROUP_NAME}"
                for bot in BOT_LIST:
                    try:
                        yyy_prince = await app.send_message(bot, "/start")
                        aaa = yyy_prince.message_id
                        await asyncio.sleep(10)
                        zzz_prince = await app.get_history(bot, limit = 1)
                        for ccc in zzz_prince:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            xxx_prince += f"\n\nπ€ **BOT**: @{bot}\nπ΄ **STATUS**: down β"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"π¨ **Beep! Beep!! @{bot} is down** β")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            xxx_prince += f"\n\nπ€ **BOT**: @{bot}\nπ’ **STATUS**: alive β"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_prince += f"\n\nβοΈ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>β»οΈ Updates every 45min</i> - Made By [Dα΄α΄ α΄Κα΄α΄α΄Κπ₯](https://t.me/sup3rst4r_op) π"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_prince)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(2700)
                        
app.run(main_prince())
