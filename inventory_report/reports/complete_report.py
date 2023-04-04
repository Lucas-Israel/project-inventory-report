if __name__ == "__main__":
    from simple_report import SimpleReport
else:
    from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        oldest_product = CompleteReport._get_oldest_product(list)
        nearest_expiration = CompleteReport._get_nearest_expiration_date(list)
        most_products = CompleteReport._get_company_with_more_products(list)
        first_message = CompleteReport._generate_message(
            oldest_product, nearest_expiration, most_products
        )
        company_inventory_dict = CompleteReport._get_company_max_inventory(
            list
        )
        second_message = CompleteReport._generate_stock_message(
            company_inventory_dict
        )
        return CompleteReport._generate_complete_message(
            first_message, second_message
        )

    @staticmethod
    def _get_company_max_inventory(list):
        new_dict = {}
        for product in list:
            if product.get("nome_da_empresa") in new_dict:
                new_dict[product.get("nome_da_empresa")] += 1
            else:
                new_dict[product.get("nome_da_empresa")] = 1
        return new_dict

    @staticmethod
    def _generate_stock_message(dict):
        message = "Produtos estocados por empresa:\n"

        for element in dict:
            message += f"- {element}: {dict[element]}\n"

        return message

    @staticmethod
    def _generate_complete_message(message1, message2):
        return f"{message1}\n{message2}"
