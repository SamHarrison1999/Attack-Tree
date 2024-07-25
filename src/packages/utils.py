"""Utility modules"""
import json
import tkinter as tk


def read_json(file: str) -> dict[str]:
    """
    Read JSON file
    :param file: path to file
    :return: JSON file as dictionary
    """
    # Loads the json file into a dictionary
    with open(file, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
        return data


def center_window(root: tk.Tk, height: int, width: int) -> None:
    """
    Centers the window on the screen
    :param root: The application
    :param height: The height of the window
    :param width: The width of the window
    :return: None
    """
    # Centers the application on the user's screen
    x = root.winfo_screenwidth() // 2 - width // 2
    y = root.winfo_screenheight() // 2 - height // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
