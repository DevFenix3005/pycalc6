from PySide6.QtCore import QObject, Signal
from model.calculadora_model import CalculadoraModel


class CalculadoraViewmodel(QObject):
    __model: CalculadoraModel
    __screen_value: str = ""
    __history: list[str] = []
    __clear_on_next_input: bool = True

    screen_updated = Signal(str)
    history_signal = Signal(list)

    def __init__(self, model: CalculadoraModel):
        super().__init__()
        self.__model = model

    def __update_screen(self):
        self.screen_updated.emit(self.__screen_value)

    def press_equal(self) -> None:
        current_screen_value: str = self.__screen_value
        if current_screen_value:
            result = self.__model.solve(current_screen_value)
            self.__history.append(f"{current_screen_value} = {result}")
            self.__screen_value = result
            self.__update_screen()
            self.__clear_on_next_input = True

    def push_button(self, value: str):
        if self.__clear_on_next_input:
            self.__screen_value = ""
            self.__clear_on_next_input = False
        if (
            value in "+-*/"
            and self.__screen_value
            and self.__screen_value[-1] in "+-*/"
        ):
            return
        self.__screen_value += value
        self.__update_screen()

    def remove_last_character(self):
        self.__screen_value = self.__screen_value[:-1]
        self.__update_screen()

    def clean_screen(self):
        self.__screen_value = ""
        self.__update_screen()

    def show_history(self):
        self.history_signal.emit(self.__history)
