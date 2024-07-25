"""Main application file"""
# Import statements
import tkinter as tk
from tkinter import ttk

import packages.utils


def clear_frame(frame: tk.Frame) -> None:
    """
    Removes all widgets from a selected frame
    :param frame: The frame you want to remove all the widgets from
    :return: None
    """
    # Removes the frame and all its contents
    for widget in frame.winfo_children():
        widget.destroy()
        frame.pack_forget()


def pre_digitisation(
        frame_one: tk.Frame,
        frame_two: tk.Frame,
        app: tk.Tk,
        button_1: tk.Button,
        button_2: tk.Button
) -> None:
    """
    Creates the pre-digitisation attack tree
    :param frame_one: The pre-digitisation frame
    :param frame_two: The post-digitisation frame
    :param app: The Tkinter application
    :param button_1: Load the pre-digitisation attack trees
    :param button_2: Load the post-digitisation attack trees
    :return: None
    """
    # Clear the screen
    clear_frame(frame_one)
    clear_frame(frame_two)
    # Read the data from the json file
    data = packages.utils.read_json('data/pre-digitisation.json')
    # Update the title label
    tk.Label(
        frame_one,
        text="Pre Digitisation Attack Tree",
        font=("Verdana", 28)
    ).pack(
        side=tk.TOP,
        pady=20
    )
    # Update the window title
    app.title('Pre Digitisation Attack Tree for Pampered Pets')
    # Set up the individual tabs for the attack tree
    canvases = setup_gui(
        frame_one, data
    )
    for i in range(len(list(data.keys()))):
        key = list(data.keys())[i]
        draw_root_node(app, canvases[i], list(data.keys())[i])
        for index, k in enumerate(data[key]['Threats'].keys()):
            draw_child_nodes(
                app,
                canvases[i],
                index,
                k,
                len(data[key]['Threats'])
            )
        draw_arrows(canvases[i], len(data[key]['Threats'].keys()), app)
    button_1.config(
        command=lambda: pre_digitisation(
            frame_one,
            frame_two,
            app,
            button_1,
            button_2
        )
    )
    button_2.config(
        command=lambda: post_digitisation(
            frame_one,
            frame_two,
            app,
            button_1,
            button_2
        )
    )
    # Put the frame on the screen
    frame_one.pack(
        fill='both',
        expand=1
    )


def draw_root_node(app: tk.Tk, canvas: tk.Canvas, text: str) -> None:
    """
    Draw the root nodes in each attack tree
    :param app: The application
    :param canvas: The canvas being drawn on
    :param text: The text being drawn on the root node
    :return: None
    """
    # Drawing the root node
    canvas.create_rectangle(
        app.winfo_width() // 4,
        20,
        (app.winfo_width() // 4) * 3,
        200,
        outline="black",
        fill="white",
        width=2
    )
    # Adding the text to the root node
    canvas.create_text(
        app.winfo_width() // 2,
        120,
        font=("Verdana", 15),
        text=text,
        width=app.winfo_width() // 2
    )


def draw_child_nodes(
        app: tk.Tk,
        canvas: tk.Canvas,
        x: int,
        text: str,
        length: int
) -> None:
    """
    Drawing the child nodes
    :param app: The application
    :param canvas: The canvas being drawn on
    :param x: The index
    :param text: The text being drawn on the node.
    :param length: The number of nodes
    :return: None
    """
    # Drawing the child nodes
    x0 = 5 + app.winfo_width() // length * x
    x1 = x0 + app.winfo_width() // length - 20
    # Draw the node on the canvas
    canvas.create_rectangle(
        x0,
        300,
        x1,
        400,
        outline="black",
        fill="white",
        width=2
    )
    # Drawing the text on the child nodes
    canvas.create_text(
        x0 + (x1 - x0) // 2,
        350,
        font=("Verdana", 15),
        text=text,
        width=200
    )


def draw_arrows(canvas: tk.Canvas, arrows: int, app: tk.Tk) -> None:
    """
    Draw arrows to connect the nodes
    :param canvas: The canvas being drawn on
    :param arrows: The number of arrows being drawn
    :param app: The Tkinter app
    :return: None
    """
    # Draws an arrow connecting each child node to the root node
    for i in range(1, arrows + 1):
        canvas.create_line(
            app.winfo_width() // 2,
            200,
            (app.winfo_width() // arrows) * i
            - (app.winfo_width() // arrows) // 2,
            300,
            arrow=tk.LAST,
            arrowshape=(10, 20, 10),
            width=3
        )


def post_digitisation(
        frame_one: tk.Frame,
        frame_two: tk.Frame,
        app: tk.Tk,
        button_1: tk.Button,
        button_2: tk.Button
) -> None:
    """
    Creates the post-digitisation attack tree
    :param frame_one: The post-digitisation frame
    :param frame_two: The pre-digitisation frame
    :param app: The Tkinter application
    :param button_1: Load the pre-digitisation attack trees
    :param button_2: Load the post-digitisation attack trees
    :return: None
    """
    # Clear the screen
    clear_frame(frame_two)
    clear_frame(frame_one)
    # Read the data from the json file
    data = packages.utils.read_json('data/post_digitisation.json')
    # Update the title label
    tk.Label(
        frame_one,
        text="Post Digitisation Attack Tree",
        font=("Verdana", 28)
    ).pack(
        side=tk.TOP,
        pady=20
    )
    # Update the window title
    app.title('Post Digitisation Attack Tree for Pampered Pets')
    # Set up the individual tabs for the attack tree
    canvases = setup_gui(
        frame_one,
        data
    )
    for i in range(len(list(data.keys()))):
        dread_values = get_dread_values(
            data,
            list(data.keys())[i]
        )
        key = list(data.keys())[i]
        draw_root_node(app, canvases[i], dread_values)
        for index, k in enumerate(data[key]['Threats'].keys()):
            draw_child_nodes(
                app,
                canvases[i],
                index,
                k,
                len(data[key]['Threats'])
            )
        draw_arrows(canvases[i], len(data[key]['Threats'].keys()), app)
    # Button configurations to switch between frames
    button_1.config(
        command=lambda: pre_digitisation(
            frame_one,
            frame_two,
            app,
            button_1,
            button_2
        )
    )
    button_2.config(
        command=lambda: post_digitisation(
            frame_one,
            frame_two,
            app,
            button_1,
            button_2
        )
    )
    # Put the frame on the screen
    frame_one.pack(
        fill='both',
        expand=1
    )


def get_dread_values(data: dict[str], key: str) -> str:
    """
    :param data: The data from the json file
    :param key: The keys from the json file
    :return: The root nodes with the dread values from the json file
    """
    # Sets up the root nodes
    root_nodes = {}
    stride_values = []
    for k, v in data[key].items():
        if k != 'Threats':
            stride_values.append(k + " - " + str(v))
            root_nodes[key] = stride_values
    # Reads the DREAD values from the json file
    dread_values = key + "\n"
    for x in range(len(root_nodes[key])):
        dread_values += root_nodes[key][x] + "\n"
    return dread_values


def setup_gui(frame: tk.Frame, data: dict[str]) -> list[tk.Canvas]:
    """
    Creates a canvas for each of the individual tabs in the notebook
    :param frame: The frame the canvas is being added to
    :param data: The data from the json file
    :return: A list of the canvases
    """
    notebook = ttk.Notebook(frame)
    canvases = []
    tabs = list(data.keys())
    # Creates a separate tab for each attack tree
    for i in range(len(data.keys())):
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=tabs[i])
        canvas = tk.Canvas(tab)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        notebook.pack(expand=1, fill=tk.BOTH)
        canvases.append(canvas)
    return canvases


if __name__ == '__main__':
    # Creating the application
    root = tk.Tk()
    # Centering the app
    packages.utils.center_window(
        root,
        1080,
        1920
    )
    # Setting the window title
    root.title('Attack Tree Application for Pampered Pets')
    root.resizable(False, False)
    # Creating separate frames for the attack trees
    pre_digitisation_frame = tk.Frame(root)
    post_digitisation_frame = tk.Frame(root)
    # Adding the button to switch between the two frames
    btn1 = tk.Button(
        root,
        text="View Pre Digitisation Attack Tree",
        name="button-one",
        font=("Verdana", 28),
        command=lambda: pre_digitisation(
            pre_digitisation_frame,
            post_digitisation_frame,
            root,
            btn1,
            btn2
        )
    )
    # Putting the switch button on the screen
    btn1.pack(
        side=tk.BOTTOM,
        pady=20
    )
    btn2 = tk.Button(
        root,
        text="View Post Digitisation Attack Tree",
        name="button-two",
        font=("Verdana", 28),
        command=lambda: post_digitisation(
            post_digitisation_frame,
            pre_digitisation_frame,
            root,
            btn1,
            btn2
        )
    )
    # Putting the switch button on the screen
    btn2.pack(
        side=tk.BOTTOM,
        pady=20
    )
    root.mainloop()
