def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function

# Создание замыкания
closure = outer_function(10) # Создается замыкание, где x=10

# Вызов замыкания с аргументом 5
print(closure(8))