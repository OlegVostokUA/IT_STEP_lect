# import numpy as np
# import time
#
# # Определяем две матрицы размером 1000x1000 со случайными целыми числами от 0 до 9
# A = np.random.randint(0, 10, size=(1000, 1000))
# B = np.random.randint(0, 10, size=(1000, 1000))
#
# # Сложение матриц средствами Python
# start_time = time.time()
# C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
# end_time = time.time()
#
# # Сложение матриц с помощью NumPy
# start_time_np = time.time()
# D = A + B
# end_time_np = time.time()
#
# # Выводим результаты и время выполнения
# print(f"Время выполнения Python сложения: {end_time - start_time} сек")
# print(f"Время выполнения NumPy сложения: {end_time_np - start_time_np} сек")
#
# # Сравниваем результаты
# print("Результаты совпадают:", np.array_equal(C, D))


# import numpy as np
#
# # Создание массива из списка
# a = np.array([1, 2, 3, 4, 5])
# print(a)
#
# # Создание двумерного массива из списка списков
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(b)
#
# # Создание массива из диапазона значений
# c = np.arange(0, 10, 2)  # Создаем массив из значений от 0 до 10 с шагом 2
# print(c)
#
# # Создание массива из равномерно распределенных значений
# d = np.linspace(0, 1, 5)  # Создаем массив из 5 равномерно распределенных значений от 0 до 1
# print(d)
#
# # Создание массива из случайных значений
# e = np.random.rand(3, 3)  # Создаем массив из 3x3 случайных значений
# print(e)
#
# # Создание массива из нулей
# f = np.zeros((2, 3))  # Создаем массив из нулей размером 2x3
# print(f)
#
# # Создание массива из единиц
# g = np.ones((3, 3))   # Создаем массив из единиц размером 3x3
# print(g)


# import numpy as np
#
# # Создаем двумерный массив
# arr = np.array([[1, 2], [3, 4], [5, 6]])
#
# # Выводим массив на экран
# print(arr)
#
# # Получаем размерность массива
# print(arr.shape)
#
# # Получаем элементы массива
# print(arr[0, 1])   # Выведет 2
# print(arr[2, 0])   # Выведет 5
#
# # Изменяем элементы массива
# arr[0, 1] = 7
# arr[1, 1] = 8
# arr[2, 1] = 9
# print(arr)
#
# # Выводим строку
# print(arr[1])   # Выведет [3 8]
#
# # Выводим столбец
# print(arr[:, 0])   # Выведет [1 3 5]
#
# # Выводим срез
# print(arr[:2, 1])   # Выведет [7 8]


# import numpy as np
#
# # Создаем два массива размером 6x6 со случайными целыми числами от 0 до 9
# a = np.random.randint(1, 10, size=(6, 6))
# b = np.random.randint(1, 10, size=(6, 6))
#
# # Выводим массивы на экран
# print("Массив a:\n", a)
# print("Массив b:\n", b)
#
# # Вычитаем массивы
# d = a - b
# print("Разность массивов a и b:\n", d)
#
#
# # Умножение массивов
# m = np.dot(a, b)
# print("Произведение массивов a и b:\n", m)
#
# # Деление массивов (умножение на обратную матрицу)
# # Вычисляем обратную матрицу b
# b_inv = np.linalg.inv(b)
#
# # Умножаем матрицу a на обратную матрицу b_inv
# result = np.dot(a, b_inv)
# print("Результат деления массива a на b:\n", result)
#
# # Транспонируем массивы
# h = np.transpose(a)
# i = np.transpose(b)
# print("Массив a после транспонирования:\n", h)
# print("Массив b после транспонирования:\n", i)
#
# # Получаем статистические параметры массивов
# std_a = np.std(a)            # Стандартное отклонение массива a
# median_b = np.median(b)      # Медиана массива b
# variance_a = np.var(a)       # Дисперсия массива a
# min_b = np.min(b)            # Минимальное значение массива b
# max_a = np.max(a)            # Максимальное значение массива a
# sum_b = np.sum(b)            # Сумма элементов массива b
# product_a = np.product(a, dtype=np.uint64)    # Произведение элементов массива a
# prod_b = np.prod(b, dtype=np.uint64)          # Еще один метод вычисления произведения элементов
# print("Стандартное отклонение массива a:", std_a)
# print("Медиана массива b:", median_b)
# print("Дисперсия массива a:", variance_a)
# print("Минимальное значение массива b:", min_b)
# print("Максимальное значение массива a:", max_a)
# print("Сумма элементов массива b:", sum_b)
# print("Произведение элементов массива a:", product_a)
# print("Произведение элементов массива b:", prod_b)


# import numpy as np
#
# # створюємо масив розміром 3x4
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) #
#
# # використовуємо метод reshape() для зміни форми масиву на 2x6
# new_arr = arr.reshape(2, 6)
#
# print("Початковий масив:")
# print(arr)
# print("Масив після зміни форми:")
# print(new_arr)


# import numpy as np
#
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# c = np.array( [[9, 10], [11, 12]])
#
# #об'єднуємо масиви по горизонтальній осі (по рядках)
# d = np.concatenate((a, b, c), axis=1)
# print(d)
# #об'єднуємо масиви по вертикальної осі (по стовпцях)
# e = np.concatenate((a, b, c), axis=0)
# print(e)


# import numpy as np
# a = np.array([[1, 2, 9, 8], [7, 5, 3, 4], [2, 1, 5, 6], [4, 8, 7, 8]])
# print(a.flatten())


# import numpy as np
#
# data = np.array([[1, 2, 3], [4, 5, 6]])
# np.savetxt("data.txt", data, delimiter=",")
# data = np.loadtxt("data.txt", delimiter=",", dtype=np.int32)
# print(data)


# # pip install Pillow
# import numpy as np
# from PIL import Image
#
#
# # загрузка изображения
# img = np.array(Image.open('cat.jpeg'))
#
# # преобразование в черно-белое изображение
# img_gray = np.mean(img, axis=2).astype(np.uint8)
#
# # преобразование цветных каналов
# img_R = img.copy()
# img_R[:, :, (1, 2)] = 0
# img_G = img.copy()
# img_G[:, :, (0, 2)] = 0
# img_B = img.copy()
# img_B[:, :, (0, 1)] = 0
#
# # объединение изображений
# img_1 = Image.fromarray(img_gray)
# img_2 = Image.fromarray(img_R)
# img_3 = Image.fromarray(img_G)
# img_4 = Image.fromarray(img_B)
#
# result = Image.new("RGB", (img.shape[1]*2, img.shape[0]*2))
# result.paste(img_1, (0,0))
# result.paste(img_2, (img.shape[1],0))
# result.paste(img_3, (0,img.shape[0]))
# result.paste(img_4, (img.shape[1],img.shape[0]))
#
# result.save("result.png", format="PNG")
#dfsfdsfds
