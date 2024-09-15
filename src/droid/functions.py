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


def format_table(data=[], outfile=None):
    if not data:
        print("No data to display")
        return

    # Extract headers and rows
    headers = list(data[0].keys())
    rows = [list(item.values()) for item in data]

    # Create the header row
    header_row = " | ".join(headers)
    separator_row = " | ".join(["---"] * len(headers))

    # Create the data rows
    data_rows = [" | ".join(map(str, row)) for row in rows]

    # Print the Markdown table
    print(header_row)
    print(separator_row)
    for row in data_rows:
        print(row)


def format_list(data=[], outfile=None):
    if not data:
        print("No data to display")
        return
    if not outfile:
        for item in data:
            print("---")
            for key, value in item.items():
                print(f"{key}: {value}")
            print()  # Blank line to separate items
    else:
        with open(outfile, "w", encoding="utf8") as f:
            for item in data:
                f.write("---\n")
                for key, value in item.items():
                    f.write(f"{key}: {value}\n")
                f.write("\n")