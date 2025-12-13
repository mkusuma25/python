import csv
import os


def is_valid_amount(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


def save_row_to_csv(filename: str, row: list[str]) -> None:
    """
    Appends one row [description, amount] to CSV.
    """
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def load_rows_from_csv(filename: str) -> list[list[str]]:
    """
    Loads rows from CSV.
    Each row is [description, amount].
    """
    if not os.path.exists(filename):
        return []

    rows: list[list[str]] = []

    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                rows.append(row)

    return rows
