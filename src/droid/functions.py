from droid.color import ColorLogger


def set_logger(logger_name: str = "Droid", params: dict = {}):
    logger = ColorLogger(
        logger_name,
        debug_mode=params["debug_mode"],
        json_enabled=params["json_enabled"],
        json_stdout=params["json_stdout"],
        log_file=params["log_file"],
    )
    return logger
