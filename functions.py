import random
import re


from find_ships import find_all_ships
from neighbours import *
from add_random_ships import *


def check_input(data):
    """Check if user inputed valid coordinates"""
    if len(data) < 2:
        return False
    if not isinstance(data[0], str):
        return False
    data = data.upper()
    res = re.split('\s|(?<!\d)[,.]|[,.](?!\d)', data)
    if len(res) == 1:
        res = [res[0][0], res[0][1:]]
    try:
        res[1] = int(res[1])
    except ValueError:
        return False

    if not 64 < ord(res[0]) < 76:
        return False
    if not 0 < int(res[1]) < 11:
        return False

    return res if len(res) == 2 else False


def read_field(filename):
    """
    (str) -> (data)
    Read and return field from file

    :param name: str
    :return: list
    """
    field = []
    with open(filename) as field_file:
        for line in field_file:
            field.append(line.rstrip() + ' '*(10 - len(line.rstrip())))

    return field


def has_ship(field, cell):
    """
    Return True if field with coordinates as cell has ship,
    otherwise False
    :param field: list
    :param cell: tuple
    :return: bool
    """
    return False if field[ord(cell[0]) - 65][cell[1] - 1]\
                    == ' ' else True


def is_valid(field, ships):
    """
    Return True if field is valid, otherwise False
    :param field: list
    :return: bool
    """
    if sum([line.count('X') for line in field]) != 20:
        return False
    if len(field) != 10:
        return False
    if sum([x * len(ships[x]) for x in ships.keys()]) != 20:
        return False

    for key in ships:
        if key + len(ships[key]) != 5:
            return False

    return True


def ship_size(field, coordinates, ships):
    """Return ship size as tuple"""
    tile = [ord(coordinates[0]) - 65, coordinates[1] - 1]
    place = field[tile[0]][tile[1]]
    if place == ' ':
        return None
    for key in ships:
        for value in ships[key]:
            if coordinates in value:
                return (1, key) if len(value) == 1\
                                   or value[0][1] == value[1][1]\
                                   else (key, 1)


def field_to_str(field):
    """
    (list) -> (str)
    Return field as string
    :param field: list
    :return: str
    """
    result = '  '
    for i in range(1, 11):
        result += str(i) + '│' if i < 9 else str(i) + '│'
    result += '\n' + '─'*24
    result += '\n'
    for line in range(len(field)):
        result += chr(65 + line) + '│'
        for x in field[line]:
            result += x + '│' + ''
        result += '\n' + '─'*23 + '\n'
    return result


def generate_field():
    """Randomly generate fiels"""
    field = [[' ' for _ in range(10)] for _ in range(10)]
    res = []

    for length in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
        try_field = False
        while not try_field:
            (y, x), ch = choose_coordinates(field, length)
            try_field = add_ship(field.copy(), length, (y, x), ch)

    for line in try_field:
        for thing in range(10):
            if line[thing] == '·':
                line[thing] = ' '

    return try_field
