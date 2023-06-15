
''' Определяет високосный год или нет'''
year = int(input('Введите год:'))
def is_year_leap(year):
    if year % 4 != 0:
        return print('Невисокосный год')
    elif year % 100 == 0:
        if year % 400 == 0:
            print('Год високосный.')
        else:
            print('Год не високосный.')
    else:
        print('Год високосный.')

print(is_year_leap(year))
