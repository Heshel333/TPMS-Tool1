import dearpygui.dearpygui as dpg
from TPMS_functions import *
from numpy import pi


def controls(callback):
    with dpg.window(
        pos=(0, 650),
        width=900, height=450,
        no_move=True, no_close=True, no_resize=True, no_collapse=True
    ):
        dpg.add_checkbox(label="(Custom)", tag="custom_on", callback=callback[2])

        dpg.add_combo(items=tuple(form.keys()), tag='select_form', default_value="Schwarz P",
                      callback=callback[0])

        dpg.add_input_text(width=600, height=40, default_value="cos(x) + cos(y) + cos(z)", tag='custom', show=False)

        dpg.add_button(label="solve custom", tag='custom_btn', callback=callback[0], show=False)

        dpg.add_text(label='\n')

        dpg.add_slider_float(label="Z", min_value=0, max_value=1, default_value=0, tag="z_slider",
                             callback=callback[1])
