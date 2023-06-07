from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import gestor
#importamos otras funciones
import encriptador

Window.size = (400, 500)


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.label = Label(text="Menú", font_size=30)
        self.layout.add_widget(self.label)

        self.encrypt_button = Button(text="Gestor de Contraseñas", font_size=24)
        self.encrypt_button.bind(on_release=self.go_to_hello_world_1)
        self.layout.add_widget(self.encrypt_button)

        self.password_button = Button(text="Encriptar", font_size=24)
        self.password_button.bind(on_release=self.go_to_hello_world_2)
        self.layout.add_widget(self.password_button)

        self.quit_button = Button(text="Salir", font_size=24)
        self.quit_button.bind(on_release=self.quit_app)
        self.layout.add_widget(self.quit_button)

        self.add_widget(self.layout)

    def go_to_hello_world_1(self, button):
        self.manager.current = "hello_world_1"

    def go_to_hello_world_2(self, button):
        self.manager.current = "hello_world_2"

    def quit_app(self, button):
        App.get_running_app().stop()
        Window.close()


class HelloWorld2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.label = Label(text="Hello World 2", font_size=30)
        self.layout.add_widget(self.label)

        self.back_button = Button(text="Volver al Menú", font_size=24)
        self.back_button.bind(on_release=self.go_to_menu)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def go_to_menu(self, button):
        self.manager.current = "menu"


class CipherApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.menu_screen = MenuScreen(name="menu")
        self.hello_world_1_screen = gestor.PasswordManagerApp(name="hello_world_1")
        self.hello_world_2_screen = encriptador.CipherApp(name="hello_world_2")

        self.screen_manager.add_widget(self.menu_screen)
        self.screen_manager.add_widget(self.hello_world_1_screen)
        self.screen_manager.add_widget(self.hello_world_2_screen)

        return self.screen_manager


if __name__ == "__main__":
    CipherApp().run()
