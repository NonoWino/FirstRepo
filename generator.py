def natural_numbers():
    n = 1
    while True:
        yield n # Возвращает текущее значение n и приостанавливает выполнение функции
        n += 1
# Создаем объект-генератор
naturals = natural_numbers()
# Итерируемся по генератору и выводим первые 10 чисел
for _ in range(10):

    print(next(naturals))