import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Створення діапазону значень для x для побудови графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Обчислення інтегралу через Монте-Карло
N = 10000
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
integral_mc = (b - a) * np.mean(y_random)

print(f"Інтеграл, обчислений методом Монте-Карло: {integral_mc}")

# Аналітичне обчислення
integral_exact = (b**3 / 3) - (a**3 / 3)
print(f"Аналітично обчислений інтеграл: {integral_exact}")

# Обчислення в quad
integral_quad, _ = quad(f, a, b)
print(f"Інтеграл, обчислений за допомогою функції quad: {integral_quad}")
