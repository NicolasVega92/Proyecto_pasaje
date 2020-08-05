from Vuelo_class_error import *
from pprint import pprint as pp


a = Aircraft('G-EUPP', 'Airbus A319', num_rows=22, num_seats_per_row=6)
print(a.registration())
print(a.model())
print(a.seating_plan())

g = Flight('BA756', Aircraft('G-AAAA', 'Airbus B123', num_rows=22, num_seats_per_row=7))
print(g.aircraft_model())

print(pp(g._seating))

print('*********************')
g.allocate_seat('12A', 'Nicolas Vega')
# El siguiente en el mismo lugar da error debido
# a que el asiento 12A ya esta ocupado
# g.allocate_seat('12A', 'Juan Gabriel')
g.allocate_seat('12B', 'Nicolas Vega')
g.allocate_seat('1A', 'Jauan Vega')
g.allocate_seat('2C', 'Sofia Bolt')
g.allocate_seat('10F', 'Federico Juasda')
g.allocate_seat('10E', 'Ignacio Yun')
g.allocate_seat('12E', 'Sanrtia losda')
print(pp(g._seating))