#12. (|х(2n-1)|)/(2n-1)!
import math

def calculate_sum(k, t):
    x = [[random.randint(1, 10) for _ in range(k)] for _ in range(k)]
    sum = 0
    n = 1
    first_sign = 1

    while True:
        term = (abs(x * (2 * n - 1))) / math.factorial(2 * n - 1)
        sum += first_sign * term

        if round(sum, t) == sum:
            break

        first_sign = -first_sign
        n += 1

    return sum

k = 3 # Размерность матрицы
t = 6 # Точность после запятой

result = calculate_sum(k, t)
print(result)