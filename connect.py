import kivy
import mysql.connector
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import mysql.connector
from kivy.uix.popup import Popup

db = mysql.connector.connect(
    db="kivy_test",
    host="localhost",
    user="root",
    password="root"
)

cursor = db.cursor(buffered=True)

class registerScreen(Screen):

    usernameInput = ObjectProperty(None)
    emailInput = ObjectProperty(None)
    passwordInput = ObjectProperty(None)

    def addInfoToDB(self):
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (self.usernameInput.text, self.emailInput.text, self.passwordInput.text)
        cursor.execute(query, values)
        db.commit()
        print(cursor.rowcount, "record inserted.")

class loginScreen(Screen):

    usernameInputLogin = ObjectProperty(None)
    passwordInputLogin = ObjectProperty(None)

    def checkIfDetailsExist(self):
        cursor.execute("SELECT * FROM users")
        fetchInfo = cursor.fetchone()

        if self.usernameInputLogin.text in fetchInfo and self.passwordInputLogin.text in fetchInfo:
            # print("success")
            popup = Popup(title='Test popup', content=Label(text='Hello world'),
              auto_dismiss=False)
            popup.open()
        else:
            # print("fail")
            popup = Popup(title='Test popup', content=Label(text='Hello world'),
              auto_dismiss=False)
            popup.open()



class MyApp(App):
    def build(self):
        Builder.load_file("styles/my.kv")
        sm = ScreenManager()
        sm.add_widget(loginScreen(name='login'))
        sm.add_widget(registerScreen(name='register'))
        return sm


if __name__ == "__main__":
    MyApp().run()