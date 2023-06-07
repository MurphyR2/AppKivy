# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 03:53:48 2023

@author: jesus
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class PasswordManagerApp(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.label = Label(text="Gestor de contraseñas", font_size=30)
        self.layout.add_widget(self.label)

        self.add_password_button = Button(text="Agregar Contraseña", font_size=24)
        self.add_password_button.bind(on_release=self.add_password)
        self.layout.add_widget(self.add_password_button)

        self.show_passwords_button = Button(text="Mostrar Contraseñas", font_size=24)
        self.show_passwords_button.bind(on_release=self.show_passwords)
        self.layout.add_widget(self.show_passwords_button)

        self.clear_passwords_button = Button(text="Borrar Contraseñas", font_size=24)
        self.clear_passwords_button.bind(on_release=self.clear_passwords)
        self.layout.add_widget(self.clear_passwords_button)
        
        self.menu_button = Button(text="Menu", font_size=24)
        self.menu_button.bind(on_release=self.go_to_menu)
        self.layout.add_widget(self.menu_button)


        self.add_widget(self.layout)

    def go_to_menu(self, button):
        self.manager.current = "menu"
        
    def add_password(self, button):
        # Aquí puedes implementar la lógica para agregar una contraseña
        print("Contraseña agregada")

    def show_passwords(self, button):
        # Aquí puedes implementar la lógica para mostrar las contraseñas guardadas
        print("Contraseñas guardadas:")

    def clear_passwords(self, button):
        # Aquí puedes implementar la lógica para borrar todas las contraseñas
        print("Contraseñas borradas")

    

