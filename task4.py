import random
m = int(input("Введите размер n матриц: "))
a = [[random.randint(0, 9) for _ in range(m)] for _ in range(m)] #заполняем первую матрицу
b = [[random.randint(0, 9) for _ in range(m)] for _ in range(m)] #заполняем вторую матрицу
c = [[x + y for x, y in zip(one, two)] for (one, two) in zip(a, b)] #сложение двух матриц
print("Первая матрица: ", a)
print("Вторая матрица: ", b)
print("Результат суммы: ", c)