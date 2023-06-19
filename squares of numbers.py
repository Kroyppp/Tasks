
'''
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
 пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.

Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.

В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма 
этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.

------------------------------------------------------------------------------------------------------------------------------------------

Write a program that reads numbers from the console (one per line) until
  until the sum of the entered numbers is equal to 0 and immediately after that displays the sum of the squares of all the read numbers.

It is guaranteed that at some point the sum of the entered numbers will be equal to 0, after which there is no need to continue reading.

In the example, we read the numbers 1, -3, 5, -6, -10, 13; at this point we notice that the sum
of these numbers is equal to zero and print the sum of their squares, ignoring the fact that there are still unread values.
'''

list = []
list.append (int (input ()))
sum_list = sum (list)
while sum_list != 0:
    list.append (int (input ()))
    sum_list = sum (list)
else:
    for i in list:
        sum_list += i**2

print (sum_list)
