from itertools import islice


def find_ships(field, x, z):
    """Finds all ships on the field"""
    global ships
    rang = iter([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    for y in rang:
        if field[x][y] == 'X':
            if field[x + z][y] == 'X' and x + z > -1 and\
               (x == 9 or field[x + 1][y] != 'X'):
                if field[x + 2 * z][y] == field[x + 3 * z][y] == 'X'\
                                                   and x + 3*z > -1:
                    ships[4].append(tuple((chr(x + i * z + 66),
                                          y + 1) for i in range(1, 5)))
                elif field[x + 2 * z][y] == 'X' and x + 2*z > -1:
                    ships[3].append(tuple((chr(x + i * z + 66),
                                          y + 1) for i in range(1, 4)))
                else:
                    ships[2].append(tuple((chr(x + i * z + 66),
                                          y + 1) for i in range(1, 3)))
                next(rang, None)
            elif field[x][y + z] == 'X' and y + z > -1:
                if field[x][y + 2 * z] == field[x][y + 3 * z] == 'X'\
                                                   and y + 3*z > -1:
                    ships[4].append(tuple((chr(x + 65),
                                          y + z * i + 1) for i in range(4)))
                    next(islice(rang, 3, None), None)
                elif field[x][y + 2 * z] == 'X' and y + 2*z > -1:
                    ships[3].append(tuple((chr(x + 65),
                                          y + z * i + 1) for i in range(3)))
                    next(islice(rang, 2, None), None)
                else:
                    ships[2].append(tuple((chr(x + 65),
                                          y + z * i + 1) for i in range(2)))
                    next(islice(rang, 1, None), None)
            else:
                if (x != 9 and field[x + 1][y] != 'X') or x == 9:
                    ships[1].append(((chr(x + 65), y + 1),))
                    next(rang, None)


def find_all_ships(field):
    global ships
    ships = {1: [], 2: [], 3: [], 4: []}

    for x in range(0, 10):
        find_ships(field, x, -1)

    return ships
