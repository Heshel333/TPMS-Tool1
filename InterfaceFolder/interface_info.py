import dearpygui.dearpygui as dpg


def info():
    with dpg.window(
        pos=(900, 650),
        width=900, height=450,
        no_move=True, no_close=True, no_resize=True, no_collapse=True
    ):
        dpg.add_text(f"Transparent: -", tag="transparent_info")
        dpg.add_text(f"Z: 0 ", tag="z_info")

