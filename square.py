
'''
Написать функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
площадь квадрата и диагональ квадрата.

Write a function square that takes 1 argument - the side of the square,
and returning 3 values (using a tuple): the perimeter of the square,
the area of a square and the diagonal of a square.
'''



num1 = float(input('Введите первое число:').replace(',','.'))
def square(num1):
   S = num1*num1*num1*num1
   P = 4*num1
   d = (2**0.5)*num1
   result = (S, P, d)
      
   return result

print(square(num1))
