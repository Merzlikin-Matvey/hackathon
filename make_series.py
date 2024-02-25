import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

# Экспоненциальное сглаживание
def exponential_smoothing(series, alpha):
    result = [series[0]]
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])
    return result

def get_all_dates():
    return pd.date_range(start='2022-01-01', end='2023-01-31', freq='D')

# Создадим временной ряд для категории
def rolling_mean(series, value):
    return series.rolling(window=value).mean()

def make_series(df,
                category,
                is_exponential_smoothing=False,
                alpha=0.15,
                is_rolling_mean=False,
                rolling_value=20
                ):
    
    if isinstance(category, str):
        category = [category]

    # Выделим нужные данные
    data = df[df['category'].isin(category)]

    # Оставим только дату и нормированный кешбек
    data = data[['day', 'z_cashback_norm']]

    # Получим все даты с 01.01.2022 по 01.01.2023
    dates = get_all_dates()

    values = []
    for date in dates:
        temp = np.array([])

        # Если дата есть в данных, то добавим значение кешбека
        if date in data['day'].values:
            temp = data[data['day'] == date]['z_cashback_norm'].values

        # Иначе добавим 0
        else:
            temp = np.array([0])

        values.append(np.mean(temp))

    values = np.array(values)

    if is_exponential_smoothing:
        values = exponential_smoothing(values, alpha)
    elif is_rolling_mean:
        values= rolling_mean(values, rolling_value)
    return values


# Тест Дики-Фуллера на стационарность
def test_stationarity(timeseries):
    timeseries = pd.Series(timeseries)

    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value

    print(dfoutput)
  
