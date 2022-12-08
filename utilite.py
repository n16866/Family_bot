import keyboards
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Data_Base_var (StatesGroup):
     kind_of_pay = State()
     kind_of_category = State()
     summa = State()
     stat_date = State()
     date = State()


async def get_category(message: types.Message, state: FSMContext):
     await message.answer (
          text='Выберете категорию расхода',
          reply_markup=keyboards.kb_category()
          )
     await state.set_state(Data_Base_var.kind_of_category)

async def get_summa(message: types.Message, state: FSMContext):
     await message.answer (
          text='Введите сумму операции'
          )
     await state.set_state(Data_Base_var.summa)
     await state.update_data(summa=message.text)

async def get_date(message: types.Message, state: FSMContext):
     await message.answer (
          text='Выберете месяц',
          reply_markup=keyboards.kb_date()
          )
     await state.set_state(Data_Base_var.date)
     await state.update_data(date=message.text)


# async def get_name(message: types.Message, state: FSMContext):
#      await message.answer ('Введи свою фамилию')
#      await state.update_data(name = message.text)
#      await state.set_state(User_form.waiting_last_name)

# async def get_last_name(message: types.Message, state: FSMContext):
#      await message.answer ('Введи свою возраст')
#      await state.update_data(last_name = message.text)
#      await state.set_state(User_form.waiting_Age)

# async def get_age(message: types.Message, state: FSMContext):
#      await message.answer ('Введи свой возраст')
#      await state.update_data(age=message.text)
#      data = await state.get_data()
#      name = data.get('name')
#      last_name = data.get('last_name')
#      user_data = f'Вот твои данные\r\n' \
#                  f'Имя {name}\r\n'\
#                  f'Фамилия {last_name}\r\n'\
#                  f'Возраст {message.text}'
#      await message.answer(user_data)
#      await state.clear()            


async def cmd_start(message: types.Message, state: FSMContext):
     await message.answer(
          text='Привет! Выбери действие',
          reply_markup=keyboards.kb_start()
          )
     await state.set_state(Data_Base_var.kind_of_pay)     


