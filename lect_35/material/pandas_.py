#############################
########## PANDAS ###########
#############################

import pandas as pd

dataframe = pd.read_csv('data.csv')
series_1 = dataframe['столбец_1']
series_2 = dataframe['столбец_2']
series_3 = dataframe['столбец_3']

print(series_1)
print(series_2)
print(series_3)


# Чтение данных из файла CSV
dataframe = pd.read_csv('data.csv')

# Вывод первых 2 строк DataFrame
print(dataframe.head(2))

# Вывод последних 2 строк DataFrame
print(dataframe.tail(2))

# pip install openpyxl

# читаем Excel файл
df = pd.read_excel('data.xlsx')

# выводим DataFrame
print(df)


import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# загружаем данные из файла
data = pd.read_csv('nvidia.csv')

# преобразуем столбец 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# создаем столбец 'YearMonth' с комбинированным значением года и месяца
data['YearMonth'] = data['Date'].dt.to_period('M')

# группируем данные по году и месяцу и вычисляем среднее значение цены закрытия
monthly_data = data.groupby('YearMonth')['Close'].mean()

# преобразуем индекс в тип datetime
monthly_data.index = pd.to_datetime(monthly_data.index.to_timestamp())

# строим график
fig, ax = plt.subplots()
ax.plot(monthly_data.index, monthly_data.values)

# настройки оси X для отображения лет и месяцев
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.xlabel('Годы и месяцы')
plt.ylabel('Средняя цена закрытия')
plt.title('Ежемесячные колебания цен на акции Nvidia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()