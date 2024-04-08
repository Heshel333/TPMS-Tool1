import dearpygui.dearpygui as dpg
import numpy as np


def scatter_plot(data):
    with dpg.window(
        pos=(0, 0),
        width=650, height=650,
        no_move=True, no_close=True, no_resize=True, no_collapse=True
    ):
        with dpg.plot(width=600, height=600):

            dpg.add_plot_axis(dpg.mvXAxis, tag="x_axis")
            dpg.add_plot_axis(dpg.mvYAxis, tag="y_axis")

            dpg.set_axis_limits("x_axis", 0, 2 * np.pi)
            dpg.set_axis_limits("y_axis", 0, 2 * np.pi)

            dpg.add_scatter_series(tuple(data[0][0]), tuple(data[0][1]), label="-", parent="y_axis", tag="series")
            dpg.add_scatter_series(tuple(data[1][0]), tuple(data[1][1]), label="-", parent="y_axis", tag="series_in")
            dpg.add_scatter_series(tuple(data[2][0]), tuple(data[2][1]), label="-", parent="y_axis", tag="series_out")


def transparent_plot(data):
    with dpg.window(
        pos=(650, 0),
        width=950, height=650,
        no_move=True, no_close=True, no_resize=True, no_collapse=True
    ):
        with dpg.plot(width=900, height=600):

            dpg.add_plot_axis(dpg.mvXAxis, tag="x_axis1")
            dpg.add_plot_axis(dpg.mvYAxis, tag="y_axis1")

            dpg.set_axis_limits("x_axis1", 0, 1)
            dpg.set_axis_limits("y_axis1", min(data[0]), max(data[0]))

            dpg.add_line_series(tuple(data[1]), tuple(data[0]), label="-", parent="y_axis1", tag="series1")
            dpg.add_line_series((0, 0), (min(data[0]), max(data[0])), label="-", parent="y_axis1", tag="series1_line")
            dpg.add_line_series((-100, 100), (0, 0), label="-", parent="y_axis1", tag="series2_line")
