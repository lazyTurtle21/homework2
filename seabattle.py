import os

from functions import *


class Game:
    def __init__(self, fields, players, current_player):
        self.__fields = fields[:]
        self.__players = players[:]
        self.__current_player = current_player

    def field_with_ships(self, index):
        return self.__fields[index].field_with_ships()

    def field_without_ships(self, index):
        return self.__fields[index].field_without_ships()

    def shoot_at(self, index, tile):
        hit = self.__fields[index - 1].shoot_at(tile)
        if not hit:
            return False
        if self.check_win(index):
            return '{}, you won!'.format(self.__players[self.__current_player])
        return True

    def check_win(self, index):
        if self.__fields[index - 1].field_with_ships().count('S') == 0:
            return True


class Player:
    def __init__(self, name='Bob'):
        self.__name = name

    def read_position(self, tile):
        if type(tile[0]) == str:
            return (ord(tile[0]) - 65, tile[1] - 1)
        return tile


class Ship:
    def __init__(self, bow, length, hit=[], horizontal=True):
        self.bow = bow
        self.__length = length
        self.__hit = hit[:] if hit else [False for _ in range(max(length))]
        self.horizontal = horizontal

    def shoot_at(self, tile):
        if self.horizontal:
            self.__hit[tile[1] - self.bow[1]] = True
        else:
            self.__hit[tile[0] - self.bow[0]] = True

    def __repr__(self):
        return '{}({}, {}, {}, {})'.format(type(self).__name__,
                                           self.bow, self.__length,
                                           self.__hit, self.horizontal)


class Field:
    def __init__(self, ships=[]):
        self.__ships = ships[:] if len(ships) > 0 else self.generate_board()
        self.show_ships = self.show_ship()

    def generate_board(self):
        field = generate_field()
        board = []
        ships = find_all_ships(field)
        for line in range(10):
            row = []
            for x in range(10):
                if field[line][x] == ' ':
                    row.append(None)
                else:
                    if ((line != 0 and field[line - 1][x] == ' ') or
                        line == 0) and ((x != 0 and
                                        field[line][x - 1] == ' ') or x == 0):
                        length = ship_size(field, (chr(65 + line),
                                                   x + 1), ships)
                        for ship in ships[max(length)]:
                            if (chr(65 + line), x + 1) in ship:
                                bow = (ord(ship[-1][0]) - 65, ship[-1][1] - 1)
                                row.append(Ship(bow, length, horizontal=True
                                           if length[1] == 1 else False))
                                break
                    else:
                        row.append(None)

            board.append(row)
        return board

    def show_ship(self):
        field = self.__ships[:]
        ships = []
        board = []
        for line in field:
            row = []
            for thing in line:
                if type(thing).__name__ == 'Ship':
                    row.append(thing)
                    ships.append(thing)
                else:
                    if not thing:
                        row.append(' ')
                    else:
                        row.append(thing)
            board.append(row)

        for ship in ships:
            if ship.horizontal:
                for x in range(ship.bow[1], ship._Ship__length[0] +
                               ship.bow[1]):
                    board[ship.bow[0]][x] = ship
            else:
                for x in range(ship.bow[0], ship._Ship__length[1] +
                               ship.bow[0]):
                    board[x][ship.bow[1]] = ship
        return board

    def shoot_at(self, tile):
        ships_all = self.show_ships
        ship = ships_all[tile[0]][tile[1]]
        board = self.__ships
        if not ship or type(ship).__name__ != 'Ship':
            self.show_ships[tile[0]][tile[1]] = '·'
            return False

        ship1 = board[ship.bow[0]][ship.bow[1]]
        ship1.shoot_at(tile)
        self.show_ships[tile[0]][tile[1]] = 'X'

        if sum(ship1._Ship__hit) == max(ship1._Ship__length):
            self.show_ships = add_neighbour(self.show_ships, ship1.bow,
                                            'hr' if ship1._Ship__length[1] ==
                                            1 else 'vb',
                                            max(ship1._Ship__length))
        return True

    def field_with_ships(self):
        field = self.show_ships
        result = '  '
        for i in range(1, 11):
            result += str(i) + '  '
        result += '\n'

        for line in range(10):
            result += chr(65 + line)
            for thing in range(10):
                if type(field[line][thing]).__name__ == "Ship":
                    result += ' S'
                elif not field[line][thing]:
                    result += '  '
                else:
                    result += ' ' + str(field[line][thing])
                result += ' '
            result += '\n'
        return result

    def field_without_ships(self):
        field = self.show_ships
        result = '  '
        for i in range(1, 11):
            result += str(i) + '  '
        result += '\n'

        for line in range(10):
            result += chr(65 + line)
            for thing in range(10):
                if type(field[line][thing]).__name__ == "Ship"\
                        or not field[line][thing]:
                    result += '  '
                else:
                    result += ' ' + str(field[line][thing])
                result += ' '
            result += '\n'
        return result


def main():
    field1 = Field()
    field2 = Field()

    player1 = Player(input('Player1, type your name: '))
    player2 = Player(input('Player2, type your name: '))

    print('═════════Game BATTLESHIP════════')

    game = Game([field1, field2], [player1, player2], 0)
    while True:
        os.system('cls')
        move = ''
        print('\nField of the {}:\n'.format(
              game._Game__players[game._Game__current_player - 1].
              _Player__name))
        print(game.field_without_ships(game._Game__current_player))
        while not move:
            move = input(game._Game__players[game._Game__current_player].
                         _Player__name + ', enter move (e.g. B2): ')
            move = check_input(move)
        tile = game._Game__players[game._Game__current_player]\
                   .read_position((move[0], int(move[1])))

        win = game.shoot_at(game._Game__current_player - 1, tile)
        if not win:
            print('Miss! ')
        else:
            print('Hit!')
        if win is not False and win is not True:
            print('\n', win)
            break

        if not win:
            game._Game__current_player = abs(game._Game__current_player - 1)
        else:
            game._Game__current_player = game._Game__current_player


if __name__ == '__main__':
    main()
