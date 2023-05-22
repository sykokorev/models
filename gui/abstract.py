from __future__ import annotations

import os
import sys
from typing import Any, Union

from PySide6.QtWidgets import (
    QWidget, QAbstractItemDelegate,
    QListView
)
from PySide6.QtCore import (
    Qt, QAbstractListModel, QModelIndex,
    QPersistentModelIndex, QObject
)


class AbstractListModel(QAbstractListModel):

    def __init__(self, parent: QObject | None = ...) -> None:
        super(AbstractListModel, self).__init__(parent)
        self._data = None

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> Any:
        
        if not index.isValid() : return None
        if not 0 <= index.row() <= len(self._data.data) : return None

        if role == Qt.ItemDataRole.DisplayRole:
            return self._data.get(index.row()).view()


class AbstrctListView(QListView):

    def __init__(self, parent: QWidget | None = ...) -> None:
        super(AbstrctListView, self).__init__(parent)

