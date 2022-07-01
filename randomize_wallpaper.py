import argparse
import sys

from win_wallpaper_randomizer import *


def parse_args():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-r', '--random', help="set wallpaper with randomly generated colors", action='store_true')
    group.add_argument('-p', '--random-predefined', help="set one of wallpapers from\
            predefined in ./win_wallpaper_randomizer/art/predefined_color_sets.json", action='store_true')
    group.add_argument('-s', '--selected', type=str, help="name of selected color scheme predefined in "
                                                          "./win_wallpaper_randomizer/art/predefined_color_sets.json")

    arguments = parser.parse_args()

    return arguments


if __name__ == "__main__":
    args = parse_args()
    no_args_passed = True if len(sys.argv) == 1 else False

    if args.random or no_args_passed:
        set_random_wallpaper()

    elif args.random_predefined:
        set_wallpaper_from_predefined()

    elif args.selected:
        set_selected_wallpaper(args.selected)
