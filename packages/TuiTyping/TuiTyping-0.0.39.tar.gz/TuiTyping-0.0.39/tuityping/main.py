import argparse
import curses
from tuityping.displays.typing_screen import start
from tuityping.utilities.utilities import edit_setting_value
from tuityping.utilities.colors import init_colors
from tuityping.displays.start_screen import start_screen


def get_args():
    parser = argparse.ArgumentParser(description="Terminal Type Tester.")
    parser.add_argument("-t", dest="tempo", type=int, help="Test duration")
    return parser.parse_args()


def main():
    args = get_args()
    if args.tempo is not None:
        edit_setting_value("time", args.tempo)
    curses.wrapper(start_screen)
