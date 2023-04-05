if __name__ == "__main__":
    from importer import Importer
else:
    from inventory_report.importer.importer import Importer

import re
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        JsonImporter.__extention_check(file_path)
        new_list = []
        with open(file_path, "r") as json_file:
            json_reader = json.load(json_file)
            new_list = json_reader

        return new_list

    @staticmethod
    def __extention_check(file_path):
        extention = re.sub(r"\w*.*\.", "", file_path)
        if extention != "json":
            raise ValueError("Arquivo inválido")


if __name__ == "__main__":
    a = JsonImporter.import_data("inventory_report/data/inventory.json")
    print(a)
