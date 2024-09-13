from droid.color import ColorLogger
def set_logger(params):
    logger = ColorLogger("droid", **params)
    return logger