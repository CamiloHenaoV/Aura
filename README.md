# Aura - Chatbot emocional basado en IA

Aura es un chatbot interactivo diseñado para mantener conversaciones empáticas y brindar apoyo emocional. Utiliza el modelo **DialoGPT** de Microsoft para generar respuestas y la biblioteca **googletrans** para traducir entre español e inglés, permitiendo una experiencia conversacional fluida en español.

## Características

- Conversaciones interactivas en español.
- Traducción automática de entradas y salidas para mejorar la comprensión.
- Basado en el modelo **DialoGPT-medium** de Microsoft.
- Soporte para GPU (si está disponible) para un rendimiento más rápido.

## Requisitos

- **Python 3.7 o superior**
- Bibliotecas necesarias:
  - `transformers`
  - `torch`
  - `googletrans`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/CamiloHenaoV/Aura.git
   cd Aura
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate       # En Linux/Mac
   .\venv\Scripts\activate        # En Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el chatbot:
   ```bash
   python Aura.py
   ```

2. Interactúa con Aura escribiendo tus mensajes en la consola. Escribe `salir` para terminar la conversación.

## Ejemplo de conversación

```
Aura: ¡Hola! Escribe 'salir' para terminar la conversación.
Tú: Hola
Aura: ¡Hola! ¿Cómo estás?
Tú: Me siento triste.
Aura: Lamento que te sientas así. ¿Qué ha estado pasando?
Tú: Gracias por escucharme.
Aura: Siempre estoy aquí para ayudarte.
```

## Notas importantes

- **Aura no reemplaza el consejo profesional.** Está diseñado únicamente para conversaciones generales y no debe ser utilizado como una herramienta de asesoramiento psicológico o médico.
- Si deseas personalizar el comportamiento del chatbot, puedes realizar un **fine-tuning** del modelo con datos específicos.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar Aura, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección:
   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Agregué una nueva funcionalidad"
   ```
4. Sube tus cambios:
   ```bash
   git push origin mi-nueva-funcionalidad
   ```
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme:

- **Autor:** Camilo Henao
- **GitHub:** [CamiloHenaoV](https://github.com/CamiloHenaoV)