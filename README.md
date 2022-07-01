# windows-wallpaper-randomizer
#### _Small script to randomize wallpaper on windows 10 based machines_

This script was made to make it easier to distinguish different sessions when working with multiple remote desktop instances by assigning them a different wallpaper.

## Example
<img src="https://user-images.githubusercontent.com/31797203/176911664-9faf9827-a80d-4013-b56c-50f5f1dc753b.png" width="512" height="288" />

# Command line arguments

## [-r, --random] 
### How is wallpaper generated?
- ip address is read automatically
- resolution of the wallpaper is read from currently used 
- background and ip adresses colors are random
- proportions are hardcoded

## [-p, --random-predefined] 
Picks a random background and text set from a file in `./win_wallpaper_randomizer/art/predefined_color_sets.json`.
Feel free to add your own stylish mixes!

| Name | Background | Text |
| --- | --- | --- |
| yellow_and_blue | ![#f4b41a](https://via.placeholder.com/15/f4b41a/f4b41a.png) | ![#143d59](https://via.placeholder.com/15/143d59/143d59.png) |
| navy_and_teal | ![#21007](https://via.placeholder.com/15/21007/21007.png) | ![#213970](https://via.placeholder.com/15/213970/213970.png) |
| black_and_orange | ![#ffe042](https://via.placeholder.com/15/ffe042/ffe042.png) | ![#e71989](https://via.placeholder.com/15/e71989/e71989.png) |
| maroon_and_peach | ![#ffa781](https://via.placeholder.com/15/ffa781/ffa781.png) | ![#5b0e2d](https://via.placeholder.com/15/5b0e2d/5b0e2d.png) |
| deep_purple_and_blue | ![#00e1d9](https://via.placeholder.com/15/00e1d9/00e1d9.png) | ![#5e001f](https://via.placeholder.com/15/5e001f/5e001f.png) |
| blue_and_gray | ![#0e387a](https://via.placeholder.com/15/0e387a/0e387a.png) | ![#9fafca](https://via.placeholder.com/15/9fafca/9fafca.png) |
| blue_and_yellow | ![#fcc729](https://via.placeholder.com/15/fcc729/fcc729.png) | ![#337def](https://via.placeholder.com/15/337def/337def.png) |
| olive_and_white | ![#a3842c](https://via.placeholder.com/15/a3842c/a3842c.png) | ![#ffffff](https://via.placeholder.com/15/ffffff/ffffff.png) |
| forest_green_and_dark_sea_green | ![#0f4d19](https://via.placeholder.com/15/0f4d19/0f4d19.png) | ![#6fc27c](https://via.placeholder.com/15/6fc27c/6fc27c.png) |
| orange_and_blue | ![#54b22](https://via.placeholder.com/15/54b22/54b22.png) | ![#abd1ff](https://via.placeholder.com/15/abd1ff/abd1ff.png) |
| blue_and_peach | ![#0f149a](https://via.placeholder.com/15/0f149a/0f149a.png) | ![#fd9b4d](https://via.placeholder.com/15/fd9b4d/fd9b4d.png) |
| dark_brown_and_marigold | ![#372800](https://via.placeholder.com/15/372800/372800.png) | ![#f6b60d](https://via.placeholder.com/15/f6b60d/f6b60d.png) |
| pink_and_maroon | ![#f9858b](https://via.placeholder.com/15/f9858b/f9858b.png) | ![#761137](https://via.placeholder.com/15/761137/761137.png) |


