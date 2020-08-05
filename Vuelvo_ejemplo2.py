from Vuelo_class_error import *
from Vuelo_class_error import make_flights

from pprint import pprint as pp
"""
p = make_flight()
print(p)

# Reubica un pasajero a otro lugar
p.relocate_passenger('2A', '4A')
print(pp(p._seating))

# Imprime la cant de asientos disponibles
# Toma el valor de las row (7) * cantidad de rows en el avion (22)
# y sustrae el Numero de asiento ocupados (3)
# es decir 7 * 22 - 3
print(p.num_available_seats())
"""

p, w = make_flights()
print(p.aircraft_model())
print(p.num_available_seats())
print(w.aircraft_model())
print(w.num_available_seats())
w.relocate_passenger('2A', '1A')
"""
nose de donde sacar el 
make_boarding_cards

print(w.make_boarding_cards(console_card_printer))

"""

a = AirbusA319('G-AAAA')
print(a.num_seats())