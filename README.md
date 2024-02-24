
# hackathony
Представляем проект команды  "Гектогон"
В наши задачи входил как можно более точный бпрогноз динамики акций до последнего дня месяца.
Решение данной задачи мы осущетвили за счет линейной регрессии и использования mcc кодов ,взятых из базы данных Тинькоффа.За счет совмещения данных параметров мы получили наиболее точный прогноз. 
Рассмотрим все пункты более точно :
Регрессия :мы берем последние значения за 5 прошлых дней , какой это день недели и на основе этих данных предсказываем 6 день.
MCC:мы берем тип магазина (продуктовый,ресторан ,фастфуд и т.д.) и смотрим зависимость даты от значения кешбека и так мы вычисляем в какие дни недели и месяца спрос на тот или иной тип магазина больше и на основе этого вносим изменения в прогноз.
Для примера, если дата  - 14 февраля , то спрос на ювилирные изделия и рестораны будет выше,следовательно кешбек будет выше .На основе этого строится большинство наших вычислений в коде.

В папке [graphs](graphs) содержаться графики всех 422 компаний ,на основе которых делается  прогноз.
В папке [linear regression](<linear regression>) содержится код - вычислитель регрессии ,одного из главных параметров нашего проекта.Он считывает последние  5 дней и на их основе строит 6 день.
В папке [classification](classification) содержится наше главное оружие ,нечто отличающее наше решение от других - это mcc .В этой папке беруться значения из https://img-cdn.tinkoffjournal.ru/-/mcc_new_codes.pdf , отсюда считывается эффективность тех или иных видов магазина в разные дни недели и праздники.На основы которых делаем зависимость типа магазина и дней ,у которых наиболее ввысокие кешбеки.
В [data](data) содержатся все Excel таблицы , с которыми мы  взаимодейтсвовали при обработке  данных . 
Папка [helpful](helpful.py) содержит все полезные функции для работой с датой.

В [normalize_data](normalize_data.ipynb) мы отпарвляем обработанные данные и преобразуем значения cashback в диапазон от 0 до 1 в завимости от максимума и минимума для каждого merchant_name.
