#!/usr/bin/env python3
import ctypes
import os
import random
import socket
import json

from PIL import Image, ImageDraw, ImageFont
from win32api import GetSystemMetrics

from .my_decorators import catch_all_and_print
from .windows_utils import set_reg_sz, set_reg_dword


def convert_rgb_to_tuple(hex_rgb):
    """Converts RGB color to tuple. Example: input = #0099FF, output tuple=(0x00, 0x99,0xFF)"""
    if hex_rgb[0] != "#":
        raise ValueError
    else:
        hex_rgb = hex_rgb[1:]
        return tuple(int(hex_rgb[i:i + 2], 16) for i in (0, 2, 4))


def get_current_resolution():
    """Returns current sessions screen resolution"""
    return GetSystemMetrics(0), GetSystemMetrics(1)


def get_random_color_tuple():
    """Generates a random RGB numer in form of tuple"""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def create_and_save_wallpaper(backgroud_color_tuple=None, text_color_tuple=None):
    if not backgroud_color_tuple:
        backgroud_color_tuple = get_random_color_tuple()

    if not text_color_tuple:
        text_color_tuple = get_random_color_tuple()

    print('background:', backgroud_color_tuple, 'text', text_color_tuple)
    height, width = get_current_resolution()

    img = Image.new(
        'RGB',
        (height, width),
        color=backgroud_color_tuple
    )

    d = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("art/fonts/arial.ttf", height // 20)
    d.text(
        (0.7 * height, 0.8 * width),
        socket.gethostbyname(socket.gethostname()),
        font=fnt,
        fill=text_color_tuple
    )

    d.text(
        (0.1 * height, 0.1 * width),
        socket.gethostbyname(socket.gethostname()),
        font=fnt,
        fill=text_color_tuple
    )

    wallpaper_path = os.path.dirname(os.path.abspath(__file__)) + "/art/random_wallpaper.png"
    img.save(wallpaper_path)
    return wallpaper_path


def set_background_type_to_picture():
    set_reg_dword(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Wallpapers", "BackgroundType", 0)


def set_wallpaper(wallpaper_path, permanent=True):
    SPI_SETDESKWALLPAPER = 20
    # winapi permanent settings https://devblogs.microsoft.com/oldnewthing/20160721-00/?p=93925
    CURRENT_SESSION_ONLY = 0
    SPIF_UPDATE_INI_FILE = 1  # wallpaper will survive OS session res

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path,
                                               SPIF_UPDATE_INI_FILE if permanent else CURRENT_SESSION_ONLY)


def strech_wallpaper():
    WALLPAPER_STRETCH = str(2)
    set_reg_sz(r"Control Panel\Desktop", r"WallpaperStyle", WALLPAPER_STRETCH)


@catch_all_and_print
def set_random_wallpaper():
    """Creates and sets wallpaper with random colors"""
    set_background_type_to_picture()
    wallpaper_path = create_and_save_wallpaper()
    set_wallpaper(wallpaper_path)
    strech_wallpaper()


@catch_all_and_print
def set_wallpaper_from_predefined():
    """Creates and sets wallpaper using random scheme from predefined file"""
    set_background_type_to_picture()

    predefined_path = os.path.dirname(os.path.abspath(__file__)) + "/art/predefined_color_sets.json"
    with open(predefined_path, 'r') as f:
        pred_color_sets_list = json.loads(f.read())

    random_wallpaper_idx = random.randint(0, len(pred_color_sets_list) - 1)
    random_wallpaper_dict = pred_color_sets_list[random_wallpaper_idx]

    print(f"Setting {random_wallpaper_dict['name']} as wallpaper")

    wallpaper_path = create_and_save_wallpaper(convert_rgb_to_tuple(random_wallpaper_dict['background']),
                                               convert_rgb_to_tuple(random_wallpaper_dict['text']))
    set_wallpaper(wallpaper_path)
    strech_wallpaper()


@catch_all_and_print
def set_selected_wallpaper(chosen_colors_scheme):
    """Create and sets wallpaper from predefined file indicated by name as argument"""
    if not chosen_colors_scheme:
        print("No color set was indicated! Did you mean to use [-r] or [-p] flags?")
        exit()

    set_background_type_to_picture()

    predefined_path = os.path.dirname(os.path.abspath(__file__)) + "/art/predefined_color_sets.json"
    with open(predefined_path, 'r') as f:
        pred_color_sets_list = json.loads(f.read())

    selected = next((elem for elem in pred_color_sets_list if elem["name"] == chosen_colors_scheme),
                    None)

    if selected is None:
        print(f"Predefined color set with \'{chosen_colors_scheme}\' could not be found!")
        exit()

    wallpaper_path = create_and_save_wallpaper(convert_rgb_to_tuple(selected['background']),
                                               convert_rgb_to_tuple(selected['text']))
    set_wallpaper(wallpaper_path)
    strech_wallpaper()
