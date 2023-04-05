from inventory_report.inventory.product import Product

expected = (
    "O produto abc fabricado em 2000-01-01 por def com validade até "
    "2001-01-01 precisa ser armazenado na luz."
)


def test_relatorio_produto():
    a = Product(
        id=1,
        nome_do_produto="abc",
        nome_da_empresa="def",
        data_de_fabricacao="2000-01-01",
        data_de_validade="2001-01-01",
        numero_de_serie=123456789,
        instrucoes_de_armazenamento="na luz",
    )
    assert repr(a) == expected
