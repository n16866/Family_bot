import keyboards
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class User_form (StatesGroup):
     waiting_name = State()
     waiting_last_name = State()
     waiting_Age = State()


async def get_form(message: types.Message, state: FSMContext):
     await message.answer ('Введи своё имя')
     await state.set_state(User_form.waiting_name)

async def get_name(message: types.Message, state: FSMContext):
     await message.answer ('Введи свою фамилию')
     await state.update_data(name = message.text)
     await state.set_state(User_form.waiting_last_name)

async def get_last_name(message: types.Message, state: FSMContext):
     await message.answer ('Введи свою возраст')
     await state.update_data(last_name = message.text)
     await state.set_state(User_form.waiting_Age)

async def get_age(message: types.Message, state: FSMContext):
     await message.answer ('Введи свой возраст')
     await state.update_data(age=message.text)
     data = await state.get_data()
     name = data.get('name')
     last_name = data.get('last_name')
     user_data = f'Вот твои данные\r\n' \
                 f'Имя {name}\r\n'\
                 f'Фамилия {last_name}\r\n'\
                 f'Возраст {message.text}'
     await message.answer(user_data)
     await state.clear()            


async def cmd_start(message: types.Message):
     await message.answer("Hello!")

async def button(message: types.Message):
     await message.answer(
          text = 'Привет', 
          reply_markup=keyboards.get_start_reply()
          )


async def button2(message: types.Message):
     await message.reply(
          text = 'Привет', 
          reply_markup=keyboards.start_kb_inline()
          )

async def start_func(call: types.CallbackQuery):
     
     if call.data == 'start_income':
          await call.message.answer('Вы нажали ввести доход')
     elif call.data == 'start_pay':
          await call.message.answer('Вы нажали кнопку ввести расход')
     else:
          await call.message.answer('Вы нажали кнопку вывести статистику')
