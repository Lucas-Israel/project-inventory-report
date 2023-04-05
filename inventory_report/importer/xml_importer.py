if __name__ == "__main__":
    from importer import Importer
else:
    from inventory_report.importer.importer import Importer

import xml.etree.ElementTree as ET
import re


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        XmlImporter.__extention_check(file_path)
        new_list = []
        with open(file_path, "r") as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for element in root.findall("record"):
                new_obj = {
                    "id": element.find("id").text,
                    "nome_do_produto": element.find("nome_do_produto").text,
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

    @staticmethod
    def __extention_check(file_path):
        extention = re.sub(r"\w*.*\.", "", file_path)
        if extention != "xml":
            raise ValueError("Arquivo inválido")
