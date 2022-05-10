import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token='5381772852:AAGKAXhbx6oSKUh677ztEPTsh_x8-ZBDktY')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)

