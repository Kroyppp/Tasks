
'''
Написать функцию season, принимающую 1 аргумент —
номер месяца (от 1 до 12), и возвращающую время года,
которому этот месяц принадлежит (зима, весна, лето или осень).

Write a season function that takes 1 argument −
month number (from 1 to 12), and returning the time of year,
to which this month belongs (winter, spring, summer or autumn).
'''


season = int(input("Введите номер месяца: "))

if season >= 1 and season <= 2 or season == 12:
    print("Зима")
elif season >= 3 and season <= 5:
    print("Весна")
elif season >= 6 and season <= 8:
    print("Лето")
elif season >= 9 and season <= 11:
    print("Осень")
else:
    print("Неверный номер месяца")