from PyQt5.QtWidgets import QApplication,QStackedWidget,QDialog, QTableWidgetItem
import sys
from PyQt5 import QtWidgets
import PyQt5.QtCore as QtCore
from PyQt5 import QtGui
import pprint
from MongoClient import Mongo_Client
from Sql_Managing  import *
import os


class WelcomeScreen(QDialog):

    def __init__(self) -> None:
        super(WelcomeScreen,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.Log_in_button.clicked.connect(self.go_to_login)
        self.sign_up_button.clicked.connect(self.go_to_signup)

    
    def go_to_login(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_signup(self):
        signup = Sign_up()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1229, 779)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1231, 781))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
        "background-color:rgb(46,52,50);}")
        self.bgwidget.setObjectName("bgwidget")
        self.welcome_label = QtWidgets.QLabel(self.bgwidget)
        self.welcome_label.setGeometry(QtCore.QRect(530, 170, 161, 51))
        self.welcome_label.setStyleSheet("font: 75 36pt \"Ubuntu Condensed\";")
        self.welcome_label.setObjectName("welcome_label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 280, 351, 41))
        self.label_2.setStyleSheet("\n"
        "font: 75 23pt \"Ubuntu Condensed\";\n"
        "color: rgb(238, 238, 236);")
        self.label_2.setObjectName("label_2")
        self.Log_in_button = QtWidgets.QPushButton(self.bgwidget)
        self.Log_in_button.setGeometry(QtCore.QRect(490, 380, 241, 51))
        self.Log_in_button.setStyleSheet("border-radius:20px;\n"
        "font: 75 18pt \"Ubuntu Condensed\";\n"
        "background-color: rgb(85, 87, 83);")
        self.Log_in_button.setObjectName("Log_in_button")
        self.sign_up_button = QtWidgets.QPushButton(self.bgwidget)
        self.sign_up_button.setGeometry(QtCore.QRect(490, 470, 241, 51))
        self.sign_up_button.setStyleSheet("border-radius:20px;\n"
        "font: 75 18pt \"Ubuntu Condensed\";\n"
        "background-color: rgb(85, 87, 83);")
        self.sign_up_button.setObjectName("sign_up_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome_label.setText(_translate("Dialog", "Welcome "))
        self.label_2.setText(_translate("Dialog", "Sign in or create a new account"))
        self.Log_in_button.setText(_translate("Dialog", "LOG IN"))
        self.sign_up_button.setText(_translate("Dialog", "CREATE NEW ACCOUNT"))


class LoginScreen(QDialog):
    def __init__(self) -> None:
        super(LoginScreen,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.Log_in_button.clicked.connect(self.login_function)

    def getuser():
        return inuser

    def login_function(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if (password == sql.getpassword(username)[0]):
            global inuser
            inuser = username
            global manage 
            manage= Sql_managing('localhost','marver','marvermarver')
            #user_ıd = manage.getuserid(inuser)######################################################################################
            main = main_page()
            widget.addWidget(main)
            widget.setCurrentIndex(widget.currentIndex()+1)
            
        elif len(username) == 0 and len(password) == 0:
            self.warning_label.setText("Please fill up all the lines")
        else:
            self.warning_label.setText("Your informations are not correct")

    

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1229, 779)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1231, 781))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
        "background-color:rgb(46,52,50);}")
        self.bgwidget.setObjectName("bgwidget")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 190, 361, 41))
        self.label_2.setStyleSheet("\n"
        "font: 75 23pt \"Ubuntu Condensed\";\n"
        "color: rgb(238, 238, 236);")
        self.label_2.setObjectName("label_2")
        self.Log_in_button = QtWidgets.QPushButton(self.bgwidget)
        self.Log_in_button.setGeometry(QtCore.QRect(500, 500, 241, 51))
        self.Log_in_button.setStyleSheet("border-radius:20px;\n"
        "font: 75 18pt \"Ubuntu Condensed\";\n"
        "background-color: rgb(85, 87, 83);")
        self.Log_in_button.setObjectName("Log_in_button")
        self.username_field = QtWidgets.QLineEdit(self.bgwidget)
        self.username_field.setGeometry(QtCore.QRect(490, 330, 271, 41))
        self.username_field.setStyleSheet("background-color:rgba(47,13,29,0.2);")
        self.username_field.setObjectName("username_field")
        self.password_field = QtWidgets.QLineEdit(self.bgwidget)
        self.password_field.setGeometry(QtCore.QRect(490, 420, 271, 41))
        self.password_field.setStyleSheet("background-color:rgba(47,13,29,0.2);")
        self.password_field.setObjectName("password_field")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(490, 310, 71, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 400, 67, 17))
        self.label_3.setObjectName("label_3")
        self.warning_label = QtWidgets.QLabel(self.bgwidget)
        self.warning_label.setGeometry(QtCore.QRect(490, 470, 271, 17))
        self.warning_label.setStyleSheet("color: rgb(164, 30, 0);\n"
        "font: italic 11pt \"Ubuntu Condensed\";")
        self.warning_label.setText("")
        self.warning_label.setObjectName("warning_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Sign in to your existing account"))
        self.Log_in_button.setText(_translate("Dialog", "LOG IN"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)


class Sign_up(QDialog):
    def __init__(self) -> None:
        super(Sign_up,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.Sign_up_button.clicked.connect(self.sign_up_clicked)
        self.user_radio_button.setChecked(True)


    def sign_up_clicked(self):

        global user_name
        user_name = self.username_field.text()
        global password 
        password = self.password_field.text()
        name = self.name_field.text()
        last_name = self.last_name_field.text()
        global type_of_user 
        if(self.user_radio_button.isChecked()):
            type_of_user = "user"
        else:
            type_of_user = "admin"

        sql.register(name,last_name,user_name,password,1,"mongodb://localhost:27017")

        main = main_page()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1229, 781)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1231, 781))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    color: rgb(204, 0, 0);\n"
"background-color:rgb(46,52,50);}")
        self.bgwidget.setObjectName("bgwidget")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 120, 351, 41))
        self.label_2.setStyleSheet("\n"
"font: 75 23pt \"Ubuntu Condensed\";\n"
"color: rgb(238, 238, 236);")
        self.label_2.setObjectName("label_2")
        self.Sign_up_button = QtWidgets.QPushButton(self.bgwidget)
        self.Sign_up_button.setGeometry(QtCore.QRect(500, 670, 241, 51))
        self.Sign_up_button.setStyleSheet("border-radius:20px;\n"
"font: 75 18pt \"Ubuntu Condensed\";\n"
"background-color: rgb(85, 87, 83);")
        self.Sign_up_button.setObjectName("Sign_up_button")
        self.username_field = QtWidgets.QLineEdit(self.bgwidget)
        self.username_field.setGeometry(QtCore.QRect(490, 190, 271, 41))
        self.username_field.setStyleSheet("background-color:rgba(47,13,29,0.2);")
        self.username_field.setObjectName("username_field")
        self.password_field = QtWidgets.QLineEdit(self.bgwidget)
        self.password_field.setGeometry(QtCore.QRect(490, 440, 271, 41))
        self.password_field.setStyleSheet("background-color:rgba(47,13,29,0.2);")
        self.password_field.setObjectName("password_field")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(490, 170, 71, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 420, 67, 17))
        self.label_3.setObjectName("label_3")
        self.warning_label = QtWidgets.QLabel(self.bgwidget)
        self.warning_label.setGeometry(QtCore.QRect(490, 470, 271, 17))
        self.warning_label.setStyleSheet("color: rgb(164, 0, 0);\n"
"font: italic 11pt \"Ubuntu Condensed\";")
        self.warning_label.setText("")
        self.warning_label.setObjectName("warning_label")
        self.password_field_confirm = QtWidgets.QLineEdit(self.bgwidget)
        self.password_field_confirm.setGeometry(QtCore.QRect(490, 520, 271, 41))
        self.password_field_confirm.setStyleSheet("background-color:rgba(47,13,29,0.2);")
        self.password_field_confirm.setObjectName("password_field_confirm")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 500, 131, 17))
        self.label_4.setObjectName("label_4")
        self.admin_radio_button = QtWidgets.QRadioButton(self.bgwidget)
        self.admin_radio_button.setGeometry(QtCore.QRect(560, 570, 141, 23))
        self.admin_radio_button.setObjectName("admin_radio_button")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.admin_radio_button)
        self.user_radio_button = QtWidgets.QRadioButton(self.bgwidget)
        self.user_radio_button.setGeometry(QtCore.QRect(560, 600, 131, 23))
        self.user_radio_button.setObjectName("user_radio_button")
        self.buttonGroup.addButton(self.user_radio_button)
        self.name_field = QtWidgets.QLineEdit(self.bgwidget)
        self.name_field.setGeometry(QtCore.QRect(490, 270, 271, 41))
        self.name_field.setStyleSheet("background-color:rgba(47,13,29,0.2);")
        self.name_field.setObjectName("name_field")
        self.last_name_field = QtWidgets.QLineEdit(self.bgwidget)
        self.last_name_field.setGeometry(QtCore.QRect(490, 350, 271, 41))
        self.last_name_field.setStyleSheet("background-color:rgba(47,13,29,0.2);")
        self.last_name_field.setObjectName("last_name_field")
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 250, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 330, 71, 17))
        self.label_6.setObjectName("label_6")
        self.warnig_label = QtWidgets.QLabel(self.bgwidget)
        self.warnig_label.setGeometry(QtCore.QRect(490, 630, 271, 17))
        self.warnig_label.setStyleSheet("color: rgb(204, 0, 0);")
        self.warnig_label.setText("")
        self.warnig_label.setObjectName("warnig_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", " Register a brand new account"))
        self.Sign_up_button.setText(_translate("Dialog", "SIGN UP"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.label_4.setText(_translate("Dialog", "Confirm Password"))
        self.admin_radio_button.setText(_translate("Dialog", "Register as admin"))
        self.user_radio_button.setText(_translate("Dialog", "Register as user"))
        self.label_5.setText(_translate("Dialog", "Name"))
        self.label_6.setText(_translate("Dialog", "Last Name"))
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field_confirm.setEchoMode(QtWidgets.QLineEdit.Password)


class main_page(QDialog):

    def __init__(self) -> None:
        super(main_page,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.user_name = user_name
        self.password = password
        self.userAuthorityName = userAuthorityName
        self.data_visulazation_button.clicked.connect(self.statistics_clicked)
        self.add_experiment.clicked.connect(self.add_experiment_function)
        self.settings_button.clicked.connect(self.settings_button_clicked)
        self.model = QtGui.QStandardItemModel()
        self.list_data_from_mongodb.setModel(self.model)
        self.printer = pprint.PrettyPrinter()
        self.experiment_tables()
        if(userAuthorityName == "user"):
            self.add_experiment.hide()
        

    def settings_button_clicked(self):
        settings_page = Settings()
        widget.addWidget(settings_page)
        widget.setCurrentIndex(widget.currentIndex()+1)  


    def statistics_clicked(self):
        statistics_page = statistics()
        widget.addWidget(statistics_page)
        widget.setCurrentIndex(widget.currentIndex()+1)    

    def add_experiment_function(self):
        fname  = QtWidgets.QFileDialog.getOpenFileName(self,'Select File','/home ',"Txt Files(*.txt)")

        filename = fname[0]
        pathname,extension =os.path.splitext(filename)
        filename = pathname.split('/')

        client.change_collection("experiment_%s"%(filename[-1]))#%s yanına tırnak ekle hata çıkarsa
        print(client.collection.name)


        client.insert_documents_from_txt(fname[0])
        #acc = manage.accuracy_calculator(client.collection.name)
        #manage.dataimport(client.collection.name, manage.gettime(),manage.gettotal(),acc,1,manage.getuserid(inuser))

        self.experiment_tables()


    
    def experiment_tables(self):

        self.model.clear()
        self.collections_list.setRowCount(len(client.list_collections()))
        row = 0
        for collection in client.list_collections():
            self.collections_list.setItem(row,0,QTableWidgetItem(collection))
            self.collections_list.setItem(row,1,QTableWidgetItem("date"))
            self.collections_list.setItem(row,2,QTableWidgetItem("Time"))
            row = row + 1
        

    def list_experiment_variables(self):
        x = 1
        for document in client.find_documents():
            self.model.appendRow(QtGui.QStandardItem(str(x) + "\n" + self.printer.pformat(document)+"\n\n"))
            x = x+1


    def experiment_clicked(self,item):
        self.label_2.setText(item.text())
        if(client.list_collections().count(item.text())):
            client.change_collection(item.text())
        self.model.clear()
        self.list_experiment_variables()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1227, 779)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1231, 781))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:rgb(46,52,50);}")
        self.bgwidget.setObjectName("bgwidget")
        self.profile_button = QtWidgets.QPushButton(self.bgwidget)
        self.profile_button.setGeometry(QtCore.QRect(1110, 10, 89, 25))
        self.profile_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.profile_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.profile_button.setObjectName("profile_button")
        self.control_panel_button = QtWidgets.QPushButton(self.bgwidget)
        self.control_panel_button.setGeometry(QtCore.QRect(20, 10, 101, 25))
        self.control_panel_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.control_panel_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.control_panel_button.setObjectName("control_panel_button")
        self.list_data_from_mongodb = QtWidgets.QListView(self.bgwidget)
        self.list_data_from_mongodb.setGeometry(QtCore.QRect(10, 390, 881, 381))
        self.list_data_from_mongodb.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(186, 189, 182);\n"
"font: 13pt \"Ubuntu Condensed\";")
        self.list_data_from_mongodb.setObjectName("list_data_from_mongodb")
        self.statistics_button = QtWidgets.QPushButton(self.bgwidget)
        self.statistics_button.setGeometry(QtCore.QRect(130, 10, 101, 25))
        self.statistics_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.statistics_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.statistics_button.setObjectName("statistics_button")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(520, 10, 171, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 23pt \"KacstBook\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(1020, 370, 91, 17))
        self.label_3.setObjectName("label_3")
        self.add_experiment = QtWidgets.QPushButton(self.bgwidget)
        self.add_experiment.setGeometry(QtCore.QRect(20, 240, 211, 51))
        self.add_experiment.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"font: 75 italic 15pt \"Ubuntu Condensed\";")
        self.add_experiment.setObjectName("add_experiment")
        self.collections_list = QtWidgets.QTableWidget(self.bgwidget)
        self.collections_list.setGeometry(QtCore.QRect(900, 390, 311, 381))
        self.collections_list.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(186, 189, 182);\n"
"font: 13pt \"Ubuntu Condensed\";")
        self.collections_list.setObjectName("collections_list")
        self.collections_list.setColumnCount(2)
        self.collections_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.collections_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.collections_list.setHorizontalHeaderItem(1, item)
        self.settings_button = QtWidgets.QPushButton(self.bgwidget)
        self.settings_button.setGeometry(QtCore.QRect(240, 10, 101, 25))
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.settings_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.settings_button.setObjectName("settings_button")
        self.collections_list.itemClicked.connect(self.experiment_clicked)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.profile_button.setText(_translate("Dialog", "Profile"))
        self.control_panel_button.setText(_translate("Dialog", "Control Panel"))
        self.statistics_button.setText(_translate("Dialog", "Statistics"))
        self.label.setText(_translate("Dialog", "MARverDB"))
        self.label_3.setText(_translate("Dialog", "Experiments"))
        self.add_experiment.setText(_translate("Dialog", "Add Experiment"))
        item = self.collections_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.collections_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Date"))
        self.settings_button.setText(_translate("Dialog", "Settings"))



class statistics(QDialog):
    def __init__(self) -> None:
        super(statistics,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.model = QtGui.QStandardItemModel()
        self.experiment_tables()
        self.control_panel_button.clicked.connect(self.control_panel_button_clicked)

    
    def control_panel_button_clicked(self):
        main = main_page()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def experiment_clicked(self,item):
        self.x_key.clear()
        self.y_key.clear()
        if(client.list_collections().count(item.text())):
            client.change_collection(item.text())
        keys = client.return_keys()
        self.x_key.addItems(keys)
        self.y_key.addItems(keys)


    def experiment_tables(self):
        self.collections_list.setRowCount(len(client.list_collections()))
        row = 0
        for collection in client.list_collections():
            self.collections_list.setItem(row,0,QTableWidgetItem(collection))
            self.collections_list.setItem(row,1,QTableWidgetItem("Date"))
            row = row + 1
        


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1227, 788)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1231, 791))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:rgb(46,52,50);}")
        self.bgwidget.setObjectName("bgwidget")
        self.profile_button = QtWidgets.QPushButton(self.bgwidget)
        self.profile_button.setGeometry(QtCore.QRect(1110, 10, 89, 25))
        self.profile_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.profile_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.profile_button.setObjectName("profile_button")
        self.control_panel_button = QtWidgets.QPushButton(self.bgwidget)
        self.control_panel_button.setGeometry(QtCore.QRect(20, 10, 101, 25))
        self.control_panel_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.control_panel_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.control_panel_button.setObjectName("control_panel_button")
        self.statistics_button = QtWidgets.QPushButton(self.bgwidget)
        self.statistics_button.setGeometry(QtCore.QRect(130, 10, 101, 25))
        self.statistics_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.statistics_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.statistics_button.setObjectName("statistics_button")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(520, 10, 171, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 23pt \"KacstBook\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(1070, 170, 91, 17))
        self.label_3.setObjectName("label_3")
        self.collections_list = QtWidgets.QTableWidget(self.bgwidget)
        self.collections_list.setGeometry(QtCore.QRect(1010, 190, 211, 581))
        self.collections_list.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(186, 189, 182);\n"
"font: 13pt \"Ubuntu Condensed\";")
        self.collections_list.setObjectName("collections_list")
        self.collections_list.setColumnCount(2)
        self.collections_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.collections_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.collections_list.setHorizontalHeaderItem(1, item)
        self.x_key = QtWidgets.QComboBox(self.bgwidget)
        self.x_key.setGeometry(QtCore.QRect(120, 380, 86, 25))
        self.x_key.setObjectName("x_key")
        self.y_key = QtWidgets.QComboBox(self.bgwidget)
        self.y_key.setGeometry(QtCore.QRect(300, 380, 86, 25))
        self.y_key.setObjectName("y_key")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 350, 16, 17))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 350, 16, 17))
        self.label_4.setObjectName("label_4")
        self.collections_list.itemClicked.connect(self.experiment_clicked)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.profile_button.setText(_translate("Dialog", "Profile"))
        self.control_panel_button.setText(_translate("Dialog", "Control Panel"))
        self.statistics_button.setText(_translate("Dialog", "Statistics"))
        self.label.setText(_translate("Dialog", "MARverDB"))
        self.label_3.setText(_translate("Dialog", "Experiments"))
        item = self.collections_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.collections_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Date"))
        self.label_2.setText(_translate("Dialog", "X"))
        self.label_4.setText(_translate("Dialog", "Y"))


class Settings(QDialog):
    def __init__(self) -> None:
        super(Settings,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.statistics_button.clicked.connect(self.statistics_clicked)
        self.control_panel_button.clicked.connect(self.control_panel_button_clicked)
        self.add_settings_button.clicked.connect(self.add_settings_button_clicked)
        self.model = QtGui.QStandardItemModel()
        self.list_settings.setModel(self.model)
        self.get_settings()

        
    def add_settings_button_clicked(self):
        settings_name = self.settings_name_field.text()
        settings_explanation = self.settings_explanation_field.text()
        # bu ikisini tabloya atacak sql 
        
    
    def get_settings(self):
        # data = sql query yazın
        
        #x = 1
        #for row in data:
        #   self.model.appendRow(QtGui.QStandardItem("Settings Name: row.settingsName \n Settings Explanation: row.settingsExp"))
        #   x = x+1
        return


    def control_panel_button_clicked(self):
        main = main_page()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def statistics_clicked(self):
        statistics_page = statistics()
        widget.addWidget(statistics_page)
        widget.setCurrentIndex(widget.currentIndex()+1)   


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1227, 779)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1231, 781))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:rgb(46,52,50);}")
        self.bgwidget.setObjectName("bgwidget")
        self.control_panel_button = QtWidgets.QPushButton(self.bgwidget)
        self.control_panel_button.setGeometry(QtCore.QRect(20, 10, 101, 25))
        self.control_panel_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.control_panel_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.control_panel_button.setObjectName("control_panel_button")
        self.list_settings = QtWidgets.QListView(self.bgwidget)
        self.list_settings.setGeometry(QtCore.QRect(10, 490, 1211, 281))
        self.list_settings.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(186, 189, 182);\n"
"font: 13pt \"Ubuntu Condensed\";")
        self.list_settings.setObjectName("list_settings")
        self.statistics_button = QtWidgets.QPushButton(self.bgwidget)
        self.statistics_button.setGeometry(QtCore.QRect(130, 10, 101, 25))
        self.statistics_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.statistics_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.statistics_button.setObjectName("statistics_button")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(520, 10, 171, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 23pt \"KacstBook\";")
        self.label.setObjectName("label")
        self.settings_button = QtWidgets.QPushButton(self.bgwidget)
        self.settings_button.setGeometry(QtCore.QRect(240, 10, 101, 25))
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.settings_button.setStyleSheet("font: 75 italic 11pt \"Ubuntu Condensed\";\n"
"background-color: rgba(85, 87, 83,0.5);\n"
"border-radius:8px;\n"
"border-color: rgb(136, 138, 133);")
        self.settings_button.setObjectName("settings_button")
        self.settings_name_field = QtWidgets.QLineEdit(self.bgwidget)
        self.settings_name_field.setGeometry(QtCore.QRect(40, 100, 113, 25))
        self.settings_name_field.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.settings_name_field.setObjectName("settings_name_field")
        self.settings_explanation_field = QtWidgets.QTextEdit(self.bgwidget)
        self.settings_explanation_field.setGeometry(QtCore.QRect(40, 150, 531, 111))
        self.settings_explanation_field.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.settings_explanation_field.setObjectName("settings_explanation_field")
        self.add_settings_button = QtWidgets.QPushButton(self.bgwidget)
        self.add_settings_button.setGeometry(QtCore.QRect(250, 280, 111, 41))
        self.add_settings_button.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.add_settings_button.setObjectName("add_settings_button")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 460, 101, 20))
        self.label_2.setStyleSheet("font: 75 italic 20pt \"Ubuntu Condensed\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.control_panel_button.setText(_translate("Dialog", "Control Panel"))
        self.statistics_button.setText(_translate("Dialog", "Statistics"))
        self.label.setText(_translate("Dialog", "MARverDB"))
        self.settings_button.setText(_translate("Dialog", "Settings"))
        self.settings_name_field.setPlaceholderText(_translate("Dialog", "Settings Name"))
        self.settings_explanation_field.setPlaceholderText(_translate("Dialog", "Settings Explanation..."))
        self.add_settings_button.setText(_translate("Dialog", "Add settings"))
        self.label_2.setText(_translate("Dialog", "SETTİNGS"))




user_name,password,userAuthorityName = "","",""
sql = Sql_managing("localhost","marver","marvermarver")
client = Mongo_Client()
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
