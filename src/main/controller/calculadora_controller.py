from itertools import count

from PySide6 import QtWidgets, QtGui
from ui import CalculadoraView
from model.calculadora_model import CalculadoraModel
from viewmodel.calculadora_viewmodel import CalculadoraViewmodel


class CalculadoraController(object):
    __viewmodel: CalculadoraViewmodel
    __view: CalculadoraView

    def __init__(
        self,
        viewmodel: CalculadoraViewmodel,
        view: CalculadoraView,
    ) -> None:
        self.__viewmodel = viewmodel
        self.__view = view
        self.connect()

    def connect(self):
        view = self.__view
        viewmodel = self.__viewmodel

        for i in range(10):
            current_button: QtWidgets.QPushButton = getattr(view, f"button_{i}")
            current_button.clicked.connect(lambda _, x=str(i): viewmodel.push_button(x))

        view.button_divide.clicked.connect(lambda _: viewmodel.push_button("/"))
        view.button_sub.clicked.connect(lambda _: viewmodel.push_button("-"))
        view.button_add.clicked.connect(lambda _: viewmodel.push_button("+"))
        view.button_times.clicked.connect(lambda _: viewmodel.push_button("*"))
        view.button_dot.clicked.connect(lambda _: viewmodel.push_button("."))
        view.button_equal.clicked.connect(lambda _: viewmodel.press_equal())
        view.button_delete.clicked.connect(lambda _: viewmodel.remove_last_character())
        view.button_clear.clicked.connect(lambda _: viewmodel.clean_screen())
        view.button_history.clicked.connect(lambda _: viewmodel.show_history())

        viewmodel.screen_updated.connect(lambda x: view.result_lcd.setText(x))
        viewmodel.history_signal.connect(lambda ops: self.show_dialog(ops))

    def show_dialog(self, ops: list[str]) -> None:
        dlg = QtWidgets.QDialog(self.__view)
        dlg.setWindowTitle("History!")

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        content_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        for indx, op in zip(count(), ops):
            label = QtWidgets.QLabel(f"{indx + 1}.- {op}")
            font = QtGui.QFont()
            font.setPointSize(20)
            label.setFont(font)
            layout.addWidget(label)
            layout.addWidget(QtWidgets.QSplitter())

        content_widget.setLayout(layout)
        scroll_area.setWidget(content_widget)

        dlg_layout = QtWidgets.QVBoxLayout()
        dlg_layout.addWidget(scroll_area)
        dlg.setLayout(dlg_layout)
        dlg.exec()

    def show(self):
        self.__view.show()
