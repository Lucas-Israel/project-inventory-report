from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self._importer = importer
        self._data = []

    @property
    def importer(self):
        return self._importer

    @property
    def data(self):
        return self._data

    @importer.setter
    def importer(self, new_importer):
        self._importer = new_importer

    @data.setter
    def data(self, new_data):
        self._data = new_data

    def import_data(self, path: str, report_type="simples"):
        getting_info = self._importer.import_data(path)
        for info in getting_info:
            self._data.append(info)
        reporter_type = self._report_type_selector(report_type)
        return reporter_type.generate(self._data)

    @staticmethod
    def _report_type_selector(report_type):
        reporter = ""
        if report_type == "simples":
            reporter = SimpleReport
        else:
            reporter = CompleteReport
        return reporter

    def __iter__(self):
        return InventoryIterator(self._data)
