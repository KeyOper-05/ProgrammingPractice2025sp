# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QIcon, QPixmap
import os

from ui_selectAvatar import Ui_Avatar
class AvatarDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.avatarSelected = ""
        self.ui = Ui_Avatar()
        self.ui.setupUi(self)
        self.base_dir = os.path.dirname(__file__)
        for i in range(1,7):
            filePos = os.path.join(self.base_dir, "avatars", f"avatar{i}.png")
            pixmap = QPixmap(filePos)
            avButton = getattr(self.ui, f"av{i}")
            avButton.setIcon(QIcon(pixmap))
            avButton.setIconSize(avButton.size())
            avButton.setStyleSheet("""
            QPushButton {
                border: none;
            }
            QPushButton:pressed {
                background-color: rgba(0, 0, 0, 30);
            }
            """)
            avButton.clicked.connect(lambda _, num=i: self.sendSignal(num))
        self.ui.upload.clicked.connect(self.selectOnMyOwn)
    def sendSignal(self, num):
        filePos = os.path.join(self.base_dir, "avatars", f"avatar{num}.png")
        self.avatarSelected = filePos
        self.accept()
    def selectOnMyOwn(self):
        filePos, _ = QFileDialog.getOpenFileName(self, "选择头像文件", "", "图片文件 (*.png *.jpg *.bmp)")
        if filePos:
            self.avatarSelected = filePos
            self.accept()
