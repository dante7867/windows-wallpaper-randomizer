#!/usr/bin/env python3
import ctypes
import os
import random
import socket

from PIL import Image, ImageDraw, ImageFont
from win32api import GetSystemMetrics

from .my_decorators import catch_all_and_print
from .windows_utils import set_reg_sz, set_reg_dword


def get_current_resolution():
    return GetSystemMetrics(0), GetSystemMetrics(1)


def create_and_save_wallpaper():
    height, width = get_current_resolution()

    img = Image.new(
        'RGB',
        (height, width),
        color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    )

    d = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("art/fonts/arial.ttf", height // 20)
    d.text(
        (0.7 * height, 0.8 * width),
        socket.gethostbyname(socket.gethostname()),
        font=fnt,
        fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    )

    d.text(
        (0.1 * height, 0.1 * width),
        socket.gethostbyname(socket.gethostname()),
        font=fnt,
        fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
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
    set_background_type_to_picture()
    wallpaper_path = create_and_save_wallpaper()
    set_wallpaper(wallpaper_path)
    strech_wallpaper()

