"""Threat modelling module"""
import tkinter
import tkinter as tk
from tkinter import ttk

def create_window() -> tkinter.Tk:
    """
    Creates the Tkinter application
    :return: The app
    """
    return tk.Tk()

def center_window(
        root: tkinter.Tk,
        height: int,
        width: int
) -> None:
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

def set_window_title(
        root: tkinter.Tk,
        title: str
) -> None:
    """
    Sets the window title
    :param root: The application
    :param title: The title of the window
    :return: None
    """
    root.title(title)

def create_notebook(frame: tkinter.Frame) -> tkinter.ttk.Notebook:
    """
    Create a notebook object
    :param frame: The frame the notebook is in
    :return: The notebook
    """
    return ttk.Notebook(frame)

def create_tab(
        notebook: tkinter.ttk.Notebook,
        tab_name: str
) -> ttk.Frame:
    """
    Create a tab on the Tkinter notebook object
    :param notebook: The notebook
    :param tab_name: The name of the tab
    :return: The notebook tab
    """
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)
    return tab

def pack_tabs(notebook: tkinter.ttk.Notebook) -> None:
    """
    Add the notebook to the app
    :param notebook: The notebook
    :return: None
    """
    notebook.pack(expand=1, fill=tk.BOTH)

def create_canvas(frame: tkinter.Frame) -> tkinter.Canvas:
    """
    Creating a canvas in tkinter
    :param frame: The frame, the canvas is being added to
    :return: The canvas
    """
    canvas = tkinter.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    return canvas

def add_frame_to_tab(canvas: tkinter.Canvas) -> None:
    """
    Add a frame to a tab on the notebook
    :param canvas: The canvas being added
    :return: None
    """
    main = tkinter.Frame(canvas)
    main.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=main, anchor="nw")

def draw_node(canvas: tkinter.Canvas,
              x0: int,
              y0: int,
              x1: int,
              y1: int,
              outline: str,
              fill: str,
              width: int,
) -> None:
    """
    Draw a node on the app
    :param canvas: The canvas being drawn on
    :param x0: The left most x coordinate
    :param y0: The top y coordinate
    :param x1: The right most x coordinate
    :param y1: The bottom y coordinate
    :param outline: The outline colour
    :param fill: The fill colour
    :param width: The node's width
    :return: None
    """
    # Draw the node on the canvas
    canvas.create_rectangle(x0, y0, x1, y1, outline=outline, fill=fill, width=width)

def draw_text(
        canvas: tkinter.Canvas,
        x: int,
        y: int,
        text: str,
        width: int,
        font_size: int
) -> None:
    """
    Add text to the node
    :param canvas: The canvas being drawn on
    :param x: The x coordinate
    :param y: The y coordinate
    :param text: The text being drawn
    :param width: The max width of the text
    :param font_size: The font size
    :return: None
    """
    # Draw the text on the node
    canvas.create_text(x, y, font=("Verdana", font_size), text=text, width=width)

def draw_arrow(
        canvas: tkinter,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        arrow_shape: tuple[int, int, int],
        width: int
) -> None:
    """
    Draw arrow on the screen to connect nodes
    :param canvas: The canvas being drawn on
    :param x1: The first x coordinate
    :param y1: The first y coordinate
    :param x2: The second x coordinate
    :param y2: The second y coordinate
    :param arrow_shape: The arrow head
    :param width: The width of the line
    :return: None
    """
    # Draw a line on the screen
    canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, arrowshape=arrow_shape, width=width)
