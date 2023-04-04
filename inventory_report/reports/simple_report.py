from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(list):
        oldest_product = SimpleReport._get_oldest_product(list)
        nearest_expiration = SimpleReport._get_nearest_expiration_date(list)
        most_products = SimpleReport._get_company_with_more_products(list)
        return SimpleReport._generate_message(
            oldest_product, nearest_expiration, most_products
        )

    @staticmethod
    def _get_oldest_product(list):
        oldest = ""
        today = datetime.today().strftime("%Y%m%d")
        diff_check = 0
        for product in list:
            product_date = product.get("data_de_fabricacao").replace("-", "")
            difference = int(today) - int(product_date)
            if diff_check < difference:
                diff_check = difference
                oldest = product.get("data_de_fabricacao")
        return oldest

    @staticmethod
    def _get_nearest_expiration_date(list):
        newest = ""
        today = datetime.today().strftime("%Y%m%d")
        # diff_check needs to be one big number that is used for initial
        # comparison
        diff_check = 99999999999999
        for product in list:
            product_date = product.get("data_de_validade").replace("-", "")
            difference = abs(int(today) - int(product_date))
            if diff_check > difference:
                diff_check = difference
                newest = product.get("data_de_validade")
        return newest

    @staticmethod
    def _get_company_with_more_products(list):
        new_list = []

        for product in list:
            new_list.append(product.get("nome_da_empresa"))

        return max(set(new_list), key=new_list.count)

    @staticmethod
    def _generate_message(old_prod, nearest_expiration, most_prod):
        return (
            f"Data de fabricação mais antiga: {old_prod}\n"
            f"Data de validade mais próxima: {nearest_expiration}\n"
            f"Empresa com mais produtos: {most_prod}"
        )


if __name__ == "__main__":
    to_send = [
        {
            "id": 1,
            "nome_do_produto": "XABLAU",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-05",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 1,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-03",
            "data_de_validade": "2023-03-03",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 1,
            "nome_do_produto": "XABLAU",
            "nome_da_empresa": "zzz",
            "data_de_fabricacao": "2008-04-05",
            "data_de_validade": "2023-04-05",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 1,
            "nome_do_produto": "XABLAU",
            "nome_da_empresa": "aaa",
            "data_de_fabricacao": "2008-04-05",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 1,
            "nome_do_produto": "XABLAU",
            "nome_da_empresa": "aaa",
            "data_de_fabricacao": "2008-04-05",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 1,
            "nome_do_produto": "XABLAU",
            "nome_da_empresa": "aaa",
            "data_de_fabricacao": "2008-04-05",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
    ]

    a = SimpleReport.generate(to_send)
    print(a)
