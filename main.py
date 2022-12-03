import config
import utilite
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command



async def main():
  # Включаем логирование, чтобы не пропустить важные сообщения
  logging.basicConfig(level=logging.DEBUG)
  # Объект бота
  bot = Bot(token=config.TOKEN)
  # Диспетчер
  dp = Dispatcher()
  # Хэндлер на команду /start
  dp.message.register(utilite.cmd_start, Command(commands=["start"]))
  dp.message.register(utilite.button, Command(commands=['show']))
  dp.message.register(utilite.button2, Command(commands=['give']))
  dp.callback_query.register(utilite.start_func, F.data.startswith('start_'))
  dp.message.register(utilite.get_form, Command(commands=["form"]))
  dp.message.register(utilite.get_name, utilite.User_form.waiting_name)
  dp.message.register(utilite.get_last_name, utilite.User_form.waiting_last_name)
  dp.message.register(utilite.get_age, utilite.User_form.waiting_Age)

  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
