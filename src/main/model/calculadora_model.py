from sympy import sympify, Float, N, SympifyError
from sympy.core.numbers import int_valued


class CalculadoraModel(object):
    def solve(self, expression: str) -> str:
        try:
            expr = sympify(expression)
            result: Float = N(expr, 4)
            if self.is_this_an_integer(result):
                return f"{result:.0f}"
            else:
                return f"{result:.4f}"
        except SympifyError:
            return "Error: expresión inválida"
        except Exception as e:
            return f"Error inesperado: {e}"

    def is_this_an_integer(self, number) -> bool:
        return int_valued(number)
