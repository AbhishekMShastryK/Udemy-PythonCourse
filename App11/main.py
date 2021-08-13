from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
import json, glob, random
from datetime import datetime
from pathlib import Path
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file ("design.kv")

class LoginScreen (Screen):
    def sign_up(self):
        self.manager.current = "Sign_Up_Screen"
        
    def login (self,u_name,p_word):
        self.manager.transition.direction = "left"
        with open("user_data.json") as file:
            users_data = json.load(file)
        if u_name in users_data and users_data[u_name]['password'] == p_word:
            self.manager.current = "Login_Screen_Success"
        else:
            self.ids.un_login.text = "Wrong username or password"


class SignUpScreen (Screen):
    def add_user (self, u_name, p_word):
        with open("user_data.json") as file:
            users_data = json.load(file)
        
        users_data[u_name] = {"username":u_name,"password":p_word,
        "created":datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        with open("user_data.json", 'w') as file:
            json.dump(users_data, file) 

        self.manager.current = "Sign_Up_Screen_Success"

class SignUpScreenSuccess (Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_Screen"

class LoginScreenSuccess (Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_Screen"

    def get_quote (self,feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
      
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt",encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"

class ImageButton (ButtonBehavior, HoverBehavior, Image ):
    pass

class RootWidget (ScreenManager):
    pass

class MainApp (App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
