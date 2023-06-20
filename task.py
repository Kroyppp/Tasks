
'''
Выведите таблицу размером 
n×n, заполненную числами 
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь 
�
=
5
n=5)
'''

#number = (int (input ('Введите число: '))**2) + 1
number = (5**2) + 1
list_rn = list (range (1, number))
print (list_rn)
num_arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]
           ]

for i in range (len (num_arr)):
    for j in range (len (num_arr[i])):
        print (num_arr[i][j], end = ' ')
    print ()