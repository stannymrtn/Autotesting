def month_to_season(month_number):
    if month_number in [12,1,2]:
        return "Зима"
    elif month_number in [3,4,5]:
        return "Весна"
    elif month_number in [6,7,8]:
        return "Лето"
    elif month_number in [9,10,11]:
        return "Осень"
    else:
        return"Указан неверный номер месяца"
    
month_number = int(input("Введите номер месяца: "))
season = month_to_season(month_number)
print("Сезон: ", season)