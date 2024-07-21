import unittest
import tkinter
import tkinter as tk
from tkinter import ttk
import main
import packages.threat_modelling

def _widgets_by_name(parent, name, widgets):
    if not parent.winfo_children():
        if name == parent.winfo_name():
            widgets.append(parent)
    else:
        for child in parent.winfo_children():
            _widgets_by_name(child, name, widgets)


def find_widget_by_name(parent, name):
    """ ui automation function that can find a widget in an application/hierarchy of widgets by its name """
    widgets = []
    _widgets_by_name(parent, name, widgets)
    if len(widgets) == 0:
        raise Exception(f'no widget named {name} found')
    elif len(widgets) > 1:
        raise Exception(f'multiple widget named {name} found')
    return widgets[0]


class MyTestCase(unittest.TestCase):

    def test_clear_frame(self):
        app = main
        app.root = tk.Tk()
        app.pre_digitisation_frame = tk.Frame()
        app.post_digitisation_frame = tk.Frame()
        app.btn1 = tk.Button(app.pre_digitisation_frame, text="Test Button", name="button-one", font=("Verdana", 28), command=lambda :app.post_digitisation(app.post_digitisation_frame, app.pre_digitisation_frame, app.root, app.btn1, app.btn2))
        assert len(app.pre_digitisation_frame.winfo_children()) == 1
        app.clear_frame(app.pre_digitisation_frame)
        assert len(app.pre_digitisation_frame.winfo_children()) == 0

    def test_pre_digitisation_gui_layout(self):
        app = main
        app.root = tk.Tk()
        app.pre_digitisation_frame = tk.Frame()
        app.post_digitisation_frame = tk.Frame()
        app.btn1 = tk.Button(app.root,
                             text="View Pre Digitisation Attack Tree",
                             name="button-one",
                             font=("Verdana", 28),
                             command=lambda : app.pre_digitisation(app.pre_digitisation_frame,
                                                                   app.post_digitisation_frame,
                                                                   app.root,
                                                                   app.btn1,
                                                                   app.btn2
                                                                   )
                             )
        app.btn2 = tk.Button(app.root,
                             text="View Post Digitisation Attack Tree",
                             name="button-two",
                             font=("Verdana", 28),
                             command=lambda: app.post_digitisation(app.post_digitisation_frame,
                                                                   app.pre_digitisation_frame,
                                                                   app.root,
                                                                   app.btn1,
                                                                   app.btn2
                                                                   )
                             )
        app.pre_digitisation(app.pre_digitisation_frame, app.post_digitisation_frame, app.root, app.btn1, app.btn2)
        print(app.pre_digitisation_frame.winfo_children()[0].cget('text'))
        app.root.update()
        assert app.pre_digitisation_frame.winfo_children()[0].cget('text') == 'Pre Digitisation Attack Tree'
        tab_names = []
        for i in app.pre_digitisation_frame.winfo_children()[1].tabs():
            tab_names.append(app.pre_digitisation_frame.winfo_children()[1].tab(i, "text"))
        assert 'Router' in tab_names
        assert 'Computers/Phones' in tab_names
        assert 'Databases' in tab_names
        assert 'Payment System' in tab_names
        assert 'Staff' in tab_names
        assert 'Customers' in tab_names
        assert 'Buildings' in tab_names
        assert 'Inventory' in tab_names
        assert 'Customer Data' in tab_names

    def test_post_digitisation_gui_layout(self):
        app = main
        app.root = tk.Tk()
        app.pre_digitisation_frame = tk.Frame()
        app.post_digitisation_frame = tk.Frame()
        app.btn1 = tk.Button(app.root, text="View Pre Digitisation Attack Tree", name="button-one",
                             font=("Verdana", 28),
                             command=lambda :app.pre_digitisation(app.pre_digitisation_frame,
                                                                                        app.post_digitisation_frame,
                                                                                        app.root,
                                                                                        app.btn1,
                                                                                        app.btn2)
                             )
        app.btn2 = tk.Button(app.root, text="View Post Digitisation Attack Tree", name="button-two",
                             font=("Verdana", 28),
                             command=lambda: app.post_digitisation(app.post_digitisation_frame,
                                                                                         app.pre_digitisation_frame,
                                                                                         app.root,
                                                                                         app.btn1,
                                                                                         app.btn2)
                            )
        app.post_digitisation(app.post_digitisation_frame, app.pre_digitisation_frame, app.root, app.btn1, app.btn2)
        app.root.update()
        assert app.post_digitisation_frame.winfo_children()[0].cget('text') == 'Post Digitisation Attack Tree'
        tab_names = []
        for i in app.post_digitisation_frame.winfo_children()[1].tabs():
            tab_names.append(app.post_digitisation_frame.winfo_children()[1].tab(i, "text"))
        assert 'Spoofing' in tab_names
        assert 'Tampering' in tab_names
        assert 'Repudiation' in tab_names
        assert 'Information Disclosure' in tab_names
        assert 'Denial of Service' in tab_names
        assert 'Elevation of Privilege' in tab_names

    def test_create_window(self):
        app = packages.threat_modelling.create_window()
        packages.threat_modelling.center_window(app, 1080, 1920)
        assert app.winfo_screenwidth() == 1920
        assert app.winfo_screenheight() == 1080
        assert app.winfo_rootx() == 0
        assert app.winfo_rooty() == 0

    def test_add_frame_to_notebook_tab(self):
        app = packages.threat_modelling.create_window()
        app.frame = tk.Frame(app)
        packages.threat_modelling.create_notebook(app.frame)
        app.canvas = packages.threat_modelling.create_canvas(app.frame)
        packages.threat_modelling.add_frame_to_tab(app.canvas)

if __name__ == '__main__':
    unittest.main()
