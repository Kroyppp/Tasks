
'''
Написать функцию is_prime, принимающую 1 аргумент — число от 0
до 1000, и возвращающую True, если оно простое, и False - иначе.

-----------------------------------------------------------------------

Write a function is_prime that takes 1 argument - a number from 0
up to 1000, and returning True if it is prime, and False otherwise.
'''

def is_prime(number = int(input('Введите число от 0 до 1000:'))):
    if number >= 1 and number <= 1000:
        dividers = 0
        for i in range(1, number+1):
            if number % i == 0:
                dividers += 1
        if dividers > 2:
            return print ("Число " + str(number) + " непростое ")
        else: 
            return print ("Число " + str(number) + " простое ")
    elif number == 0: 
        return print ("Число 0")
    elif number > 1000: 
        return print ("Число больше 1000")
    else:
        return print ("Число некорректное")
    
print (is_prime())
