import matplotlib.pyplot as plt
import numpy as np

random_array = np.random.rand(5)

x = np.random.rand(5)
y = np.random.rand(5)

plt.scatter(x, y)

plt.title('Диаграмма рассеяния для 5 случайных чисел')

plt.xlabel('Ось абсцисс')
plt.ylabel('Ось ординат')

plt.grid(True)

plt.show()
print(random_array)