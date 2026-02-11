# CimaTVPDetect

## Descripción

CimaTVPDetect es una aplicación móvil desarrollada en Python utilizando Kivy, diseñada para calcular el riesgo de padecer Trombosis Venosa Profunda (TVP) mediante un cuestionario basado en las Métricas de Wells. La app integra un modelo de machine learning entrenado con Scikit-Learn y Joblib para proporcionar una evaluación rápida y precisa del riesgo, ayudando a los usuarios a tomar decisiones informadas sobre su salud.

El cuestionario evalúa factores como síntomas clínicos, antecedentes médicos y condiciones de riesgo, asignando una puntuación que clasifica el riesgo en bajo, moderado o alto.

## Características

- **Interfaz intuitiva**: Desarrollada con Kivy para una experiencia móvil fluida en Android e iOS.
- **Cuestionario basado en Wells**: Implementa las métricas estándar para la evaluación de TVP.
- **Modelo de ML**: Utiliza un clasificador entrenado con Scikit-Learn y cargado vía Joblib para predicciones precisas.
- **Procesamiento de datos**: Manejo eficiente de datos con Pandas.
- **Resultados claros**: Muestra el riesgo calculado con recomendaciones básicas (no sustituye a un diagnóstico médico profesional).

## Requisitos

- Python 3.8 o superior
- Kivy 2.0+
- Scikit-Learn 1.0+
- Joblib 1.0+
- Pandas 1.3+
- Un dispositivo móvil con Android (para APK) o iOS (requiere Buildozer para compilación)

## Instalación

1. Clona el repositorio:
git clone https://github.com/tu-usuario/CimaTVPDetect.git cd CimaTVPDetect

2. Instala las dependencias:
pip install -r requirements.txt

3. Para ejecutar en modo de desarrollo (escritorio):
python main.py


4. Para compilar en APK (Android):
- Instala Buildozer: `pip install buildozer`
- Configura `buildozer.spec` según tus necesidades.
- Ejecuta: `buildozer android debug`

Para iOS, usa Xcode en macOS con Kivy-ios.

## Uso

1. Abre la app en tu dispositivo móvil.
2. Completa el cuestionario respondiendo a las preguntas sobre síntomas y factores de riesgo.
3. La app procesa las respuestas usando el modelo de ML y muestra el nivel de riesgo (bajo, moderado, alto).
4. Revisa las recomendaciones y consulta a un médico si es necesario.

**Nota**: Esta app es una herramienta educativa y no reemplaza la evaluación médica profesional. Siempre busca atención médica para diagnósticos precisos.

## Contribución

Las contribuciones son bienvenidas. Para contribuir:
1. Haz un fork del repositorio.
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`.
3. Realiza tus cambios y haz commit: `git commit -m 'Agrega nueva funcionalidad'`.
4. Push a la rama: `git push origin feature/nueva-funcionalidad`.
5. Abre un Pull Request.

Asegúrate de seguir las mejores prácticas de código y agregar tests si es posible.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o soporte, contacta a andre.cadena@gmail.com o abre un issue en el repositorio.










