"""
==================================================
  EJEMPLO: Cómo configurar la función de IA
==================================================

Este archivo contiene ejemplos listos para copiar y pegar
en la función pedir_a_la_ia() del archivo generador_superheroes.py

Elige UNA de las opciones y reemplaza la función completa.
"""

# ============================================
# OPCIÓN 1: GROQ (Recomendado - Gratis y rápido)
# ============================================
# Pasos:
# 1. Ve a https://console.groq.com/ y crea cuenta
# 2. Crea una API key
# 3. pip install groq
# 4. Copia y pega este código en generador_superheroes.py

def pedir_a_la_ia_groq(mensaje):
    from groq import Groq
    
    client = Groq(api_key="TU_CLAVE_GROQ_AQUI")  # Reemplaza con tu clave
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Eres un escritor creativo que crea historias de superhéroes para niños de 10 años. Las historias deben ser cortas (3-4 párrafos), emocionantes y apropiadas para niños."},
            {"role": "user", "content": mensaje}
        ],
        max_tokens=300,
        temperature=0.8
    )
    
    return response.choices[0].message.content


# ============================================
# OPCIÓN 2: OPENAI (Con créditos gratuitos)
# ============================================
# Pasos:
# 1. Ve a https://platform.openai.com/ y crea cuenta
# 2. Crea una API key (tienes $5 gratis)
# 3. pip install openai
# 4. Copia y pega este código en generador_superheroes.py

def pedir_a_la_ia_openai(mensaje):
    from openai import OpenAI
    
    client = OpenAI(api_key="TU_CLAVE_OPENAI_AQUI")  # Reemplaza con tu clave
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Modelo económico
        messages=[
            {"role": "system", "content": "Eres un escritor creativo que crea historias de superhéroes para niños de 10 años. Las historias deben ser cortas (3-4 párrafos), emocionantes y apropiadas para niños."},
            {"role": "user", "content": mensaje}
        ],
        max_tokens=300,
        temperature=0.8
    )
    
    return response.choices[0].message.content


# ============================================
# OPCIÓN 3: HUGGING FACE (100% gratis)
# ============================================
# Pasos:
# 1. Ve a https://huggingface.co/ y crea cuenta
# 2. Ve a https://huggingface.co/settings/tokens y crea token
# 3. pip install requests
# 4. Copia y pega este código en generador_superheroes.py

def pedir_a_la_ia_huggingface(mensaje):
    import requests
    
    API_TOKEN = "TU_TOKEN_HUGGINGFACE_AQUI"  # Reemplaza con tu token
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    payload = {
        "inputs": f"Escribe una historia corta y emocionante sobre un superhéroe para niños. {mensaje}",
        "parameters": {"max_length": 300, "temperature": 0.8, "return_full_text": False}
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            resultado = response.json()
            if isinstance(resultado, list) and len(resultado) > 0:
                texto = resultado[0].get("generated_text", "")
                return texto if texto else "Historia generada con éxito."
        else:
            # Si el modelo está cargando, esperar un poco
            if response.status_code == 503:
                return "El modelo está cargando. Intenta de nuevo en unos segundos."
            
    except Exception as e:
        pass
    
    # Fallback: devolver historia de ejemplo
    return f"Historia de ejemplo generada para: {mensaje[:50]}..."


# ============================================
# INSTRUCCIONES PARA USAR:
# ============================================
# 
# 1. Elige UNA de las opciones de arriba
# 2. Abre generador_superheroes.py
# 3. Busca la función pedir_a_la_ia() (línea ~32)
# 4. Reemplaza TODO el contenido de la función con el código elegido
# 5. Reemplaza "TU_CLAVE_AQUI" con tu clave real
# 6. Guarda el archivo
# 7. Ejecuta el programa y prueba las opciones 2 o 3 del menú
#
# NOTA: Si no quieres configurar nada, el programa funciona
# en modo demo con historias de ejemplo.
