# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RenameFieldDialog
                                 A QGIS plugin
 This plugin lets users change a field's name and type in a vector layer
                             -------------------
        begin                : 2025-06-22
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Anustup Jana
        email                : anustupjana21@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


import os
from qgis.PyQt import uic, QtWidgets

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), 'rename_field_and_type_dialog_base.ui')
)

class RenameFieldAndTypeDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(RenameFieldAndTypeDialog, self).__init__(parent)
        self.setupUi(self)