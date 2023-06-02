from __future__ import annotations

import os
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

DIR_IMP = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir
))
sys.path.append(DIR_IMP)

from gui.concrete import *


if __name__ == "__main__":

    app = QApplication()

    data = {
        'Domain 1': ['Interface 11', 'Interface 12', 'Interface 13'],
        'Domain 2': ['Interface 21', 'Interface 22', 'Interface 23'],
        'Domain 3': ['Interface 31', 'Interface 32', 'Interface 33']
    }
    dialog = TreeDialog()
    dialog.setData(data)
    dialog.show()
    app.exec()

    if data := dialog.data: print(data)
