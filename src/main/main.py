import sys
from PySide6 import QtWidgets

from controller.calculadora_controller import CalculadoraController
from ui import CalculadoraView
from model.calculadora_model import CalculadoraModel
from viewmodel.calculadora_viewmodel import CalculadoraViewmodel


def load_stylesheet(app: QtWidgets.QApplication, css_file):
    with open(css_file, "r") as f:
        app.setStyleSheet(f.read())


def launch_calc():
    app = QtWidgets.QApplication(sys.argv)
    try:
        load_stylesheet(app, "./assets/styles.qss")
    except Exception:
        print(
            """
            The application does not load the style, 
            please try to put the style.qss 
            inside of the assets folder to load them
            """
        )
    controller = CalculadoraController(
        CalculadoraViewmodel(CalculadoraModel()), CalculadoraView()
    )
    controller.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    try:
        launch_calc()
    except Exception as e:
        print(e)
