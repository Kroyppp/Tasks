
'''
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое
 число n — столько элементов последовательности должна отобразить программа. На выходе ожидается
   последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

---------------------------------------------------------------------------------------------------

Write a program that prints part of the sequence 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(the number is repeated as many times as it is equal to). The input to the program is a non-negative integer.
  the number n is how many elements of the sequence the program should display. The output is expected
    a sequence of numbers written with a space in one line.

For example, if n = 7, then the program should output 1 2 2 3 3 3 4.
'''
lists = []
number = int (input ('Сколько чисел отобразить: '))
count = int()

while number < 0:   # если вводимое число ниже нуля
    number = int (input ('Сколько чисел отобразить: '))
    continue

if number >= 0: # если вводимое число больше нуля

    for i in range (0, number+1): 
        i_number = i
        i_str = []

        for k in range(i_number):
            i_str.append(i)
        
        sum_i_str = []
        sum_i_str += i_str
        len_i_str = len (sum_i_str)

        for j in i_str:
            count += 1

            if count <= number:
                lists.append (int(j))
            
    print (" ".join (map (str, lists)))
