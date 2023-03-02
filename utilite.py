import keyboards
import dbfunc
import datetime
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


def get_stat_query(stat_date):
    
     if stat_date == '01':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-01-01' AND '2023-01-31'
                """
     if stat_date == '02':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-02-01' AND '2023-02-29'
                """
     if stat_date == '03':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-03-01' AND '2023-03-31';
                """
     if stat_date == '04':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-04-01' AND '2023-04-31'
                """
     if stat_date == '05':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-05-01' AND '2023-05-31'
                """
     if stat_date == '06':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-06-01' AND '2023-06-31'
                """
     if stat_date == '07':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-07-01' AND '2023-07-31'
                """
     if stat_date == '08':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-08-01' AND '2023-08-31'
                """
     if stat_date == '09':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-09-01' AND '2023-09-31'
                """
     if stat_date == '10':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-10-01' AND '2023-10-31'
                """
     if stat_date == '11':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-11-01' AND '2023-11-31'
                """
     if stat_date == '12':
        query = """SELECT * FROM budget
                    WHERE DATE(date) BETWEEN '2023-12-01' AND '2023-12-31'
                """
     
     return query

async def get_date(message: types.Message, state: FSMContext):
     await state.update_data(summa=message.text)
     await state.update_data(date=datetime.datetime.now())
     data = await state.get_data()
     kind_of_pay = data.get('kind_of_pay')
     kind_of_category = data.get('kind_of_category')
     summa =  data.get('summa')
     stat_date = data.get('stat_date')
     date = data.get('date')
     if kind_of_pay == 'income':
          dbfunc.bd_write_income(summa, date)
          user_data = f'Вот твои данные\r\n' \
                        f'Операция: доход\r\n'\
                        f'Сумма {summa}\r\n'\
                        f'Дата {date}'
     elif kind_of_pay == 'pay':
          dbfunc.bd_write_pay(kind_of_category, summa, date)
          user_data = f'Вот твои данные\r\n' \
                 f'Операция: расход\r\n'\
                 f'Вид категории {kind_of_category}\r\n'\
                 f'Сумма {summa}\r\n'\
                 f'Дата {date}'
     elif kind_of_pay == 'stat':
          stat_query = get_stat_query(stat_date)
          print(stat_query)
          user_data = dbfunc.bd_read_state(stat_date, stat_query)

    
     await message.answer(user_data)
     await state.clear()



