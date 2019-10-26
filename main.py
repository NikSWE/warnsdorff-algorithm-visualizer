import curses
from time import sleep
from typing import List
from utils.cursor import Cursor


def update_board(stdscr, cursor: Cursor, board: List[List[int]]) -> None:
    cursor.reset_x()
    cursor.reset_y()
    print_board(stdscr, cursor, board)


def print_board(stdscr, cursor: Cursor, board: List[List[int]]) -> None:
    # horizontal boundry line
    cursor.set_x(1)
    stdscr.addstr(cursor.get_y(), cursor.get_x(), '-' * 29,
                  curses.color_pair(1))
    cursor.set_y(1)

    for row in range(8):
        cursor.reset_x()

        # print empty line
        if 0 < row <= 7:
            stdscr.addstr(cursor.get_y(), cursor.get_x(), '|' + ' ' * 29 + '|',
                          curses.color_pair(1))
            cursor.set_y(1)

        # print left border
        stdscr.addstr(cursor.get_y(), cursor.get_x(), '|',
                      curses.color_pair(1))
        cursor.set_x(1)

        for col in range(8):
            # cell is visited
            if board[row][col] == 1:
                stdscr.addstr(cursor.get_y(), cursor.get_x(),
                              str(board[row][col]), curses.color_pair(2))
            # knight's cell
            elif board[row][col] == 2:
                stdscr.addstr(cursor.get_y(), cursor.get_x(),
                              str(board[row][col]), curses.color_pair(3))
            # cell is unvisited
            else:
                stdscr.addstr(cursor.get_y(), cursor.get_x(),
                              str(board[row][col]), curses.color_pair(4))
            cursor.set_x(1)

            if col != 7:
                cursor.set_x(3)

        # print right border
        stdscr.addstr(cursor.get_y(), cursor.get_x(), '|',
                      curses.color_pair(1))
        cursor.set_y(1)

    cursor.reset_x()

    # horizontal boundry line
    cursor.set_x(1)
    stdscr.addstr(cursor.get_y(), cursor.get_x(), '-' * 29,
                  curses.color_pair(1))
    cursor.set_y(1)

    stdscr.refresh()


def main(stdscr) -> None:
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

    # get max x and y co-ordinates of the window
    max_y, max_x = stdscr.getmaxyx()

    # 8 x 8 chess board
    board: List[List[int]] = [[0] * 8 for _ in range(8)]

    # initialize the cursor
    cursor: Cursor = Cursor(max_x, max_y)

    print_board(stdscr, cursor, board)
    sleep(1)

    for row in range(8):
        for col in range(8):
            board[row][col] = 1
            update_board(stdscr, cursor, board)
            sleep(1)


curses.wrapper(main)
