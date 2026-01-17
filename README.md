# Generador de Superhéroes con IA

Un programa divertido para crear historias de superhéroes usando programación y IA.

## 📦 Instalación

**Súper simple: solo ejecuta:**

```bash
python generador_superheroes.py
```

¡Eso es todo! El programa funciona inmediatamente sin necesidad de instalar nada.

**Requisitos:** Python 3.6 o superior (eso es todo)

## 🚀 Cómo empezar

### 📚 Progresión de aprendizaje (recomendada)

**PASO 1: Empieza con la versión simple** (para entender lo básico)
1. Abre el archivo `generador_superheroes_simple.py`
2. Ejecútalo con: `python generador_superheroes_simple.py`
3. Responde las preguntas que te hace el programa
4. ¡Mira el resultado!
5. **Aprende:** Entrada → Proceso → Salida (sin funciones, sin IA)

**PASO 2: Luego usa la versión completa** (con IA y automatización)
1. Abre el archivo `generador_superheroes.py`
2. Ejecútalo con: `python generador_superheroes.py`
3. Elige una opción del menú:
   - **Opción 1**: Crear un superhéroe simple (sin IA)
   - **Opción 2**: Crear un superhéroe con IA (más creativo)
   - **Opción 3**: Crear VARIOS superhéroes automáticamente (¡esto es lo más importante!)
   - **Opción 4**: Modo Aleatorio con IA - Generar superhéroes aleatorios (¡divertido!)
   - **Opción 5**: Ver historias guardadas
   - **Opción 6**: Ver estadísticas
   - **Opción 7**: Ver información sobre el programa
   - **Opción 8**: Salir

## 📋 Qué hace el programa

### Nivel 1: Sin IA
- Hace preguntas sobre tu superhéroe
- Combina las respuestas en un texto
- Muestra el resultado

### Nivel 2: Con IA
- Hace preguntas sobre tu superhéroe
- Le pide a la IA que cree una historia completa
- Muestra la historia generada

### Nivel 2 Avanzado: Lo más importante
- Toma una lista de varios superhéroes
- **Automáticamente** crea una historia para cada uno
- Muestra todas las historias

### Modo Aleatorio con IA (Opción 4)
- El programa genera superhéroes aleatorios automáticamente
- Tú eliges cuántos quieres generar (1-10)
- El programa crea nombres, poderes y orígenes aleatorios
- **Usa IA para generar historias creativas** para cada superhéroe
- **Más divertido, menos control** - perfecto para experimentar

**Esto es lo que NO puedes hacer solo conversando con la IA:**
- Sin programación: tendrías que pedir cada historia una por una, manualmente
- Con programación: el programa lo hace automáticamente en segundos

## 🎯 Qué aprenderás

- Cómo hacer preguntas al usuario
- Cómo guardar respuestas en variables
- Cómo combinar texto
- Cómo usar la IA dentro de un programa
- Cómo hacer que el programa repita algo varias veces automáticamente

## 💡 Consejos

- Empieza con la versión simple
- Prueba cada opción del menú
- Experimenta cambiando las respuestas
- ¡Diviértete creando superhéroes!

## ❓ Preguntas frecuentes

**¿Necesito saber programación?**
No, el programa está hecho para que sea fácil de usar. Solo sigue las instrucciones.

**¿Funciona sin internet?**
La versión simple sí. La versión con IA necesita que el profesor haya configurado la conexión a la IA.

**¿Puedo modificar el programa?**
¡Sí! Puedes cambiar las preguntas, añadir más superhéroes a la lista, o cambiar cómo se muestra el resultado.

## 🤖 Configurar IA real (opcional)

El programa funciona en **modo demo** sin configuración, pero puedes usar una IA real:

### Opción rápida (3 minutos) - Groq (Gratis):
1. Ve a https://console.groq.com/ y crea cuenta (gratis, sin tarjeta)
2. Crea una API key en "API Keys"
3. Instala: `pip install groq python-dotenv`
4. Crea un archivo `.env` en la carpeta del proyecto:
   ```
   GROQ_API_KEY=tu_clave_aqui
   ```
5. ¡Listo! El programa usará la IA real automáticamente

**Nota:** El archivo `.env` está protegido (no se sube a Git), así que tu clave está segura.

### Otras opciones gratuitas:
- **OpenAI**: $5 créditos gratis al registrarte
- **Hugging Face**: 100% gratis (puede ser más lento)

**Nota:** El código actual está configurado para **Groq**. Si quieres usar otra API (OpenAI, Hugging Face, etc.), debes modificar la función `pedir_a_la_ia()` en el código. Ver `INSTRUCCIONES_PROFESOR.md` para más detalles.

📖 **Ver `INSTRUCCIONES_PROFESOR.md`** para instrucciones detalladas y todas las opciones.
