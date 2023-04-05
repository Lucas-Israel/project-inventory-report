from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter


class color:
    END = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[36m"


g = color.GREEN
b = color.BLUE
r = color.RED
e = color.END

report_expected = (
    f"{g}Data de fabricação mais antiga:{e} {b}2020-09-06{e}\n"
    f"{g}Data de validade mais próxima:{e} {b}2023-09-17{e}\n"
    f"{g}Empresa com mais produtos:{e} {r}Target Corporation{e}"
)

complete_report_expected = (
    f"{report_expected}\n"
    "Produtos estocados por empresa:\n"
    "- Target Corporation: 4\n"
    "- Galena Biopharma: 2\n"
    "- Cantrell Drug Company: 2\n"
    "- Moore Medical LLC: 1\n"
    "- REMEDYREPACK: 1\n"
)


def test_decorar_relatorio():
    json_list = JsonImporter.import_data(
        "inventory_report/data/inventory.json"
    )
    csv_list = CsvImporter.import_data("inventory_report/data/inventory.csv")
    xml_list = XmlImporter.import_data("inventory_report/data/inventory.xml")

    simple_colored_reporter = ColoredReport(SimpleReport)
    complete_colored_reporter = ColoredReport(CompleteReport)

    json_report = simple_colored_reporter.generate(json_list)
    csv_report = simple_colored_reporter.generate(csv_list)
    xml_report = simple_colored_reporter.generate(xml_list)

    complete_json_report = complete_colored_reporter.generate(json_list)
    complete_csv_report = complete_colored_reporter.generate(csv_list)
    complete_xml_report = complete_colored_reporter.generate(xml_list)

    assert json_report == report_expected
    assert csv_report == report_expected
    assert xml_report == report_expected

    assert complete_json_report == complete_report_expected
    assert complete_csv_report == complete_report_expected
    assert complete_xml_report == complete_report_expected
