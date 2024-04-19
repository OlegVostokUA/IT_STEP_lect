import time

import numpy as np

# A = np.random.randint(0, 10, size=(2000, 2000))
# B = np.random.randint(0, 10, size=(2000, 2000))
# print(type(A))
#
# start_p = time.time()
# C = [[A[i][j] + B[i][j] for i in range(len(A[0]))] for j in range(len(A))]
# stop_p = time.time()
#
# start_np = time.time()
# D = A + B
# stop_np = time.time()
#
# print('Python', stop_p - start_p)
# print('Numpy', stop_np - start_np)

#a = np.array([[1,2,3,4,5], [1,2,3424343242,4,5]])
# a = np.arange(0, 20, 2)
# a = np.linspace(0, 10, 25)
# a = np.random.rand(5, 5, 2)

# from PIL import Image

# img = np.array(Image.open('material/cat.jpeg'))
#
# img_R = img.copy()
# img_R[:, :, (1, 2)] = 0
# img_G = img.copy()
# img_G[:, :, (0, 2)] = 0
# img_B = img.copy()
# img_B[:, :, (0, 1)] = 0
#
# img1 = Image.fromarray(img)
# img2 = Image.fromarray(img_R)
# img3 = Image.fromarray(img_G)
# img4 = Image.fromarray(img_B)
#
# result = Image.new('RGB', (img.shape[1]*2, img.shape[0]*2))
# result.paste(img1, (0,0))
# result.paste(img2, (img.shape[1], 0))
# result.paste(img3, (0, img.shape[0]))
# result.paste(img4, (img.shape[1], img.shape[0]))
#
# result.save('result_cat.png', format='PNG')

# import matplotlib.pyplot as plt
#
# data = np.genfromtxt('material/litecoin.csv', delimiter=',', skip_header=1, usecols=(1, 2, 3, 4, 5, 6))
#
# open_, high_, low_, close_, adj_, volumes = data.T
#
# plt.plot(close_)
#
# plt.xlabel('Month')
# plt.ylabel('Price close')
# plt.title('LITECOIN')
#
# n = len(close_)
# step = n // 10
# plt.xticks(range(0, n, step))
#
# plt.show()

import pandas as pd

# data = {'Name': ['Allie', 'John', 'Tracy', 'Frank'],
#         'age': [25,33,66,41],
#         'City': ['Kiev', 'Lviv', 'Smaria', 'Donetsk']}
#
# df = pd.DataFrame(data)
# #print(df)
#
# data2 = [25000, 35000, 45000]
# labels = ['Notebooks', 'Monitors', 'Printers']
#
# series = pd.Series(data2, index=labels)
#
# print(series['Monitors'])

index = pd.MultiIndex.from_tuples(
    [
        ('Kiev', 'Notebooks'), ('Kiev', 'Desctops'),
        ('Lviv', 'Notebooks'), ('Lviv', 'Desctops'),
    ]
)

data = [[1000, 20000], [3000, 40000], [5000, 60000], [7000, 80000]]

df = pd.DataFrame(data, index=index, columns=['Sales', 'Profit'])
print(df)