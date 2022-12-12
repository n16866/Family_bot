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

async def cmd_start(message: types.Message, state: FSMContext):
     await message.answer(
          text='Привет! Выбери действие',
          reply_markup=keyboards.kb_start()
          )
     await state.set_state(Data_Base_var.kind_of_pay)    
     
async def get_category(message: types.Message, state: FSMContext):
     await message.answer (
          text='Выберете категорию расхода',
          reply_markup=keyboards.kb_category()
          )
     await state.set_state(Data_Base_var.kind_of_category)
    
async def get_stat_date(message: types.Message, state: FSMContext):
     await message.answer (
          text='Выберете месяц',
          reply_markup=keyboards.kb_date()
          )
     await state.update_data(stat_date=message.text)
     await state.set_state(Data_Base_var.date)
     await state.update_data(date=message.date)

async def get_summa(message: types.Message, state: FSMContext):
     await message.answer (
          text='Введите сумму операции'
          )
     await state.set_state(Data_Base_var.summa)

async def get_date(message: types.Message, state: FSMContext):
     await state.update_data(summa=message.text)
     await state.update_data(date=message.date)
     data = await state.get_data()
     kind_of_pay = data.get('kind_of_pay')
     kind_of_category = data.get('kind_of_category')
     summa =  data.get('summa')
     stat_date = data.get('stat_date')
     date = data.get('date')
     if kind_of_pay == 'income':
          user_data = f'Вот твои данные\r\n' \
                 f'Операция: доход\r\n'\
                 f'Сумма {summa}\r\n'\
                 f'Дата {date}'
     elif kind_of_pay == 'pay':
          user_data = f'Вот твои данные\r\n' \
                 f'Операция: расход\r\n'\
                 f'Вид категории {kind_of_category}\r\n'\
                 f'Сумма {summa}\r\n'\
                 f'Дата {date}'
     else:
          user_data = f'Вот твои данные\r\n' \
                 f'Операция: получить статистику\r\n'\
                 f'Месяц {stat_date}\r\n'\
    
     await message.answer(user_data)
     await state.clear()            
