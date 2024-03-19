import asyncio

from os import getenv
from dotenv import load_dotenv
from SpotifyGetTrack import get_track

from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, F
from aiogram.utils.markdown import hbold
from aiogram.filters import CommandStart, Command


load_dotenv()
bot_token = getenv("BOT_TOKEN")
spotify_clinet_id = getenv("SPOTIFY_CLIENT_ID")
spotify_clinet_secret = getenv("SPOTIFY_CLIENT_SECRET")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(F.text, Command("music"))
async def send_music(message: Message):
    await message.answer(f"Your track is: {get_track(spotify_clinet_id, spotify_clinet_secret)}")


async def main():
    bot = Bot(bot_token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
