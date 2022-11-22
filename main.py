import config
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message


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
async def send_text(message):
    if message.text.lower() == 'привет':
        await message.answer ('Доброго времени суток!')
    elif message.text.lower() == 'пока':
        await message.answer ('До новых встреч!')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
