print('ax + b = 0')
a = float(input('Enter a: '))
b = float(input('Enter b: '))

if a == 0 and b == 0:
    print('Every x is root')
elif a == 0 and b != 0:
    print('No real roots')
else:
    x = -b / a
    print('x = %f' % (x))
