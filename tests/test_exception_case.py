from models.exception_case import ExceptionCase


def test_cria_exception_case_com_dados_informados():
    case = ExceptionCase(
        title="Nota fiscal divergente",
        description="Valor diferente do pedido",
        category="financeiro",
        priority="high",
    )

    assert case.id is None
    assert case.title == "Nota fiscal divergente"
    assert case.description == "Valor diferente do pedido"
    assert case.category == "financeiro"
    assert case.priority == "high"
    assert case.status == "open"

    assert case.created_at
    assert case.updated_at


def test_exception_case_usa_valores_padrao():
    case = ExceptionCase()

    assert case.id is None
    assert case.title == ""
    assert case.description == ""
    assert case.category == ""
    assert case.priority == "medium"
    assert case.status == "open"
