# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RenameFieldAndType
                                 A QGIS plugin
 Rename field name and change field type in a vector layer
                             -------------------
        begin                : 2025-06-22
        copyright            : (C) 2026 by Anustup Jana
        email                : anustupjana21@gmail.com
 ***************************************************************************/
"""

def classFactory(iface):
    from .rename_field_and_type import RenameFieldAndType
    return RenameFieldAndType(iface)