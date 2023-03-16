import random


class Card:

    def __init__(self, name):
        self.name = name
        self.barrels = [i for i in range(1, 91)]
        self.cals = [i for i in range(9)]
        self.barrels_in_row = 5
        self.rows = 3
        self.card = self.get_card()

    def get_card(self):
        card = []
        for i in range(3):
            cells_to_fill = random.sample(self.cals, self.barrels_in_row)
            row_barrels = [self.barrels.pop(random.randint(0, len(self.barrels) - 1))
                           for i in range(self.barrels_in_row)]
            row_barrels.sort()
            row = [0 for i in range(len(self.cals))]

            for j in range(self.barrels_in_row):
                row[cells_to_fill[j]] = row_barrels[j]

            card.append(row)
        return card

    def print_card(self):
        pos = int((26 - len(self.name)) / 2)
        line = '-' * pos + self.name + '-' * (pos + 1 if pos % 2 == 0 else pos)
        print(line)
        for row in self.card:
            for cell in row:
                if cell == 0:
                    print(' ' * 3, end='')
                else:
                    if cell < 10:
                        print(end=' ')
                        if cell == -1:
                            cell = '-'
                    print(cell, end=' ')
            print()
        print('-' * 26)

    def try_number(self, number):
        for line in self.card:
            if number in line:
                index = int(line.index(number))
                line[index] = -1
                return True
        return False

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.name == other.name

    def __contains__(self, item):
        return self.try_number(item)
