import curses
from time import sleep
from typing import List
from utils.cursor import Cursor


def main(stdscr) -> None:
    # clear the window
    stdscr.clear()

    # hide the cursor
    curses.curs_set(0)

    # colors
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # boundry

    # get max x and y co-ordinates of the window
    max_y, max_x = stdscr.getmaxyx()

    # 8 x 8 chess board
    board: List[List[int]] = [[0] * 8] * 8

    # initialize the cursor
    cursor: Cursor = Cursor(max_x, max_y)

    # horizontal boundry line
    cursor.set_x(1)
    stdscr.addstr(cursor.get_y(), cursor.get_x(), '-' * 29,
                  curses.color_pair(1))
    cursor.set_y(1)

    for row in range(8):
        cursor.reset_x(max_x)

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
            stdscr.addch(cursor.get_y(), cursor.get_x(), str(board[row][col]))
            cursor.set_x(1)

            if col != 7:
                cursor.set_x(3)

        # print right border
        stdscr.addstr(cursor.get_y(), cursor.get_x(), '|',
                      curses.color_pair(1))
        cursor.set_y(1)

    cursor.reset_x(max_x)

    # horizontal boundry line
    cursor.set_x(1)
    stdscr.addstr(cursor.get_y(), cursor.get_x(), '-' * 29,
                  curses.color_pair(1))
    cursor.set_y(1)

    stdscr.refresh()
    sleep(30)


curses.wrapper(main)
