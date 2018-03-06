def add_neighbour(field, tile, choice, length):
    if choice == 'vt':  # nor
        if tile[0] - length != -1:
            field[tile[0] - length][tile[1]] = '·'
        if tile[0] != 9:
            field[tile[0] + 1][tile[1]] = '·'
        if tile[1] != 0 and tile[0] - length != -1:
            field[tile[0] - length][tile[1] - 1] = '·'
        if tile[1] != 9 and tile[0] - length != -1:
            field[tile[0] - length][tile[1] + 1] = '·'
        if tile[1] != 0 and tile[0] != 9:
            field[tile[0] + 1][tile[1] - 1] = '·'
        if tile[1] != 9 and tile[0] != 9:
            field[tile[0] + 1][tile[1] + 1] = '·'
        for i in range(tile[0] - length + 1, tile[0] + 1):
            if tile[1] != 0:
                field[i][tile[1] - 1] = '·'
            if tile[1] != 9:
                field[i][tile[1] + 1] = '·'

    elif choice == 'vb':  # norm
        if tile[0] != 0:
            field[tile[0] - 1][tile[1]] = '·'
        if tile[0] + length - 1 != 9:
            field[tile[0] + length][tile[1]] = '·'
        if tile[1] != 0 and tile[0] != 0:
            field[tile[0] - 1][tile[1] - 1] = '·'
        if tile[1] != 9 and tile[0] != 0:
            field[tile[0] - 1][tile[1] + 1] = '·'
        if tile[1] != 0 and tile[0] + length < 10:
            field[tile[0] + length][tile[1] - 1] = '·'
        if tile[1] != 9 and tile[0] + length < 10:
            field[tile[0] + length][tile[1] + 1] = '·'
        for i in range(tile[0], length + tile[0]):
            if tile[1] != 0:
                field[i][tile[1] - 1] = '·'
            if tile[1] != 9:
                field[i][tile[1] + 1] = '·'

    elif choice == 'hr':  # norm
        if tile[1] != 0:
            field[tile[0]][tile[1] - 1] = '·'
        if tile[1] + length < 10:
            field[tile[0]][tile[1] + length] = '·'
        if tile[1] != 0 and tile[0] != 9:
            field[tile[0] + 1][tile[1] - 1] = '·'
        if tile[1] != 0 and tile[0] != 0:
            field[tile[0] - 1][tile[1] - 1] = '·'
        if tile[1] + length < 10 and tile[0] != 9:
            field[tile[0] + 1][tile[1] + length] = '·'
        if tile[1] + length < 10 and tile[0] != 0:
            field[tile[0] - 1][tile[1] + length] = '·'
        for i in range(tile[1], length + tile[1]):
            if tile[0] != 0:
                field[tile[0] - 1][i] = '·'
            if tile[0] != 9:
                field[tile[0] + 1][i] = '·'
    else:  # norm
        if tile[1] != 9:
            field[tile[0]][tile[1] + 1] = '·'
        if tile[1] - length != -1:
            field[tile[0]][tile[1] - length] = '·'
        if tile[1] != 9 and tile[0] != 0:
            field[tile[0] - 1][tile[1] + 1] = '·'
        if tile[1] != 9 and tile[0] != 9:
            field[tile[0] + 1][tile[1] + 1] = '·'
        if tile[1] - length != -1 and tile[0] != 9:
            field[tile[0] + 1][tile[1] - length] = '·'
        if tile[1] - length != -1 and tile[0] != 0:
            field[tile[0] - 1][tile[1] - length] = '·'
        for i in range(tile[1] - length + 1, tile[1] + 1):
            if tile[0] != 0:
                field[tile[0] - 1][i] = '·'
            if tile[0] != 9:
                field[tile[0] + 1][i] = '·'
    return field


def check_neighbour(field, tile, choice, length):
    if choice == 'vt':  # nor
        if tile[0] - length != -1 and field[tile[0] - length][tile[1]] == 'X':
            return False
        if tile[0] != 9 and field[tile[0] + 1][tile[1]] == 'X':
            return False
        if tile[1] != 0 and tile[0] - length != -1 and\
           field[tile[0] - length][tile[1] - 1] == 'X':
            return False
        if tile[1] != 9 and tile[0] - length != -1 and\
           field[tile[0] - length][tile[1] + 1] == 'X':
            return False
        if tile[1] != 0 and tile[0] != 9 and\
           field[tile[0] + 1][tile[1] - 1] == 'X':
            return False
        if tile[1] != 9 and tile[0] != 9 and\
           field[tile[0] + 1][tile[1] + 1] == 'X':
            return False

        for i in range(tile[0] - length + 1, tile[0] + 1):
            if field[i][tile[1]] != ' ':
                return False
            if tile[1] != 0 and field[i][tile[1] - 1] == 'X':
                return False
            if tile[1] != 9 and field[i][tile[1] + 1] == 'X':
                return False

    elif choice == 'vb':  # norm
        if tile[0] != 0 and field[tile[0] - 1][tile[1]] == 'X':
            return False
        if tile[0] + length - 1 != 9 and\
           field[tile[0] + length][tile[1]] == 'X':
            return False
        if tile[1] != 0 and tile[0] != 0 and\
           field[tile[0] - 1][tile[1] - 1] == 'X':
            return False
        if tile[1] != 9 and tile[0] != 0 and\
           field[tile[0] - 1][tile[1] + 1] == 'X':
            return False
        if tile[1] != 0 and tile[0] + length < 10 and\
           field[tile[0] + length][tile[1] - 1] == 'X':
            return False
        if tile[1] != 9 and tile[0] + length < 10 and\
           field[tile[0] + length][tile[1] + 1] == 'X':
            return False

        for i in range(tile[0], length + tile[0]):
            if field[i][tile[1]] != ' ':
                return False
            if tile[1] != 0 and field[i][tile[1] - 1] == 'X':
                return False
            if tile[1] != 9 and field[i][tile[1] + 1] == 'X':
                return False

    elif choice == 'hr':  # norm
        if tile[1] != 0 and field[tile[0]][tile[1] - 1] == 'X':
            return False
        if tile[1] + length < 10 and field[tile[0]][tile[1] + length] == 'X':
            return False
        if tile[1] != 0 and tile[0] < 9 and\
           field[tile[0] + 1][tile[1] - 1] == 'X':
            return False
        if tile[1] != 0 and tile[0] != 0 and\
           field[tile[0] - 1][tile[1] - 1] == 'X':
            return False
        if tile[1] + length < 10 and tile[0] < 9 and\
           field[tile[0] + 1][tile[1] + length - 1] == 'X':
            return False
        if tile[1] + length < 10 and tile[0] != 0 and\
           field[tile[0] - 1][tile[1] + length - 1] == 'X':
            return False

        for i in range(tile[1], length + tile[1]):
            if field[tile[0]][i] != ' ':
                return False
            if tile[0] != 0 and field[tile[0] - 1][i] == 'X':
                return False
            if tile[0] != 9 and field[tile[0] + 1][i] == 'X':
                return False
    else:  # norm
        if tile[1] != 9 and field[tile[0]][tile[1] + 1] == 'X':
            return False
        if tile[1] - length != -1 and\
           field[tile[0]][tile[1] - length] == 'X':
            return False
        if tile[1] != 9 and tile[0] != 0 and\
           field[tile[0] - 1][tile[1] + 1] == 'X':
            return False
        if tile[1] != 9 and tile[0] != 9 and\
           field[tile[0] + 1][tile[1] + 1] == 'X':
            return False
        if tile[1] - length != -1 and tile[0] != 9 and\
           field[tile[0] + 1][tile[1] - length] == 'X':
            return False
        if tile[1] - length != -1 and tile[0] != 0 and\
           field[tile[0] - 1][tile[1] - length] == 'X':
            return False

        for i in range(tile[1] - length + 1, tile[1] + 1):
            if field[tile[0]][i] != ' ':
                return False
            if tile[0] != 0 and field[tile[0] - 1][i] == 'X':
                return False
            if tile[0] != 9 and field[tile[0] + 1][i] == 'X':
                return False

    return True
