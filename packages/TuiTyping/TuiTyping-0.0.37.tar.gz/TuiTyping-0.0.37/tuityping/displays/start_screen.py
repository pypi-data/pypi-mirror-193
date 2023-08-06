import curses
from tuityping.utilities.colors import init_colors
from tuityping.displays.typing_screen import start


def print_logo(stdscr, middle_row, x_position):
    logo = [
        "  ______      _ ______            _            ",
        " /_  __/_  __(_)_  __/_  ______  (_)___  ____ _",
        "  / / / / / / / / / / / / / __ \/ / __ \/ __ `/",
        " / / / /_/ / / / / / /_/ / /_/ / / / / / /_/ / ",
        "/_/  \__,_/_/ /_/  \__, / .___/_/_/ /_/\__, /  ",
        "                  /____/_/            /____/   ",
    ]
    i = 7
    for line in logo:
        stdscr.addstr(middle_row - i, x_position - int(47 / 2), line)
        i -= 1


def start_screen(stdscr):
    stdscr.clear()
    screen = curses.initscr()
    y, x = screen.getmaxyx()
    middle_row = int(y / 2)
    x_position = int((x / 2))
    print_logo(stdscr, middle_row, x_position)
    stdscr.addstr(
        middle_row + 3, x_position - int(30 / 2), "PRESS ENTER TO START TYPING..."
    )
    while True:
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            break
    curses.curs_set(0)
    init_colors()
    curses.wrapper(start)
