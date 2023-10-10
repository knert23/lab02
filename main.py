n = int(input('Введите число, до которого будет осуществляться поиск:\n'))

array = [i for i in range(n + 1)]

# 1 не считается простым число, поэтому 0
array[1] = 0

i = 2
while i < n:
    if array[i] != 0:
        j = i * 2
        while j <= n:
            array[j] = 0
            j += i
    i += 1

# Откидываем все нули
array = [i for i in array if i != 0]
print(array)
