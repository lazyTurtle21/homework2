import random

from neighbours import *


lst = list(range(0, 10))


def choose_coordinates(field, length):
    """Randomly choose coordinates for the ship"""
    y = random.choice(lst)
    x = random.choice(lst)
    if y < length:
        if x < length:
            ch = random.choice(['vb', 'hr'])
        elif x > 10 - length:
            ch = random.choice(['vb', 'hl'])
        else:
            ch = random.choice(['vb', 'hl', 'hr'])
    elif y > 10 - length:
        if x < length:
            ch = random.choice(['vt', 'hr'])
        elif x > 10 - length:
            ch = random.choice(['vt', 'hl'])
        else:
            ch = random.choice(['vt', 'hl', 'hr'])
    else:
        if x < length:
            ch = random.choice(['vt', 'hr', 'vb'])
        elif x > 10 - length:
            ch = random.choice(['vt', 'hl', 'vb'])
        else:
            ch = random.choice(['vt', 'hl', 'hr', 'vb'])

    return (y, x), ch


def add_ship(field, length, tile, choice):
    """Adds ship on the field along with neighbours"""
    if not check_neighbour(field, tile, choice, length):
        return False
    if choice == 'vb':
        for i in range(tile[0], length + tile[0]):
            field[i][tile[1]] = 'X'
    elif choice == 'hr':
        for i in range(tile[1], length + tile[1]):
            field[tile[0]][i] = 'X'
    elif choice == 'hl':
        for i in range(tile[1] - length + 1, tile[1] + 1):
            field[tile[0]][i] = 'X'
    elif choice == 'vt':
        for i in range(tile[0] - length + 1, tile[0] + 1):
            field[i][tile[1]] = 'X'

    field = add_neighbour(field, tile, choice, length)
    return field
