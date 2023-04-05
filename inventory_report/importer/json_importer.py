if __name__ == "__main__":
    from importer import Importer
else:
    from inventory_report.importer.importer import Importer
import re


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_name):
        JsonImporter.__extention_check(file_name)
        return file_name

    @staticmethod
    def __extention_check(file_name):
        extention = re.sub(r"\w*.*\.", "", file_name)
        if extention != "json":
            raise ValueError(
                f"file must be .json, received a .{extention} file instead"
            )


if __name__ == "__main__":
    a = JsonImporter.import_data("abc.jsons")
    # print(a)
