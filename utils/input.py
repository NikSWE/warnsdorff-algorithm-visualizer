from colorama import Fore
from os import system, name


def clear() -> None:
    '''
    clears the console
    '''
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def print_dummy_board() -> None:
    '''
    print a dummy board with indexes for all the cells
    '''
    j: int = 0
    for i in range(9):
        if i != 0:
            print(
                str(j) + '   ' + Fore.YELLOW +
                '|   |   |   |   |   |   |   |   |')
            print('    ' + Fore.YELLOW + '---------------------------------')
            j += 1
        else:
            print('      ' + '0   1   2   3   4   5   6   7\n')
            print('    ' + Fore.YELLOW + '---------------------------------')
    print('\n')


def validate(pos: str) -> bool:
    '''
    check if user's input is valid
    '''
    try:
        row, col = list(map(int, pos.split(',')))
        
        if not 0<=row<=7 or not 0<=col<=7:
            raise ValueError()
    except:
        return False
    return True
