from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QSpacerItem, QMessageBox, QCheckBox, QScrollArea, QComboBox, QToolButton, QTextEdit, QTabWidget, QDialog, QHBoxLayout, QMainWindow, QWidget, QLineEdit, QAction, QPushButton, QLabel, QVBoxLayout, QStackedWidget, QDesktopWidget, QGridLayout, QMenu
from PyQt5.QtCore import QFile, QTextStream, Qt, QTimer, QCoreApplication
from PyQt5.QtGui import QIcon, QFont

import re
import DB

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
        new_name = self.line_edit.text()
        if not new_name:
            self.warning_label.setText("Please Enter valid Name!")
            return
        elif len(new_name) > 20:
            self.warning_label.setText("Please Enter folder name between (_1 and 19_) charcter!")
            return
        elif DB.folder_name_exists(new_name):
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
        uic.loadUi('MainWindow.ui', self)
        self.load_stylesheet("MainWindow.qss")
        self.setGeometry(700, 500, 500, 200)
                    # initialize UI elements from UI file
                            # QWidget
        self.allWidgetsScan       = self.findChild(QWidget,        "allWidgetsScan"       )
        self.seconWidgets         = self.findChild(QWidget,        "seconWidgets"         )
        self.InputsWidget         = self.findChild(QWidget,        "InputsWidget"         )
        self.underTopBar          = self.findChild(QWidget,        "underTopBar"          )
        self.sidBar               = self.findChild(QWidget,        "sidBar"               )
        self.topBar               = self.findChild(QWidget,        "topBar"               )
        self.page_4               = self.findChild(QWidget,        "page_4"               )
        self.widget               = self.findChild(QWidget,        "widget"               )

        self.titleOfScansWidget   = self.findChild(QWidget,        "titleOfScansWidget"   )
        self.scan_1_widget        = self.findChild(QWidget,        "scan_1_widget"        )
        self.scan_2_widget        = self.findChild(QWidget,        "scan_2_widget"        )
        self.scan_3_widget        = self.findChild(QWidget,        "scan_3_widget"        )
        self.scan_4_widget        = self.findChild(QWidget,        "scan_4_widget"        )
        self.scan_5_widget        = self.findChild(QWidget,        "scan_5_widget"        )
        self.scan_6_widget        = self.findChild(QWidget,        "scan_6_widget"        )
        self.scan_7_widget        = self.findChild(QWidget,        "scan_7_widget"        )
        self.scan_8_widget        = self.findChild(QWidget,        "scan_8_widget"        )
        self.scan_9_widget        = self.findChild(QWidget,        "scan_9_widget"        )
        self.scan_10_widget       = self.findChild(QWidget,        "scan_10_widget"       )
        self.scan_11_widget       = self.findChild(QWidget,        "scan_11_widget"       )
        self.scan_12_widget       = self.findChild(QWidget,        "scan_12_widget"       )
        self.scan_13_widget       = self.findChild(QWidget,        "scan_13_widget"       )
        self.scan_14_widget       = self.findChild(QWidget,        "scan_14_widget"       )
        self.scan_15_widget       = self.findChild(QWidget,        "scan_15_widget"       )
        self.scan_16_widget       = self.findChild(QWidget,        "scan_16_widget"       )
        self.scan_17_widget       = self.findChild(QWidget,        "scan_17_widget"       )
        self.scan_18_widget       = self.findChild(QWidget,        "scan_18_widget"       )
        self.scan_19_widget       = self.findChild(QWidget,        "scan_19_widget"       )
                            # QCheckBox
        self.checkBoxSellectAll   = self.findChild(QCheckBox,      "checkBoxSellectAll"   )
        self.checkBox_1           = self.findChild(QCheckBox,       "checkBox_1"          )
        self.checkBox_2           = self.findChild(QCheckBox,       "checkBox_2"          )
        self.checkBox_3           = self.findChild(QCheckBox,       "checkBox_3"          )
        self.checkBox_4           = self.findChild(QCheckBox,       "checkBox_4"          )
        self.checkBox_5           = self.findChild(QCheckBox,       "checkBox_5"          )
        self.checkBox_6           = self.findChild(QCheckBox,       "checkBox_6"          )
        self.checkBox_7           = self.findChild(QCheckBox,       "checkBox_7"          )
        self.checkBox_8           = self.findChild(QCheckBox,       "checkBox_8"          )
        self.checkBox_9           = self.findChild(QCheckBox,       "checkBox_9"          )
        self.checkBox_10          = self.findChild(QCheckBox,       "checkBox_10"         )
        self.checkBox_11          = self.findChild(QCheckBox,       "checkBox_11"         )
        self.checkBox_12          = self.findChild(QCheckBox,       "checkBox_12"         )
        self.checkBox_13          = self.findChild(QCheckBox,       "checkBox_13"         )
        self.checkBox_14          = self.findChild(QCheckBox,       "checkBox_14"         )
        self.checkBox_15          = self.findChild(QCheckBox,       "checkBox_15"         )
        self.checkBox_16          = self.findChild(QCheckBox,       "checkBox_16"         )
        self.checkBox_17          = self.findChild(QCheckBox,       "checkBox_17"         )
        self.checkBox_18          = self.findChild(QCheckBox,       "checkBox_18"         )
        self.checkBox_19          = self.findChild(QCheckBox,       "checkBox_19"         )

                            # QStackedWidget
        self.pagesStackedWidget   = self.findChild(QStackedWidget, "pagesStackedWidget"   )
                            # QLabel
        self.logedInUserLabel     = self.findChild(QLabel,          "logedInUserLabel"    )
        self.cyberScopeLabel      = self.findChild(QLabel,          "cyberScopeLabel"     )
        self.newFolderLbel        = self.findChild(QLabel,          "newFolderLbel"       )
        self.myScansLabel         = self.findChild(QLabel,          "myScansLabel"        )
                            # QPushButton
        self.createNewScan_btn    = self.findChild(QPushButton,     "createNewScan_btn"   )
        self.cancelSetting_btn    = self.findChild(QPushButton,     "cancelSetting_btn"   )
        self.saveSetting_btn      = self.findChild(QPushButton,     "saveSetting_btn"     )
        self.scansTopBar_btn      = self.findChild(QPushButton,     "scansTopBar_btn"     )
        self.logedUser_btn        = self.findChild(QPushButton,     "logedUser_btn"       )
        self.newFolder_btn        = self.findChild(QPushButton,     "newFolder_btn"       )
        self.myAccount_btn        = self.findChild(QPushButton,     "myAccount_btn"       )
        self.allScans_btn         = self.findChild(QPushButton,     "allScans_btn"        )
        self.myScans_btn          = self.findChild(QPushButton,     "myScans_btn"         )
        self.newScan_btn          = self.findChild(QPushButton,     "newScan_btn"         )
        self.OWASP_btn_1          = self.findChild(QPushButton,     "OWASP_btn_1"         )
        self.OWASP_btn_2          = self.findChild(QPushButton,     "OWASP_btn_2"         )
        self.OWASP_btn_3          = self.findChild(QPushButton,     "OWASP_btn_3"         )
        self.cancel_btn           = self.findChild(QPushButton,     "cancel_btn"          )
        self.about_btn            = self.findChild(QPushButton,     "about_btn"           )
        self.trash_btn            = self.findChild(QPushButton,     "trash_btn"           )
        self.back_btn             = self.findChild(QPushButton,     "back_btn"            )
                            # QLineEdit
        self.currentPasswordInput = self.findChild(QLineEdit,       "currentPasswordInput")
        self.newPasswordInput     = self.findChild(QLineEdit,       "newPasswordInput"    )
        self.fullNameInput        = self.findChild(QLineEdit,       "fullNameInput"       )
        self.targetInput          = self.findChild(QLineEdit,       "targetInput"         )
        self.searchInput          = self.findChild(QLineEdit,       "searchInput"         )
        self.emailInput           = self.findChild(QLineEdit,       "emailInput"          )
        self.nameInput            = self.findChild(QLineEdit,       "nameInput"           )
                            # QTabWidget
        self.tabWidgetForInputs   = self.findChild(QTabWidget,      "tabWidgetForInputs"  )
        self.accountSettingTab    = self.findChild(QTabWidget,      "accountSettingTab"   )
        self.overviewTab          = self.findChild(QTabWidget,      "overviewTab"         )
                            # QTextEdit
        self.descriptionInput     = self.findChild(QTextEdit,       "descriptionInput"    )
                            # QGridLayout
        self.gridLayout_8         = self.findChild(QGridLayout,     "gridLayout_8"        )
        self.gridLayout_9         = self.findChild(QGridLayout,     "gridLayout_9"        )
        self.gridLayout_18        = self.findChild(QGridLayout,     "gridLayout_18"       )
                            # QComboBox
        self.folderInput          = self.findChild(QComboBox,       "folderInput"         )
                            # QScrollArea
        self.scrollArea           = self.findChild(QScrollArea,     "scrollArea"          )
                            # QToolButton
        self.save_btn             = self.findChild(QToolButton,     "save_btn"            )


                            # Buttons Section
        self.createNewScan_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(1))
        self.myAccount_btn.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(7))
        self.newScan_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(1))
        self.about_btn.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(8))

        self.OWASP_btn_1.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(2))
        self.OWASP_btn_2.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(2))
        self.OWASP_btn_3.clicked.connect(lambda:self.pagesStackedWidget.setCurrentIndex(2))


        self.newFolder_btn.clicked.connect(self.AddNewFolderWindow)
        self.settingsTopBar_btn.clicked.connect(self.settingPage)
        self.scansTopBar_btn.clicked.connect(self.scansTopBar)
        self.allScans_btn.clicked.connect(self.clicked_btn)
        self.myScans_btn.clicked.connect(self.clicked_btn)
        self.save_btn.clicked.connect(self.save_scan)

        self.myScans_btn.click()
        self.pagesStackedWidget.currentChanged.connect(self.on_page_changed)



                            # called Func Section
        DB.craet_all_tables()
        self.addTabSpace()
        self.center_on_screen()        
        self.addBtns(DB.select_all_data())
        self.show()
        self.showMaximized()

    def save_scan(self):
        validate_nameInput  = False
        validate_targetInput = False
        if len(self.nameInput.text().strip()) == 0:
            self.nameInput.setToolTip("Field cannot be empty!")
            self.nameInput.setStyleSheet('border: 1px solid red;background-color: white;')
        elif DB.value_exists_in_column(self.nameInput.text().strip()):
            self.nameInput.setToolTip("Scan name already exists try another name!")
            self.nameInput.setStyleSheet('border: 1px solid red;background-color: white;')      
        else:
            self.nameInput.setStyleSheet('background-color: white;border: 1px solid black;')
            validate_nameInput = True

        if self.is_valid_input(self.targetInput.text()) and len(self.targetInput.text().strip()) != 0:
            self.targetInput.setStyleSheet('background-color: white;border: 1px solid black;')
            validate_targetInput = True
        else:
            self.targetInput.setToolTip("Please Enter Valid Target Like : 192.168.1.3 or URL or Link or example.com") 
            self.targetInput.setStyleSheet('border: 1px solid red;background-color: white;')

        if validate_nameInput and validate_targetInput:
            DB.insert_scan_info_data(self.nameInput.text(), self.descriptionInput.toPlainText(), self.folderInput.currentText(), self.targetInput.text())
            btn = self.find_button_by_text(self.folderInput.currentText())
            self.nameInput.setText('')
            self.descriptionInput.setPlainText('')
            self.folderInput.setCurrentText('')
            self.targetInput.setText('')
            btn.click()

    def find_button_by_text(self, target_text):
        for child in self.sidBar.findChildren(QPushButton):
            if child.text().strip() == target_text:
                return child
        return None

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
            data = DB.select_all_data()
            for i in data:
                self.folderInput.addItem(i[1])
        elif index == 7:
            self.back_btn.setText("< back to My Scans")
            self.back_btn.clicked.connect(self.scansTopBar)
            self.myScansLabel.setText("Test.com")

    def settingPage(self):
        self.pagesStackedWidget.setCurrentIndex(7)
        all_buttons = self.sidBar.findChildren(QPushButton)
        for button in all_buttons:
            button.hide()
        self.newFolder_btn.hide()
        self.newScan_btn.hide()
        self.foldersLabel.setText("     SETTINGS")
        self.myAccount_btn.show()
        self.about_btn.show()
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

            self.new_btn.setStyleSheet('QPushButton:checked{border-left: 5px solid rgb(63, 174, 73);background-color: rgb(222, 222, 222);color: black;border-radius: 5px;height: 40px;font-size: 15px;text-align: left;}QPushButton{height: 40px;font-size: 15px;border: none;text-align: left;}QPushButton:hover{background-color: rgb(38, 55, 70);color: rgb(255, 255, 255);}')
            self.new_btn.clicked.connect(self.clicked_btn)

            index = self.gridLayout_9.indexOf(self.allScans_btn)
            self.gridLayout_9.addWidget(self.new_btn, self.gridLayout_9.rowCount() , 0)
            self.gridLayout_9.addWidget(self.trash_btn, self.gridLayout_9.rowCount() + 1, 0)

    def clicked_btn(self):
        btn = self.sender()

        self.myScansLabel.setText(btn.text().strip())

        self.myAccount_btn.hide()
        self.about_btn.hide()
        if btn.objectName() == "allScans_btn":
            self.pagesStackedWidget.setCurrentIndex(3)
            self.create_table_scans("All")
        elif DB.get_scans_menu_columns_by_folder(btn.objectName()): # if find any scan for this folder
            self.pagesStackedWidget.setCurrentIndex(3)
            self.create_table_scans(btn.objectName())
        else:
            self.pagesStackedWidget.setCurrentIndex(0)             # if not find any scan for this folder

    def create_table_scans(self, folderName):    
        ParintLayout = QGridLayout()         #######> this is the main layout that all windget inside it 
        main_v_layout = QVBoxLayout()  # create virtival layout to add all widget virticaly and set it as main layout for main widget 
        main_v_layout.setSpacing(0)
        ParintLayout.setContentsMargins(0, 0, 0, 0)

        h_layout = QHBoxLayout()
        checkbox = QCheckBox()
        name_label = QLabel("Name")
        checkbox.setStyleSheet('border-left: none;border-right: none; ')
        name_label.setStyleSheet('border-left: none;border-right: none; ')

        h_layout.addWidget(checkbox, 0)
        h_layout.addWidget(name_label, 1)
        h_layout.setSpacing(20)

        h_layout2 = QHBoxLayout()
        schedule_label = QLabel("Schedule")
        lastModify_label = QLabel("Last Modify")
        schedule_label.setStyleSheet('border-left: none;border-right: none; ')
        lastModify_label.setStyleSheet('border-left: none;border-right: none; ')

        h_layout2.addWidget(schedule_label, 7)
        h_layout2.addWidget(lastModify_label, 2)

        main_layout = QGridLayout()
        main_layout.setContentsMargins(10, 0, 100, 0)
        btn1 = QPushButton("x")
        btn2 = QPushButton("/")

        main_layout.addLayout(h_layout, 0, 0)
        main_layout.addLayout(h_layout2, 0, 1)
        self.widget_2 = QWidget(self)
        self.widget_2.setStyleSheet(f'background-color: rgb(30,50,30);')
        self.widget_2.setStyleSheet("border: 1px solid rgb(221, 221, 221); height: 35px; background-color: rgb(245, 245, 245);font-size: 13px; font-weight: bold;")
        self.widget_2.setLayout(main_layout)  # set layout of widget_2 with his elements

        main_v_layout.addLayout(ParintLayout)
        main_v_layout.addWidget(self.widget_2)
        
        if folderName == "All":
            data = DB.get_scans_menu_values()
        else:
            data = DB.get_scans_menu_columns_by_folder(folderName)
        self.child_checkboxes = []
        for i in data:    
            h_layout = QHBoxLayout()
            child_checkbox = QCheckBox()
            name_label = QLabel(f"{i[0]}")
            child_checkbox.setStyleSheet('border-left: none;border-right: none; ')
            name_label.setStyleSheet('border-left: none;border-right: none; ')

            h_layout.addWidget(child_checkbox, 0)
            h_layout.addWidget(name_label, 1)
            h_layout.setSpacing(20)
            self.child_checkboxes.append(child_checkbox)

            h_layout2 = QHBoxLayout()
            schedule_label = QLabel(f"       {i[1]}")
            label_text = f'<span style="font-weight:600; display:inline-block; white-space:nowrap;font-size: 20px; ">&nbsp;&nbsp;🗸</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-weight:600; font-size: 13px;">{i[2]}</span>'
            lastModify_label = QLabel(f"{label_text}")
            # lastModify_label = QLabel("🗸      Label 3")
            schedule_label.setStyleSheet('border-left: none;border-right: none; ')
            lastModify_label.setStyleSheet('border-left: none;border-right: none; ')

            h_layout2.addWidget(schedule_label, 7)
            h_layout2.addWidget(lastModify_label, 2)

            main_layout = QGridLayout()
            main_layout.setContentsMargins(10, 0, 20, 0)
            btn1 = QPushButton("►")
            btn2 = QPushButton("X")
            btn2.setStyleSheet('''
                QPushButton:hover{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(165, 165, 165);}
                QPushButton{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(217, 217, 217);}
                ''')
            btn1.setStyleSheet("""
                QPushButton:hover{border-left: none;border-right: none; font-size: 17px;color: rgb(165, 165, 165); margin-left: 52px;}
                QPushButton {border-left: none;border-right: none; font-size: 17px;color: rgb(217, 217, 217); margin-left: 52px;}
                """)
            font = QFont("Sitka Subheading Semibold")
            btn2.setFont(font)

            btn2.setObjectName(f"{i[0]}_btn2")
            btn1.setObjectName(f"{i[0]}_btn1")
            child_checkbox.setObjectName(f"{i[0]}_checkbox")

            btn2.clicked.connect(self.button_clicked)
            btn1.clicked.connect(self.button_clicked)

            main_layout.addWidget(btn1, 0, 2)
            main_layout.addWidget(btn2, 0, 3)
            main_layout.addLayout(h_layout, 0, 0)
            main_layout.addLayout(h_layout2, 0, 1)
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

        checkbox.stateChanged.connect(self.mark_all_children)

    def button_clicked(self):
        sender = self.sender()  # Get the object that triggered the event
        print("Clicked button:", sender.objectName())

    def mark_all_children(self, state):
        for checkbox in self.child_checkboxes:
            checkbox.setChecked(state == 2)  # state == 2 means checked

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
            DB.insert_folder_name(dialog.line_edit.text().strip())
            self.addBtns([(1,dialog.line_edit.text().strip())])
            self.folderInput.addItem(dialog.line_edit.text().strip())

    def deleteButton(self, button):
        value_to_delete = button.objectName()
        index = self.folderInput.findText(value_to_delete)
        if index != -1:
            self.folderInput.removeItem(index)

        DB.delete_scans_menu_rows_by_folder(button.objectName())
        button.deleteLater()

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

            DB.rename_folder(button.objectName(),dialog.line_edit.text().strip())
            button.setObjectName(dialog.line_edit.text().strip())
            button.setText(f"        {dialog.line_edit.text().strip()}")

    def showContextMenu(self, pos, button, menu):
        global_pos = button.mapToGlobal(pos)
        menu.exec_(global_pos)
    def addTabSpace(self):
        all_buttons = self.sidBar.findChildren(QPushButton)
        for button in all_buttons:
            button.setText(f"        {button.text()}")
            button.setContextMenuPolicy(3)
    def load_stylesheet(self, filename):
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