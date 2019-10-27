import curses
from typing import List, Tuple
from colorama import init, Fore
from time import sleep
from heapq import heappush, heappop
from utils.cursor import Cursor
from utils.input import print_dummy_board, clear, validate
from utils.board import print_board, update_board


def algorithm() -> None:
    pass


def visualize(stdscr, pos: Tuple[int, int]) -> None:
    # clear the window
    stdscr.clear()

    # hide the cursor
    curses.curs_set(0)

    # colors
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # boundry
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # visited cell
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # knight's cell
    curses.init_pair(4, curses.COLOR_WHITE,
                     curses.COLOR_BLACK)  # unvisited cell
    curses.init_pair(5, curses.COLOR_MAGENTA,
                     curses.COLOR_BLACK)  # progress bar

    # get max x and y co-ordinates of the window
    max_y, max_x = stdscr.getmaxyx()

    # 8 x 8 chess board
    board: List[List[int]] = [[0] * 8 for _ in range(8)]

    # initialize the cursor
    cursor: Cursor = Cursor(max_x, max_y)

    # place the knight on the board
    board[pos[0]][pos[1]] = 2

    # print the chess board
    print_board(stdscr, cursor, board, sleep_value=2.0, initialize=True)

    for row in range(8):
        for col in range(8):
            if board[row][col] != 2:
                board[row][col] = 1
            update_board(stdscr, cursor, board)


def main() -> None:
    # initialize colorama
    init(autoreset=True)

    while True:
        clear()

        # print dummy chess board to help user decide knight's position
        print_dummy_board()

        pos = input('knight\'s position (row, col): ')

        # check user's input
        if validate(pos):
            break
        else:
            print(Fore.RED + 'Invalid, Try Again.')
            sleep(1)

    # start visualization
    curses.wrapper(visualize, tuple(map(int, pos.split(','))))

    clear()


if __name__ == '__main__':
    main()
