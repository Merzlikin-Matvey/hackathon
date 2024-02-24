import datetime


# Получает на вход строку вида "YYYY-MM-DD hh:mm:ss" и возвращает "YYYY-MM-DD"
def get_date(date):
    return str(date).split(' ')[0]

# Получает на вход "YYYY-MM-DD" и возвращает день недели в виде его номера
def get_weekday(date):
    return datetime.date(*map(int, date.split('-'))).weekday()

# Функция принимает на вход 2 строки "YYYY-MM-DD" возвращает разницу в днях между ними
def get_days_diff(date1, date2):
    date1 = datetime.date(*map(int, date1.split('-')))
    date2 = datetime.date(*map(int, date2.split('-')))
    return (date2 - date1).days

# Функция принимает на вход строку "YYYY-MM-DD" и возвращает следующий день
def get_next_day(date):
    date = datetime.date(*map(int, date.split('-'))) + datetime.timedelta(days=1)
    return str(date)