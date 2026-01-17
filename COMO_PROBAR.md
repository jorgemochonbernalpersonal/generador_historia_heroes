# Cómo Probar el Programa

## 🚀 Ejecutar el Programa

Simplemente ejecuta:
```bash
python generador_superheroes.py
```

¡Eso es todo! No necesitas instalar nada ni configurar venv.

## Prueba Rápida

### Paso 1: Abre una terminal en la carpeta del proyecto

**Windows:**
- Presiona `Win + R`, escribe `cmd` y presiona Enter
- Navega a la carpeta: `cd C:\Users\jorge\Desktop\programa`

**O desde el explorador:**
- Abre la carpeta del proyecto
- Haz clic derecho en la carpeta → "Abrir en terminal" o "Abrir PowerShell aquí"

### Paso 2: Ejecuta el programa simple

```bash
python generador_superheroes_simple.py
```

**Qué esperar:**
- Te hará 3 preguntas sobre tu superhéroe
- Responde cada una y presiona Enter
- Verás el resultado combinado

**Ejemplo de respuestas:**
```
¿Cómo se llama tu superhéroe? Rayo Veloz
¿Qué poder especial tiene? velocidad
¿De dónde viene su poder? un accidente
```

### Paso 3: Prueba el programa completo

```bash
python generador_superheroes.py
```

**Qué esperar:**
- Verás un menú con opciones
- Elige la opción 1 para empezar (más fácil)
- Sigue las instrucciones en pantalla

## Qué Probar

### ✅ Prueba Básica (Nivel 1)
1. Ejecuta el programa
2. Elige opción 1 del menú
3. Responde las preguntas
4. Verifica que muestra el resultado

### ✅ Prueba con IA (Nivel 2)
1. Elige opción 2 del menú
2. Responde las preguntas
3. Verás que "genera" una historia (en modo demo será un texto de ejemplo)
4. Prueba guardar el archivo

### ✅ Prueba Avanzada (Nivel 2 Avanzado) - LA MÁS IMPORTANTE
1. Elige opción 3 del menú
2. Elige usar lista predefinida (opción 1)
3. Presiona Enter para comenzar
4. **Verás cómo procesa 3 superhéroes automáticamente**
5. Esto demuestra el valor de la programación

### ✅ Prueba Modo Aleatorio (Divertido)
1. Elige opción 4 del menú
2. Elige cuántos superhéroes quieres generar (1-10)
3. El programa generará superhéroes aleatorios automáticamente
4. Verás cómo el programa crea personajes y sus historias sin que escribas nada
5. **Nota:** Este modo es más divertido, pero el modo 3 es más didáctico

### ✅ Prueba Crear Lista Propia
1. Elige opción 3 del menú
2. Elige crear lista propia (opción 2)
3. Crea 2-3 superhéroes
4. Escribe "fin" cuando termines
5. Verás cómo procesa tu lista automáticamente

### ✅ Prueba Guardar Archivos
1. Después de generar historias, elige guardar (s)
2. Verifica que se crea el archivo `.txt`
3. **El archivo se guarda en el directorio `historias/` dentro de la carpeta del programa**
4. El programa creará el directorio `historias/` automáticamente si no existe
5. El programa te mostrará la ruta completa donde se guardó
6. Abre el archivo para ver el contenido

**Ejemplo:**
- Si ejecutas desde: `C:\Users\jorge\Desktop\programa`
- El archivo se guardará en: `C:\Users\jorge\Desktop\programa\historias\historia_coco.txt`

## Solución de Problemas

**Error: "python no se reconoce"**
- Usa `python3` en lugar de `python`
- O verifica que Python esté instalado

**Error de codificación (caracteres raros)**
- El programa usa UTF-8, debería funcionar bien
- Si ves problemas, verifica la codificación de tu terminal

**El programa no responde**
- Asegúrate de escribir respuestas y presionar Enter
- No dejes campos vacíos (a menos que diga "opcional")

## Verificación Rápida

Si todo funciona correctamente, deberías poder:
- ✅ Ver el menú principal
- ✅ Crear un superhéroe simple
- ✅ Crear un superhéroe con IA (modo demo)
- ✅ Procesar varios superhéroes automáticamente
- ✅ Guardar archivos

## Nota Importante

El programa funciona en **modo demo** sin necesidad de configurar APIs de IA reales. Las historias serán textos de ejemplo, pero el flujo del programa es exactamente el mismo que con IA real.

Para usar IA real, el profesor debe configurar la función `pedir_a_la_ia()` según `INSTRUCCIONES_PROFESOR.md`.
