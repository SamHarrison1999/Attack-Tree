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
        pre_digitisation_attack_tree_frame: tk.Frame,
        post_digitisation_attack_tree_frame: tk.Frame,
        app: tk.Tk,
        button_1: tk.Button,
        button_2: tk.Button
) -> None:
    """
    Creates the pre-digitisation attack tree
    :param pre_digitisation_attack_tree_frame: The pre-digitisation attack tree frame
    :param post_digitisation_attack_tree_frame: The post-digitisation attack tree frame
    :param app: The Tkinter application
    :param button_1: Load the pre-digitisation attack trees
    :param button_2: Load the post-digitisation attack trees
    :return: None
    """
    # Clear the screen
    clear_frame(pre_digitisation_attack_tree_frame)
    clear_frame(post_digitisation_attack_tree_frame)
    # Read the data from the json file
    data = packages.utils.read_json('data/pre-digitisation.json')
    # Update the title label
    tk.Label(
        pre_digitisation_attack_tree_frame,
        text="Pre Digitisation Attack Tree",
        font=("Verdana", 28)
    ).pack(
        side=tk.TOP,
        pady=20
    )
    # Update the window title
    app.title ('Pre Digitisation Attack Tree for Pampered Pets')
    # Set up the individual tabs for the attack tree
    canvases = setup_notebook(
        pre_digitisation_attack_tree_frame, data
    )
    nodes = data.items()
    for i in range(len(list(data.keys()))):
        draw_root_node(app, canvases[i], list(data.keys())[i])
    for node in nodes:
        for index, key in enumerate(dict(list(node)[1]).keys()):
            if "Router" in list(node)[0]:
                draw_arrows(canvases[0], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[0], index, key, len(list(node)[1]))
            elif "Computers/Phones" in list(node)[0]:
                draw_arrows(canvases[1], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[1], index, key, len(list(node)[1]))
            elif "Database" in list(node)[0]:
                draw_arrows(canvases[2], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[2], index, key, len(list(node)[1]))
            elif "Payment System" in list(node)[0]:
                draw_arrows(canvases[3], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[3], index, key, len(list(node)[1]))
            elif "Staff" in list(node)[0]:
                draw_arrows(canvases[4], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[4], index, key, len(list(node)[1]))
            elif "Customers" in list(node)[0]:
                draw_arrows(canvases[5], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[5], index, key, len(list(node)[1]))
            elif "Buildings" in list(node)[0]:
                draw_arrows(canvases[6], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[6], index, key, len(list(node)[1]))
            elif "Inventory" in list(node)[0]:
                draw_arrows(canvases[7], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[7], index, key, len(list(node)[1]))
            elif "Customer Data" in list(node)[0]:
                draw_arrows(canvases[8], len(list(node)[1]), app)
                draw_child_nodes(app, canvases[8], index, key, len(list(node)[1]))
    button_1.config(
        command=lambda: pre_digitisation(
            pre_digitisation_attack_tree_frame,
            post_digitisation_attack_tree_frame,
            app,
            button_1,
            button_2
        )
    )
    button_2.config(
        command= lambda : post_digitisation(
            post_digitisation_attack_tree_frame,
            pre_digitisation_attack_tree_frame,
            app,
            button_1,
            button_2
        )
    )
    # Put the frame on the screen
    pre_digitisation_attack_tree_frame.pack(
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


def draw_child_nodes(app: tk.Tk, canvas: tk.Canvas, x: int, text: str, length: int) -> None:
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
    canvas.create_rectangle(x0, 300, x1, 400, outline="black", fill="white", width=2)
    # Drawing the text on the child nodes
    canvas.create_text(x0 + (x1 - x0) // 2, 350, font=("Verdana", 15), text=text, width=200)


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
            (app.winfo_width() // arrows) * i - (app.winfo_width() // arrows) // 2,
            300,
            arrow=tk.LAST,
            arrowshape=(10, 20, 10),
            width=3
        )


def post_digitisation(
        post_digitisation_attack_tree_frame: tk.Frame,
        pre_digitisation_attack_tree_frame: tk.Frame,
        app: tk.Tk,
        button_1: tk.Button,
        button_2: tk.Button
) -> None:
    """
    Creates the post-digitisation attack tree
    :param post_digitisation_attack_tree_frame: The post-digitisation attack tree frame
    :param pre_digitisation_attack_tree_frame: The pre-digitisation attack tree frame
    :param app: The Tkinter application
    :param button_1: Load the pre-digitisation attack trees
    :param button_2: Load the post-digitisation attack trees
    :return: None
    """
    # Clear the screen
    clear_frame(pre_digitisation_attack_tree_frame)
    clear_frame(post_digitisation_attack_tree_frame)
    # Read the data from the json file
    data = packages.utils.read_json('data/post_digitisation.json')
    # Update the title label
    tk.Label(
        post_digitisation_attack_tree_frame,
        text="Post Digitisation Attack Tree",
        font=("Verdana", 28)
    ).pack(
        side=tk.TOP,
        pady=20
    )
    # Update the window title
    app.title('Post Digitisation Attack Tree for Pampered Pets')
    # Set up the individual tabs for the attack tree
    canvases = setup_notebook(
        post_digitisation_attack_tree_frame, data
    )
    for key in data.keys():
        # Draw the attack tree for each tab on the application
        dread_values = get_dread_values(data, key)
        if "Spoofing" in dread_values:
            draw_attack_tree(app, data, dread_values, key, canvases[0])
            draw_arrows(canvases[0],len(data[key]['Threats'].keys()), app)
        elif "Tampering" in dread_values:
            draw_attack_tree(app, data, dread_values, key, canvases[1])
            draw_arrows(canvases[1], len(data[key]['Threats'].keys()), app)
        elif "Repudiation" in dread_values:
            draw_attack_tree(app, data, dread_values, key, canvases[2])
            draw_arrows(canvases[2], len(data[key]['Threats'].keys()), app)
        elif "Information Disclosure" in dread_values:
            draw_attack_tree(app, data, dread_values, key, canvases[3])
            draw_arrows(canvases[3], len(data[key]['Threats'].keys()), app)
        elif "Denial of Service" in dread_values:
            draw_attack_tree(app, data, dread_values, key, canvases[4])
            draw_arrows(canvases[4], len(data[key]['Threats'].keys()), app)
        elif "Elevation of Privilege" in dread_values:
            draw_attack_tree(app, data, dread_values, key, canvases[5])
            draw_arrows(canvases[5], len(data[key]['Threats'].keys()), app)
    # Button configurations to switch between frames
    button_1.config(
        command= lambda : pre_digitisation(
            pre_digitisation_attack_tree_frame,
            post_digitisation_attack_tree_frame,
            app,
            button_1,
            button_2
        )
    )
    button_2.config(
        command= lambda : post_digitisation(
            post_digitisation_attack_tree_frame,
            pre_digitisation_attack_tree_frame,
            app,
            button_1,
            button_2
        )
    )
    # Put the frame on the screen
    post_digitisation_attack_tree_frame.pack(
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



def setup_notebook(frame: tk.Frame, data: dict[str]) -> list[tk.Canvas]:
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


def draw_attack_tree(
        app: tk.Tk,
        data: dict[str],
        dread_values: str,
        key: str,
        canvas: tk.Canvas
) -> None:
    """
    Draw the attack tree using the data from the json file
    :param app: The Tkinter application
    :param data: The data from the json file
    :param dread_values: The dread values for each vulnerability
    :param key: The name of the nodes
    :param canvas: The canvas being drawn on
    :return: None
    """
    draw_root_node(app, canvas, dread_values)
    for i, k in enumerate(data[key]['Threats'].keys()):
        draw_child_nodes(app, canvas, i, k, len(data[key]['Threats']))


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
        command=lambda : pre_digitisation(
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
