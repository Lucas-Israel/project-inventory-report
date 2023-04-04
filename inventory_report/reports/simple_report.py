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
