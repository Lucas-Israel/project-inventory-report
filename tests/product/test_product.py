from inventory_report.inventory.product import Product

id = 1
nome_do_produto = "abc"
nome_da_empresa = "abc Maker"
data_de_fabricacao = "07-09-1992"
data_de_validade = "07-09-2052"
numero_de_serie = 123456789
instrucoes_de_armazenamento = "deixar livre"

expected = (
    f"O produto {nome_do_produto}"
    f" fabricado em {data_de_fabricacao}"
    f" por {nome_da_empresa} com validade"
    f" até {data_de_validade}"
    f" precisa ser armazenado {instrucoes_de_armazenamento}."
)


def test_cria_produto():
    to_check = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert repr(to_check) == expected
