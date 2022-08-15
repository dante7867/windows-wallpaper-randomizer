import json

if __name__ == "__main__":
    """Prints a table that can be copied to README.md to present color schemes"""
    predefined_color_sets_path = "../art/predefined_color_sets.json"
    with open(predefined_color_sets_path, 'r') as f:
        pred_color_sets_list = json.loads(f.read())

    print("| Name | Background | Text |")
    print("| --- | --- | --- |")
    for color_set in pred_color_sets_list:
        color_set['background'] = color_set['background'][1:]
        color_set['text'] = color_set['text'][1:]
        # example: yellow_and_green: background: ![#f4b41a](https://via.placeholder.com/15/f4b41a/f4b41a.png)
        # `#f4b41a` text: ![#c5f015](https://via.placeholder.com/15/c5f015/c5f015.png) `#c5f015`
        print(f"| {color_set['name']} | ![#{color_set['background']}](https://via.placeholder.com/15/"
              f"{color_set['background']}/{color_set['background']}.png)"
              f"| ![#{color_set['text']}](https://via.placeholder.com/15/{color_set['text']}/{color_set['text']}.png) |")
