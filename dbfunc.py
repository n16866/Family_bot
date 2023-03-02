import sqlite3


def bd_create():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budget(
    id INTEGER PRIMARY KEY,
    operation varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    sum numeric(5,2) NOT NULL,
    date date NOT NULL
    );""")
    connection.commit()
    cursor.close()


def bd_read(query):
    bd_data = []

    try:
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(query)
        bd_data = cursor.fetchall()
        connection.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

    return bd_data


def bd_write(query, data):
    
    try:
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def bd_write_income(summa, date):
    date_income = ('income', '0', summa, date)
    query_income = """INSERT INTO budget (operation,category,sum,date) VALUES (?,?,?,?);"""
    bd_write(query_income, date_income)
                

def bd_write_pay(kind_of_category, summa, date):
    date_kind_of_pay = ('pay', kind_of_category, summa, date)
    query_kind_of_pay = """INSERT INTO budget (operation,category,sum,date) VALUES (?,?,?,?);"""
    bd_write(query_kind_of_pay, date_kind_of_pay)


def bd_read_state(stat_date, stat_query):
    query = stat_query
    
    stat_data = bd_read(query)

    month_incom = 0
    month_pay = 0
    pay_home = 0
    pay_food = 0
    pay_auto = 0
    pay_save = 0
    pay_personal = 0
    pay_rest = 0

    for operation in stat_data:
        if operation[1] == 'income':
            month_incom = month_incom + operation[3]
        if operation[1] == 'pay':
            month_pay = month_pay + operation[3]
            if operation[2] == 'home':
                pay_home = pay_home + operation[3]
            if operation[2] == 'food':
                pay_food = pay_food + operation[3]
            if operation[2] == 'auto':
                pay_auto = pay_auto + operation[3]
            if operation[2] == 'save':
                pay_save = pay_save + operation[3]
            if operation[2] == 'personal':
                pay_personal = pay_personal + operation[3]
            if operation[2] == 'rest':
                pay_rest = pay_rest + operation[3]
            
    
    user_data = f'Вот твои данные\r\n' \
                f'Операция: получить статистику\r\n'\
                f'Месяц {stat_date}\r\n'\
                f'Доход за месяц: {month_incom}\r\n'\
                f'Доход за месяц: {month_pay}. Из них:\r\n \
                        Жилье: {pay_home}, Еда: {pay_food}, Авто: {pay_auto}, Сбережения: {pay_save}, Личные: {pay_personal}, Отдых: {pay_rest}.'
    
    return user_data
