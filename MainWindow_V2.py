from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QFrame, QSizePolicy, QSpacerItem, QMessageBox, QCheckBox, QRadioButton, QScrollArea, QComboBox, QToolButton, QTextEdit, QTabWidget, QDialog, QHBoxLayout, QMainWindow, QWidget, QLineEdit, QAction, QPushButton, QLabel, QVBoxLayout, QStackedWidget, QDesktopWidget, QGridLayout, QMenu, QPlainTextEdit, QTextBrowser
from PyQt5.QtCore import QFile, QTextStream, Qt, QTimer, QCoreApplication, QMargins ,QSize
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor, QPen, QTextCursor
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSet, QBarSeries
import pngs_rc
import re
import DB_V2
from datetime import datetime
import webbrowser


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setFixedSize(613, 100)  # Set fixed size
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Load QSS file for styling
        with open("Dialog.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.line_edit = QLineEdit()
        self.warning_label = QLabel("")
        self.ok_button = QPushButton("")
        self.ok_button.setStyleSheet('height: 15px;')
        
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.warning_label)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
        
        self.ok_button.clicked.connect(self.validate_and_accept)

    def validate_and_accept(self):
        new_name = self.line_edit.text().strip()
        if not new_name:
            self.warning_label.setText("Please Enter valid Name!")
            return
        elif len(new_name) > 20:
            self.warning_label.setText("Please Enter folder name between (_1 and 19_) charcter!")
            return
        elif DB_V2.check_folder_exist_in_folderNames_table(new_name):
            self.warning_label.setText("Folder name already exists try another name!")
            return
        self.accept()

    def create_folder(self):
        self.setWindowTitle("Create Folder")
        self.line_edit.setPlaceholderText("Enter Folder Name")
        self.ok_button.setText("Create")

    def rename_folder(self):
        self.setWindowTitle("Rename Folder")
        self.line_edit.setPlaceholderText("Enter New Folder Name")
        self.ok_button.setText("Rename")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWindow_V2.ui', self)
        self.load_stylesheet("MainWindow_V2.qss")
        self.setGeometry(700, 500, 500, 200)
                    # initialize UI elements from UI file
                            # QWidget
        self.sidBar                    = self.findChild(QWidget,        "sidBar"                     )
        self.chart_widget              = self.findChild(QWidget,        "chart_widget"               )
        self.widget                    = self.findChild(QWidget,        "widget"                     )
        self.chart_widget_2            = self.findChild(QWidget,        "chart_widget_2"             )

                            # QStackedWidget
        self.pagesStackedWidget        = self.findChild(QStackedWidget, "pagesStackedWidget"         )
                                    # QLabel
        self.myScansLabel              = self.findChild(QLabel,          "myScansLabel"              )
        self.critical_label            = self.findChild(QLabel,          "critical_label"            )
        self.high_label                = self.findChild(QLabel,          "high_label"                )
        self.medium_label              = self.findChild(QLabel,          "medium_label"              )
        self.low_label                 = self.findChild(QLabel,          "low_label"                 )
        self.info_label                = self.findChild(QLabel,          "info_label"                )
        self.ScanDetails_Name_label    = self.findChild(QLabel,          "ScanDetails_Name_label"    )
        self.ScanDetails_Status_label  = self.findChild(QLabel,          "ScanDetails_Status_label"  )
        self.ScanDetails_Policy_label  = self.findChild(QLabel,          "ScanDetails_Policy_label"  )
        self.ScanDetails_Scanner_label = self.findChild(QLabel,          "ScanDetails_Scanner_label" )
        self.ScanDetails_Start_label   = self.findChild(QLabel,          "ScanDetails_Start_label"   )
        self.ScanDetails_End_label     = self.findChild(QLabel,          "ScanDetails_End_label"     )
        self.ScanDetails_Elapsed_label = self.findChild(QLabel,          "ScanDetails_Elapsed_label" )
        self.searchFindLabel           = self.findChild(QLabel,          "searchFindLabel"           )
        self.searchFindLabel_2         = self.findChild(QLabel,          "searchFindLabel_2"         )
        self.searchFindLabel_3         = self.findChild(QLabel,          "searchFindLabel_3"         )
        self.see_al_label              = self.findChild(QLabel,          "see_al_label"              )
        self.vuln_name_label           = self.findChild(QLabel,          "vuln_name_label"           )
        self.sev_label                 = self.findChild(QLabel,          "sev_label"                 )
                            # QPushButton
        self.createNewScan_btn         = self.findChild(QPushButton,     "createNewScan_btn"         )
        self.cancelSetting_btn         = self.findChild(QPushButton,     "cancelSetting_btn"         )
        self.saveSetting_btn           = self.findChild(QPushButton,     "saveSetting_btn"           )
        self.scansTopBar_btn           = self.findChild(QPushButton,     "scansTopBar_btn"           )
        self.logedUser_btn             = self.findChild(QPushButton,     "logedUser_btn"             )
        self.newFolder_btn             = self.findChild(QPushButton,     "newFolder_btn"             )
        self.myAccount_btn             = self.findChild(QPushButton,     "myAccount_btn"             )
        self.allScans_btn              = self.findChild(QPushButton,     "allScans_btn"              )
        self.myScans_btn               = self.findChild(QPushButton,     "myScans_btn"               )
        self.newScan_btn               = self.findChild(QPushButton,     "newScan_btn"               )
        self.OWASP_btn_1               = self.findChild(QPushButton,     "OWASP_btn_1"               )
        self.OWASP_btn_2               = self.findChild(QPushButton,     "OWASP_btn_2"               )
        self.OWASP_btn_3               = self.findChild(QPushButton,     "OWASP_btn_3"               )
        self.cancel_btn                = self.findChild(QPushButton,     "cancel_btn"                )
        self.about_btn                 = self.findChild(QPushButton,     "about_btn"                 )
        self.trash_btn                 = self.findChild(QPushButton,     "trash_btn"                 )
        self.back_btn                  = self.findChild(QPushButton,     "back_btn"                  )
        self.scan_Name                 = self.findChild(QPushButton,     "scan_Name"                 )
        self.theme_btn                 = self.findChild(QPushButton,     "theme_btn"                 )
                            # QLineEdit
        self.currentPasswordInput      = self.findChild(QLineEdit,       "currentPasswordInput"      )
        self.newPasswordInput          = self.findChild(QLineEdit,       "newPasswordInput"          )
        self.fullNameInput             = self.findChild(QLineEdit,       "fullNameInput"             )
        self.targetInput               = self.findChild(QLineEdit,       "targetInput"               )
        self.searchInput               = self.findChild(QLineEdit,       "searchInput"               )
        self.emailInput                = self.findChild(QLineEdit,       "emailInput"                )
        self.nameInput                 = self.findChild(QLineEdit,       "nameInput"                 )
                            # QTabWidget      
        self.tabWidgetForInputs        = self.findChild(QTabWidget,      "tabWidgetForInputs"        )
        self.accountSettingTab         = self.findChild(QTabWidget,      "accountSettingTab"         )
        self.overviewTab               = self.findChild(QTabWidget,      "overviewTab"               )
        self.tabWidget_2               = self.findChild(QTabWidget,      "tabWidget_2"               )
                            # QTextEdit      
        self.descriptionInput          = self.findChild(QTextEdit,       "descriptionInput"          )
        self.output_plainTextEdit      = self.findChild(QTextEdit,       "output_plainTextEdit"      )
        self.see_al_plainTextEdit      = self.findChild(QTextEdit,       "see_al_plainTextEdit"      )
        self.solu_plainTextEdit        = self.findChild(QTextEdit,       "solu_plainTextEdit"        )
        self.desc_plainTextEdit        = self.findChild(QTextEdit,       "desc_plainTextEdit"        )
        self.impacts_plainTextEdit     = self.findChild(QTextEdit,       "impacts_plainTextEdit"     )
                            # QGridLayout      
        self.gridLayout_8              = self.findChild(QGridLayout,     "gridLayout_8"              )
        self.gridLayout_12             = self.findChild(QGridLayout,     "gridLayout_12"             )
        self.gridLayout_18             = self.findChild(QGridLayout,     "gridLayout_18"             )
        self.gridLayout_2              = self.findChild(QGridLayout,     "gridLayout_2"              )
        self.gridLayout_36             = self.findChild(QGridLayout,     "gridLayout_36"             )
                            # QComboBox
        self.folderInput               = self.findChild(QComboBox,       "folderInput"               )
                            # QScrollArea
        self.scrollArea                = self.findChild(QScrollArea,     "scrollArea"                )
                            # QToolButton
        self.save_btn                  = self.findChild(QToolButton,     "save_btn"                  )
                            # QRadioButton
        self.dark_theme_radioButton    = self.findChild(QRadioButton,    "dark_theme_radioButton"    )

        self.last_btn_pressed = [1]


        self.save_btn.setPopupMode(QToolButton.MenuButtonPopup)

        launch_action = QAction("             launch", self)
        launch_action.triggered.connect(self.launch_scan)
        self.save_btn.addAction(launch_action)

                            # ####################
                            #   Buttons Section  #
                            # ####################
                        #   Change Page with index btns
        self.createNewScan_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(1))
        self.myAccount_btn.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(6))
        self.theme_btn.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(5))
        # self.myAccount_btn.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(4))
        self.newScan_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(1))
        self.about_btn.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(7))
        self.OWASP_btn_1.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(2))
        self.OWASP_btn_2.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(2))
        self.OWASP_btn_3.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(2))

        self.newFolder_btn.clicked.connect(self.AddNewFolderWindow)
     
        # self.logedUser_btn.clicked.connect(self.settingPage)


        self.dark_theme_radioButton.clicked.connect(self.dark_theme_and_light_theme)

        

        self.logedUser_btn.clicked.connect(lambda: self.tabWidget_2.setCurrentIndex(1))
        self.settingsTopBar_btn.clicked.connect(self.settingPage)
        self.scansTopBar_btn.clicked.connect(self.scansTopBar)
        self.allScans_btn.clicked.connect(self.clicked_btn)
        self.myScans_btn.clicked.connect(self.clicked_btn)
        self.save_btn.clicked.connect(self.save_scan)

        self.myScans_btn.setObjectName("My Scans")
        self.myScans_btn.click()
        self.pagesStackedWidget.setCurrentIndex(5)
        self.dark_theme_radioButton.click()
        self.pagesStackedWidget.currentChanged.connect(self.on_page_changed)


##################################################################################################################
                            # Chart section
        chart_layout = QVBoxLayout(self.chart_widget)
        self.circleChart(chart_layout, 25,10, 0, 0, 1)

        chart_layout = QVBoxLayout(self.chart_widget_2)
        self.circleChart(chart_layout, 25,10, 0, 0, 1)

        self.lineChart(25,10,0,0,1)

##################################################################################################################


                            # called Func Section
        DB_V2.create_table()
        DB_V2.craet_all_tables()
        self.center_on_screen()

        self.addBtns(DB_V2.select_all_data())


        # self.tabWidget_2.currentChanged.connect(self.on_tab_changed)

        self.create_table_scans_for_vulnerability()

        self.show()
        self.showMaximized()



    def dark_theme_and_light_theme(self):
        sender = self.sender()
        if sender.isChecked():
            self.load_stylesheet('dark_theme.qss')
        else:
            self.load_stylesheet('light_theme.qss')



    def on_tab_changed(self, index):
        if index == 1:  # Index 1 corresponds to Tab 2
            self.create_table_scans_for_vulnerability()


    def lineChart(self, info, low, medium, high, critical):
        self.critical_label.setText(f"{critical}")
        self.high_label.setText(f"{high}")
        self.medium_label.setText(f"{medium}")
        self.low_label.setText(f"{low}")
        self.info_label.setText(f"{info}")
        spacer = QSpacerItem(1, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacer)
        self.gridLayout_2.addItem(spacer,0 ,0)

        self.gridLayout_2.setColumnStretch(4,critical)
        self.gridLayout_2.setColumnStretch(3,high)
        self.gridLayout_2.setColumnStretch(2,medium)  
        self.gridLayout_2.setColumnStretch(1,low)
        self.gridLayout_2.setColumnStretch(0,info)
        self.hide_if_zero(self.critical_label, critical)
        self.hide_if_zero(self.high_label, high)
        self.hide_if_zero(self.medium_label, medium)
        self.hide_if_zero(self.low_label, low)
        self.hide_if_zero(self.info_label, info)

    def hide_if_zero(self, label, num):
        if num == 0:
            label.setVisible(False)

    def circleChart(self, target_layout, info, low, medium, high, critical):
        series = QPieSeries()
        slice1 = series.append("Critical", critical)
        slice2 = series.append("High", high)
        slice3 = series.append("Medium", medium)
        slice4 = series.append("Low", low)
        slice5 = series.append("Info", info)

        slice1.setBrush(QColor(245, 2, 2))
        slice2.setBrush(QColor(238, 147, 54))
        slice3.setBrush(QColor(253, 195, 46))
        slice4.setBrush(QColor(70, 177, 79))
        slice5.setBrush(QColor(43, 100, 149))

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().setAlignment(Qt.AlignRight)

        center_series = QPieSeries()
        center_slice = center_series.append("", 100)  
        center_series.setPieSize(0.38)  

        center_slice.setBrush(QColor(255,255,255))
        chart.addSeries(center_series)
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        chartview.setStyleSheet("border: none;")
        chart.setMargins(QMargins(0, 0, 0, 0))

        chartview.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        chartview.setMaximumSize(350, 250)  
        chartview.setMinimumSize(350,250)  

        target_layout.addWidget(chartview)

    def addBtns(self, folderNames):
        for i in folderNames:
            self.new_btn = QPushButton(f"        {i[1]}", self)
            self.new_btn.setObjectName(i[1])
            self.new_btn.setCheckable(True)
            self.new_btn.setAutoExclusive(True)

            context_menu = QMenu(self)
            delete_action = QAction("Delete", self)
            delete_action.triggered.connect(lambda _, button=self.new_btn: self.deleteButton(button))
            context_menu.addAction(delete_action)
            Rename_action = QAction("Rename", self)
            Rename_action.triggered.connect(lambda _, button=self.new_btn: self.renameButton(button))
            context_menu.addAction(Rename_action)
            self.new_btn.setContextMenuPolicy(3)
            self.new_btn.customContextMenuRequested.connect(
                lambda pos, button=self.new_btn, menu=context_menu: self.showContextMenu(pos, button, menu)
            )

            self.new_btn.setStyleSheet('QPushButton:checked{border-left: 5px solid rgb(63, 174, 73);background-color: rgb(222, 222, 222);color: black;height: 40px;font-size: 15px;text-align: left;}QPushButton{height: 40px;font-size: 15px;border: none;text-align: left;}QPushButton:hover{background-color: rgb(38, 55, 70);color: rgb(255, 255, 255);}')
            self.new_btn.clicked.connect(self.clicked_btn)

            index = self.gridLayout_12.indexOf(self.allScans_btn)
            self.gridLayout_12.addWidget(self.new_btn, self.gridLayout_12.rowCount() , 0)
            self.gridLayout_12.addWidget(self.trash_btn, self.gridLayout_12.rowCount() + 1, 0)

    def on_page_changed(self, index):

        if not index == 2:
            self.folderInput.clear()
        if index == 0 or index == 3:
            self.back_btn.setText("")
            self.back_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(index))
        elif index == 1:
            self.back_btn.setText("< back to My Scans")
            self.myScansLabel.setText("Scan Templates")
            self.back_btn.clicked.connect(lambda: self.myScans_btn.click())
        elif index == 2:
            self.myScansLabel.setText("New Scan / Web Alication Test")
            self.back_btn.setText("< back to Scan Templates")
            self.back_btn.clicked.connect(lambda: self.newScan_btn.click())
            self.folderInput.addItem("My Scans")
            data = DB_V2.select_all_data()
            for i in data:
                self.folderInput.addItem(i[1])
        elif index == 7:
            self.back_btn.setText("< back to Vulnerabilites page")
            try:
                self.back_btn.clicked.connect(self.last_btn_pressed[0].click)
            except:
                pass
        elif index == 4:
            btn = self.findClickedButton()
            if btn.objectName() == "allScans_btn":
                self.back_btn.setText(f"< back to All Scans")
            elif btn.objectName() == "myScans_btn":
                self.back_btn.setText(f"< back to My Scan")
            elif btn.objectName() == "trash_btn":
                self.back_btn.setText(f"< back to Trash")
            else:
                self.back_btn.setText(f"< back to {btn.objectName()}")
            self.back_btn.clicked.connect(lambda: btn.click)

    def save_scan(self):
        validate_nameInput  = False
        validate_targetInput = False
        if len(self.nameInput.text().strip()) == 0:
            self.nameInput.setToolTip("Field cannot be empty!") 
            self.nameInput.setStyleSheet('border: 1px solid red;background-color: white;color: black;height: 30px;')
        elif DB_V2.check_name_exist(self.nameInput.text().strip()):
            self.nameInput.setToolTip("Scan name already exists try another name!")
            self.nameInput.setStyleSheet('border: 1px solid red;background-color: white;color: black;height: 30px;')
        else:
            self.nameInput.setStyleSheet('border: 1px solid black;background-color: white;color: black;height: 30px;')
            validate_nameInput = True

        if self.is_valid_input(self.targetInput.text()) and len(self.targetInput.text().strip()) != 0:
            self.targetInput.setStyleSheet('border: 1px solid black;background-color: white;color: black;height: 30px;')
            validate_targetInput = True
        else:
            self.targetInput.setToolTip("Please Enter Valid Target Like : 192.168.1.3 or URL or Link or example.com") 
            self.targetInput.setStyleSheet('border: 1px solid red;background-color: white;color: black;height: 30px;')

        if validate_nameInput and validate_targetInput:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
            DB_V2.insert_data(self.nameInput.text(), "On Demand", current_datetime, self.folderInput.currentText(), self.descriptionInput.toPlainText(), self.targetInput.text())

            btn = self.find_button_by_text(self.folderInput.currentText())
            self.nameInput.setText('')
            self.descriptionInput.setPlainText('')
            self.folderInput.setCurrentText('')
            self.targetInput.setText('')
            btn.click()

    def launch_scan(self):
        validate_nameInput  = False
        validate_targetInput = False
        if len(self.nameInput.text().strip()) == 0:
            self.nameInput.setToolTip("Field cannot be empty!") 
            self.nameInput.setStyleSheet('border: 1px solid red;background-color: white;color: black;height: 30px;')
        elif DB_V2.check_name_exist(self.nameInput.text().strip()):
            self.nameInput.setToolTip("Scan name already exists try another name!")
            self.nameInput.setStyleSheet('border: 1px solid red;background-color: white;color: black;height: 30px;')
        else:
            self.nameInput.setStyleSheet('border: 1px solid black;background-color: white;color: black;height: 30px;')
            validate_nameInput = True

        if self.is_valid_input(self.targetInput.text()) and len(self.targetInput.text().strip()) != 0:
            self.targetInput.setStyleSheet('border: 1px solid black;background-color: white;color: black;height: 30px;')
            validate_targetInput = True
        else:
            self.targetInput.setToolTip("Please Enter Valid Target Like : 192.168.1.3 or URL or Link or example.com") 
            self.targetInput.setStyleSheet('border: 1px solid red;background-color: white;color: black;height: 30px;')

        if validate_nameInput and validate_targetInput:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
            DB_V2.insert_data(self.nameInput.text(), "On Demand", current_datetime, self.folderInput.currentText(), self.descriptionInput.toPlainText(), self.targetInput.text())

            btn = self.find_button_by_text(self.folderInput.currentText())
            self.nameInput.setText('')
            self.descriptionInput.setPlainText('')
            self.folderInput.setCurrentText('')
            self.targetInput.setText('')
            btn.click()

    def create_table_scans_for_vulnerability(self):
        ParentLayout = QGridLayout()         #######> this is the main layout that all windget inside it 
        main_v_layout = QVBoxLayout()  # create virtival layout to add all widget virticaly and set it as main layout for main widget 
        main_v_layout.setSpacing(0)
        ParentLayout.setContentsMargins(0, 0, 0, 0)

        h_layout = QHBoxLayout()
        checkbox = QCheckBox()
        sev_label = QLabel("Sev")
        sev_label.setStyleSheet('border: none; ')


        h_layout.addWidget(sev_label)


        h_layout2 = QHBoxLayout()
        name_label = QLabel("  Name")
        name_label.setStyleSheet('border: none; ')
        h_layout2.addWidget(name_label)
        h_layout2.setSpacing(20)


        h_layout3 = QHBoxLayout()
        family_label = QLabel(" Family")
        family_label.setStyleSheet('border: none; ')
        h_layout3.addWidget(family_label)

        h_layout4 = QHBoxLayout()
        count_label = QLabel("Count")
        count_label.setStyleSheet('border: none; ')
        h_layout4.addWidget(count_label)


        h_layout5 = QHBoxLayout()
        edit_btn = QPushButton()
        edit_btn.setIcon(QIcon('png/cogwheel.png'))
        edit_btn.setIconSize(QSize(18, 18))

        edit_btn.setStyleSheet('border: none;')
        h_layout5.addWidget(edit_btn)



        main_layout = QGridLayout()
        main_layout.setContentsMargins(65, 0, 17, 0)

        main_layout.addLayout(h_layout , 0, 0)
        main_layout.addLayout(h_layout2, 0, 1)
        main_layout.addLayout(h_layout3, 0, 2)
        main_layout.addLayout(h_layout4, 0, 3)
        main_layout.addLayout(h_layout5, 0, 4)

        main_layout.setColumnStretch(0, 2)
        main_layout.setColumnStretch(1, 8)
        main_layout.setColumnStretch(2, 8)
        main_layout.setColumnStretch(3, 4)
        main_layout.setColumnStretch(4, 0)

        self.widget_2 = QWidget(self)

        self.widget_2.setStyleSheet("border: 2px solid rgb(221, 221, 221); background-color: rgb(245, 245, 245);font-size: 13px; font-weight: bold;")
        self.widget_2.setMinimumHeight(35)
        self.widget_2.setMaximumHeight(35)

        self.widget_2.setLayout(main_layout)  # set layout of widget_2 with his elements

        main_v_layout.addLayout(ParentLayout)
        main_v_layout.addWidget(self.widget_2)
        spacer = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        for i in range(2):
            sev_layout = QHBoxLayout()
            child_checkbox = QCheckBox()
            sev_label = QLabel(f"CRETICAL")
            sev_label.setFixedSize(80, 25)
            child_checkbox.setStyleSheet('border-left: none;border-right: none; ')
            sev_label.setStyleSheet('background-color: red; color: white; border: none; font-weight: normal;')
            sev_label.setAlignment(Qt.AlignCenter)


            sev_layout.addWidget(child_checkbox)
            sev_layout.addWidget(sev_label)
            sev_layout.addItem(spacer)
            sev_layout.setStretch(0,0)
            sev_layout.setStretch(1,1)
            sev_layout.setSpacing(20)

            sev_label.setObjectName(f"test_2")


            vul_name_layout = QHBoxLayout()
            vuln_name_btn = QPushButton(f"Reflected XSS")
            vuln_name_btn.setStyleSheet('QPushButton{border:none; text-align: left;} QPushButton:hover{text-decoration: underline; color: rgb(56, 109, 156);}')
            vul_name_layout.addWidget(vuln_name_btn)


            vuln_name_btn.clicked.connect(lambda: self.show_vuln_info("Reflected XSS"))

            vuln_family_layout = QHBoxLayout()
            vuln_family_label = QLabel(f"Cross Site Scripting")
            vuln_family_label.setStyleSheet('border-left: none;border-right: none;text-align: center; ')
            vuln_family_layout.addWidget(vuln_family_label)


            vuln_count_layout = QHBoxLayout()
            vuln_count_label = QLabel(f"1")
            vuln_count_label.setStyleSheet('border-left: none;border-right: none;text-align: center; ')
            vuln_count_layout.addWidget(vuln_count_label)


            btns_layout = QHBoxLayout()

            edit_vuln_btn = QPushButton()
            edit_vuln_btn.setIcon(QIcon('png/pen.png'))
            edit_vuln_btn.setIconSize(QSize(18, 18))  # Set the size of the icon (optional)

            edit_vuln_btn.setStyleSheet('''
                QPushButton:hover{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(165, 165, 165);}
                QPushButton{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(217, 217, 217);}
                ''')
            font = QFont("Sitka Subheading Semibold")
            edit_vuln_btn.setFont(font)
            edit_vuln_btn.setObjectName(f"test5")

            edit_vuln_btn.clicked.connect(self.CancelScan)

            btns_layout.addWidget(edit_vuln_btn)


            main_layout = QGridLayout()
            main_layout.setContentsMargins(10, 0, 20, 0)



            main_layout.addLayout(sev_layout, 0, 0)
            main_layout.addLayout(vul_name_layout, 0, 1)
            main_layout.addLayout(vuln_family_layout, 0, 2)
            main_layout.addLayout(vuln_count_layout, 0, 3)
            main_layout.addLayout(btns_layout, 0, 4)


            main_layout.setColumnStretch(0, 5)
            main_layout.setColumnStretch(1, 12)
            main_layout.setColumnStretch(2, 13)
            main_layout.setColumnStretch(3, 4)
            main_layout.setColumnStretch(4, 1)

            self.widget_2 = QWidget(self)
            self.widget_2.setStyleSheet(f'background-color: rgb(30,50,30);')
            self.widget_2.setStyleSheet("border: 1px solid rgb(221, 221, 221); height: 60px; font-size: 12px;font-weight:500; ")
            self.widget_2.setLayout(main_layout)  # set layout of widget_2 with his elements
            main_v_layout.addWidget(self.widget_2)


        self.MainWidget = QWidget(self) # Create Main widget 
        spacer = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        main_v_layout.addItem(spacer)
        self.MainWidget.setLayout(main_v_layout) # add the main Virtical layout that contain all widget with his elements 


        self.gridLayout_36.addWidget(self.MainWidget)  # Add button to row 0, column 0


    def count_lines(self, text):
        lines = text.splitlines()
        return len(lines)

    def show_vuln_info(self, vuln_name):
        self.pagesStackedWidget.setCurrentIndex(7)

        self.see_al_label.setText("&nbsp;&nbsp;&nbsp;<a href='http://www.example.com'>Click me to open link</a>")
        self.see_al_label.setOpenExternalLinks(True)

        import sys
        sys.path.append('../Vulnerabilites Scripts')
        import Forms_of_vuln

        vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form = Forms_of_vuln.PUT_DELETE_Mathod_Form()
        self.desc_plainTextEdit.setText(vuln_Description_form.strip())
        self.desc_plainTextEdit.setStyleSheet("font-size: 16px; border: none;")


        self.solu_plainTextEdit.setText(vuln_Soluation_form.strip())
        self.solu_plainTextEdit.setStyleSheet("font-size: 16px; border: none;")

        self.impacts_plainTextEdit.setText(vuln_Impactes_form.strip())
        self.impacts_plainTextEdit.setStyleSheet("font-size: 16px; border: none;")

        self.see_al_label.setText(vuln_See_Also_form.strip())
        self.see_al_label.setStyleSheet("font-size: 16px; border: none;")

        self.output_plainTextEdit.setText(vuln_Output_form.strip())
        self.output_plainTextEdit.setStyleSheet("font-size: 16px; border: none;")

        # desc_hight   = self.count_lines(vuln_Description_form.strip()) * 26
        # solu_hight   = self.count_lines(vuln_Soluation_form.strip()) * 26
        # output_hight = self.count_lines(vuln_Output_form.strip()) * 26
        # impa_hight   = self.count_lines(vuln_Impactes_form.strip()) * 26
        desc_hight   = int(self.desc_plainTextEdit.document().size().height())
        solu_hight   = int(self.solu_plainTextEdit.document().size().height())
        output_hight = int(self.output_plainTextEdit.document().size().height())
        impa_hight   = int(self.impacts_plainTextEdit.document().size().height())

        self.desc_plainTextEdit.setMaximumSize(16777215 ,desc_hight)
        self.solu_plainTextEdit.setMaximumSize(16777215 ,solu_hight)
        self.output_plainTextEdit.setMaximumSize(16777215 ,output_hight)
        self.impacts_plainTextEdit.setMaximumSize(16777215 ,impa_hight)

        self.desc_plainTextEdit.setMinimumSize(16777215 ,desc_hight)
        self.solu_plainTextEdit.setMinimumSize(16777215 ,solu_hight)
        self.output_plainTextEdit.setMinimumSize(16777215 ,output_hight)
        self.impacts_plainTextEdit.setMinimumSize(16777215 ,impa_hight)



        self.vuln_name_label.setText(vuln_name.strip())
        self.sev_label.setText(vuln_sev.strip())


    def create_table_scans(self, folderName):
        ParentLayout = QGridLayout()         #######> this is the main layout that all windget inside it 
        main_v_layout = QVBoxLayout()  # create virtival layout to add all widget virticaly and set it as main layout for main widget 
        main_v_layout.setSpacing(0)
        ParentLayout.setContentsMargins(0, 0, 0, 0)

        h_layout = QHBoxLayout()
        checkbox = QCheckBox()
        name_label = QLabel("Name")
        checkbox.setStyleSheet('border-left: none;border-right: none; ')
        name_label.setStyleSheet('border-left: none;border-right: none; ')

        h_layout.addWidget(checkbox)
        h_layout.addWidget(name_label)
        h_layout.setStretch(0,0)
        h_layout.setStretch(1,1)
        h_layout.setSpacing(20)


        h_layout2 = QHBoxLayout()
        lastModify_label = QLabel("Last Modify")
        lastModify_label.setStyleSheet('border-left: none;border-right: none; ')
        h_layout2.addWidget(lastModify_label)


        h_layout3 = QHBoxLayout()
        schedule_label = QLabel("Schedule")
        schedule_label.setStyleSheet('border-left: none;border-right: none; ')
        h_layout3.addWidget(schedule_label)



        main_layout = QGridLayout()
        main_layout.setContentsMargins(10, 0, 100, 0)

        main_layout.addLayout(h_layout, 0, 0)
        main_layout.addLayout(h_layout3, 0, 1)
        main_layout.addLayout(h_layout2, 0, 2)

        main_layout.setColumnStretch(0, 3)
        main_layout.setColumnStretch(1, 3)
        main_layout.setColumnStretch(2, 1)

        self.widget_2 = QWidget(self)
        self.widget_2.setStyleSheet(f'background-color: rgb(30,50,30);')
        self.widget_2.setStyleSheet("border: 1px solid rgb(221, 221, 221); height: 35px; background-color: rgb(245, 245, 245);font-size: 13px; font-weight: bold;")
        self.widget_2.setLayout(main_layout)  # set layout of widget_2 with his elements

        main_v_layout.addLayout(ParentLayout)
        main_v_layout.addWidget(self.widget_2)
        
        if folderName == "All":
            data = DB_V2.get_all_data()
        else:
            data = DB_V2.get_data_by_folder_name(folderName)
        self.child_checkboxes = []
        for i in data:
            name_layout = QHBoxLayout()
            child_checkbox = QCheckBox()
            name_btn = QPushButton(f"{i[1]}")
            child_checkbox.setStyleSheet('border-left: none;border-right: none; ')
            name_btn.setStyleSheet('''
                QPushButton{border-left: none;border-right: none;text-align: left;}
                QPushButton:hover{text-decoration: underline; color: rgb(56, 109, 156);}
                ''')

            name_layout.addWidget(child_checkbox)
            name_layout.addWidget(name_btn)
            name_layout.setStretch(0,0)
            name_layout.setStretch(1,1)
            name_layout.setSpacing(20)

            self.child_checkboxes.append(child_checkbox)

            name_btn.setObjectName(f"{i[1]}")

            name_btn.clicked.connect(self.host_in_details)


            lastModify_layout = QHBoxLayout()
            label_text = f'<span style="font-weight:600; display:inline-block; white-space:nowrap;font-size: 20px; ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗸</span>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-weight:600; font-size: 13px;">{i[3]}</span>'
            lastModify_label = QLabel(f"{label_text}")
            lastModify_label.setStyleSheet('border-left: none;border-right: none; ')
            lastModify_layout.addWidget(lastModify_label)


            schedule_layout = QHBoxLayout()
            schedule_label = QLabel(f"       {i[2]}")
            schedule_label.setStyleSheet('border-left: none;border-right: none;text-align: center; ')
            schedule_layout.addWidget(schedule_label)


            btns_layout = QHBoxLayout()

            RunScan_btn = QPushButton("►")
            Cancel_scan_btn = QPushButton("X")
            Cancel_scan_btn.setStyleSheet('''
                QPushButton:hover{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(165, 165, 165);}
                QPushButton{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(217, 217, 217);}
                ''')
            RunScan_btn.setStyleSheet("""
                QPushButton:hover{border-left: none;border-right: none; font-size: 17px;color: rgb(165, 165, 165); margin-left: 52px;}
                QPushButton {border-left: none;border-right: none; font-size: 17px;color: rgb(217, 217, 217); margin-left: 52px;width: 40px;}
                """)
            font = QFont("Sitka Subheading Semibold")
            Cancel_scan_btn.setFont(font)
            Cancel_scan_btn.setObjectName(f"{i[1]}")
            RunScan_btn.setObjectName(f"{i[1]}")

            RunScan_btn.clicked.connect(self.RunScan)
            Cancel_scan_btn.clicked.connect(self.CancelScan)

            btns_layout.addWidget(RunScan_btn)
            btns_layout.addWidget(Cancel_scan_btn)


            main_layout = QGridLayout()
            main_layout.setContentsMargins(10, 0, 20, 0)



            main_layout.addLayout(name_layout, 0, 0)
            main_layout.addLayout(schedule_layout, 0, 1)
            main_layout.addLayout(lastModify_layout, 0, 2)
            main_layout.addLayout(btns_layout, 0, 3)


            main_layout.setColumnStretch(0, 3)
            main_layout.setColumnStretch(1, 3)
            main_layout.setColumnStretch(2, 1)


            self.widget_2 = QWidget(self)
            self.widget_2.setStyleSheet(f'background-color: rgb(30,50,30);')
            self.widget_2.setStyleSheet("border: 1px solid rgb(221, 221, 221); height: 60px; font-size: 12px;font-weight:500; ")
            self.widget_2.setLayout(main_layout)  # set layout of widget_2 with his elements
            main_v_layout.addWidget(self.widget_2)



        self.MainWidget = QWidget(self) # Create Main widget 
        spacer = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        main_v_layout.addItem(spacer)
        self.MainWidget.setLayout(main_v_layout) # add the main Virtical layout that contain all widget with his elements 

        self.scrollArea.setWidget(self.MainWidget)
        self.scrollArea.setStyleSheet("background-color: white;border: none;")
        self.searchFindLabel.setText(f"{len(self.child_checkboxes)} Scans")
        # self.searchFindLabel_2.setText(f"{len(self.child_checkboxes)} Scans")
        self.searchFindLabel_3.setText(f"{len(self.child_checkboxes)} Scans")
        checkbox.stateChanged.connect(self.mark_all_checkBoxes)

    def RunScan(self):
        btn = self.sender()
        if btn.text() == "►":
            btn.setText("||")
        else:
            btn.setText("►")

    def CancelScan(self):
        btn = self.sender()
        print(btn.objectName())
        reply = QMessageBox.question(self, 'Confirmation', 'Do you want to remove this Scan ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            DB_V2.remove_scan_by_name(btn.objectName())
            print(self.findClickedButton().click())

    def findClickedButton(self):
        for child in self.sidBar.children():
            if isinstance(child, QPushButton) and child.isChecked():
                return child

    def host_in_details(self):
        self.pagesStackedWidget.setCurrentIndex(4)
        btn = self.sender()
        self.last_btn_pressed[0] = btn

        domain_name = self.extract_domain(DB_V2.get_scan_by_name(btn.objectName())[6])
        self.scan_Name.setText(f"{domain_name}")

        self.ScanDetails_Name_label.setText(btn.text())
        self.ScanDetails_Status_label.setText("Completed")
        self.ScanDetails_Policy_label.setText("Web Alication Test")
        self.ScanDetails_Scanner_label.setText("Local Scan")
        # self.ScanDetails_Start_label
        # self.ScanDetails_End_label
        # self.ScanDetails_Elapsed_label

    def clicked_btn(self):
        btn = self.sender()
        self.myScansLabel.setText(btn.text().strip())

        self.myAccount_btn.hide()
        self.about_btn.hide()
        self.theme_btn.hide()
        if btn.objectName() == "allScans_btn":
            self.pagesStackedWidget.setCurrentIndex(3)
            if DB_V2.check_if_scans_exist():
                self.create_table_scans("All")
            else:
                self.pagesStackedWidget.setCurrentIndex(0)             # if not find any scan for this folder

        elif DB_V2.get_data_by_folder_name(btn.objectName()): # if find any scan for this folder
            self.pagesStackedWidget.setCurrentIndex(3)
            self.create_table_scans(btn.objectName())
            self.back_btn.setText("")
        else:
            self.pagesStackedWidget.setCurrentIndex(0)             # if not find any scan for this folder
            self.back_btn.setText("")

    def settingPage(self):
        sender_button = self.sender()
        self.last_btn_pressed.clear()
        self.last_btn_pressed.append(sender_button)

        self.pagesStackedWidget.setCurrentIndex(5)
        all_buttons = self.sidBar.findChildren(QPushButton)
        for button in all_buttons:
            button.hide()
        self.newFolder_btn.hide()
        self.newScan_btn.hide()
        self.foldersLabel.setText("     SETTINGS")
        self.myAccount_btn.show()
        self.about_btn.show()
        self.theme_btn.show()
        self.myAccount_btn.click()

    def scansTopBar(self):
        self.myScans_btn.click()
        all_buttons = self.sidBar.findChildren(QPushButton)
        for button in all_buttons:
            button.show()
        self.newFolder_btn.show()
        self.newScan_btn.show()
        self.foldersLabel.setText("     FOLDERS")
        self.myAccount_btn.hide()
        self.about_btn.hide()
        self.theme_btn.hide()

    def button_clicked(self):
        sender = self.sender()  # Get the object that triggered the event
        print("Clicked button:", sender.objectName())

    def mark_all_checkBoxes(self, state):
        for checkbox in self.child_checkboxes:
            checkbox.setChecked(state == 2)  # state == 2 means checked

    def is_valid_ip(self, ip):
        # Define a strong regular expression pattern for a valid IPv4 address
        ip_pattern = re.compile(r'''
            ^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
            (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
        ''', re.VERBOSE)

        return bool(ip_pattern.match(ip))

    def is_valid_url(self, url):
        # Define a regular expression pattern for a valid URL
        url_pattern = re.compile(r'''
            ^(https?|ftp):\/\/   # Protocol (http, https, or ftp)
            (www\.)?              # Optional "www." prefix
            [a-zA-Z0-9_-]+        # Domain name
            (\.[a-zA-Z]{2,})+     # Top-level domain (TLD)
            (:[0-9]+)?            # Optional port number
            (\/[a-zA-Z0-9_.-]*)*  # Path (optional)
            (\?[a-zA-Z0-9_=-]*)*  # Query string (optional)
            (\#[a-zA-Z0-9_]*)*$   # Fragment identifier (optional)
        ''', re.VERBOSE)

        return bool(url_pattern.match(url))

    def is_valid_domain(self, input_str):
        # Define a regular expression pattern for a valid domain
        domain_pattern = re.compile(r'''
            ^(www\.)?              # Optional "www." prefix
            [a-zA-Z0-9_-]+        # Domain name
            (\.[a-zA-Z]{2,})+$     # Top-level domain (TLD)
        ''', re.VERBOSE)

        # Check if the given string matches the domain pattern
        return bool(domain_pattern.match(input_str))

    def is_valid_input(self, input_str):
        is_valid = self.is_valid_ip(input_str)
        if is_valid:
            return input_str

        is_valid = self.is_valid_url(input_str)
        if is_valid:
            return input_str

        is_valid = self.is_valid_domain(input_str)
        if is_valid:
            return input_str

        return False

    def extract_domain(self, url):
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if not domain:
            # If netloc is empty, it's likely an IP address
            domain = parsed_url.path.split('/')[0]  # Extract IP from path
        if domain.startswith('www.'):
            domain = domain[4:]  # Remove 'www.' if present
        return domain

    def AddNewFolderWindow(self):

        dialog = Dialog(self)

        # Center the dialog on the screen
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - dialog.width()) / 2
        y = (screen_geometry.height() - dialog.height()) / 2
        dialog.move(int(x), int(y))

        dialog.create_folder()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            # new_name = dialog.line_edit.text()
            DB_V2.insert_folder_name(dialog.line_edit.text().strip())
            self.addBtns([(1,dialog.line_edit.text().strip())])
            self.folderInput.addItem(dialog.line_edit.text().strip())

    def deleteButton(self, button):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure if you delete this folder, all the scans inside it will be deleted as well !', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            value_to_delete = button.objectName()
            index = self.folderInput.findText(value_to_delete)
            if index != -1:
                self.folderInput.removeItem(index)            
            DB_V2.remove_scan_by_folder_name(button.objectName())
            DB_V2.delete_row_by_foldername(button.objectName())

            button.deleteLater()
            self.myScans_btn.click()

    def renameButton(self, button):
        dialog = Dialog(self)
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - dialog.width()) / 2
        y = (screen_geometry.height() - dialog.height()) / 2
        dialog.move(int(x), int(y))

        dialog.rename_folder()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            value_to_delete = button.objectName()
            index = self.folderInput.findText(value_to_delete)
            if index != -1:
                self.folderInput.removeItem(index)
            self.folderInput.addItem(dialog.line_edit.text().strip())      

            DB_V2.rename_folder(button.objectName(),dialog.line_edit.text().strip())

            button.setObjectName(dialog.line_edit.text().strip())
            button.setText(f"        {dialog.line_edit.text().strip()}")

    def showContextMenu(self, pos, button, menu):
        global_pos = button.mapToGlobal(pos)
        menu.exec_(global_pos)

    def find_button_by_text(self, target_text):
        for child in self.sidBar.findChildren(QPushButton):
            if child.text().strip() == target_text:
                return child
        return None

    def clear_widget_styles(self, widget):
        # Clear styles applied to the widget
        widget.setStyleSheet("")

        # Recursively clear styles for child widgets
        for child in widget.findChildren(QWidget):
            self.clear_widget_styles(child)

    def load_stylesheet(self, filename):
        self.clear_widget_styles(self)
        style_file = QFile(filename)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            content = stream.readAll()
            style_file.close()
            self.setStyleSheet(content)
        else:
            print(f"Failed to open {filename}")

    def center_on_screen(self):
        screen_geo = QDesktopWidget().screenGeometry()
        widget_geo = self.geometry()
        x = (screen_geo.width() - widget_geo.width()) // 5
        y = (screen_geo.height() - widget_geo.height()) // 3
        self.move(x, y)

app = QApplication([])
UiWindow = MainWindow()
app.exec_()
