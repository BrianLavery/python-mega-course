from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design_231.kv')

# Inheritance - we create classes to match Kivy rules
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    pass

class MainApp(App):
    # Build is a method of App
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run() # Creating an instance and running


# KIVY HIERARCHY
# 1) App (MainApp)
# 2) ScreenManager (RootWidget)
# 3) Screen (LoginScreen)
# 4) GridLayout -> Text etc.