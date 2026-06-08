# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RenameFieldAndType
                                 A QGIS plugin
 This plugin lets users rename a field in a vector layer's attribute table,
 create a new field with a specified type, transfer values, and delete the old field
                              -------------------
        begin                : 2025-06-22
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Anustup Jana
        email                : anustupjana21@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QVariant
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsMapLayerProxyModel, QgsFieldProxyModel, QgsField

from . import resources  # ensure resources loaded
from .rename_field_and_type_dialog import RenameFieldAndTypeDialog

import os


class RenameFieldAndType:

    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)

        self.actions = []
        self.menu = self.tr(u'&Rename Field and Type')
        self.first_start = True

    def tr(self, message):
        return QCoreApplication.translate('RenameFieldAndType', message)

    def get_icon(self):
        import os
        icon_path = os.path.join(self.plugin_dir, "icon.png")
        icon = QIcon(icon_path)
        print("ICON PATH:", icon_path, "NULL:", icon.isNull())
        return icon

    def add_action(self, text, callback, parent=None):
        icon = self.get_icon()

        action = QAction(icon, text, parent)
        action.triggered.connect(callback)

        self.iface.addToolBarIcon(action)
        self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)
        return action

    def initGui(self):
        self.add_action(
            text=self.tr(u'Rename Field and Type'),
            callback=self.run,
            parent=self.iface.mainWindow()
        )

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(self.menu, action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        if self.first_start:
            self.first_start = False
            self.dlg = RenameFieldAndTypeDialog()

            self.dlg.btnClose.clicked.connect(self.dlg.close)
            self.dlg.btnRename.clicked.connect(self.rename_field)
            self.dlg.cbxLayers.layerChanged.connect(self.load_fields)

            self.populate_field_types()

        self.dlg.cbxLayers.setFilters(QgsMapLayerProxyModel.VectorLayer)
        self.dlg.cbxFields.setFilters(QgsFieldProxyModel.AllTypes)

        self.load_fields()

        self.dlg.show()
        self.dlg.exec_()

    def populate_field_types(self):
        field_types = [
            ("Text (String)", QVariant.String),
            ("Integer", QVariant.Int),
            ("Double", QVariant.Double),
            ("Date", QVariant.Date),
            ("Time", QVariant.Time),
            ("DateTime", QVariant.DateTime),
            ("Boolean", QVariant.Bool),
            ("Long Integer", QVariant.LongLong),
            ("Binary", QVariant.ByteArray)
        ]

        self.dlg.cbxFieldType.clear()
        for name, val in field_types:
            self.dlg.cbxFieldType.addItem(name, val)

    def load_fields(self):
        layer = self.dlg.cbxLayers.currentLayer()
        self.dlg.cbxFields.setLayer(layer)

    def rename_field(self):
        layer = self.dlg.cbxLayers.currentLayer()

        if not layer:
            QMessageBox.warning(None, "Error", "Select a layer")
            return

        old_field = self.dlg.cbxFields.currentField()
        new_name = self.dlg.txtName.text()
        field_type = self.dlg.cbxFieldType.currentData()

        if not old_field or not new_name:
            QMessageBox.warning(None, "Error", "Fill all fields")
            return

        if new_name in [f.name() for f in layer.fields()]:
            QMessageBox.warning(None, "Error", "Field already exists")
            return

        if not layer.isEditable():
            if not layer.startEditing():
                QMessageBox.critical(None, "Error", "Layer not editable")
                return

        old_idx = layer.fields().indexOf(old_field)

        new_field = QgsField(new_name, field_type)
        layer.addAttribute(new_field)
        new_idx = layer.fields().indexOf(new_name)

        for f in layer.getFeatures():
            val = f[old_field]
            layer.changeAttributeValue(f.id(), new_idx, val)

        layer.deleteAttribute(old_idx)

        if not layer.commitChanges():
            QMessageBox.critical(None, "Error", "Commit failed")
        else:
            QMessageBox.information(None, "Success", "Field renamed successfully")

        self.load_fields()
        self.dlg.txtName.clear()