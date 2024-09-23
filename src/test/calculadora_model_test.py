from sympy import Float
from pytest import mark
from model.calculadora_model import CalculadoraModel

calculadora_model = CalculadoraModel()


def test_transform_float_to_integer_only_if_is_necessary():
    # Número flotante en sympy
    num = Float(10.000000)
    # Verificamos si tiene parte decimal
    if calculadora_model.is_this_an_integer(num):
        assert int(num) == 10  # Convertimos a entero
    else:
        assert False


def test_solve_method():
    result = calculadora_model.solve("5 + 5")
    assert "10" == result


@mark.parametrize(
    "test_input,expected",
    [("5+5", "10"), ("2+4", "6"), ("5*5", "25"), ("75*2/9", "16.6700")],
)
def test_solve_with_diff_entries(test_input, expected):
    result = calculadora_model.solve(test_input)
    assert expected == result
