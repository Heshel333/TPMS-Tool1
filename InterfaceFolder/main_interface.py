from .interface_plots import *
from .interface_controls import *
from .interface_info import *
from Solve import *
from TPMS_functions import *


class Interface:
    def __init__(self):
        self.width, self.height = 1600, 1000
        self.title = "TPMS tool"

        self.thickness = 0.4

        self.form = form['Schwarz P']

        self.scatter_data = count_points_z(0, form['Schwarz P'], self.thickness, self.thickness)
        self.scatter_data_in = count_points_z(0, self.form, self.thickness, 0.02-self.thickness)[0]
        self.scatter_data_out = count_points_z(0, self.form, 0.02-self.thickness, self.thickness)[0]

        self.transparent_data = count_transparent(self.form, self.thickness, self.thickness)

    def update_mode(self):
        if dpg.get_value('custom_on'):
            dpg.hide_item('select_form')
            dpg.show_item('custom')
            dpg.show_item('custom_btn')
        elif not dpg.get_value('custom_on'):
            dpg.show_item('select_form')
            dpg.hide_item('custom')
            dpg.hide_item('custom_btn')

        self.update_scatter()
        self.update_transparent()

    def update_scatter(self):
        form_sel = form[dpg.get_value('select_form')] if not dpg.get_value('custom_on') else eval(f"lambda x, y, z: {dpg.get_value('custom')}")

        # new solve
        sd = count_points_z(dpg.get_value("z_slider"), form_sel, self.thickness, self.thickness)
        sd_in = count_points_z(dpg.get_value("z_slider"), form_sel, self.thickness, 0.05-self.thickness)[0]
        sd_out = count_points_z(dpg.get_value("z_slider"), form_sel, 0.05-self.thickness, self.thickness)[0]

        # change data
        dpg.set_value('series', (tuple(sd[0][0]), tuple(sd[0][1])))
        dpg.set_value('series_in', (tuple(sd_in[0]), tuple(sd_in[1])))
        dpg.set_value('series_out', (tuple(sd_out[0]), tuple(sd_out[1])))

        dpg.set_value('series1_line', ((dpg.get_value("z_slider"), dpg.get_value("z_slider")), (-100, 100)))
        dpg.set_value('series2_line', ((-100, 100), (sd[1], sd[1])))

        dpg.set_value('transparent_info', f"Transparent: {sd[1]:0.5f}")
        dpg.set_value('z_info', f"Z: {dpg.get_value("z_slider"):0.3f}")

    def update_transparent(self):
        form_sel = form[dpg.get_value('select_form')] if not dpg.get_value('custom_on') else eval(f"lambda x, y, z: {dpg.get_value('custom')}")
        td = count_transparent(form_sel, self.thickness, self.thickness)

        dpg.set_axis_limits("x_axis1", 0, 1)
        dpg.set_axis_limits("y_axis1", min(td[0]), max(td[0]))

        dpg.set_value('series1', (tuple(td[1]), tuple(td[0])))

        self.update_scatter()

    def run(self):
        dpg.create_context()

        scatter_plot((self.scatter_data[0], self.scatter_data_in, self.scatter_data_out))
        transparent_plot(self.transparent_data)
        controls((self.update_transparent, self.update_scatter, self.update_mode))
        info()

        dpg.create_viewport(
            title=self.title,
            width=self.width,
            height=self.height,
            large_icon="TPMS_icon.ico",
            small_icon="TPMS_icon.ico",
        )

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
