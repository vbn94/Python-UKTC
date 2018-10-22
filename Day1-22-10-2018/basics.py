# аритметични оператори
print(2 + 3)    # събиране
print(10 - 3)   # изваждане
print(5 * 6)    # умножение
print(15 / 5)   # деление
print(11 % 3)   # остатък от целочислено деление
print(7 // 2)   # целочислено деление
print(4 ** 3)   # степенуване

# оператори за сравнение
print(10 > 3)   # по-голямо
print(5 < 4)    # по-малко
print(6 >= 10)  # по-голямо или равно
print(20 <= 20) # по-малко или равно
print(10 == 10) # равно ли е
print(10 != 10) # различно ли е

# логически оператори
print(True and False)  # логическо И
print(True or False)   # логическо ИЛИ
print(not True)        # логическо отрицание

# типове данни и променливи
num = 10
pi = 3.14
name = 'Kleopatra'
is_bigger = 4 < 5
print(type(num))        # тип int
print(type(pi))         # тип float
print(type(name))       # тип str
print(type(is_bigger))  # тип bool


# операции със стрингове
first_name = 'Stamat'
last_name = 'Stavrov'
full_name = first_name + ' ' + last_name # конкатенация (долепване)
print(full_name)
print(first_name * 3)   # дублиране

# преобразуване на типове
s = '3'
num = int(s) # преобразуване от стринг в цяло число
pi_str = '3.14'
pi_num = float(pi_str)  # преобразуване от стринг в десетично число

# вход и изход от конзолата
a_in = input('Enter text: ') # въвеждане на текст
b_in = int(input('Enter integer number: ')) # въвеждане на цяло число
c_in = float(input('Enter float number '))  # въвеждане на десетично число
print('a_in = %s, b_in = %d, c_in = %f' % (a_in, b_in, c_in))  # извеждане на променливите
