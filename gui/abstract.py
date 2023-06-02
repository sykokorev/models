from __future__ import annotations

import os
import sys

from typing import Any
from abc import abstractmethod

DIR_IMP = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir
))
sys.path.append(DIR_IMP)

from PySide6.QtWidgets import (
    QWidget, QListView, QTreeWidget,
    QTreeWidgetItem
)
from PySide6.QtCore import (
    Qt, QAbstractListModel, QModelIndex,
    QPersistentModelIndex, QObject
)


from data.abstract import AbstractDataCache, AbstractDataModel


class AbstractListModel(QAbstractListModel):

    def __init__(self, parent: QObject | None = ...) -> None:
        super(AbstractListModel, self).__init__(parent)
        self._data: AbstractDataCache = None

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> Any:
        
        if not index.isValid() : return None
        if not 0 <= index.row() <= len(self._data.data) : return None

        if role == Qt.ItemDataRole.DisplayRole:
            return self._data.get(index.row()).view()
        
        if role == Qt.ItemDataRole.ToolTipRole:
            if hasattr(self._data.get(index.row()), 'tooltip'):
                return self._data.get(index.row()).tooltip
            else:
                return None
        
    def add(self, data: dict) -> bool:

        if not isinstance(data, AbstractDataModel): return False
        return self._data.add(data)
    
    def update(self, data: AbstractDataModel, index: QModelIndex | QPersistentModelIndex) -> bool:

        if not index.isValid() : return False
        if not 0 <= index.row() <= len(self._data.data) : return False
        return self._data.update(index.row(), data)

    def delete(self, index: QModelIndex | QPersistentModelIndex) -> bool:

        if not index.isValid() : return False
        if not 0 <= index.row() <= len(self._data.data) : return False
        return self._data.delete(index.row())

    def get(self, index: QModelIndex | QPersistentModelIndex) -> bool:

        if not index.isValid() : return False
        if not 0 <= index.row() <= len(self._data.data) : return False
        return self._data.get(index.row())

    def moveUp(self, index: QModelIndex | QPersistentModelIndex) -> None:

        if not index.isValid() : return None
        if not 0 <= index.row() <= len(self._data.data) : return None
        return self._data.moveUp(index.row())

    def moveDown(self, index: QModelIndex | QPersistentModelIndex) -> None:

        if not index.isValid() : return None
        if not 0 <= index.row() <= len(self._data.data) : return None
        return self._data.moveDown(index.row())
    
    def insert(self, data: AbstractDataModel, index: QModelIndex | QPersistentModelIndex) -> bool:

        if not index.isValid() : return False
        if not 0 <= index.row() <= len(self._data.data) : return False
        return self._data.insert(data, index.row())
    
    def rowCount(self, index) -> int:
        return len(self._data)


class AbstrctListView(QListView):

    def __init__(self, parent: QWidget | None = ...) -> None:
        super(AbstrctListView, self).__init__(parent)
        self._model: AbstractListModel

    def setModel(self, model: AbstractListModel) -> None:
        if isinstance(model, AbstractListModel): self._model = model

    def add(self, data: AbstractDataModel):
        try:
            self._model.add(data)
        except:
            return False
    
    def delete(self, index: QModelIndex | QPersistentModelIndex) -> bool:
        try:
            self._model.delete(index)
            return True
        except:
            return False

    def moveUp(self, index: QModelIndex | QPersistentModelIndex) -> bool:
        try:
            self._model.moveUp(index)
            return True
        except:
            return False

    def moveDown(self, index: QModelIndex | QPersistentModelIndex) -> bool:
        try:
            self._model.moveDown(index)
            return True
        except:
            return False

    @abstractmethod
    def update(self) -> bool:
        pass
