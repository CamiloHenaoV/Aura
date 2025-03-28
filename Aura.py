from transformers import AutoModelForCausalLM, AutoTokenizer
from googletrans import Translator
import torch
import asyncio

print("El archivo se está ejecutando correctamente.")
print(torch.__version__)
print(torch.cuda.is_available())  # Verifica si hay soporte para GPU

# Inicializar traductor
translator = Translator()

# Cargar modelo y tokenizador
def cargar_modelo(modelo_nombre="microsoft/DialoGPT-medium"):
    try:
        tokenizer = AutoTokenizer.from_pretrained(modelo_nombre)
        modelo = AutoModelForCausalLM.from_pretrained(modelo_nombre)
        return tokenizer, modelo
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        raise  # Esto permitirá ver el error completo

# Función para generar respuestas
async def responder_chat(input_text, tokenizer, modelo):
    try:
        # Traducir entrada al inglés
        input_text_en = (await translator.translate(input_text, src='es', dest='en')).text
        inputs = tokenizer.encode(input_text_en + tokenizer.eos_token, return_tensors="pt")
        
        # Crear el attention_mask
        attention_mask = torch.ones_like(inputs)

        # Generar respuesta con el attention_mask
        respuesta_ids = modelo.generate(
            inputs,
            attention_mask=attention_mask,
            max_length=100,
            pad_token_id=tokenizer.eos_token_id
        )
        respuesta_en = tokenizer.decode(respuesta_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        
        # Traducir respuesta al español
        respuesta_es = (await translator.translate(respuesta_en, src='en', dest='es')).text
        return respuesta_es
    except Exception as e:
        return f"Error al generar respuesta: {e}"

# Función principal
async def main():
    print("Cargando modelo...")
    tokenizer, modelo = cargar_modelo()
    print("Modelo cargado correctamente.")
    print("Aura: ¡Hola! Escribe 'salir' para terminar la conversación.")
    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() == "salir":
                print("Aura: ¡Hasta luego!")
                break
            respuesta = await responder_chat(user_input, tokenizer, modelo)
            print("Aura:", respuesta)
        except KeyboardInterrupt:
            print("\nAura: ¡Hasta luego!")
            break

if __name__ == "__main__":
    asyncio.run(main())
