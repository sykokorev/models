from __future__ import annotations

import os
import sys

from typing import Optional

from PySide6.QtGui import Qt
from PySide6.QtCore import QSize


from PySide6.QtWidgets import (
    QWidget, QTreeWidget, QTreeWidgetItem,
    QDialog, QDialogButtonBox, QHBoxLayout,
    QGridLayout, QVBoxLayout
)


DIR_IMP = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir
))
sys.path.append(DIR_IMP)

from gui.abstract import *


class TreeView(QTreeWidget):

    def __init__(self, parent: Optional[QWidget] = None, **settings) -> None:
        super(TreeView, self).__init__(parent)
        self._model: dict = None
        self.items = []
        self.setHeaderHidden(settings.get('header_hidden', True))
        self.setHeaderLabels(settings.get('headers', ''))

    def setData(self, data: dict) -> bool:
        if not isinstance(data, dict): return False
        
        self._model = data
        self.clear()
        self.items.clear()

        for key, values in self._model.items():
            item = QTreeWidgetItem([key])
            item.setSelected(False)
            for val in values:
                child = QTreeWidgetItem([val])
                item.addChild(child)
            self.items.append(item)
        
        self.insertTopLevelItems(0, self.items)


class TreeDialog(QDialog):

    def __init__(self, parent: Optional[QWidget] = None, f: Qt.WindowType = Qt.WindowType.Dialog, **settings) -> None:
        super(TreeDialog, self).__init__(parent, f)

        self.data = None
        self.tree = TreeView(headers=['Domains'], header_hidden=False)
        self.tree.itemDoubleClicked.connect(self.accept)

        self.setWindowTitle(settings.get('title', 'Tree View'))
        self.resize(QSize(*settings.get('size', [320, 320])))

        btn_layout = QHBoxLayout()
        btn = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        btn.accepted.connect(self.accept)
        btn.rejected.connect(self.reject)
        btn_layout.addWidget(btn)

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def setData(self, data: dict) -> bool:
        if not self.tree.setData(data): return False
        return True
    
    def accept(self) -> None:
        idx = self.tree.currentColumn()
        item = self.tree.currentItem()
        self.data = item.text(idx)
        return super().accept()
    
    def reject(self):
        self.data = None
        return super().reject()


class ListView(AbstrctListView):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ListView, self).__init__(parent)
