# Tableau Public to HTML

- [Tableau Public to HTML](#tableau-public-to-html)
  - [Objective](#objective)
  - [Usage](#usage)
    - [FILE_DICT Mode](#file_dict-mode)
    - [Terminal Mode](#terminal-mode)
  - [Result](#result)
  - [Customization](#customization)

## Objective

By pasting the embedded code provided by Tableau Public, users only need to add some description then the html file is created automatically. Which could save lots of time, when there's a lot of Tableau table need to be generated.

## Usage

There's a `html_creator.exe` file if you want to make it easy, just follow the instructions, and the result would be the same as well as the below modes.

If you want to execute without using the `.exe` file, there are two ways to use this tool:

1. Modify the data in the `html_creator.py`file.
2. Type the data through the Terminal.

Both way are very easy, there are some comments in that file.

> The filename in the below image would be `web_creator_final_version.py` instead, sorry about that.

### FILE_DICT Mode

All the data is stored in the file, need to overwrite the `FILE_DICT`.

![FILE_DICT mode](https://i.imgur.com/xeJr8Z8.png)

### Terminal Mode

Although there's `FILE_DICT`, but we could type the data through terminal without change amy code of this file.

![Terminal mode - 1](https://i.imgur.com/3lUnYs1.png)
![Terminal mode - 2](https://i.imgur.com/A3J0XvG.png)

## Result

All the files we created would be stored in the `html\<year>_<month>_<date>\` directory.

![Html folder](https://i.imgur.com/jQOf9Sv.png)

## Customization

If you don't like the default color and layout, you could change the code in `create_file` at `html_creator.py`, the layout in based on `module.html`.
