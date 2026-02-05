
from PySide6.QtCore import Qt, QAbstractTableModel, QRectF
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QStyledItemDelegate

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._images = {}

    def update_data(self, new_data):
        self.beginResetModel()
        self._data = new_data
        self._images.clear()
        self.endResetModel()

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

class RoundedImageDelegate(QStyledItemDelegate):
    def __init__(self, radius=8, parent=None):
        super().__init__(parent)
        self.radius = radius

    def paint(self, painter, option, index):
        if index.column() == 0:
            pixmap = index.data(Qt.DecorationRole)
            if pixmap is not None and not pixmap.isNull():
                painter.save()
                painter.setRenderHint(QPainter.Antialiasing)

                rect = option.rect
                pixmap_rect = pixmap.rect()

                # 居中
                # x = rect.x() + (rect.width() - pixmap_rect.width()) // 2
                # 左对齐
                x = rect.x() + 6
                y = rect.y() + (rect.height() - pixmap_rect.height()) // 2

                target_rect = QRectF(x, y, pixmap_rect.width(), pixmap_rect.height())

                path = QPainterPath()
                path.addRoundedRect(target_rect, self.radius, self.radius)
                painter.setClipPath(path)
                painter.drawPixmap(int(x), int(y), pixmap)

                painter.restore()
                return
        super().paint(painter, option, index)

def create_rounded_pixmap(pixmap, radius=8):
    if pixmap.isNull():
        return pixmap

    rounded = QPixmap(pixmap.size())
    rounded.fill(Qt.transparent)

    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.Antialiasing)

    path = QPainterPath()
    path.addRoundedRect(QRectF(pixmap.rect()), radius, radius)

    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()

    return rounded



