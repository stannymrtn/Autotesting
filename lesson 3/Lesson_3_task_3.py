from Address import Address
from Mailto import Mailing

from_address = Address(index="123456", city="Москва", street="Ленинградский", home="1", office="10")
to_address = Address(index="654321", city="Санкт-Петербург", street="Московский", home="10", office="20")

mailing = Mailing(to_address=to_address, from_address=from_address, cost=500, track="AB123456789CD")

from_address_str = from_address.index + ", " + from_address.city + ", " + from_address.street + ", " + from_address.home + " - " + from_address.office
to_address_str = to_address.index + ", " + to_address.city + ", " + to_address.street + ", " + to_address.home + " - " + to_address.office

print("Отправление " + mailing.track + " из " + from_address_str + " в " + to_address_str + ". Стоимость " + str(mailing.cost) + " рублей.")