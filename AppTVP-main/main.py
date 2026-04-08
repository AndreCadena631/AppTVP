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
 
 
# Pantalla principal
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):  # No need for ScreenManager
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.update_main_content()  # Initialize with main content

        # Initialize checkbox states
        self.checkbox_state = 0
        self.checkbox1_state = 0
        self.checkbox2_state = 0
        self.checkbox3_state = 0
        self.checkbox4_state = 0
        self.checkbox5_state = 0
        self.checkbox6_state = 0

        # Initialize results list
        self.results_list = []

    def update_main_content(self, *args):  # Accept additional arguments
        self.clear_widgets()  # Clear existing widgets

        # Cambiar el color de fondo
        with self.canvas:
            Color(1, 0.8, 0.4, 1)  # Color Ocre
            self.rect = Rectangle(size=self.size, pos=self.pos)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)  # Reduced padding for higher positioning

        # Título
        title = Label(text='CimaTVPDetect', size_hint_y=None, height=70, color=(0, 0, 0, 1), font_size=25)  # Aumentar tamaño y cambiar color a blanco
        title.text_size = (200, None)
        title.halign = 'center'
        title.valign = 'middle'
        layout.add_widget(title)

        # Logo 
        logo = Image(source='images/images1.png', size_hint=(1, 1.0), fit_mode="contain")  # Aumentar tamaño de la imagen
        layout.add_widget(logo)

        # Botón para cambiar a la segunda pantalla
        button = Button(text='EMPEZAR', size_hint_y=None, height=50, size_hint_x=1)  # Cambiar tamaño del botón
        button.bind(on_press=self.switch_to_second_screen)  # Navegar a la segunda pantalla
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

    def switch_to_third_screen(self, *args):

        self.clear_widgets()  # Clear existing widgets

        # Cambiar el color de fondo
        with self.canvas:
            Color(1, 0.8, 0.4, 1) # Color Ocre
            self.rect = Rectangle(size=self.size, pos=self.pos)

        scroll_view = ScrollView()
        layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=20, spacing=20)
        layout.bind(minimum_height=layout.setter('height'))  # Allow the layout to grow

        button = Button(text='REGRESAR', size_hint_y=None, height=50)  # Regresar button
        button.bind(on_press=self.switch_to_second_screen)  # Navigate back to second screen
        layout.add_widget(button)

        # Título de la tercera pantalla
        title_third = Label(text='Cuestionario de Escala de Wells para Trombosis Venosa Profunda', size_hint_y=None, height=60, color=(0, 0, 0, 1), halign='center', font_size=20)  # Justified text
        title_third.text_size = (self.width - 100, None)  # Allow text to wrap
        title_third.size_hint_x = 1  # Ensure it takes full width
        layout.add_widget(title_third)

        # Recuadro de texto para Pseudónimo
        pseudonym_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        pseudonym_label = Label(text='Pseudónimo:', size_hint_x=None, width=200, color=(0, 0, 0, 1))
        self.pseudonym_input = TextInput(hint_text='Ingrese su pseudónimo', size_hint_y=None, height=40, multiline=False, background_color=(1, 0.8, 0.4, 1))
        pseudonym_layout.add_widget(pseudonym_label)
        pseudonym_layout.add_widget(self.pseudonym_input)
        layout.add_widget(pseudonym_layout)

        # Pregunta 1
        age_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)  # Horizontal layout for age question
        age_label = Label(text='¿Cuál es su edad?', size_hint_x=None, width=200, color=(0, 0, 0, 1))  # Question label
        age_spinner = Spinner(text='Edad', values=['0-5', '6-12', '13-20', '21-39', '40-49', '50-59', '60-69', '70-84', '85-100'], size_hint_y=None, height=40)  # Selector

        age_layout.add_widget(age_label)  # Add label to layout
        age_layout.add_widget(age_spinner)  # Add spinner to layout
        layout.add_widget(age_layout)  # Add the horizontal layout to the main layout

        # Pregunta 2
        gender_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)  # Horizontal layout for gender question
        gender_label = Label(text='¿Cuál es su género?', size_hint_x=None, width=200, color=(0, 0, 0, 1))  # Question label
        gender_spinner = Spinner(text='Género', values=['Masculino', 'Femenino'], size_hint_y=None, height=40)  # Selector
        self.selected_age_value = None  # Variable to store age value
        self.selected_gender_value = None  # Variable to store gender value

        age_spinner.bind(text=self.update_age_value)  # Bind the age spinner to update the age value
        self.gender_spinner = gender_spinner  # Store reference to gender spinner
        gender_spinner.bind(text=self.update_gender_value)  # Bind the gender spinner to update the gender value


        gender_layout.add_widget(gender_label)  # Add label to layout
        gender_layout.add_widget(gender_spinner)  # Add spinner to layout
        layout.add_widget(gender_layout)  # Add the horizontal layout to the main layout

        # Espacio entre la última pregunta y el botón Calcular
        layout.add_widget(Label(text='Verifique que haya seleccionado bien su edad y genero', size_hint_y=None, height=10, font_size=12, color=(0,0,0,1)))  # Adding a spacer

        # Pregunta 3
        question_label = Label(text='Cáncer Activo', size_hint_y=None, height=40, size_hint_x=0.5, color=(0, 0, 0, 1))
        question_label.text_size = (self.width - 270, None)  # Allow text to wrap
        self.checkbox = CheckBox(size_hint_y=None, height=40, color=(0, 0, 0, 1), size_hint_x=0.5)  # Checkbox for yes/no with black color
        question_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, size_hint_x=1)  # Adjust size_hint_x to fit screen
        question_layout.add_widget(question_label)
        question_layout.add_widget(self.checkbox)
        layout.add_widget(question_layout)

        # Pregunta 4
        question_label1 = Label(text='Paralisis, Paresia o Inmovilidad reciente', size_hint_y=None, height=40, size_hint_x=0.5, color=(0, 0, 0, 1))
        question_label1.text_size = (self.width - 270, None)  # Allow text to wrap
        self.checkbox1 = CheckBox(size_hint_y=None, height=40, color=(0, 0, 0, 1), size_hint_x=0.5)  # Checkbox for yes/no with black color
        question_layout1 = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, size_hint_x=1)  # Adjust size_hint_x to fit screen
        question_layout1.add_widget(question_label1)
        question_layout1.add_widget(self.checkbox1)
        layout.add_widget(question_layout1)

        # Pregunta 5
        question_label2 = Label(text='Estancia en cama reciente por mas de 3 dias reciente o cirugia mayor en las ultimas 4 semanas', size_hint_y=None, height=40, size_hint_x=0.5, color=(0, 0, 0, 1))
        question_label2.text_size = (self.width - 270, None)  # Allow text to wrap
        self.checkbox2 = CheckBox(size_hint_y=None, height=40, color=(0, 0, 0, 1), size_hint_x=0.5)  # Checkbox for yes/no with black color
        question_layout2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, size_hint_x=1)  # Adjust size_hint_x to fit screen
        question_layout2.add_widget(question_label2)
        question_layout2.add_widget(self.checkbox2)
        layout.add_widget(question_layout2)

        # Pregunta 6
        question_label3= Label(text='Dolor o Sensibilidad en una área muscular específica', size_hint_y=None, height=40, size_hint_x=0.5, color=(0, 0, 0, 1))
        question_label3.text_size = (self.width - 270, None)  # Allow text to wrap
        self.checkbox3 = CheckBox(size_hint_y=None, height=40, color=(0, 0, 0, 1), size_hint_x=0.5)  # Checkbox for yes/no with black color
        question_layout3 = BoxLayout(orientation='horizontal', size_hint_y=None, height=90, size_hint_x=1)  # Adjust size_hint_x to fit screen
        question_layout3.add_widget(question_label3)
        question_layout3.add_widget(self.checkbox3)
        layout.add_widget(question_layout3)

        # Pregunta 7
        question_label4 = Label(text='Hinchazon de la Pierna', size_hint_y=None, height=40, size_hint_x=0.5, color=(0, 0, 0, 1))
        question_label4.text_size = (self.width - 270, None)  # Allow text to wrap
        self.checkbox4 = CheckBox(size_hint_y=None, height=40, color=(0, 0, 0, 1), size_hint_x=0.5)  # Checkbox for yes/no with black color
        question_layout4 = BoxLayout(orientation='horizontal', size_hint_y=None, height=70, size_hint_x=1)  # Adjust size_hint_x to fit screen
        question_layout4.add_widget(question_label4)
        question_layout4.add_widget(self.checkbox4)
        layout.add_widget(question_layout4)

        # Pregunta 8
        question_label5 = Label(text='Aumento del perímetro de la pantorrilla de más de 3 cm respecto a la pierna contralateral', size_hint_y=None, height=40, size_hint_x=0.5, color=(0, 0, 0, 1))
        question_label5.text_size = (self.width - 270, None)  # Allow text to wrap
        self.checkbox5 = CheckBox(size_hint_y=None, height=40, color=(0, 0, 0, 1), size_hint_x=0.5)  # Checkbox for yes/no with black color
        question_layout5 = BoxLayout(orientation='horizontal', size_hint_y=None, height=70, size_hint_x=1)  # Adjust size_hint_x to fit screen
        question_layout5.add_widget(question_label5)
        question_layout5.add_widget(self.checkbox5)
        layout.add_widget(question_layout5)

        # Pregunta 9
        question_label6 = Label(text='Edema en la pierna', size_hint_y=None, height=50, size_hint_x=0.5, color=(0, 0, 0, 1))
        question_label6.text_size = (self.width - 270, None)  # Allow text to wrap
        self.checkbox6 = CheckBox(size_hint_y=None, height=60, color=(0, 0, 0, 1), size_hint_x=0.5)  # Checkbox for yes/no with black color
        question_layout6 = BoxLayout(orientation='horizontal', size_hint_y=None, height=70, size_hint_x=1)  # Adjust size_hint_x to fit screen
        question_layout6.add_widget(question_label6)
        question_layout6.add_widget(self.checkbox6)
        layout.add_widget(question_layout6)

        # Espacio entre la última pregunta y el botón Calcular
        layout.add_widget(Label(size_hint_y=None, height=10, font_size=12))  # Adding a spacer


        # Botón Calcular
        calculate_button = Button(text='DIAGNOSTICAR', size_hint_y=None, height=50)  # Calcular button
        calculate_button.bind(on_press=self.calculate_results)  # Bind the button to the calculation method
        layout.add_widget(calculate_button)  # Add the button to the layout

        # Botón para mostrar/ocultar resultados
        self.show_results_button = Button(text='MOSTRAR RESULTADOS', size_hint_y=None, height=50)
        self.show_results_button.bind(on_press=self.toggle_results_view)
        layout.add_widget(self.show_results_button)

        # Espaciador estático para separar el botón del contenedor de resultados
        spacer = Label(size_hint_y=None, height=20)
        layout.add_widget(spacer)

        # Add the layout to the scroll view
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)

    def calculate_results(self, *args):
        # Collect data from Spinners and Checkboxes
        age_value = self.selected_age_value if hasattr(self, 'selected_age_value') else None  # Ensure age_value is set
        
        gender_value = 0 if self.gender_spinner.text == 'Masculino' else 1  # Assign 0 for Masculino and 1 for Femenino

        pseudonym = self.pseudonym_input.text if self.pseudonym_input.text else "Sin pseudónimo"

        checkbox1_state = self.update_checkbox_state(self.checkbox)
        checkbox2_state = self.update_checkbox_state(self.checkbox1)
        checkbox3_state = self.update_checkbox_state(self.checkbox2)
        checkbox4_state = self.update_checkbox_state(self.checkbox3)
        checkbox5_state = self.update_checkbox_state(self.checkbox4)
        checkbox6_state = self.update_checkbox_state(self.checkbox5)
        checkbox7_state = self.update_checkbox_state(self.checkbox6)

        # Compile data into an array
        results = [age_value, gender_value, checkbox1_state, checkbox2_state, checkbox3_state, checkbox4_state, checkbox5_state, checkbox6_state, checkbox7_state]

        new_results = pd.DataFrame([results], columns=["edad", "sexo", "cancer", "inmov", "cirugia", "dolor", "inf_pierna", "inf_tobillo", "edema"])
        KNN_model = joblib.load('KNN_model.pkl')
        sc = joblib.load('escalador.pkl')

        new_scaled_results = sc.transform(new_results)

        prediction = KNN_model.predict(new_scaled_results)

        # Save results to list
        result_entry = {
            'pseudonym': pseudonym,
            'age': age_value,
            'gender': 'Masculino' if gender_value == 0 else 'Femenino',
            'cancer': checkbox1_state,
            'paralysis': checkbox2_state,
            'bed_rest': checkbox3_state,
            'pain': checkbox4_state,
            'swelling': checkbox5_state,
            'calf_increase': checkbox6_state,
            'edema': checkbox7_state,
            'prediction': 'Riesgo de TVP' if prediction[0] == 1 else 'No hay Riesgo de TVP'
        }
        self.results_list.append(result_entry)

        # Display prediction result in a popup
        result_message = "Hay Riesgo de TVP.\n \nSe recomienda asistir a consulta con \nun especialista en angiología \no equivalente para validar \ny confirmar el diagnóstico." if prediction[0] == 1 else "No hay Riesgo de TVP."
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=result_message, halign='center', valign='middle'))
        accept_button = Button(text='Aceptar', size_hint_y=None, height=40)
        def close_popup(instance):
            popup.dismiss()

        accept_button.bind(on_press=close_popup)
        content.add_widget(accept_button)
        popup = Popup(title='Resultado del Pre-Diagnóstico', content=content, size_hint=(0.8, 0.8))
        popup.open()


    def toggle_results_view(self, *args):
        # Crear contenido del popup
        content = BoxLayout(orientation='vertical', padding=5, spacing=5)
        if self.results_list:
            scroll_view = ScrollView(size_hint=(1, 1))
            results_container = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
            results_container.bind(minimum_height=results_container.setter('height'))
            for result in self.results_list:
                result_text = f"Pseudónimo: {result['pseudonym']}\nEdad (grupo): {result['age']}\nGénero: {result['gender']}\nSintomas (checkbox): {[result['cancer'],result['paralysis'],result['bed_rest'],result['pain'],result['swelling'],result['calf_increase'],result['edema']]}\nPredicción: {result['prediction']}\n"
                result_label = Label(text=result_text, size_hint_y=None, height=110, halign='left', valign='top', color=(1, 1, 1, 1))
                result_label.text_size = (Window.width * 0.8, None)  # Adjust to popup width
                results_container.add_widget(result_label)
            scroll_view.add_widget(results_container)
            content.add_widget(scroll_view)
        else:
            no_results_label = Label(text="No hay resultados guardados.", color=(1, 1, 1, 1))
            content.add_widget(no_results_label)

        # Botón para cerrar el popup
        close_button = Button(text='Cerrar', size_hint_y=None, height=40)
        content.add_widget(close_button)

        # Crear y mostrar el popup
        popup = Popup(title='Resultados Guardados', content=content, size_hint=(0.9, 0.9))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def on_size(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class MyApp(App):

    def build(self):  
        Window.size = (375, 667)  # Establecer el tamaño de la ventana para simular un dispositivo móvil

        return MainScreen()  # Return the MainScreen directly

if __name__ == '__main__':
    MyApp().run()
