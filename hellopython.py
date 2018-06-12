from numpy import *
# '''
a = array([1,2,3])
print(a)
print(a.ndim)   # размерность массива (одномерный, двумерный итд)
print(a.shape)  # размеры массива(число строк столбцов итд)

b = array([(1.5, 2, 3), (4, 5, 6)])  # создание двумерного массива из двух последовательностей чисел
print(b)  # все числа имееют один тип - число с плавающей точкой
print(b.ndim)
print(b.shape)
print(b.size)

z = zeros((3, 2))  # 3,2 помещаются в дополнительные скобки, чтобы представлять из себя один объект
print(z)

a = arange(10, 30, 5)  # функция arange аналогична функции range, но возвращает массив
print()
print(a)
print()

lin = linspace(0, 2, 9)
print(lin)

b = arange(12)
print(b)
b = b.reshape(4, 3)  # меняет размерность массива
print(b)

a = array([10, 20, 30])
b = arange(3)
print(a, b)
print(a + b)  # арифметические операции на массивах выполняются поэлементно
print(a - b)
print(a ** 2)

print(a)
a = 2 * sin(a)  # массив можно передать как аргумент какой-то функции и тогда
print(a)        # эта функция будет применена к каждому элементу массива

# '''

a = array([10, 20, 30])
print(a < 20)