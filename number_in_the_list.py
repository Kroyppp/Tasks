
'''
Напишите программу, которая считывает список чисел 
lst из первой строки и число 
x из второй строки, которая выводит все позиции, на которых встречается число 
x в переданном списке lst.
Позиции нумеруются с нуля, если число 
x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

---------------------------------------------------------------------------------------------

Write a program that reads a list of numbers
lst from the first line and a number
x from the second line, which outputs all positions where the number occurs
x in the passed list lst.
Positions are numbered from zero if the number
x is not found in the list, output the string "Missing" (without quotes, capitalized).
Positions should be displayed in one line, in ascending absolute value.
'''
lst = [1, 1, 2, 3, 4, 5, 3, 3]
x = 3
index = 0

for i in lst:
    index +=1
    if x == i:
        print (index-1)
else:
    try:
        index = lst.index(x, 0)
    except ValueError:
        print ('Отсутствует')