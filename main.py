import numpy as np
import pandas as  pd
import matplotlib as plt
import seaborn as sns
import os



# Создаем DataFrame из исходного дата-сета
df = pd.read_csv('file.csv')
# Таск 1
# Создаем Series с адресами всех товаров
addresses = df['Address']

# Создаем Series с ценами всех товаров
prices = df['Price']

# Создаем пустой DataFrame для хранения результата
result_df = pd.DataFrame(columns=['Address', 'Price'])

# Цикл по всем товарам
for i in range(len(df)):
    # Получаем адрес товара
    address = addresses[i]

    # Проверяем, является ли адрес адресом из Атланты или Далласа
    if 'Atlanta' in address or 'Dallas' in address:

        # Получаем цену товара
        price = prices[i]

        # Проверяем, больше ли цена 2.5 $
        if price > 2.5:
            # Добавляем данные о товаре в DataFrame
            result_df = result_df.append({'Address': address, 'Price': price}, ignore_index=True)

# Выводим результат
print(result_df)

# Таск 2
# Фильтруем DataFrame, чтобы оставить только товары из Атланты с названием 'Battery'
atlanta_batteries = df[(df['Address'].str.contains('Atlanta')) & (df['Product'] == 'Battery')]

# Фильтруем DataFrame, чтобы оставить только товары с ценой не более 3 долларов
cheap_batteries = atlanta_batteries[atlanta_batteries['Price'] <= 3]

# Выводим результат
print(cheap_batteries)

# Создаем Series с описанием всех товаров
descriptions = df['Description']

# Создаем Series с количеством единиц в упаковке для всех товаров
units_per_pack = df['Quantity']

# Создаем пустой DataFrame для хранения результата
result_df = pd.DataFrame(columns=['Address', 'Description', 'Quantity', 'Price'])

# Цикл по всем товарам
for i in range(len(df)):
    # Получаем адрес товара
    address = addresses[i]

    # Проверяем, является ли адрес адресом из Лос-Анжелеса или Бостона
    if 'Los Angeles' in address or 'Boston' in address:

        # Получаем описание товара
        description = descriptions[i]

        # Получаем количество единиц в упаковке
        units = units_per_pack[i]

        # Проверяем, является ли количество единиц в упаковке больше или равно 4
        if units >= 4:
            # Получаем цену товара
            price = prices[i]

            # Добавляем данные о товаре в DataFrame
            result_df = result_df.append(
                {'Address': address, 'Description': description, 'Quantity': units, 'Price': price}, ignore_index=True)

# Выводим результат
print(result_df)