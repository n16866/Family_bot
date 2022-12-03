from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def get_start_reply() -> ReplyKeyboardBuilder:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Ввести доход')
    keyboard.button(text='Ввести расход')
    keyboard.button(text='Вывести статистику')
    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)
   
    
def start_kb_inline() -> InlineKeyboardBuilder:
    keyboard2 = InlineKeyboardBuilder()
    keyboard2.button(
        text='Ввести доход',
        callback_data='start_income'
        )
    keyboard2.button(
        text='Ввести расход',
        callback_data='start_pay'
    )
    keyboard2.button(
        text='Статистика',
        callback_data='start_stat'
    )
    keyboard2.adjust(3)

    return keyboard2.as_markup()


