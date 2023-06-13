# This is the file that we use for the sql managing.
import mysql.connector
from mysql.connector import Error

class Sql_managing:

    def __init__(self,host_name, user_name, user_password):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")


    def sqlconnectionclose(self):
        self.connection.close()

    def createtables(self):
        sql1="""
            use marvertool;"""

        sql2="""CREATE TABLE authorizationTable (
            authorizationID INT AUTO_INCREMENT,
            authorizationName NVARCHAR (50) NOT NULL,
            explanation NVARCHAR (100) NULL,
            PRIMARY KEY (authorizationID)
        )"""

        sql3="""CREATE TABLE settingsTable (
            settingID INT AUTO_INCREMENT PRIMARY KEY,
            settingName NVARCHAR (50) NOT NULL,
            explanation NVARCHAR(100) NULL
        )"""

        sql4="""CREATE TABLE usersTable (
            userID INT AUTO_INCREMENT PRIMARY KEY,
            userName NVARCHAR (50) NOT NULL,
            userLastname NVARCHAR(50) NOT NULL,
            userAuthorityID INT NOT NULL,
            nickName nvarchar(50) NOT NULL,
            userPassword nvarchar(64) NOT NULL,
            mongoDBConnStr nvarchar(255) NOT NULL,
            FOREIGN KEY (userAuthorityID) REFERENCES authorizationTable (authorizationID) ON DELETE CASCADE ON UPDATE CASCADE

        )"""

        sql5="""CREATE TABLE experimentsTable (
            experimentName NVARCHAR (50) PRIMARY KEY,
            experimentTime datetime NOT NULL,
            noOfAttempts int NOT NULL,
            accuracyRate NVARCHAR(50) NOT NULL,
            experimentSettingID int NOT NULL,
            userID int NOT NULL,
            FOREIGN KEY (experimentSettingID) REFERENCES settingsTable (settingID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (userID) REFERENCES usersTable (userID) ON DELETE CASCADE ON UPDATE CASCADE
        )"""
        cursor = self.connection.cursor()

        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)


    def accuracyrate(self,value1):
        cursor = self.connection.cursor()
        sql = ('select accuracyRate from experimentsTable E where E.experimentName=%s' %(value1))
        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def register(self,userName,userLastname,nickName,userPassword,userAuthorityName,mongoDBConnStr):
        insert_stmt = ("INSERT INTO usersTable(userID,userName,userLastname,userAuthorityName,nickName,userPassword,mongoDBConnStr)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        
        data = (userName, userLastname, nickName, userPassword, mongoDBConnStr)
        cursor = self.connection.cursor()

        cursor.execute(insert_stmt, data)
        self.connection.commit()
    
    def getpassword(self,password):
        cursor = self.connection.cursor()
        sql = ("SELECT * from usersTable WHERE nickname=%s" %(password))
        cursor.execute(sql)
        result = cursor.fetchall()

        return result


    def dataimport(self,experimentName,experimentTime,noOfAttempts,accuracyRate,experimentSettingID,userID):
        insert_stmt = ("INSERT INTO experimentsTable(experimentName,experimentTime,noOfAttempts,accuracyRate,experimentSettingID,userID)"
        "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        data = (experimentName, experimentTime, noOfAttempts, accuracyRate, experimentSettingID, userID)
        cursor = self.connection.cursor()

        cursor.execute(insert_stmt, data)
        self.connection.commit()
    
    def datawithdate(self,date):
        sql = ("select experimentName from experimentsTable E where E.experimentTime=%s" %(date))
        cursor = self.connection.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        return result
