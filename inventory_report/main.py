from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys
import re


def sys_args_len_check():
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
        return True
    return False


def get_importer(file_path):
    extention = re.sub(r"\w*.*\.", "", file_path)
    importer = None
    if extention == "json":
        importer = JsonImporter
    if extention == "csv":
        importer = CsvImporter
    if extention == "xml":
        importer = XmlImporter
    return importer


def main():
    if sys_args_len_check():
        return

    path = sys.argv[1]
    report_type = sys.argv[2]
    importer = get_importer(path)

    data = InventoryRefactor(importer).import_data(path, report_type)

    sys.stdout.write(data)
