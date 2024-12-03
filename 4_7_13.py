import math
import numpy as np
import matplotlib.pyplot as plt


# Функція для обчислення значення
def compute_function(x):
    if x <= 0:
        denominator = 1 - math.exp(x)
        if denominator == 0:
            return None
        return math.tan(x / denominator)
    elif x > 1:
        if x - 3 == 0:
            return None
        try:
            return math.sqrt(math.log(x - 3))
        except ValueError:
            return None
    else:
        return None


# Генерація графіка
def plot_function():
    x1 = np.linspace(-5, 0, 500)  # Значення x для x <= 0
    x2 = np.linspace(3.01, 5, 500)  # Значення x для x > 3.01

    y1 = [compute_function(val) for val in x1]
    y2 = [compute_function(val) for val in x2]

    # Фільтрація None значень
    x1 = [val for val, y in zip(x1, y1) if y is not None]
    y1 = [y for y in y1 if y is not None]
    x2 = [val for val, y in zip(x2, y2) if y is not None]
    y2 = [y for y in y2 if y is not None]

    plt.figure(figsize=(10, 6))
    plt.plot(x1, y1, label=r"$y = \tan\left(\frac{x}{1-e^x}\right)$ для $x \leq 0$")
    plt.plot(x2, y2, label=r"$y = \sqrt{\ln(x-3)}$ для $x > 1$")

    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Графік функції")
    plt.legend()
    plt.grid()
    plt.show()


plot_function()
