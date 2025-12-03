import asyncio

from telegram import Bot

from config.settings import TG_BOT_TOKEN, TG_CHAT_ID


bot = Bot(token=TG_BOT_TOKEN)

async def send(text):
    await bot.send_message(chat_id=TG_CHAT_ID, text=text)


def send_summary(summary):
    asyncio.run(send(summary))


if __name__=="__main__":
    send_summary("Testing how does the telegram bot work.")