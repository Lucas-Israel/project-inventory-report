from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv
import json
import xml.etree.ElementTree as ET

import re


class Inventory:
    @staticmethod
    def import_data(path: str, report_type="simples"):
        reporter = Inventory._reporter_selector(report_type)
        reader_result = Inventory._reader_selector(path)

        return reporter.generate(reader_result)

    @staticmethod
    def _reporter_selector(report_type):
        reporter = ""
        if report_type == "simples":
            reporter = SimpleReport
        else:
            reporter = CompleteReport
        return reporter

    @staticmethod
    def _reader_selector(path: str):
        file_type = re.sub(r"\w*.*\.", "", path)
        file_reader = ""
        if file_type == "csv":
            file_reader = Inventory._csv_to_json_reader(path)
        if file_type == "json":
            file_reader = Inventory._json_reader(path)
        if file_type == "xml":
            file_reader = Inventory._xml_reader(path)

        return file_reader

    @staticmethod
    def _csv_to_json_reader(path):
        new_list = []
        with open(path, encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                new_list.append(row)
        return new_list

    @staticmethod
    def _json_reader(path):
        new_list = []
        with open(path, "r") as json_file:
            json_reader = json.load(json_file)
            new_list = json_reader

        return new_list

    @staticmethod
    def _xml_reader(path):
        new_list = []
        with open(path, "r") as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for element in root.findall("record"):
                new_obj = {
                    "id": element.find("id").text,
                    "product_name": element.find("nome_do_produto").text,
                    "nome_da_empresa": element.find("nome_da_empresa").text,
                    "data_de_fabricacao": element.find(
                        "data_de_fabricacao"
                    ).text,
                    "data_de_validade": element.find("data_de_validade").text,
                    "numero_de_serie": element.find("numero_de_serie").text,
                    "instrucoes_de_armazenamento": element.find(
                        "instrucoes_de_armazenamento"
                    ).text,
                }
                new_list.append(new_obj)
        return new_list
