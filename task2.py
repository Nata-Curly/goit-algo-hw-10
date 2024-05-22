import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return x**2

a = 0
b = 2

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, "r", linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)

ax.fill_between(ix, iy, color="gray", alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()


'''Метод Монте-Карло'''

N = 100000
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, b**2, N)

under_curve = y_random < f(x_random)
integral_mc = (b - a) * (b**2) * np.sum(under_curve) / N

print("\nІнтеграл методом Монте-Карло:", integral_mc)


'''Перевірка результату за допомогою SciPy'''

result, error = spi.quad(f, a, b)
print("\nІнтеграл за допомогою бібліотеки SciPy:", result)


'''Візуалізація методу Монте-Карло'''

fig, ax = plt.subplots()
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

ax.plot(x, y, "r", linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)

ax.fill_between(ix, iy, color="gray", alpha=0.3)
ax.scatter(x_random, y_random, color="blue", s=1, alpha=0.1)
ax.scatter(x_random[under_curve], y_random[under_curve], color="green", s=1, alpha=0.1)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title(
    "Метод Монте-Карло для інтегрування f(x) = x^2 від " + str(a) + " до " + str(b)
)
plt.grid()
plt.show()
