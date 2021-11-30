import csv


def get_rows_from_csv(path: str) -> list:
    with open(path, 'r', encoding="utf8") as path:
        return [row for row in csv.reader(path)][1:]
