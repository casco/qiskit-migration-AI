import os
import sys
from openai import OpenAI

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py archivo_entrada archivo_salida")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]

    # Obtener API key desde variable de entorno
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    if not api_key:
        print("Error: No se encontró la variable de entorno OPENAI_API_KEY.")
        sys.exit(1)


    # Leer prompt del archivo de entrada
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            prompt = f.read()
    except Exception as e:
        print(f"Error al leer archivo de entrada: {e}")
        sys.exit(1)

    # Llamar a la API de OpenAI (modo one-shot)
    try:
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000)
        respuesta = response.choices[0].message.content
    except Exception as e:
        print(f"Error al llamar a la API de OpenAI: {e}")
        sys.exit(1)

    # Escribir la respuesta al archivo de salida
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write(respuesta)
    except Exception as e:
        print(f"Error al escribir archivo de salida: {e}")
        sys.exit(1)

    print("Respuesta guardada en", archivo_salida)

if __name__ == "__main__":
    main()
