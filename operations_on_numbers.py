
''' Функция, принимающая два числа и операцию. Выводит результаты операции'''

num1= float(input('First number: ').replace(',', '.'))
num2= float(input('Two number: ').replace(',', '.'))
operation= str(input('Operation: '))

def arithmetic(num1, num2, operation):
    if operation == '+':
        return num1+num2
    elif operation == '-':
        return num1-num2
    elif operation == '/':
        return num1/num2
    elif operation == '*':
        return num1*num2
    else:
        print ('Неизвестная операция')

print (arithmetic(num1, num2, operation))