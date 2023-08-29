def bank(x,y):
    going_high_rate = 0.1
    my_amount = x
    for _ in range(y):
        rate = my_amount * going_high_rate
        my_amount += rate
    return my_amount
my_deposit = int (input("Введите сумму вклада: "))
years = int(input("Введите сумму(лет)"))
result = bank(my_deposit,years)
print(f"Сумма после {years} лет: {result:.2f} рублей")