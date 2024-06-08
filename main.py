import sys
from PyQt6.QtWidgets import QWidget, QApplication, QInputDialog, QPushButton
from ui_main import Ui_Form


class Widg(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setMouseTracking(True)

    def mouseDoubleClickEvent(self, event):
        m_pos = event.position()
        key_name, ok = QInputDialog.getText(self, "Новая кнопка", "Какую кнопку добавить?")
        if ok:
            button = QPushButton(self)
            button.setText(key_name)
            button.move(int(m_pos.x()), int(m_pos.y()))
            button.show()
            button.clicked.connect(self.buttons)

    def buttons(self):
        self.lineEdit.setText(f"{self.lineEdit.text()}{self.sender().text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widg()
    ex.show()
    sys.exit(app.exec())
