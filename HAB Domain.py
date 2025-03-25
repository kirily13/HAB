import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Global dark background
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        # Main vertical layout for the entire window
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(5, 5, 5, 5)
        self.mainLayout.setSpacing(5)
        
        # ---------------------------
        # Top: Main Title
        # ---------------------------
        self.label_mainTitle = QtWidgets.QLabel(self.centralwidget)
        self.label_mainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mainTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_mainTitle.setObjectName("label_mainTitle")
        self.mainLayout.addWidget(self.label_mainTitle, 0)
        
        # ---------------------------
        # Middle: Horizontal layout for 3 columns
        # ---------------------------
        self.middleLayout = QtWidgets.QHBoxLayout()
        self.middleLayout.setContentsMargins(5, 5, 5, 5)
        self.middleLayout.setSpacing(5)
        
        # ---- Left Column: Scientific Data ----
        self.sectionScientific = QtWidgets.QWidget(self.centralwidget)
        self.sectionScientific.setObjectName("sectionScientific")
        self.scientificLayout = QtWidgets.QVBoxLayout(self.sectionScientific)
        self.scientificLayout.setContentsMargins(5, 5, 5, 5)
        self.scientificLayout.setSpacing(5)
        
        # Scientific Title
        self.label_scientificTitle = QtWidgets.QLabel(self.sectionScientific)
        self.label_scientificTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scientificTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_scientificTitle.setObjectName("label_scientificTitle")
        self.scientificLayout.addWidget(self.label_scientificTitle, 0)
        
        # Readings widget (compact)
        self.readingsWidget = QtWidgets.QWidget(self.sectionScientific)
        self.readingsWidget.setObjectName("readingsWidget")
        self.readingsWidget.setFixedHeight(30)
        self.horizontalLayout_readings = QtWidgets.QHBoxLayout(self.readingsWidget)
        self.horizontalLayout_readings.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_readings.setSpacing(5)
        
        self.label_pressure = QtWidgets.QLabel(self.readingsWidget)
        self.label_pressure.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_pressure.setObjectName("label_pressure")
        self.horizontalLayout_readings.addWidget(self.label_pressure)
        
        self.label_pressure_value = QtWidgets.QLabel(self.readingsWidget)
        self.label_pressure_value.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_pressure_value.setObjectName("label_pressure_value")
        self.horizontalLayout_readings.addWidget(self.label_pressure_value)
        
        self.label_temperature = QtWidgets.QLabel(self.readingsWidget)
        self.label_temperature.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_temperature.setObjectName("label_temperature")
        self.horizontalLayout_readings.addWidget(self.label_temperature)
        
        self.label_temperature_value = QtWidgets.QLabel(self.readingsWidget)
        self.label_temperature_value.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_temperature_value.setObjectName("label_temperature_value")
        self.horizontalLayout_readings.addWidget(self.label_temperature_value)
        
        self.label_radiation = QtWidgets.QLabel(self.readingsWidget)
        self.label_radiation.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_radiation.setObjectName("label_radiation")
        self.horizontalLayout_readings.addWidget(self.label_radiation)
        
        self.label_radiation_value = QtWidgets.QLabel(self.readingsWidget)
        self.label_radiation_value.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_radiation_value.setObjectName("label_radiation_value")
        self.horizontalLayout_readings.addWidget(self.label_radiation_value)
        
        self.label_density = QtWidgets.QLabel(self.readingsWidget)
        self.label_density.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_density.setObjectName("label_density")
        self.horizontalLayout_readings.addWidget(self.label_density)
        
        self.label_density_value = QtWidgets.QLabel(self.readingsWidget)
        self.label_density_value.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_density_value.setObjectName("label_density_value")
        self.horizontalLayout_readings.addWidget(self.label_density_value)
        
        self.scientificLayout.addWidget(self.readingsWidget, 0)
        
        # Horizontal layout for 2 graph boxes (side by side)
        self.horizontalLayout_graphs = QtWidgets.QHBoxLayout()
        self.horizontalLayout_graphs.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_graphs.setSpacing(5)
        
        self.groupBox_graph1 = QtWidgets.QGroupBox(self.sectionScientific)
        self.groupBox_graph1.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_graph1.setObjectName("groupBox_graph1")
        self.verticalLayout_graph1 = QtWidgets.QVBoxLayout(self.groupBox_graph1)
        self.verticalLayout_graph1.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_graph1.setSpacing(2)
        self.frame_graph1 = QtWidgets.QFrame(self.groupBox_graph1)
        self.frame_graph1.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame_graph1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_graph1.setObjectName("frame_graph1")
        self.verticalLayout_graph1.addWidget(self.frame_graph1)
        self.horizontalLayout_graphs.addWidget(self.groupBox_graph1, 1)
        
        self.groupBox_graph2 = QtWidgets.QGroupBox(self.sectionScientific)
        self.groupBox_graph2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_graph2.setObjectName("groupBox_graph2")
        self.verticalLayout_graph2 = QtWidgets.QVBoxLayout(self.groupBox_graph2)
        self.verticalLayout_graph2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_graph2.setSpacing(2)
        self.frame_graph2 = QtWidgets.QFrame(self.groupBox_graph2)
        self.frame_graph2.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame_graph2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_graph2.setObjectName("frame_graph2")
        self.verticalLayout_graph2.addWidget(self.frame_graph2)
        self.horizontalLayout_graphs.addWidget(self.groupBox_graph2, 1)
        
        self.scientificLayout.addLayout(self.horizontalLayout_graphs, 1)
        self.middleLayout.addWidget(self.sectionScientific, 1)
        
        # ---- Middle Column: GPS Tracking ----
        self.sectionGPS = QtWidgets.QWidget(self.centralwidget)
        self.sectionGPS.setObjectName("sectionGPS")
        self.gpsLayout = QtWidgets.QVBoxLayout(self.sectionGPS)
        self.gpsLayout.setContentsMargins(5, 5, 5, 5)
        self.gpsLayout.setSpacing(5)
        
        self.label_gpsTitle = QtWidgets.QLabel(self.sectionGPS)
        self.label_gpsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gpsTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_gpsTitle.setObjectName("label_gpsTitle")
        self.gpsLayout.addWidget(self.label_gpsTitle, 0)
        
        # GPS Values widget placed above the map (values in two rows)
        self.gpsValuesWidget = QtWidgets.QWidget(self.sectionGPS)
        self.gpsValuesWidget.setObjectName("gpsValuesWidget")
        self.gpsValuesLayout = QtWidgets.QVBoxLayout(self.gpsValuesWidget)
        self.gpsValuesLayout.setContentsMargins(2, 2, 2, 2)
        self.gpsValuesLayout.setSpacing(2)
        
        # First row: x, y, z values (left aligned)
        self.gpsValuesRow1 = QtWidgets.QHBoxLayout()
        self.gpsValuesRow1.setContentsMargins(2, 2, 2, 2)
        self.gpsValuesRow1.setSpacing(5)
        self.label_xCoordinate = QtWidgets.QLabel(self.gpsValuesWidget)
        self.label_xCoordinate.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_xCoordinate.setObjectName("label_xCoordinate")
        self.gpsValuesRow1.addWidget(self.label_xCoordinate)
        self.label_yCoordinate = QtWidgets.QLabel(self.gpsValuesWidget)
        self.label_yCoordinate.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_yCoordinate.setObjectName("label_yCoordinate")
        self.gpsValuesRow1.addWidget(self.label_yCoordinate)
        self.label_zCoordinate = QtWidgets.QLabel(self.gpsValuesWidget)
        self.label_zCoordinate.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_zCoordinate.setObjectName("label_zCoordinate")
        self.gpsValuesRow1.addWidget(self.label_zCoordinate)
        self.gpsValuesLayout.addLayout(self.gpsValuesRow1)
        
        # Second row: latitude, longitude, altitude (right aligned)
        self.gpsValuesRow2 = QtWidgets.QHBoxLayout()
        self.gpsValuesRow2.setContentsMargins(2, 2, 2, 2)
        self.gpsValuesRow2.setSpacing(5)
        self.label_latitude = QtWidgets.QLabel(self.gpsValuesWidget)
        self.label_latitude.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_latitude.setObjectName("label_latitude")
        self.gpsValuesRow2.addWidget(self.label_latitude, alignment=QtCore.Qt.AlignRight)
        self.label_longitude = QtWidgets.QLabel(self.gpsValuesWidget)
        self.label_longitude.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_longitude.setObjectName("label_longitude")
        self.gpsValuesRow2.addWidget(self.label_longitude, alignment=QtCore.Qt.AlignRight)
        self.label_altitude = QtWidgets.QLabel(self.gpsValuesWidget)
        self.label_altitude.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_altitude.setObjectName("label_altitude")
        self.gpsValuesRow2.addWidget(self.label_altitude, alignment=QtCore.Qt.AlignRight)
        self.gpsValuesLayout.addLayout(self.gpsValuesRow2)
        
        self.gpsLayout.addWidget(self.gpsValuesWidget, 0)
        
        # GPS Map (large area)
        self.frame_gpsGraph = QtWidgets.QFrame(self.sectionGPS)
        self.frame_gpsGraph.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame_gpsGraph.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_gpsGraph.setObjectName("frame_gpsGraph")
        self.gpsLayout.addWidget(self.frame_gpsGraph, 1)
        
        # --- Embedding the Map into the GPS Graph Frame ---
        # Create a QWebEngineView widget as a child of frame_gpsGraph
        self.webView = QWebEngineView(self.frame_gpsGraph)
        # Load the local map HTML file
        CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(CURRENT_DIR, "map.html")
        url = QUrl.fromLocalFile(filename)
        print("Loading map from:", url.toString())
        self.webView.load(url)
        # Create a layout for frame_gpsGraph and add the QWebEngineView
        self.gpsGraphLayout = QtWidgets.QVBoxLayout(self.frame_gpsGraph)
        self.gpsGraphLayout.setContentsMargins(0, 0, 0, 0)
        self.gpsGraphLayout.addWidget(self.webView)
        
        self.middleLayout.addWidget(self.sectionGPS, 1)
        
        # ---- Right Column: Reaction Wheel (Split into Upper & Lower Boxes) ----
        self.sectionReaction = QtWidgets.QWidget(self.centralwidget)
        self.sectionReaction.setObjectName("sectionReaction")
        self.reactionLayout = QtWidgets.QVBoxLayout(self.sectionReaction)
        self.reactionLayout.setContentsMargins(5, 5, 5, 5)
        self.reactionLayout.setSpacing(5)
        
        # Upper group box: Reaction Wheel Manual Controller with 4 directional buttons
        self.groupBox_reaction = QtWidgets.QGroupBox(self.sectionReaction)
        self.groupBox_reaction.setTitle("Reaction Wheel Manual Controller")
        self.groupBox_reaction.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_reactionLayout = QtWidgets.QVBoxLayout(self.groupBox_reaction)
        self.groupBox_reactionLayout.setContentsMargins(5, 5, 5, 5)
        self.groupBox_reactionLayout.setSpacing(5)
        
        # Create a widget to hold the directional buttons using a grid layout.
        self.reactionButtonsWidget = QtWidgets.QWidget(self.groupBox_reaction)
        self.gridLayout_reactionButtons = QtWidgets.QGridLayout(self.reactionButtonsWidget)
        self.gridLayout_reactionButtons.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_reactionButtons.setSpacing(5)
        
        # Create the buttons and set them big and red.
        self.button_north = QtWidgets.QPushButton("North", self.reactionButtonsWidget)
        self.button_north.setStyleSheet("background-color: red; color: white; font-size: 16pt;")
        self.button_north.setMinimumSize(80, 80)
        
        self.button_west = QtWidgets.QPushButton("West", self.reactionButtonsWidget)
        self.button_west.setStyleSheet("background-color: red; color: white; font-size: 16pt;")
        self.button_west.setMinimumSize(80, 80)
        
        self.button_east = QtWidgets.QPushButton("East", self.reactionButtonsWidget)
        self.button_east.setStyleSheet("background-color: red; color: white; font-size: 16pt;")
        self.button_east.setMinimumSize(80, 80)
        
        self.button_south = QtWidgets.QPushButton("South", self.reactionButtonsWidget)
        self.button_south.setStyleSheet("background-color: red; color: white; font-size: 16pt;")
        self.button_south.setMinimumSize(80, 80)
        
        # Arrange buttons in the grid:
        # Row 0, Column 1: North
        self.gridLayout_reactionButtons.addWidget(self.button_north, 0, 1)
        # Row 1, Column 0: West
        self.gridLayout_reactionButtons.addWidget(self.button_west, 1, 0)
        # Row 1, Column 2: East
        self.gridLayout_reactionButtons.addWidget(self.button_east, 1, 2)
        # Row 2, Column 1: South
        self.gridLayout_reactionButtons.addWidget(self.button_south, 2, 1)
        
        # Add the buttons widget to the group box layout.
        self.groupBox_reactionLayout.addWidget(self.reactionButtonsWidget)
        self.reactionLayout.addWidget(self.groupBox_reaction, 3)
        
        # Lower group box: Termination
        self.groupBox_termination = QtWidgets.QGroupBox(self.sectionReaction)
        self.groupBox_termination.setTitle("Termination")
        self.groupBox_termination.setStyleSheet("color: rgb(255, 255, 255);")
        self.terminationLayout = QtWidgets.QVBoxLayout(self.groupBox_termination)
        self.terminationLayout.setContentsMargins(5, 5, 5, 5)
        self.terminationLayout.setSpacing(5)
        # Leave this area open for future termination controls.
        self.reactionLayout.addWidget(self.groupBox_termination, 1)
        
        self.middleLayout.addWidget(self.sectionReaction, 1)
        
        self.mainLayout.addLayout(self.middleLayout, 1)
        
        # ---------------------------
        # Bottom: Common Buttons (START, LOG, STOP)
        # ---------------------------
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setContentsMargins(5, 5, 5, 5)
        self.buttonLayout.setSpacing(10)
        
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setStyleSheet("background-color: green; color: black;")
        self.pushButton_start.setObjectName("pushButton_start")
        self.buttonLayout.addWidget(self.pushButton_start)
        
        self.pushButton_log = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_log.setStyleSheet("background-color: red; color: black;")
        self.pushButton_log.setObjectName("pushButton_log")
        self.buttonLayout.addWidget(self.pushButton_log)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)
        
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setStyleSheet("background-color: red; color: black;")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.buttonLayout.addWidget(self.pushButton_stop)
        
        self.mainLayout.addLayout(self.buttonLayout, 0)
        
        # Overall stretch factors: Title and buttons fixed; middle horizontal layout takes remaining space.
        self.mainLayout.setStretch(0, 0)  # Title
        self.mainLayout.setStretch(1, 1)  # Middle 3 columns
        self.mainLayout.setStretch(2, 0)  # Buttons
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_mainTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"font-size:26pt;\">HAB Data Domain</span></p></body></html>"))
        self.label_scientificTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"font-size:20pt;\">Scientific Readings</span></p></body></html>"))
        self.label_pressure.setText(_translate("MainWindow", "Pressure:"))
        self.label_pressure_value.setText(_translate("MainWindow", "70"))
        self.label_temperature.setText(_translate("MainWindow", "Temperature:"))
        self.label_temperature_value.setText(_translate("MainWindow", "20"))
        self.label_radiation.setText(_translate("MainWindow", "Radiation:"))
        self.label_radiation_value.setText(_translate("MainWindow", "20"))
        self.label_density.setText(_translate("MainWindow", "Density:"))
        self.label_density_value.setText(_translate("MainWindow", "1"))
        self.groupBox_graph1.setTitle(_translate("MainWindow", "Altitude v Pressure"))
        self.groupBox_graph2.setTitle(_translate("MainWindow", "Altitude v Temperature"))
        
        self.label_gpsTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"font-size:26pt;\">GPS Tracking</span></p></body></html>"))
        self.label_xCoordinate.setText(_translate("MainWindow", "x-coordinate: 0"))
        self.label_yCoordinate.setText(_translate("MainWindow", "y-coordinate: 0"))
        self.label_zCoordinate.setText(_translate("MainWindow", "z-coordinate: 0"))
        self.label_latitude.setText(_translate("MainWindow", "Latitude: 0"))
        self.label_longitude.setText(_translate("MainWindow", "Longitude: 0"))
        self.label_altitude.setText(_translate("MainWindow", "Altitude: 0"))
        
        # Reaction section titles are set via the group boxes.
        self.pushButton_start.setText(_translate("MainWindow", "START"))
        self.pushButton_log.setText(_translate("MainWindow", "LOG"))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())