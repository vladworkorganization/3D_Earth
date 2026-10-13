"""Простое тестовое приложение PyQt5."""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тестовое приложение PyQt5")
        self.resize(420, 220)
        self.click_count = 0

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите ваше имя")
        self.greeting = QLabel("Добро пожаловать!")
        self.greeting.setTextFormat(Qt.PlainText)
        self.counter = QLabel("Нажатий: 0")
        self.greet_button = QPushButton("Поздороваться")
        self.greet_button.clicked.connect(self.say_hello)
        self.name_input.returnPressed.connect(self.say_hello)

        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.addWidget(self.name_input)
        layout.addWidget(self.greet_button)
        layout.addWidget(self.greeting)
        layout.addWidget(self.counter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def say_hello(self):
        name = self.name_input.text().strip() or "мир"
        self.greeting.setText(f"Привет, {name}!")
        self.click_count += 1
        self.counter.setText(f"Нажатий: {self.click_count}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
