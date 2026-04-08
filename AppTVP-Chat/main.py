from kivy.app import App
import pandas as pd
import joblib
from kivy.core.window import Window 
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from transformers import AutoModelForSequenceClassification, AutoTokenizer, DistilBertConfig
import torch
import threading
import os
import json

# Pantalla principal
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
          super(MainScreen, self).__init__(**kwargs)
          self.orientation = 'vertical'
          self.update_main_content()

          # Cargar modelo y tokenizer para chatbot
          self.model_path = './fine_tuned_tvp_model'
          try:
              self.model = AutoModelForSequenceClassification.from_pretrained(self.model_path, local_files_only=True, dtype=torch.float32)
              self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, local_files_only=True)
              self.model.eval()
              print("Modelo cargado correctamente con from_pretrained.")
          except Exception as e:
              print(f"Error con from_pretrained: {e}. Intentando carga manual...")
              try:
                  # Cargar config manualmente
                  with open(f"{self.model_path}/config.json", 'r') as f:
                      config_dict = json.load(f)
                  print(f"Config dict cargado: {config_dict.keys()}")  # Debug
                  if 'model_type' not in config_dict:
                      raise ValueError("config.json no tiene 'model_type'. Re-descarga el modelo.")
                  config = DistilBertConfig.from_dict(config_dict)
                  
                  # Cargar state_dict con torch.load como alternativa
                  try:
                      state_dict = torch.load(f"{self.model_path}/model.safetensors", map_location='cpu')  # Alternativa a safetensors
                  except:
                      from safetensors.torch import load_file
                      state_dict = load_file(f"{self.model_path}/model.safetensors")
                  
                  # Instanciar modelo
                  self.model = AutoModelForSequenceClassification.from_config(config)
                  self.model.load_state_dict(state_dict)
                  self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, local_files_only=True)
                  self.model.eval()
                  print("Modelo cargado correctamente con carga manual.")
              except Exception as e2:
                  print(f"Error en carga manual: {e2}. Detalles: {str(e2)}")
                  print("Re-descarga el modelo de Colab. Si persiste, usa un modelo preentrenado simple.")
                  self.model = None
                  self.tokenizer = None

          # Estados de checkboxes (mantener para compatibilidad)
          self.checkbox_state = 0
          self.checkbox1_state = 0
          self.checkbox2_state = 0
          self.checkbox3_state = 0
          self.checkbox4_state = 0
          self.checkbox5_state = 0
          self.checkbox6_state = 0
          self.results_list = []

    def update_main_content(self, *args):
          self.clear_widgets()

          with self.canvas:
              Color(1, 0.8, 0.4, 1)
              self.rect = Rectangle(size=self.size, pos=self.pos)

          layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
          title = Label(text='CimaTVPDetect', size_hint_y=None, height=70, color=(0, 0, 0, 1), font_size=25)
          title.text_size = (200, None)
          title.halign = 'center'
          title.valign = 'middle'
          layout.add_widget(title)

          logo = Image(source='images/images1.png', size_hint=(1, 1.0), fit_mode="contain")
          layout.add_widget(logo)

          button = Button(text='EMPEZAR', size_hint_y=None, height=50, size_hint_x=1)
          button.bind(on_press=self.switch_to_second_screen)
          layout.add_widget(button)

          self.add_widget(layout)

    def switch_to_second_screen(self, *args):
        self.clear_widgets()  # Clear existing widgets

        # Cambiar el color de fondo
        with self.canvas:
            Color(1, 0.8, 0.4, 1)  # Color Ocre
            self.rect = Rectangle(size=self.size, pos=self.pos)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)  # Further reduced padding for better positioning

        button = Button(text='REGRESAR', size_hint_y=None, height=50)  # Regresar button
        button.bind(on_press=self.update_main_content)  # Navigate back to MainScreen
        layout.add_widget(button)

        # Título Descripción
        title_desc = Label(text='Descripción de esta aplicación', size_hint_y=None, height=60, color=(0, 0, 0, 1), halign='center', font_size=20)  # Justified text
        title_desc.text_size = (self.width - 100, None)  # Allow text to wrap
        title_desc.size_hint_x = 1  # Ensure it takes full width
        layout.add_widget(title_desc)

        # Texto Descripción
        desc_text = Label(text='Esta aplicación utiliza un cuestionario sencillo y accesible para detectar de forma temprana el riesgo de trombosis venosa profunda (TVP). A través de una serie de preguntas sobre síntomas, y factores de riesgo, la app proporciona un análisis rápido que ayuda a identificar el riesgo de padecerlo y permitirte tomar acciones preventivas a tiempo.', size_hint_y=None, height=240, halign='justify', font_size=18, color=(0, 0, 0, 1))  # Justified text
        desc_text.text_size = (self.width - 100, None)  # Allow text to wrap
        desc_text.size_hint_x = 1  # Ensure it takes full width
        layout.add_widget(desc_text)

        # Título Propósito
        title_purpose = Label(text='Propósito de esta aplicación', size_hint_y=None, height=60, color=(0, 0, 0, 1), halign='center', font_size=20)  # Justified text
        title_purpose.text_size = (self.width - 100, None)  # Allow text to wrap
        title_purpose.size_hint_x = 1  # Ensure it takes full width
        layout.add_widget(title_purpose)

        # Texto Propósito
        purpose_text = Label(text='El propósito de esta aplicación es ofrecer una herramienta de detección temprana para la trombosis venosa profunda, facilitando el diagnóstico precoz y reduciendo el riesgo de complicaciones graves. Su objetivo es promover la salud preventiva al permitir que las personas identifiquen posibles señales de alerta y busquen atención médica adecuada con anticipación.', size_hint_y=None, height=240, halign='justify', font_size=18, color=(0, 0, 0, 1))  # Justified text
        purpose_text.text_size = (self.width - 100, None)  # Allow text to wrap
        purpose_text.size_hint_x = 1  # Ensure it takes full width
        layout.add_widget(purpose_text)

        # Botones
        button1 = Button(text='CONTINUAR', size_hint_y=None, height=50)  # Continuar button
        button1.bind(on_press=self.switch_to_third_screen)  # Navigate to third screen

        layout.add_widget(button1)

        self.add_widget(layout)

    def switch_to_third_screen(self, *args):  # Chatbot con ScrollView mejorado
        self.clear_widgets()

        with self.canvas:
            Color(1, 0.8, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        scroll_view = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.bind(minimum_height=layout.setter('height'))  # Allow the layout to grow
        button = Button(text='REGRESAR', size_hint_y=None, height=50)
        button.bind(on_press=self.switch_to_second_screen)
        layout.add_widget(button)

        title_chat = Label(text='Chatbot de Evaluación de Riesgo de TVP', size_hint_y=None, height=100, color=(0, 0, 0, 1), halign='center', font_size=20)
        title_chat.text_size = (self.width - 100, None)
        title_chat.size_hint_x = 1
        layout.add_widget(title_chat)

        # ScrollView para el chat_log (crece con contenido)
        chat_scroll = ScrollView(size_hint=(1, None), height=475, do_scroll_x=False, do_scroll_y=True)  # Scroll vertical solo
        self.chat_log = Label(text='Chatbot: Hola, qué tal, soy un asistente médico virtual de angiologia.\nDescribe todos los sintomas que tienes, sin omitir alguno para poder dar un Pre-Diagnostico mas certero.', size_hint_y=None, halign='left', valign='top', color=(0, 0, 0, 1))
        self.chat_log.bind(texture_size=self.chat_log.setter('size'))  # Ajusta tamaño al texto
        self.chat_log.text_size = (self.width - 40, None)  # Ancho fijo, altura dinámica
        chat_scroll.add_widget(self.chat_log)
        layout.add_widget(chat_scroll)

        self.input_field = TextInput(hint_text="Ej: Tengo edema y cirugía reciente.", size_hint_y=None, height=50, multiline=False, background_color=(1, 0.8, 0.4, 1))
        layout.add_widget(self.input_field)

        send_button = Button(text='ENVIAR', size_hint_y=None, height=50)
        send_button.bind(on_press=self.process_input)
        layout.add_widget(send_button)

        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)


    def process_input(self, instance):
          user_input = self.input_field.text
          if not user_input.strip():
              return
          self.chat_log.text += f"\nTú: {user_input}"
          self.input_field.text = ""
          
          if self.model is None:
              self.chat_log.text += "\nChatbot: Error: Modelo no cargado."
              return
          
          threading.Thread(target=self.predict_risk, args=(user_input,)).start()

    def predict_risk(self, text):
          try:
              inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
              with torch.no_grad():
                  outputs = self.model(**inputs)
                  logits = outputs.logits
                  probs = torch.softmax(logits, dim=1)[0]
                  prob_alto = probs[1].item()
                  
                  umbral = 0.3
                  pred_ml = 1 if prob_alto > umbral else 0
                  
                  text_lower = text.lower()
                  factores = ['cirugia', 'edema', 'inmovilidad', 'cancer', 'tvp previa', 'dolor', 'inflamacion en pierna', 'venas superficiales']
                  count = sum(1 for f in factores if f in text_lower)
                  pred_final = 1 if pred_ml == 0 and count >= 2 else pred_ml
                  
              risk = "Alto Riesgo" if pred_final == 1 else "Bajo Riesgo"
              response = f"Evaluación: {risk} de TVP (Prob: {prob_alto:.2f}).\n"
              self.chat_log.text += f"\nChatbot: {response}"
          except Exception as e:
              self.chat_log.text += f"\nChatbot: Error en predicción: {str(e)}"

      # Métodos restantes (compatibilidad)
    def update_gender_value(self, spinner, text):
          if text == 'Masculino':
              self.selected_gender_value = 0
          elif text == 'Femenino':
              self.selected_gender_value = 1

    def update_age_value(self, spinner, text):
          if text == '0-5':
              self.selected_age_value = 1
          elif text == '6-12':
              self.selected_age_value = 2
          elif text == '13-20':
              self.selected_age_value = 3
          elif text == '21-39':
              self.selected_age_value = 4
          elif text == '40-49':
              self.selected_age_value = 5
          elif text == '50-59':
              self.selected_age_value = 6
          elif text == '60-69':
              self.selected_age_value = 7
          elif text == '70-84':
              self.selected_age_value = 8
          elif text == '85-100':
              self.selected_age_value = 9

    def update_checkbox_state(self, checkbox):
          return 1 if checkbox.active else 0

    def calculate_results(self, *args):
          pass

    def toggle_results_view(self, *args):
          pass

    def on_size(self, *args):
          self.rect.size = self.size
          self.rect.pos = self.pos

class MyApp(App):
    def build(self):  
          Window.size = (375, 667)
          return MainScreen()

if __name__ == '__main__':
    MyApp().run()
    