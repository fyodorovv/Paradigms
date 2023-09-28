import numpy as np

# Создаем два случайных массива данных
array1 = np.random.rand(10)
array2 = np.random.rand(10)
print(array1)
print(array2)

# Вариант 1
# Расчет средних значений
mean1 = np.mean(array1)
mean2 = np.mean(array2)

# Расчет ковариации
covariance = np.sum((array1 - mean1) * (array2 - mean2)) / len(array1)

# Расчет стандартных отклонений
std_deviation1 = np.sqrt(np.sum((array1 - mean1)**2) / len(array1))
std_deviation2 = np.sqrt(np.sum((array2 - mean2)**2) / len(array2))

# Расчет корреляции Пирсона
pearson_correlation = covariance / (std_deviation1 * std_deviation2)

print("Корреляция Пирсона:", pearson_correlation)

# Вариант 2 (более функциональный)
pearson_correlation2 = np.corrcoef(array1, array2)[0,1]

print("Корреляция Пирсона:", pearson_correlation2)

