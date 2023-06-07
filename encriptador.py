from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup

ALGORITHMS = {
    "Cifrado César": "caesar",
    "Cifrado Vigenère": "vigenere"
}

#Window.size = (400, 500)


def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result


def vigenere_cipher(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + ord(key[key_index].upper()) - 2 * 65) % 26 + 65)
            else:
                result += chr((ord(char) + ord(key[key_index].lower()) - 2 * 97) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result


class CipherApp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.label = Label(text="Encriptador", font_size=30)
        self.layout.add_widget(self.label)

        self.algorithm_label = Label(text="Selecciona un algoritmo:", font_size=20)
        self.layout.add_widget(self.algorithm_label)

        self.algorithm_button = Button(text="Seleccione un algoritmo", font_size=18, size_hint=(1, None), height=40)
        self.algorithm_button.bind(on_release=self.show_algorithm_dropdown)
        self.layout.add_widget(self.algorithm_button)

        self.key_label = Label(text="Ingresa la llave:", font_size=20)
        self.layout.add_widget(self.key_label)

        self.key_input = TextInput(multiline=False, font_size=18)
        self.layout.add_widget(self.key_input)

        self.input_label = Label(text="Ingresa el texto:", font_size=20)
        self.layout.add_widget(self.input_label)

        self.input_text = TextInput(multiline=True, font_size=18)
        self.layout.add_widget(self.input_text)

        self.output_label = Label(text="Resultado:", font_size=20)
        self.layout.add_widget(self.output_label)

        self.output_text = TextInput(multiline=True, readonly=True, font_size=18)
        self.layout.add_widget(self.output_text)

        self.encrypt_button = Button(text="Cifrar", size_hint=(1, None), height=40, font_size=18)
        self.encrypt_button.bind(on_release=self.encrypt)
        self.layout.add_widget(self.encrypt_button)

        self.decrypt_button = Button(text="Descifrar", size_hint=(1, None), height=40, font_size=18)
        self.decrypt_button.bind(on_release=self.decrypt)
        self.layout.add_widget(self.decrypt_button)
        
        self.menu_button = Button(text="Menu", font_size=24)
        self.menu_button.bind(on_release=self.go_to_menu)
        self.layout.add_widget(self.menu_button)

        self.dropdown = DropDown()
        self.algorithm_options = []
        for algorithm in ALGORITHMS.keys():
            button = Button(text=algorithm, size_hint_y=None, height=40, font_size=18)
            button.bind(on_release=lambda btn: self.select_algorithm(btn.text))
            self.algorithm_options.append(button)
            self.dropdown.add_widget(button)

        self.add_widget(self.layout)

        self.selected_algorithm = None

    def select_algorithm(self, algorithm):
        self.selected_algorithm = ALGORITHMS.get(algorithm)
        self.algorithm_button.text = algorithm
        self.dropdown.dismiss()

    def show_algorithm_dropdown(self, button):
        self.dropdown.open(button)

    def go_to_menu(self, button):
        self.manager.current = "menu"
        
    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        error_label = Label(text=message, font_size=20)
        ok_button = Button(text="OK", size_hint=(1, None), height=40, font_size=18)
        content.add_widget(error_label)
        content.add_widget(ok_button)
        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(300, 200))
        ok_button.bind(on_release=popup.dismiss)
        popup.open()

    def encrypt(self, button):
        if not self.selected_algorithm:
            self.show_error_popup("Seleccione un algoritmo primero.")
            return

        key = self.key_input.text.strip()
        text = self.input_text.text.strip()

        if not key or not text:
            self.show_error_popup("Ingrese la llave y el texto.")
            return

        result = ""
        if self.selected_algorithm == "caesar":
            result = caesar_cipher(text, int(key))
        elif self.selected_algorithm == "vigenere":
            result = vigenere_cipher(text, key)

        self.output_text.text = result
        
   
                
    def decrypt(self, button):
        if not self.selected_algorithm:
            self.show_error_popup("Seleccione un algoritmo primero.")
            return

        key = self.key_input.text.strip()
        text = self.input_text.text.strip()

        if not key or not text:
            self.show_error_popup("Ingrese la llave y el texto.")
            return

        result = ""
        if self.selected_algorithm == "caesar":
            result = caesar_cipher(text, -int(key))
        elif self.selected_algorithm == "vigenere":
            result = vigenere_cipher(text, key)

        self.output_text.text = result

