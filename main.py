import curses
from typing import List, Tuple
from colorama import init, Fore
from time import sleep
from heapq import heappush, heappop
from utils.cursor import Cursor
from utils.input import print_dummy_board, clear, validate
from utils.board import print_board, update_board


def algorithm(stdscr, cursor: Cursor, board: List[List[int]], krow: int,
              kcol: int) -> None:
    '''
    warnsdorff's algorithm implementation
    '''
    # directions the Knight can move on the chessboard
    dx: List[int] = [1, 2, 2, 1, -1, -2, -2, -1]
    dy: List[int] = [-2, -1, 1, 2, 2, 1, -1, -2]

    for _ in range(64):
        board[krow][kcol] = 1
        pq: List[Tuple[int, int]] = []  # priority queue of avialable neighbors

        # degree of neighbors
        for i in range(8):
            nrow: int = krow + dx[i]
            ncol: int = kcol + dy[i]

            if 0 <= nrow <= 7 and 0 <= ncol <= 7 and board[nrow][ncol] == 0:
                # count the available neighbors of the neighbor
                count = 0
                for j in range(8):
                    nnrow: int = nrow + dx[j]
                    nncol: int = ncol + dy[j]

                    if 0 <= nnrow <= 7 and 0 <= nncol <= 7 and board[nnrow][
                            nncol] == 0:
                        count += 1
                heappush(pq, (count, i))

        if len(pq) > 0:
            (p, m) = heappop(pq) # knight's next position
            krow += dx[m]
            kcol += dy[m]
            board[krow][kcol] = 2
            update_board(stdscr, cursor, board)
        else:
            board[krow][kcol] = 1
            update_board(stdscr, cursor, board)            


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

    # start the warnsdorff algorithm
    algorithm(stdscr, cursor, board, pos[0], pos[1])

    sleep(5.0)


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
