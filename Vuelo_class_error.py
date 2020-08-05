class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999) :
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]


    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """Ubicar a un pasajero en un asiento.
        
        Args:
            asiento: un asiento designado como '12C' o '21F'.
            pasajero: El nombre del pasajero.

        Raises:
            ValueError: si el asiento es invalido.
        """

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row {row_text}')

        if row not in rows:
            raise ValueError(f'Invalid row number {row}')

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Reubica a un pasajero a diferente asiento.

        Args:
            from_seat: el asiento existente del pasajero 
            para reubicarlo.

            to_seat: el nuevo asiento designado.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f'No passenger to relocate in seat {from_seat}')

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'Seat {to_seat} already occupied')

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating
                    if row is not None)

"""
class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), 
                "ABCDEFGHJK"[:self._num_seats_per_row])
"""

class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

    def model(self):
        return 'AirbusA319'

    def seating_plan(self):
        return range(1, 23), 'ABCDEF'


class Boeing777(Aircraft):
    
    def model(self):
        return 'Boeing777'

    def seating_plan(self):
        return range(1, 56), 'ABCDEFGHJK'


def console_card_printer(passenger, seat, flight_number, aircraft):
    output =f'| Name: {passenger}'      \
            f'  Flight: {flight_number}'\
            f'  Seat: {seat}'           \
            f'  Aircraft: {aircraft}'   \
            '| '
    banner = '+' + '-' * (len(output) - 2 ) + '+'
    border = '|' + ' ' * (len(output) - 2 ) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

def make_flights():
    p = Flight('BA756', AirbusA319('G-AAAA'))
    p.allocate_seat('2A', 'Frankestein')
    p.allocate_seat('3A', 'Dracula')
    p.allocate_seat('2B', 'Hombre lobo')

    w = Flight('AF73', Boeing777('F-BBBD'))
    w.allocate_seat('2A', 'Luffy')
    w.allocate_seat('3A', 'Zoro')
    w.allocate_seat('2B', 'Ash Ketchup')

    return p, w



    

