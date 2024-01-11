import logging

import dearpygui.dearpygui as dpg


def save_callback():
    print("Save Clicked")


class AI:
    ai_name: str
    ai_instance_id: int = 0

    def __init__(self):
        AI.ai_instance_id += 1
        self.setup()

    def setup(self):
        # Setup member variables
        self.ai_name = f"AI-{AI.ai_instance_id}"

        # Setup utilities
        self.setup_log_controller()
        self.setup_dpg()

        self.log_info("AI setup complete")

    @staticmethod
    def setup_dpg():
        dpg.create_context()
        dpg.create_viewport()
        dpg.setup_dearpygui()
        with dpg.window(label="Example Window"):
            dpg.add_text("Hello world")
            dpg.add_button(label="Save", callback=save_callback)
            dpg.add_input_text(label="string")
            dpg.add_slider_float(label="float")
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def setup_log_controller(self):
        logging.basicConfig(level=logging.DEBUG)
        self.setup_console_log_controller()
        self.setup_file_log_controller()

    def setup_console_log_controller(self):
        console_log_controller = logging.StreamHandler()
        console_log_controller.setLevel(logging.DEBUG)
        console_log_controller.setFormatter(self.get_log_formatter())
        logging.getLogger().addHandler(console_log_controller)

    @staticmethod
    def get_log_formatter():
        return logging.Formatter(
            f"[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] [%(funcName)s] %(message)s",
            "%Y-%m-%d %H:%M:%S")

    def setup_file_log_controller(self):
        file_log_controller = logging.FileHandler(f"{self.ai_name}.log")
        file_log_controller.setLevel(logging.DEBUG)
        file_log_controller.setFormatter(self.get_log_formatter())
        logging.getLogger().addHandler(file_log_controller)

    @staticmethod
    def log_info(message):
        logging.info(message)
