# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_grid_properties.ui'
#
# Created: Sun May 13 14:52:01 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GridProperties(object):
    def setupUi(self, GridProperties):
        GridProperties.setObjectName(_fromUtf8("GridProperties"))
        GridProperties.resize(418, 284)
        GridProperties.setWindowTitle(QtGui.QApplication.translate("GridProperties", "Grid Overlay Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(GridProperties)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtGui.QFormLayout.LabelRole, spacerItem)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(GridProperties)
        self.label_6.setText(QtGui.QApplication.translate("GridProperties", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(GridProperties)
        self.label_7.setText(QtGui.QApplication.translate("GridProperties", "y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label = QtGui.QLabel(GridProperties)
        self.label.setText(QtGui.QApplication.translate("GridProperties", "Origin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.editOriginX = QtGui.QLineEdit(GridProperties)
        self.editOriginX.setText(QtGui.QApplication.translate("GridProperties", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.editOriginX.setObjectName(_fromUtf8("editOriginX"))
        self.horizontalLayout.addWidget(self.editOriginX)
        self.editOriginY = QtGui.QLineEdit(GridProperties)
        self.editOriginY.setText(QtGui.QApplication.translate("GridProperties", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.editOriginY.setObjectName(_fromUtf8("editOriginY"))
        self.horizontalLayout.addWidget(self.editOriginY)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_2 = QtGui.QLabel(GridProperties)
        self.label_2.setText(QtGui.QApplication.translate("GridProperties", "Cell count", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.spinCountX = QtGui.QSpinBox(GridProperties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinCountX.sizePolicy().hasHeightForWidth())
        self.spinCountX.setSizePolicy(sizePolicy)
        self.spinCountX.setMinimum(1)
        self.spinCountX.setMaximum(9999)
        self.spinCountX.setObjectName(_fromUtf8("spinCountX"))
        self.horizontalLayout_2.addWidget(self.spinCountX)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.spinCountY = QtGui.QSpinBox(GridProperties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinCountY.sizePolicy().hasHeightForWidth())
        self.spinCountY.setSizePolicy(sizePolicy)
        self.spinCountY.setMinimum(1)
        self.spinCountY.setMaximum(9999)
        self.spinCountY.setObjectName(_fromUtf8("spinCountY"))
        self.horizontalLayout_2.addWidget(self.spinCountY)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(GridProperties)
        self.label_3.setText(QtGui.QApplication.translate("GridProperties", "Grid offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.spinOffsetX = QtGui.QSpinBox(GridProperties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinOffsetX.sizePolicy().hasHeightForWidth())
        self.spinOffsetX.setSizePolicy(sizePolicy)
        self.spinOffsetX.setMinimum(-9999)
        self.spinOffsetX.setMaximum(9999)
        self.spinOffsetX.setObjectName(_fromUtf8("spinOffsetX"))
        self.horizontalLayout_3.addWidget(self.spinOffsetX)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.spinOffsetY = QtGui.QSpinBox(GridProperties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinOffsetY.sizePolicy().hasHeightForWidth())
        self.spinOffsetY.setSizePolicy(sizePolicy)
        self.spinOffsetY.setMinimum(-9999)
        self.spinOffsetY.setMaximum(9999)
        self.spinOffsetY.setObjectName(_fromUtf8("spinOffsetY"))
        self.horizontalLayout_3.addWidget(self.spinOffsetY)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_4 = QtGui.QLabel(GridProperties)
        self.label_4.setText(QtGui.QApplication.translate("GridProperties", "Cell size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.spinCellSizeX = QtGui.QDoubleSpinBox(GridProperties)
        self.spinCellSizeX.setDecimals(6)
        self.spinCellSizeX.setMaximum(100000.0)
        self.spinCellSizeX.setProperty("value", 10.0)
        self.spinCellSizeX.setObjectName(_fromUtf8("spinCellSizeX"))
        self.horizontalLayout_4.addWidget(self.spinCellSizeX)
        self.spinCellSizeY = QtGui.QDoubleSpinBox(GridProperties)
        self.spinCellSizeY.setDecimals(6)
        self.spinCellSizeY.setMaximum(100000.0)
        self.spinCellSizeY.setProperty("value", 10.0)
        self.spinCellSizeY.setObjectName(_fromUtf8("spinCellSizeY"))
        self.horizontalLayout_4.addWidget(self.spinCellSizeY)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_5 = QtGui.QLabel(GridProperties)
        self.label_5.setText(QtGui.QApplication.translate("GridProperties", "Baseline angle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.spinAngle = QtGui.QDoubleSpinBox(GridProperties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinAngle.sizePolicy().hasHeightForWidth())
        self.spinAngle.setSizePolicy(sizePolicy)
        self.spinAngle.setMaximum(359.99)
        self.spinAngle.setObjectName(_fromUtf8("spinAngle"))
        self.horizontalLayout_6.addWidget(self.spinAngle)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.btnStyle = QtGui.QPushButton(GridProperties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStyle.sizePolicy().hasHeightForWidth())
        self.btnStyle.setSizePolicy(sizePolicy)
        self.btnStyle.setText(QtGui.QApplication.translate("GridProperties", "Set Style...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStyle.setObjectName(_fromUtf8("btnStyle"))
        self.horizontalLayout_7.addWidget(self.btnStyle)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem7 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.buttonBox = QtGui.QDialogButtonBox(GridProperties)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(GridProperties)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GridProperties.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GridProperties.reject)
        QtCore.QMetaObject.connectSlotsByName(GridProperties)
        GridProperties.setTabOrder(self.editOriginX, self.editOriginY)
        GridProperties.setTabOrder(self.editOriginY, self.spinCountX)
        GridProperties.setTabOrder(self.spinCountX, self.spinCountY)
        GridProperties.setTabOrder(self.spinCountY, self.spinOffsetX)
        GridProperties.setTabOrder(self.spinOffsetX, self.spinOffsetY)
        GridProperties.setTabOrder(self.spinOffsetY, self.spinCellSizeX)
        GridProperties.setTabOrder(self.spinCellSizeX, self.spinCellSizeY)
        GridProperties.setTabOrder(self.spinCellSizeY, self.spinAngle)
        GridProperties.setTabOrder(self.spinAngle, self.btnStyle)
        GridProperties.setTabOrder(self.btnStyle, self.buttonBox)

    def retranslateUi(self, GridProperties):
        pass
