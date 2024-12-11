import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("изменение фона")

url_input = QLineEdit()
url_input.setPlaceholderText("введите адрес изображения")

color_input = QLineEdit()
color_input.setPlaceholderText("введите цвет на английском")

change_button = QPushButton("изменить")

layout = QVBoxLayout()
layout.addWidget(url_input)
layout.addWidget(color_input)
layout.addWidget(change_button)
window.setLayout(layout)


def change_background():
    url = url_input.text()
    window.setStyleSheet(f"background-image: url('{url}');")
    color = color_input.text()
    window.setStyleSheet(f"background-color: {color};")



change_button.clicked.connect(change_background)
window.show()
app.exec()