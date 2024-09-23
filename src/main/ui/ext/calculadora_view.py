from PySide6 import QtWidgets
from ui.gen.ui_calculadora_view import Ui_CalculadoraView


class CalculadoraView(QtWidgets.QMainWindow, Ui_CalculadoraView):
    def __init__(self, *args, obj=None, **kwargs):
        super(CalculadoraView, self).__init__(*args, **kwargs)
        self.setupUi(self)
