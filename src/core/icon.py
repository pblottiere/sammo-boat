# coding: utf8

__contact__ = "info@hytech-imaging.fr"
__copyright__ = "Copyright (c) 2021 Hytech Imaging"

import os

from qgis.PyQt.QtCore import QSize
from qgis.PyQt.QtGui import QIcon, QPixmap


def icon(name: str) -> QIcon:
    d = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(d))
    return QIcon(os.path.join(root, "images", name))


def pixmap(name: str, size: QSize) -> QPixmap:
    d = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(d))
    return QIcon(os.path.join(root, "images", name)).pixmap(size)
