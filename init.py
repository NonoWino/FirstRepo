'''# def large_range(n): 
    #     for i in range(n):
    #         yield i
    # 
    # def num_s(value):
    #     digits = []
    #     while value > 0:
    #         digit = value % 10  # Получаем последнюю цифру
    #         digits.insert(0, digit)  # Вставляем в начало списка
    #         value //= 10
    #     if not digits:  # Проверяем, пуст ли список digits
    #         return 0.0
    #     total = sum(digits)
    #     count = len(digits)
    #     average = total / count
    #     return average
    # 
    # 
    # for value in large_range(1000000):
    #     # Обрабатываем значения по одному
    #     print(num_s(value))
''' #  <--код вывода среднего значения

def echo():
    while True:
        received = yield
        print(received)

e = echo()
next(e)  # Запускаем генератор
e.send("Hello, world!")  # Вывод: Hello, world!
