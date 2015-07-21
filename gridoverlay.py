"""
/***************************************************************************
 Grid Overlay
                                 A QGIS plugin
 Overlays a user-definable grid on the map.
                             -------------------
        begin                : 2012-05-11
        copyright            : (C) 2012 by John Donovan
        email                : mersey.viking@gmail.com
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

from PyQt4 import QtCore
from PyQt4 import QtGui
from qgis import core

# Initialize Qt resources from file resources.py
import resources_rc

from gridpropertiesdialog import GridPropertiesDialog
from gridpluginlayertype import GridPluginLayerType
from gridpluginlayer import GridPluginLayer
import os.path

class GridOverlay:
    '''
    The main entry-point class.
    '''

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.action_newGrid = None
        self.plugin_folder = os.path.abspath(os.path.dirname(__file__))

        # initialize locale
        locale = QtCore.QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_folder, 'i18n', 'gridoverlay_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        '''
        Sets this up as a QGIS plug-in.
        '''
        # Create action_newGrid that will start plugin configuration
        self.action_newGrid = QtGui.QAction(QtGui.QIcon(self.plugin_folder + "/icon.png"),
                        "Add Grid Overlay...", self.iface.mainWindow())

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action_newGrid)
        self.iface.insertAddLayerAction(self.action_newGrid)

        self.action_newGrid.triggered.connect(self.run)

        core.QgsPluginLayerRegistry.instance().addPluginLayerType(GridPluginLayerType())

    def unload(self):
        '''
        Removes the plug-in menu item and icon.
        '''
        self.iface.removeAddLayerAction(self.action_newGrid)
        self.iface.removeToolBarIcon(self.action_newGrid)
        core.QgsPluginLayerRegistry.instance().removePluginLayerType(GridPluginLayer.LAYER_TYPE)

    def run(self):
        layer = GridPluginLayer()
        layer.showDialog()

        if layer.isValid():
            core.QgsMapLayerRegistry.instance().addMapLayer(layer)
