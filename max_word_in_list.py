
'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова
может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной 
строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно 
встретилось. Если таких слов несколько, вывести лексикографически первое (можно 
использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

--------------------------------------------------------------------------------------------

Recently, we counted for each word the number of its occurrences in a string. But for all words
may not be as interesting to look at as, for example, the most commonly used ones.

Write a program that reads text from a file (there can be more than one
lines) and displays the most frequent word in this text and, separated by a space, how many times it
met. If there are several such words, output the first one lexicographically (you can
use the < operator for strings).

Give the output of the program as your answer, not the program itself.

Words written in different registers are considered the same.
'''

with open ('dataset_3363_3.txt', 'r') as dataset:
    list_dataset = dataset.readlines()
    list_dataset = [line.rstrip() for line in list_dataset]

dictionary_dataset = {}

for i in list_dataset: # подсчитывает количество повторений слов в документе и помещает результат в словарь
    lower_str_dataset = i.lower()
    first_list_dataset = list(lower_str_dataset.split())

    for j in first_list_dataset:

        if j not in list(dictionary_dataset.keys()):
            dictionary_dataset[j] = 1           

        else:
            dictionary_dataset[j] += 1

mx = 0
mx_dictionary_dataset = ''

for k in dictionary_dataset.keys(): # выводит слово с максимальным количеством повторений в документе

    if mx < dictionary_dataset.get(k):
        mx_dictionary_dataset = k
        mx = dictionary_dataset[k]
print (mx_dictionary_dataset, ' = ', mx)


