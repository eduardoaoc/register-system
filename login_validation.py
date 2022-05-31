from genericpath import exists
import sqlite3
from PyQt5 import  uic,QtWidgets
import PyQt5

banco= sqlite3.connect('new.db')
cursor= banco.cursor()

def singIn():
    login.label_2.setText("")
    user= login.lineEdit.text()
    password= login.lineEdit_2.text()
    banco= sqlite3.connect('new.db')
    cursor= banco.cursor()
    try:
        cursor.execute(f"SELECT password FROM users WHERE login ='{user}'")
        password_bd= cursor.fetchall()
        print(password_bd[0][0])
        banco.close()
    except:
        login.label_2.setText("INCORRECT DATA") 

    if password == password_bd[0][0]:
        login.close()
        sucess_login.show()
    elif password != password_bd[0][0]:    
        login.label_2.setText("INCORRECT DATA")


def loginSucess():
    sucess_login.show()
    login.hide()


def singUp():
    new_user.show()
    login.hide()

def registerSucess():
    sucess_registered.show()
    new_user.close()
    login.close()    


def newUser():
    name= new_user.lineEdit.text()
    login= new_user.lineEdit_2.text()
    password= new_user.lineEdit_3.text()
    confirm_password= new_user.lineEdit_4.text()
    
    
    if (password == confirm_password) and new_user.checkBox.isChecked():
        try:
            banco= sqlite3.connect('new.db')
            cursor= banco.cursor()
            cursor.execute("INSERT INTO users VALUES ('"+str(name)+"', '"+str(login)+"', '"+str(password)+"','"+str(confirm_password)+"')")
            banco.commit()
            banco.close()
            new_user.close()
            sucess_registered.show()

        except sqlite3.Error as erro:
              new_user.label_2.setText("ERROR ENTERING DATA, TRY AGAIN")  
    elif not new_user.checkBox.isChecked():
        new_user.label_2.setText("ACCEPT THE TERMS")  

    else:
        new_user.label_2.setText("ANY TYPE FIELD IS DIFFERENT")        



def loginFuncion():
    login.label_erro.setText("")
    user= login.lineEdit.text()
    password= login.lineEdit_2.text()
   
    print('User: ', user)
    print('Passowrd: ', password)

    if login.checkBox.isChecked() :
        login.label_erro.setText("SAVE USER")

def exit():
    sucess_registered.close()
    sucess_login.close()
    login.close()
    new_user.close()
    
    


app=QtWidgets.QApplication([])

sucess_login=uic.loadUi('sucess_login.ui')
sucess_registered=uic.loadUi('sucess_registered.ui')
login=uic.loadUi('login.ui')
new_user=uic.loadUi('new_user.ui')

login.pushButton_2.clicked.connect(singIn)
login.pushButton_3.clicked.connect(singUp)

new_user.pushButton_2.clicked.connect(newUser)

sucess_login.pushButton_2.clicked.connect(exit)
sucess_registered.pushButton_2.clicked.connect(exit)



login.show()
app.exec()
