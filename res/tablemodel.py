
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QPixmap

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._images = {}

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        if self._data:
            return len(self._data[0])
        return 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            data = self._data[row][col]
            if col == 0:
                return None
            return data
        elif role == Qt.DecorationRole:
            if col == 0:
                image_data = self._data[row][col]
                if isinstance(image_data, bytes):
                    if row not in self._images:
                        pixmap = QPixmap()
                        pixmap.loadFromData(image_data)
                        if not pixmap.isNull():
                            scaled_pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                            self._images[row] = scaled_pixmap
                    return self._images.get(row)
                elif isinstance(image_data, str):
                    if row not in self._images:
                        pixmap = QPixmap(image_data)
                        if not pixmap.isNull():
                            scaled_pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                            self._images[row] = scaled_pixmap
                    return self._images.get(row)
        elif role == Qt.TextAlignmentRole:
            if col == 2:
                return Qt.AlignCenter
            return Qt.AlignVCenter | Qt.AlignLeft
