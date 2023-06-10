num1 = float(input('Введите первое число:').replace(',','.'))
def square(num1):
   S = num1*num1*num1*num1
   P = 4*num1
   d = (2**0,5)*num1
   result = (S, P, d)
      
   return result

print(square(num1))