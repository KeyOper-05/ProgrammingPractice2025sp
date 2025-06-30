from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class AIInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("智能事件输入")
        self.resize(400, 150)

        self.layout = QVBoxLayout()
        self.label = QLabel("请输入一句话描述事件：")
        self.text_input = QLineEdit()
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_input)
        self.layout.addWidget(self.ok_button)
        self.layout.addWidget(self.cancel_button)
        self.setLayout(self.layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_input_text(self):
        return self.text_input.text()
