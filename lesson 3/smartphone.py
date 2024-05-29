class Smartphone:
    def __init__(self,phone_brand,phone_model,phone_number):
        self.brand = phone_brand
        self.model = phone_model
        self.number = phone_number
    def print_phone_brand(self):
        print("Марка телефона: ",self.brand)
    def print_phone_model(self):
        print("Модель телефона: ",self.model)
    def print_phone_number(self):
        print("Номер телефона: ",self.number )

phone_brand = input("Марка телефона: ", )
phone_model = input("Модель телефона: ", )
phone_number = input("Номер телефона:", )

smartphone = Smartphone(phone_brand,phone_model,phone_number)
smartphone.print_phone_brand()
smartphone.print_phone_model()
smartphone.print_phone_number()

    