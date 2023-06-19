
'''
Пользователь делает вклад в размере a рублей сроком
на years лет под 10% годовых (каждый год размер его
вклада увеличивается на 10%. Эти деньги прибавляются
к сумме вклада, и на них в следующем году тоже будут проценты).

Написать функцию bank, принимающая аргументы a и years,
и возвращающую сумму, которая будет на счету пользователя.

---------------------------------------------------------------------------

The user makes a deposit in the amount of a rubles for a period
for years under 10% per annum (each year the size of its
contribution is increased by 10%. This money is added
to the amount of the deposit, and they will also have interest next year).

Write a bank function that takes arguments a and years,
and returning the amount that will be on the user's account.
'''



def bank(a = float(input("Введите количество рублей: ").replace(',','.')), 
         years = float(input("Введите количество годов: ").replace(',','.'))):
    day_year = 365
    sum = a * (1 + 0.1 / day_year)**(years*day_year)
    return sum
print (bank())