import config
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

#Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
#@dp.message()
#async def echo(message: types.Message):
 #   await message.answer(message.text)

#Создание функции, чтобы бот отвечал на "Привет" от пользователя "Доброго времени суток"

@dp.message()
async def router(message):
    if message.text.lower() == 'привет':
        await message.answer ('Доброго времени суток!')
    elif message.text.lower() == 'пока':
        await message.answer ('До новых встреч!')
    elif message.text.lower() == 'солнце':
        sun = FSInputFile("img/Sun.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=sun)
    elif message.text.lower() == 'луна':    
        moon = FSInputFile("img/Moon.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=moon)
    elif message.text.lower() == 'звезды': 
        stars = FSInputFile("img/Stars.jpg") 
        await bot.send_photo(chat_id=message.chat.id, photo=stars)
    elif message.text.lower() == 'снежинка':
        snow = FSInputFile("img/Snowflae.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=snow)
    else:
        await message.answer(message.text)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
