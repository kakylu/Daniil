import random
print('1 - Протокол на базе RSA\n'
      '2 - Алгоритм цифровой подписи ГОСТ 34.10-94')


r = str(input())
if r == '1':
    h = int(input())
    print('Введите открытый ключ')
    n = int(input())
    d = random.randrange(1,99)
    print('Выборка цифровой подписи')
    s = (h**d) % n
    print('Вычисление хеш-образа где h = h1')
    h1 = int(input())
    print('Введите открытый ключ е')
    e = int(input())
    h = (s**e) % n
    print(h,h1)
    if h1 == h:
        print('Все верно')
elif r == '2':
    print('Выбор p - простого числа')
    p = int(input())
    print('Выбор q - простого числа - множителя (р – 1)')
    q = int(input())
    print('Выбор а - любого числа, меньшего (р – 1)')
    a = int(input())
    print('Выбор закрытого ключа х - числа, меньшего q.')
    x = int(input())
    y = (a ** x) % p
    print(y)
    print('Вычисление хеш-образа h = h(T) (для ГОСТ длина хеш-образа 256бит).')
    h = int(input())
    print('Выбор k - любого числа, меньшего q.')
    k = int(input())
    w = (a ** k) % p
    w1 = w % q
    if w1 == 0:
        print('Не верно')
    else:
        s = (x * w1 + k * h) % q
        print (w1,s)
        print('Вычисление хеш - образа')
        h1 = int(input())
        v = (h1 ** (q-2)) % q
        z1 = (s * v) % q
        z2 = ((q - w1) * v) % q
        u = (((a ** z1) * (y ** z2)) % p) % q
        print (w1,u)
        if w1 == u:
            print ('Все верно')







