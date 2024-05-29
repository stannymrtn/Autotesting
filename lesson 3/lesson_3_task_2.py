from smartphone import Smartphone

catalog =[
    ("Apple", "iPhone 12", "+79161234567"),
    ("Samsung", "Galaxy S21", "+79162345678"),
    ("Google", "Pixel 5", "+79163456789"),
    ("OnePlus", "8 Pro", "+79164567890"),
    ("Xiaomi", "Mi 11", "+79165678901")
]

data = [Smartphone(brand, model, number) for brand, model, number in catalog]

for phone in data:
    phone.print_phone_brand()
    phone.print_phone_model()
    phone.print_phone_number()
