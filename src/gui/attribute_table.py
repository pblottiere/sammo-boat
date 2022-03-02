# coding: utf8

__contact__ = "info@hytech-imaging.fr"
__copyright__ = "Copyright (c) 2021 Hytech Imaging"

from qgis.PyQt import QtCore
from qgis.PyQt.QtWidgets import QFrame, QTableView, QAction, QToolBar


class SammoAttributeTable:
    @staticmethod
    def toolbar(table):
        return table.findChild(QToolBar, "mToolbar")

    @staticmethod
    def refresh(table):
        table.findChild(QAction, "mActionReload").trigger()
        table.findChild(QAction, "mActionApplyFilter").trigger()

        view = table.findChild(QTableView, "mTableView")
        view.resizeColumnsToContents()
        index = view.model().index(0, 1)
        view.selectionModel().setCurrentIndex(
            index,
            QtCore.QItemSelectionModel.ClearAndSelect
            | QtCore.QItemSelectionModel.Rows,
        )

    @staticmethod
    def attributeTable(
        iface,
        layer,
        filterExpr="",
        sortExpr='"dateTime"',
    ):
        # hide some columns
        hiddens = [
            "copy",
            "fid",
            "soundFile",
            "soundStart",
            "soundEnd",
            "status",
            "validated",
        ]
        config = layer.attributeTableConfig()
        columns = config.columns()
        for column in columns:
            if column.name in hiddens:
                column.hidden = True
        config.setColumns(columns)
        config.setSortExpression(sortExpr)
        config.setSortOrder(QtCore.Qt.DescendingOrder)
        layer.setAttributeTableConfig(config)

        # init attribute table
        table = iface.showAttributeTable(layer, filterExpr)

        # hide some items
        last = table.layout().rowCount() - 1
        layout = table.layout().itemAtPosition(last, 0).itemAt(0)
        for idx in range(layout.count()):
            layout.itemAt(idx).widget().hide()

        layout = table.findChild(QFrame, "mUpdateExpressionBox").layout()
        for idx in range(layout.count()):
            layout.itemAt(idx).widget().hide()

        SammoAttributeTable.toolbar(table).hide()

        # update table view
        view = table.findChild(QTableView, "mTableView")
        view.horizontalHeader().setStretchLastSection(True)
        view.model().rowsInserted.connect(
            lambda: QtCore.QTimer.singleShot(0, view.scrollToTop)
        )

        return table
