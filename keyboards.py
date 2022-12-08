from aiogram.utils.keyboard import InlineKeyboardBuilder
   
    
def kb_start() -> InlineKeyboardBuilder:
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
    keyboard2.button(
        text='Отмена',
        callback_data='cancel'
    )
    keyboard2.adjust(3)

    return keyboard2.as_markup()


def kb_category() -> InlineKeyboardBuilder:
    keyboard2 = InlineKeyboardBuilder()
    keyboard2.button(
        text='Жилье',
        callback_data='category_home'
        )
    keyboard2.button(
        text='Еда',
        callback_data='category_food'
    )
    keyboard2.button(
        text='Транспорт',
        callback_data='category_auto'
    )
    keyboard2.button(
        text='Сбережения',
        callback_data='category_save'
    )
    keyboard2.button(
        text='Личные',
        callback_data='category_personal'
    )
    keyboard2.button(
        text='Отдых',
        callback_data='category_rest'
    )
    keyboard2.button(
        text='Отмена',
        callback_data='cancel'
    )
    keyboard2.adjust(3)

    return keyboard2.as_markup()

def kb_date() -> InlineKeyboardBuilder:
    keyboard2 = InlineKeyboardBuilder()
    keyboard2.button(
        text='Январь',
        callback_data='date_01'
        )
    keyboard2.button(
        text='Февраль',
        callback_data='date_02'
    )
    keyboard2.button(
        text='Март',
        callback_data='date_03'
    )
    keyboard2.button(
        text='Апрель',
        callback_data='date_04'
    )
    keyboard2.button(
        text='Май',
        callback_data='date_05'
    )
    keyboard2.button(
        text='Июнь',
        callback_data='date_06'
    )
    keyboard2.button(
        text='Июль',
        callback_data='date_07'
        )
    keyboard2.button(
        text='Август',
        callback_data='date_08'
    )
    keyboard2.button(
        text='Сентябрь',
        callback_data='date_09'
    )
    keyboard2.button(
        text='Октябрь',
        callback_data='date_10'
    )
    keyboard2.button(
        text='Ноябрь',
        callback_data='date_11'
    )
    keyboard2.button(
        text='Декабрь',
        callback_data='date_12'
    )
    keyboard2.button(
        text='Отмена',
        callback_data='cancel'
    )
    keyboard2.adjust(3)

    return keyboard2.as_markup()
