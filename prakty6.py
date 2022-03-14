import random, time



print('Выберите пункт залдания\n'
      '1 - Протокол тайных многосторонних вычислений для расчета средней величины трех чисел\n'
      '2 - Протокол разбиения секрета с использование гаммирования для трех участников\n'
      '3 - Протокол разделения секрета по схеме Шамира для (3, 5)-пороговой схеwмы\n'
      '4 - Протокол разделения секрета по схеме Асмута-Блума для (3, 5)-пороговой схемы')
p = str(input())
if p == '1':
    time.sleep(1)
    print('Введите первые 3 буквы Фамилии')
    f = str(input())
    i = str(input())
    m = str(input())
    print('Присвоить случайные числа для 3 значений для 3-х букв')
    q = int(input())
    w = int(input())
    e = int(input())
    print('Происходит генерация открытого ключа...')
    n = random.randrange(1, 100)
    time.sleep(1)
    print('Выполнено')
    print('Происходит генерация закрытого ключа для 3-х букв...')
    a = random.randrange(1, 100)
    b = random.randrange(1, 100)
    c = random.randrange(1, 100)
    time.sleep(1)
    print('Выполнено')
    my_list = ['0', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
               'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
               'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    ef = my_list.index(f)
    ea = my_list.index(i)
    em = my_list.index(m)

    # Описания операций
    print('Загадываем секретное число')
    x = int(input())
    z = (((e + x) ** ea) % n)
    v = (z ** b) % n
    g = (((v + w) ** ef) % n)
    l = (g ** a) % n
    o = (((l + q) ** em) % n)
    p = (o ** c) % n
    sz = (p - x) / 3
    print('Ответ ', sz)

elif p == '2':
    # Преобразование
    def make_bitseq(s: str) -> str:
        if not s.isascii():
            return " ".join(f"{ord(i) - 880:08b}" for i in s)
        else:
            return " ".join(f"{ord(i):08b}" for i in s)


    print('Введите кодовое слово буквы вводить поочередно')
    k = str(input())
    o = str(input())
    d = str(input())

    k1 = make_bitseq(k)
    o1 = make_bitseq(o)
    d1 = make_bitseq(d)

    print('Гамма 1')
    g = str(input())
    a = str(input())
    m = str(input())

    g1 = make_bitseq(g)
    a1 = make_bitseq(a)
    m1 = make_bitseq(m)

    print('Гамма 2')
    g2 = str(input())
    a2 = str(input())
    m2 = str(input())

    g3 = make_bitseq(g2)
    a3 = make_bitseq(a2)
    m3 = make_bitseq(m2)

    print('Гамма 3')
    g4 = str(input())
    a4 = str(input())
    m4 = str(input())

    g5 = make_bitseq(g4)
    a5 = make_bitseq(a4)
    m5 = make_bitseq(m4)

    f = int(k1, base=2) + int(g1, base=2) + int(g3, base=2) + int(g5, base=2)
    i = int(o1, base=2) + int(a1, base=2) + int(a3, base=2) + int(a5, base=2)
    w = int(d1, base=2) + int(m1, base=2) + int(m3, base=2) + int(m5, base=2)

    print('Шифрограмма ', bin(f), bin(i), bin(w))

    f1 = bin(f)
    i1 = bin(i)
    w1 = bin(w)

    s = int(f1, base=2) + int(g3, base=2) + int(g1, base=2) + int(g5, base=2)
    e = int(i1, base=2) + int(a3, base=2) + int(a1, base=2) + int(a5, base=2)
    c = int(w1, base=2) + int(m3, base=2) + int(m1, base=2) + int(m5, base=2)

    print('Восстановление секрета ', bin(s), bin(e), bin(c))
    print('Секрет', k1, o1, d1)

elif p == '3':
    print('Введите первую букву своей фамилии')
    f = str(input())
    print('Введите последнюю букву своей фамилии')
    a = str(input())
    print('Введите вторую букву своей фамилии')
    m = str(input())
    print('Введите предпоследнюю букву своей фамилии')
    i = str(input())

    my_list = ['0', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
               'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
               'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    f1 = my_list.index(f)
    a1 = my_list.index(a)
    m1 = my_list.index(m)
    i1 = my_list.index(i)
    ch = 0

    s = abs(f1 - a1) + abs(m1 - i1)
    print('Секрет S-', s)

    print('Введите колличество долей ')
    n = int(input())

    print('Введите число P которое больше количества долей n и секрета S')
    p = int(input())
    if p > n ^ s:
        a1 = random.randrange(1, 100)
        a2 = random.randrange(1, 100)
        print('a1 = ', a1)
        print('a2 = ', a2)
        while ch < n:
            ch += 1
            if ch == 3:
                fx1 = (a2 * ch ** 2 + a1 * ch + s) % p
                m1 = ch
                print(m1, fx1)
            if ch == 4:
                fx2 = (a2 * ch ** 2 + a1 * ch + s) % p
                m2 = ch
                print(m2, fx2)
            if ch == 5:
                fx3 = (a2 * ch ** 2 + a1 * ch + s) % p
                m3 = ch
                print(m3, fx3)
    else:
        print('Ошибка число P меньше числа N или S')

    print('Сбор m долей')

elif p == '4':

    def gcd_rem_division(num1, num2):
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 %= num2
            else:
                num2 %= num1
        return num1 or num2


    def bezout(a, b):
        x, xx, y, yy = 1, 0, 0, 1
        while b:
            q = a // b
            a, b = b, a % b
            x, xx = xx, x - xx * q
            y, yy = yy, y - yy * q
        #return (x, y, a)
        return (x)

    print('Введите первую букву своей фамилии')
    f = str(input())
    print('Введите последнюю букву своей фамилии')
    a = str(input())
    print('Введите вторую букву своей фамилии')
    m = str(input())
    print('Введите предпоследнюю букву своей фамилии')
    i = str(input())

    my_list = ['0', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
               'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
               'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    f1 = my_list.index(f)
    a1 = my_list.index(a)
    m1 = my_list.index(m)
    i1 = my_list.index(i)
    ch = 0

    s = abs(f1 - a1) + abs(m1 - i1)
    print('Секрет S-', s)

    print('Введите колличество долей ')
    n = int(input())

    print('Введите число P которое больше количества долей n и секрета S')
    p = int(input())

    print('Введите di ')
    d1 = int(input())
    d2 = int(input())
    d3 = int(input())
    d4 = int(input())
    d5 = int(input())

    print('Выбрать произвольное число r ')
    r = int(input())

    print('S-')
    S1 = s + r * p
    print(S1)

    print('Определение долей (di, ki), где ki = S’ mod di')
    k1 = S1 % d1
    k2 = S1 % d2
    k3 = S1 % d3
    k4 = S1 % d4
    k5 = S1 % d5

    print(d1, k1)
    print(d2, k2)
    print(d3, k3)
    print(d4, k4)
    print(d5, k5)

    print('Сбор m долей для 3-5 пороговой схемы')
    print('Вычисление произведения D взаимно простых чисел dj')
    D = d3 * d4 * d5
    print(D)
    print('Вычисление сомножителей Dj = D / dj')
    D1 = D / d4
    D2 = D / d3
    D3 = D / d5
    print(D1, D2, D3)

    print('Определение обратных чисел Dj-1 по модулям dj.')

    D11 = bezout(D1, d4)
    D21 = bezout(D2, d3)
    D31 = bezout(D3, d5)
    print(D11, D21, D31)

    print('Вычисление S’ = (Σ kj Dj Dj-1) mod D')

    #S1 = (k3 * D1 * D11 + k4 * D2 * D21 + k5 * D3 * D31) % D
    S1 = (k3 * D2 * D21 + k4 * D1 * D11 + k5 * D3 * D31) % D
    print(S1)

    print('Определение секрета S')
    S = S1 % p
    print(S)
