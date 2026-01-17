# Instrucciones para el Profesor

## 🚀 GUÍA RÁPIDA: Configurar IA en 3 minutos

### Opción más fácil: Groq (Gratis y rápido) ⭐ RECOMENDADO

1. **Crear cuenta en Groq:**
   - Ve a: https://console.groq.com/
   - Crea una cuenta (gratis, no requiere tarjeta)
   - Ve a "API Keys" y crea una nueva clave
   - Copia la clave (empieza con `gsk_...`)

2. **Instalar las librerías:**
   ```bash
   pip install groq python-dotenv
   ```

3. **Configurar el archivo .env (más seguro):**
   - Copia el archivo `env.example` y renómbralo a `.env`
   - O crea un archivo nuevo llamado `.env` en la carpeta del proyecto
   - Abre el archivo `.env` y escribe:
     ```
     GROQ_API_KEY=tu_clave_aqui
     ```
   - Reemplaza `tu_clave_aqui` con tu clave real de Groq

4. **¡Listo!** Ejecuta el programa:
   ```bash
   python generador_superheroes.py
   ```
   - Elige la opción 2, 3 o 4 del menú para probar la IA real
   - Opción 2: Un superhéroe con IA
   - Opción 3: Varios superhéroes automáticamente con IA
   - Opción 4: Superhéroes aleatorios con IA

**Nota:** El archivo `.env` no se sube a Git (está protegido), así que tu clave está segura.

---

## Configuración de la función de IA

**IMPORTANTE:** El programa ya está configurado para usar **Groq** automáticamente. Solo necesitas crear el archivo `.env` con tu API key de Groq (ver guía rápida arriba). **NO necesitas modificar el código.**

**Si quieres usar otra API (OpenAI, Hugging Face, etc.):**
- Debes modificar la función `pedir_a_la_ia()` en `generador_superheroes.py`
- Ver sección "CÓDIGOS PARA CONFIGURAR" más abajo
- Puedes leer la API key del archivo `.env` usando `os.getenv("NOMBRE_DE_LA_VARIABLE")`

## 🆓 OPCIONES GRATUITAS PARA PROBAR

### Opción 1: OpenAI (Créditos gratuitos iniciales) ⭐ RECOMENDADO

**Ventajas:**
- ✅ $5 USD de crédito gratuito al registrarte
- ✅ Fácil de usar
- ✅ Buena calidad

**Pasos:**
1. Ve a https://platform.openai.com/
2. Crea una cuenta (necesitas tarjeta, pero no se cobra si solo usas créditos gratuitos)
3. Ve a "API Keys" y crea una nueva clave
4. Instala: `pip install openai`
5. Usa el código de abajo

### Opción 2: Hugging Face (Completamente gratis) 🎁

**Ventajas:**
- ✅ 100% gratis
- ✅ No requiere tarjeta
- ✅ Funciona bien para pruebas

**Pasos:**
1. Ve a https://huggingface.co/ y crea cuenta
2. Ve a https://huggingface.co/settings/tokens y crea un token
3. Instala: `pip install transformers requests`
4. Usa el código de abajo

### Opción 3: Groq (Muy rápido y gratis) ⚡

**Ventajas:**
- ✅ API gratuita con límites generosos
- ✅ Muy rápido
- ✅ No requiere tarjeta

**Pasos:**
1. Ve a https://console.groq.com/
2. Crea una cuenta
3. Crea una API key
4. Instala: `pip install groq`
5. Usa el código de abajo

### Opción 4: Usar el modo demo (sin API real)

El código actual funciona en modo demo sin necesidad de API. Los niños pueden probar el programa y ver cómo funciona, aunque las historias serán de ejemplo.

---

## CÓDIGOS PARA CONFIGURAR

### Opción 1: Usando OpenAI (ChatGPT) - Con créditos gratuitos

**Paso 1:** Añade tu API key al archivo `.env`:
```
OPENAI_API_KEY=tu_clave_openai_aqui
```

**Paso 2:** Modifica la función `pedir_a_la_ia()` en `generador_superheroes.py`:

```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del .env

def pedir_a_la_ia(mensaje):
    # Leer API key del archivo .env
    API_KEY_OPENAI = os.getenv("OPENAI_API_KEY")
    
    if not API_KEY_OPENAI:
        # Si no está configurada, usar modo demo
        return "Historia de ejemplo..."
    
    client = OpenAI(api_key=API_KEY_OPENAI)
    
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
```

**Instalación:**
```bash
pip install openai
```

### Opción 2: Usando Hugging Face (100% gratis)

**Paso 1:** Añade tu token al archivo `.env`:
```
HUGGINGFACE_API_KEY=tu_token_huggingface_aqui
```

**Paso 2:** Modifica la función `pedir_a_la_ia()` en `generador_superheroes.py`:

```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del .env

def pedir_a_la_ia(mensaje):
    # Leer token del archivo .env
    API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")
    
    if not API_TOKEN:
        # Si no está configurada, usar modo demo
        return "Historia de ejemplo..."
    API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    # Usar un modelo de texto más adecuado
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    
    response = requests.post(API_URL, headers=headers, json={
        "inputs": f"Escribe una historia corta sobre un superhéroe. {mensaje}",
        "parameters": {"max_length": 200, "temperature": 0.8}
    })
    
    if response.status_code == 200:
        resultado = response.json()
        if isinstance(resultado, list) and len(resultado) > 0:
            return resultado[0].get("generated_text", "Historia generada")
    else:
        # Si falla, devolver mensaje de ejemplo
        return f"Historia de ejemplo generada para: {mensaje[:50]}..."
    
    return "No se pudo generar la historia en este momento."
```

**Instalación:**
```bash
pip install requests
```

**Nota:** Hugging Face puede tener límites de velocidad. Si falla, el programa usará un mensaje de ejemplo.

### Opción 3: Usando Groq (Gratis y rápido) ⚡ - **YA CONFIGURADO**

**El código actual ya está configurado para Groq.** Solo necesitas:

1. Añade tu API key al archivo `.env`:
   ```
   GROQ_API_KEY=tu_clave_groq_aqui
   ```

2. El código ya lee automáticamente del `.env` (no necesitas modificar nada)

**Si quieres ver cómo funciona internamente:**

```python
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del .env

def pedir_a_la_ia(mensaje):
    # Leer API key del archivo .env
    API_KEY_GROQ = os.getenv("GROQ_API_KEY") or os.getenv("API_KEY_GROQ")
    
    if not API_KEY_GROQ:
        # Si no está configurada, usar modo demo
        return "Historia de ejemplo..."
    
    client = Groq(api_key=API_KEY_GROQ)
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Modelo rápido y gratuito
        messages=[
            {"role": "system", "content": "Eres un escritor creativo que crea historias de superhéroes para niños de 10 años. Las historias deben ser cortas (3-4 párrafos), emocionantes y apropiadas para niños."},
            {"role": "user", "content": mensaje}
        ],
        max_tokens=300,
        temperature=0.8
    )
    
    return response.choices[0].message.content
```

**Instalación:**
```bash
pip install groq
```

### Opción 4: Usando Anthropic (Claude) - Opción de pago

```python
import anthropic

def pedir_a_la_ia(mensaje):
    client = anthropic.Anthropic(api_key="TU_API_KEY_AQUI")
    
    message = client.messages.create(
        model="claude-3-haiku-20240307",  # versión más económica
        max_tokens=300,
        messages=[
            {"role": "user", "content": mensaje}
        ]
    )
    
    return message.content[0].text
```

## 📋 RECOMENDACIONES POR CASO DE USO

### Para probar rápido (sin registro):
- ✅ **Modo Demo**: Ya funciona sin configuración
- ✅ **Groq**: Registro rápido, muy fácil

### Para uso educativo prolongado:
- ✅ **OpenAI**: $5 gratis inicial, luego muy económico (gpt-3.5-turbo cuesta ~$0.001 por historia)
- ✅ **Groq**: Gratis con límites generosos

### Para uso completamente gratis:
- ✅ **Hugging Face**: 100% gratis, pero puede ser más lento
- ✅ **Modo Demo**: Funciona perfectamente para enseñar el concepto

## Instalación de dependencias

Dependiendo de la opción que elijas:

```bash
# Para OpenAI
pip install openai

# Para Groq
pip install groq

# Para Hugging Face
pip install requests

# Para Anthropic (opción de pago)
pip install anthropic
```

## 📝 Cómo funciona el archivo .env

El archivo `.env` es la forma más segura de guardar tus API keys. **NO se sube a Git** (está protegido).

### Estructura del archivo .env:

```
# Para Groq (ya configurado en el código)
GROQ_API_KEY=tu_clave_groq_aqui

# Para OpenAI (requiere modificar código)
OPENAI_API_KEY=tu_clave_openai_aqui

# Para Hugging Face (requiere modificar código)
HUGGINGFACE_API_KEY=tu_token_huggingface_aqui
```

### Cómo leer del .env en Python:

```python
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Leer una variable específica
api_key = os.getenv("GROQ_API_KEY")  # Lee GROQ_API_KEY del .env
```

### Alternativa: Variables de entorno del sistema

También puedes configurar variables de entorno del sistema (menos recomendado para este proyecto):

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="tu_clave_aqui"
```

**Linux/Mac:**
```bash
export GROQ_API_KEY="tu_clave_aqui"
```

## Uso en clase

1. **Primera sesión**: Ejecuta el programa en modo demo (sin API) para que los niños vean cómo funciona.

2. **Segunda sesión**: Si tienes acceso a una API, configura la función y deja que los niños usen la versión real.

3. **Enfoque progresivo**:
   - Empieza con Nivel 1 (sin IA)
   - Luego Nivel 2 (un superhéroe con IA)
   - Finalmente Nivel 2 Avanzado (varios superhéroes automáticamente)

## Personalización

Puedes modificar:
- La lista de superhéroes en `crear_varios_superheroes()`
- Las preguntas que se hacen al usuario
- El formato de salida
- Los mensajes de la interfaz

## Notas importantes

- **Costos**: Si usas una API de pago, ten en cuenta los costos por llamada. Para niños, usa modelos más económicos (gpt-3.5-turbo o claude-haiku).
- **Límites de velocidad**: Algunas APIs tienen límites de velocidad. Para procesar varios superhéroes, considera añadir un pequeño delay entre llamadas.
- **Errores**: Añade manejo de errores básico para que si falla la API, el programa no se rompa completamente.
