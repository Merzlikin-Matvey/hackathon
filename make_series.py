import pandas as pd
import numpy as np


# Экспоненциальное сглаживание
def exponential_smoothing(series, alpha):
    result = [series[0]]
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])
    return result

def get_all_dates():
    return pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')

# Создадим временной ряд для категории
def make_series(df, category, smooth=False, alpha=0.15):
    if isinstance(category, str):
        category = [category]

    # Выделим нужные данные
    data = df[df['category'].isin(category)]

    # Оставим только дату и нормированный кешбек
    data = data[['day', 'cashback_norm']]

    # Получим все даты с 01.01.2022 по 31.12.2022
    dates = get_all_dates()

    values = []
    for date in dates:
        temp = np.array([])

        # Если дата есть в данных, то добавим значение кешбека
        if date in data['day'].values:
            temp = data[data['day'] == date]['cashback_norm'].values

        # Иначе добавим 0
        else:
            temp = np.array([0])

        values.append(np.median(temp))

    if smooth:
        values = exponential_smoothing(values, alpha)

    return values
