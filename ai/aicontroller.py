import logging


class AI:
    ai_name: str
    ai_instance_id: int = 0

    def __init__(self):
        AI.ai_instance_id += 1
        self.setup()

    def setup(self):
        self.ai_name = f"AI-{AI.ai_instance_id}"
        self.setup_log_controller()
        self.log_info("AI setup complete")

    def setup_log_controller(self):
        logging.basicConfig(level=logging.DEBUG)
        self.setup_console_log_controller()
        self.setup_file_log_controller()

    def setup_console_log_controller(self):
        console_log_controller = logging.StreamHandler()
        console_log_controller.setLevel(logging.DEBUG)
        console_log_controller.setFormatter(self.get_log_formatter())
        logging.getLogger().addHandler(console_log_controller)

    def get_log_formatter(self):
        return logging.Formatter(
            f"[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] [%(funcName)s] %(message)s",
            "%Y-%m-%d %H:%M:%S")

    def setup_file_log_controller(self):
        file_log_controller = logging.FileHandler(f"{self.ai_name}.log")
        file_log_controller.setLevel(logging.DEBUG)
        file_log_controller.setFormatter(self.get_log_formatter())
        logging.getLogger().addHandler(file_log_controller)

    def log_info(self, message):
        logging.info(message)
