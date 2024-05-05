def month_to_season(number_month):
    if number_month in [12,1,2]:
        print("Winter")
    elif number_month in [3,4,5]:
        print("Spring")
    elif number_month in [6,7,8]:
        print("Summer")
    elif number_month in [9,10,11]:
        print("Autumn")
    else:
    
        return("Incorrect number of month")

number_month = (int(input("Enter a number of month: ")))
time_of_season = month_to_season(number_month)