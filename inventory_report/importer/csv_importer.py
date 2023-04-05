if __name__ == "__main__":
    from importer import Importer
else:
    from inventory_report.importer.importer import Importer

import csv
import re


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        CsvImporter.__extention_check(file_path)
        new_list = []
        with open(file_path, encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                new_list.append(row)
        return new_list

    @staticmethod
    def __extention_check(file_path):
        extention = re.sub(r"\w*.*\.", "", file_path)
        if extention != "csv":
            raise ValueError(
                f"file must be .csv, received a .{extention} file instead"
            )
