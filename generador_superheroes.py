"""
==================================================
  GENERADOR DE SUPERHÉROES CON IA
  Versión para niños de 10 años
==================================================

Este programa enseña:
  1. Cómo hacer preguntas al usuario (input)
  2. Cómo guardar respuestas en variables
  3. Cómo combinar texto (concatenación)
  4. Cómo usar la IA dentro de un programa
  5. Cómo automatizar tareas repetitivas (bucles)

Lo más importante:
  El Nivel 2 Avanzado muestra cómo procesar VARIOS
  superhéroes automáticamente. Esto es algo que NO
  se puede hacer solo conversando con la IA.

Estructura del programa:
  - Entrada: Recibe datos del usuario
  - Proceso: Construye prompts y llama a la IA
  - Salida: Muestra o guarda los resultados

Autor: Para uso educativo
Fecha: 2024
"""


# ============================================
# FUNCIÓN HELPER PARA LA IA (configurada por el profesor)
# ============================================
def pedir_a_la_ia(mensaje):
    """
    Esta función llama a la IA para generar historias.
    Configurada para usar Groq (gratis y rápido).

    La API key se lee del archivo .env para mayor seguridad.
    """
    import os

    # Intentar cargar variables de entorno desde .env
    try:
        from dotenv import load_dotenv

        # Cargar .env con encoding UTF-8 explícito
        load_dotenv(encoding="utf-8")
    except ImportError:
        # Si no está instalado python-dotenv, intentar leer directamente
        pass
    except Exception as e:
        # Si hay error al cargar .env, continuar sin él (modo demo)
        pass

    # Leer API key del archivo .env o variable de entorno
    API_KEY_GROQ = os.getenv("GROQ_API_KEY") or os.getenv("API_KEY_GROQ")

    # Si no está configurada, usar modo demo
    if not API_KEY_GROQ:
        # MODO DEMO: Genera una historia de ejemplo
        import re

        nombre_match = re.search(r"llamado (\w+(?:\s+\w+)?)", mensaje)
        poder_match = re.search(r"poder de ([^.]+)", mensaje)
        origen_match = re.search(r"viene de ([^.]+)", mensaje)

        nombre = nombre_match.group(1) if nombre_match else "el superhéroe"
        poder = poder_match.group(1).strip() if poder_match else "poderes especiales"
        origen = (
            origen_match.group(1).strip()
            if origen_match
            else "circunstancias especiales"
        )

        historia = f"""HISTORIA DE {nombre.upper()}

{nombre} es un superhéroe extraordinario cuya vida cambió para siempre cuando {origen}. 
Este evento transformó completamente su existencia y le otorgó el increíble poder de {poder}.

Desde ese momento, {nombre} ha dedicado su vida a usar sus habilidades para proteger 
a los inocentes y luchar contra el mal. Su poder de {poder} le permite realizar hazañas 
que parecen imposibles para los humanos comunes.

Aunque a veces se siente solo en su misión, {nombre} sabe que su responsabilidad es 
grande. Cada día enfrenta nuevos desafíos, pero nunca se rinde. Su determinación y 
sus poderes especiales lo convierten en un verdadero héroe.

La historia de {nombre} es una inspiración para todos aquellos que creen que un solo 
individuo puede marcar la diferencia en el mundo."""

        return historia

    # MODO REAL: Usar Groq API
    try:
        from groq import Groq

        client = Groq(api_key=API_KEY_GROQ)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Modelo rápido y gratuito
            messages=[
                {
                    "role": "system",
                    "content": "Eres un escritor creativo que crea historias de superhéroes para niños de 10 años. Las historias deben ser cortas (3-4 párrafos), emocionantes y apropiadas para niños.",
                },
                {"role": "user", "content": mensaje},
            ],
            max_tokens=300,
            temperature=0.8,
        )

        return response.choices[0].message.content

    except Exception as e:
        # Si hay error, mostrar mensaje y usar modo demo
        print(f"\n[AVISO] Error al conectar con Groq: {e}")
        print("[INFO] Usando modo demo...")

        # Volver a modo demo como fallback
        import re

        nombre_match = re.search(r"llamado (\w+(?:\s+\w+)?)", mensaje)
        poder_match = re.search(r"poder de ([^.]+)", mensaje)
        origen_match = re.search(r"viene de ([^.]+)", mensaje)

        nombre = nombre_match.group(1) if nombre_match else "el superhéroe"
        poder = poder_match.group(1).strip() if poder_match else "poderes especiales"
        origen = (
            origen_match.group(1).strip()
            if origen_match
            else "circunstancias especiales"
        )

        return f"""HISTORIA DE {nombre.upper()}

{nombre} es un superhéroe extraordinario cuya vida cambió para siempre cuando {origen}. 
Este evento transformó completamente su existencia y le otorgó el increíble poder de {poder}.

Desde ese momento, {nombre} ha dedicado su vida a usar sus habilidades para proteger 
a los inocentes y luchar contra el mal."""


# ============================================
# FUNCIONES AUXILIARES PARA LA INTERFAZ
# ============================================
def mostrar_titulo():
    """Muestra el título del programa"""
    print("=" * 50)
    print("    GENERADOR DE SUPERHÉROES CON IA")
    print("=" * 50)
    print()


def mostrar_separador():
    """Muestra un separador visual"""
    print("-" * 50)
    print()


def preguntar(texto, requerido=True):
    """Hace una pregunta y devuelve la respuesta"""
    while True:
        respuesta = input(f"  {texto}: ").strip()
        if requerido and respuesta == "":
            print("  [AVISO] Este campo es obligatorio. Por favor, escribe algo.")
            continue
        return respuesta


def es_respuesta_afirmativa(respuesta):
    """Verifica si la respuesta es afirmativa (s, si, sí, yes, y)"""
    respuesta_limpia = respuesta.strip().lower()
    respuestas_afirmativas = ["s", "si", "sí", "yes", "y", "ok", "vale"]
    return respuesta_limpia in respuestas_afirmativas


def limpiar_nombre_archivo(nombre):
    """Limpia el nombre para que sea válido como nombre de archivo"""
    import re

    # Reemplazar espacios y caracteres problemáticos
    nombre_limpio = nombre.replace(" ", "_")
    # Eliminar caracteres no permitidos en nombres de archivo
    nombre_limpio = re.sub(r'[<>:"/\\|?*]', "", nombre_limpio)
    # Limitar longitud
    if len(nombre_limpio) > 50:
        nombre_limpio = nombre_limpio[:50]
    return nombre_limpio


def listar_historias_guardadas():
    """Lista las historias guardadas en el directorio historias"""
    import os

    directorio_historias = "historias"

    if not os.path.exists(directorio_historias):
        print("\n[INFO] Aún no has guardado ninguna historia.")
        print(
            "       El directorio 'historias' se creará cuando guardes tu primera historia."
        )
        return []

    archivos = [f for f in os.listdir(directorio_historias) if f.endswith(".txt")]

    if len(archivos) == 0:
        print("\n[INFO] No hay historias guardadas aún.")
        return []

    print("\n" + "=" * 50)
    print("  HISTORIAS GUARDADAS")
    print("=" * 50)
    print()
    print(f"Total: {len(archivos)} archivo(s) guardado(s)\n")

    for i, archivo in enumerate(sorted(archivos), 1):
        ruta_completa = os.path.abspath(os.path.join(directorio_historias, archivo))
        tamaño = os.path.getsize(ruta_completa)
        print(f"  {i}. {archivo}")
        print(f"     Tamaño: {tamaño} bytes")
        print(f"     Ruta: {ruta_completa}")
        print()

    print("=" * 50)

    # Preguntar si quiere ver el contenido de alguna historia
    if len(archivos) > 0:
        print("\n¿Quieres ver el contenido de alguna historia?")
        print("  (Escribe el número de la historia, o presiona ENTER para salir)")
        respuesta = input("  Opción: ").strip()

        if respuesta.isdigit():
            num = int(respuesta)
            if 1 <= num <= len(archivos):
                ver_historia_guardada(archivos[num - 1])
            else:
                print(
                    f"\n[AVISO] Número inválido. Debe estar entre 1 y {len(archivos)}"
                )

    return archivos


def ver_historia_guardada(nombre_archivo):
    """Muestra el contenido de una historia guardada"""
    import os

    directorio_historias = "historias"
    ruta_archivo = os.path.join(directorio_historias, nombre_archivo)

    if not os.path.exists(ruta_archivo):
        print(f"\n[ERROR] El archivo '{nombre_archivo}' no existe.")
        return

    try:
        print("\n" + "=" * 50)
        print(f"  CONTENIDO: {nombre_archivo}")
        print("=" * 50)
        print()

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido)

        print("=" * 50)
    except Exception as e:
        print(f"\n[ERROR] No se pudo leer el archivo: {e}")


def guardar_historias(historias, nombre_archivo="historias_superheroes.txt"):
    """Guarda las historias en un archivo de texto dentro del directorio 'historias'"""
    import os
    from datetime import datetime

    try:
        # Crear directorio 'historias' si no existe
        directorio_historias = "historias"
        if not os.path.exists(directorio_historias):
            os.makedirs(directorio_historias)
            print(f"\n[INFO] Directorio '{directorio_historias}' creado")

        # Ruta completa del archivo dentro del directorio historias
        ruta_archivo = os.path.join(directorio_historias, nombre_archivo)
        ruta_completa = os.path.abspath(ruta_archivo)

        # Obtener fecha y hora actual
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("=" * 50 + "\n")
            archivo.write("  HISTORIAS DE SUPERHÉROES GENERADAS\n")
            archivo.write(f"  Fecha: {fecha_actual}\n")
            archivo.write("=" * 50 + "\n\n")

            for heroe_info in historias:
                archivo.write("=" * 50 + "\n")
                archivo.write(f"  {heroe_info['nombre'].upper()}\n")
                archivo.write("=" * 50 + "\n\n")
                archivo.write(heroe_info["historia"] + "\n\n")

            archivo.write("=" * 50 + "\n")
            archivo.write(f"Total: {len(historias)} historias generadas\n")
            archivo.write("=" * 50 + "\n")

        print(f"\n[OK] Historias guardadas en:")
        print(f"     Archivo: {directorio_historias}/{nombre_archivo}")
        print(f"     Ruta completa: {ruta_completa}")
        return True
    except Exception as e:
        print(f"\n[ERROR] Error al guardar: {e}")
        return False


# ============================================
# NIVEL 1: Versión simple sin IA
# ============================================
def crear_superheroe_simple():
    """Crea un superhéroe simple sin usar IA"""
    mostrar_titulo()
    print("NIVEL 1: Crear un superhéroe simple")
    mostrar_separador()

    # Hacer preguntas
    nombre = preguntar("¿Cómo se llama tu superhéroe?")
    poder = preguntar("¿Qué poder especial tiene?")
    origen = preguntar(
        "¿De dónde viene su poder? (ej: accidente, nacimiento, experimento)"
    )

    # Crear el texto combinando las respuestas
    texto = f"\n{'='*50}\n"
    texto += f"  MI SUPERHÉROE\n"
    texto += f"{'='*50}\n\n"
    texto += f"Nombre: {nombre}\n"
    texto += f"Poder: {poder}\n"
    texto += f"Origen: {origen}\n"
    texto += f"\n{nombre} es un superhéroe increíble con el poder de {poder}.\n"
    texto += f"Su poder viene de {origen}.\n"

    # Mostrar el resultado
    print()
    print(texto)
    print("=" * 50)

    # Preguntar si quiere guardar
    guardar = input("\n¿Quieres guardar este superhéroe en un archivo? (s/n): ")
    if es_respuesta_afirmativa(guardar):
        # Crear formato más completo y estructurado para guardar
        contenido_guardar = f"""INFORMACIÓN DEL SUPERHÉROE

Nombre: {nombre}
Poder: {poder}
Origen del poder: {origen}

DESCRIPCIÓN:

{nombre} es un superhéroe increíble con el poder de {poder}. 
Su poder viene de {origen}, lo que lo convierte en un personaje único y especial.

Aunque este es solo un resumen básico, {nombre} tiene el potencial de convertirse 
en un héroe legendario. Con su poder de {poder}, puede enfrentar cualquier desafío 
que se le presente.

Este superhéroe fue creado usando el Nivel 1 del programa (sin IA), 
demostrando cómo se pueden combinar datos del usuario para crear descripciones."""

        historias = [{"nombre": nombre, "historia": contenido_guardar}]
        nombre_archivo = f"superheroe_{limpiar_nombre_archivo(nombre)}.txt"
        guardar_historias(historias, nombre_archivo)

    return texto


# ============================================
# NIVEL 2: Versión con IA (UN superhéroe)
# ============================================
def crear_superheroe_con_ia():
    """Crea un superhéroe usando IA para generar la historia"""
    mostrar_titulo()
    print("NIVEL 2: Crear un superhéroe con IA")
    mostrar_separador()

    # Hacer preguntas
    nombre = preguntar("¿Cómo se llama tu superhéroe?")
    poder = preguntar("¿Qué poder especial tiene?")
    origen = preguntar("¿De dónde viene su poder?")
    color_traje = preguntar("¿Qué color de traje tiene? (opcional)", requerido=False)

    # Construir el mensaje para la IA
    mensaje = (
        f"Crea una historia corta y divertida sobre un superhéroe llamado {nombre} "
    )
    mensaje += f"que tiene el poder de {poder}. Su poder viene de {origen}. "
    if color_traje:
        mensaje += f"Lleva un traje de color {color_traje}. "
    mensaje += "La historia debe ser de 3-4 párrafos y debe ser emocionante."

    print("\n  Generando historia con IA... Por favor espera...\n")

    # Pedir a la IA que cree la historia
    historia = pedir_a_la_ia(mensaje)

    # Mostrar el resultado
    print("=" * 50)
    print(f"  HISTORIA DE {nombre.upper()}")
    print("=" * 50)
    print()
    print(historia)
    print()
    print("=" * 50)

    # Preguntar si quiere guardar
    guardar = input("\n¿Quieres guardar esta historia en un archivo? (s/n): ")
    if es_respuesta_afirmativa(guardar):
        historias = [{"nombre": nombre, "historia": historia}]
        nombre_archivo = f"historia_{limpiar_nombre_archivo(nombre)}.txt"
        guardar_historias(historias, nombre_archivo)

    return historia


# ============================================
# NIVEL 2 AVANZADO: Varios superhéroes automáticamente
# ============================================
def obtener_lista_superheroes():
    """Permite elegir entre lista predefinida o crear una propia"""
    print("¿Qué quieres hacer?")
    print("  1. Usar lista predefinida (3 superhéroes)")
    print("  2. Crear mi propia lista")
    print()
    opcion = input("  Elige (1 o 2): ").strip()

    if opcion == "2":
        # Crear lista propia
        superheroes = []
        print("\nVamos a crear tu lista de superhéroes.")
        print("(Escribe 'fin' cuando termines)\n")

        contador = 1
        while True:
            print(f"Superhéroe {contador}:")
            nombre = input("  Nombre: ").strip()
            if nombre.lower() == "fin" or nombre == "":
                break

            poder = input("  Poder: ").strip()
            origen = input("  Origen del poder: ").strip()

            superheroes.append({"nombre": nombre, "poder": poder, "origen": origen})
            contador += 1
            print()

        if len(superheroes) == 0:
            print("\nNo creaste ningún superhéroe. Usando lista predefinida...\n")
            opcion = "1"
        else:
            return superheroes

    # Lista predefinida (cargar desde JSON)
    if opcion == "1" or opcion != "2":
        datos = cargar_datos_superheroes()
        return datos.get(
            "lista_predefinida",
            [
                {
                    "nombre": "Rayo Veloz",
                    "poder": "velocidad y electricidad",
                    "origen": "un accidente con un rayo",
                },
                {
                    "nombre": "Sombra Nocturna",
                    "poder": "invisibilidad",
                    "origen": "un experimento científico",
                },
                {
                    "nombre": "Fuerza Mental",
                    "poder": "telequinesis",
                    "origen": "nacimiento con poderes especiales",
                },
            ],
        )


def crear_varios_superheroes():
    """Crea varios superhéroes automáticamente usando IA"""
    mostrar_titulo()
    print("NIVEL 2 AVANZADO: Crear varios superhéroes automáticamente")
    mostrar_separador()

    # Obtener lista de superhéroes
    superheroes = obtener_lista_superheroes()

    if len(superheroes) == 0:
        print("No hay superhéroes para procesar.")
        return []

    # Mostrar la lista
    print("\nVamos a crear historias para estos superhéroes:")
    print()
    for i, heroe in enumerate(superheroes, 1):
        print(f"  {i}. {heroe['nombre']} - Poder: {heroe['poder']}")
    print()
    print(f"Total: {len(superheroes)} superhéroe(s)")
    print()

    input("Presiona ENTER para comenzar a generar las historias...")
    print()

    # Procesar cada superhéroe automáticamente
    todas_las_historias = []

    for i, heroe in enumerate(superheroes, 1):
        print(f"[{i}/{len(superheroes)}] Generando historia de {heroe['nombre']}...")

        # Construir el mensaje para la IA
        mensaje = f"Crea una historia corta y divertida sobre un superhéroe llamado {heroe['nombre']} "
        mensaje += f"que tiene el poder de {heroe['poder']}. Su poder viene de {heroe['origen']}. "
        mensaje += "La historia debe ser de 3-4 párrafos y debe ser emocionante."

        # Pedir a la IA que cree la historia
        historia = pedir_a_la_ia(mensaje)

        todas_las_historias.append({"nombre": heroe["nombre"], "historia": historia})

        print(f"  ✓ Historia de {heroe['nombre']} completada!\n")

    # Mostrar todos los resultados
    print("\n" + "=" * 50)
    print("  TODAS LAS HISTORIAS GENERADAS")
    print("=" * 50)
    print()

    for heroe_info in todas_las_historias:
        print("=" * 50)
        print(f"  {heroe_info['nombre'].upper()}")
        print("=" * 50)
        print()
        print(heroe_info["historia"])
        print()

    print("=" * 50)
    print(f"\n¡Listo! Se generaron {len(superheroes)} historias automáticamente.")
    print("Sin programación, tendrías que hacerlo una por una manualmente.")
    print()

    # Preguntar si quiere guardar
    guardar = input("¿Quieres guardar las historias en un archivo? (s/n): ")
    if es_respuesta_afirmativa(guardar):
        guardar_historias(todas_las_historias)

    return todas_las_historias


# ============================================
# MODO ALEATORIO: Generar superhéroes aleatorios
# ============================================
def cargar_datos_superheroes():
    """Carga los datos de superhéroes desde el archivo JSON"""
    import json
    import os

    try:
        ruta_json = os.path.join(os.path.dirname(__file__), "datos_superheroes.json")
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Si no existe el JSON, usar datos por defecto
        return {
            "nombres": ["Rayo Veloz", "Sombra Nocturna", "Fuerza Mental"],
            "poderes": ["velocidad", "invisibilidad", "telequinesis"],
            "origenes": ["un accidente", "un experimento", "nacimiento"],
            "lista_predefinida": [
                {"nombre": "Rayo Veloz", "poder": "velocidad", "origen": "un accidente"}
            ],
        }
    except Exception:
        # En caso de error, devolver datos mínimos
        return {
            "nombres": ["Superhéroe"],
            "poderes": ["poderes especiales"],
            "origenes": ["origen especial"],
            "lista_predefinida": [],
        }


def generar_superheroe_aleatorio():
    """Genera un superhéroe aleatorio con nombre, poder y origen"""
    import random

    datos = cargar_datos_superheroes()

    return {
        "nombre": random.choice(datos["nombres"]),
        "poder": random.choice(datos["poderes"]),
        "origen": random.choice(datos["origenes"]),
    }


def crear_superheroes_aleatorios():
    """Crea varios superhéroes aleatorios automáticamente usando IA"""
    mostrar_titulo()
    print("MODO ALEATORIO: Generar superhéroes aleatorios con IA")
    mostrar_separador()

    print("Este modo genera superhéroes aleatorios automáticamente.")
    print("El programa crea nombres, poderes y orígenes aleatorios,")
    print("y luego usa IA para generar historias creativas para cada uno.")
    print("¡Es divertido ver qué personajes se crean!")
    print()

    # Preguntar cuántos superhéroes generar
    try:
        cantidad = input("¿Cuántos superhéroes quieres generar? (1-10): ").strip()
        cantidad = int(cantidad)
        if cantidad < 1 or cantidad > 10:
            print("Usando 3 superhéroes por defecto.")
            cantidad = 3
    except ValueError:
        print("Usando 3 superhéroes por defecto.")
        cantidad = 3

    print()
    print(f"Generando {cantidad} superhéroe(s) aleatorio(s)...")
    print()

    # Generar lista de superhéroes aleatorios
    superheroes = []
    for i in range(cantidad):
        heroe = generar_superheroe_aleatorio()
        superheroes.append(heroe)

    # Mostrar la lista generada
    print("Superhéroes generados:")
    print()
    for i, heroe in enumerate(superheroes, 1):
        print(f"  {i}. {heroe['nombre']} - Poder: {heroe['poder']}")
    print()

    input("Presiona ENTER para comenzar a generar las historias...")
    print()

    # Procesar cada superhéroe automáticamente
    todas_las_historias = []

    for i, heroe in enumerate(superheroes, 1):
        print(
            f"[{i}/{len(superheroes)}] Generando historia de {heroe['nombre']} con IA..."
        )

        # Construir el mensaje para la IA
        mensaje = f"Crea una historia corta y divertida sobre un superhéroe llamado {heroe['nombre']} "
        mensaje += f"que tiene el poder de {heroe['poder']}. Su poder viene de {heroe['origen']}. "
        mensaje += "La historia debe ser de 3-4 párrafos y debe ser emocionante."

        # Pedir a la IA que cree la historia
        historia = pedir_a_la_ia(mensaje)

        todas_las_historias.append({"nombre": heroe["nombre"], "historia": historia})

        print(f"  [OK] Historia de {heroe['nombre']} generada con IA!\n")

    # Mostrar todos los resultados
    print("\n" + "=" * 50)
    print("  TODAS LAS HISTORIAS GENERADAS")
    print("=" * 50)
    print()

    for heroe_info in todas_las_historias:
        print("=" * 50)
        print(f"  {heroe_info['nombre'].upper()}")
        print("=" * 50)
        print()
        print(heroe_info["historia"])
        print()

    print("=" * 50)
    print(
        f"\n¡Listo! Se generaron {len(superheroes)} historias automáticamente con IA."
    )
    print(
        "El programa creó los superhéroes aleatorios y usó IA para generar sus historias"
    )
    print("sin que tú tuvieras que escribir nada.")
    print()

    # Preguntar si quiere guardar
    guardar = input("¿Quieres guardar las historias en un archivo? (s/n): ")
    if es_respuesta_afirmativa(guardar):
        guardar_historias(todas_las_historias, "superheroes_aleatorios.txt")

    return todas_las_historias


# ============================================
# MENÚ PRINCIPAL
# ============================================
def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("    MENÚ PRINCIPAL")
    print("=" * 50)
    print()
    print("  1. Nivel 1: Crear un superhéroe simple (sin IA)")
    print("  2. Nivel 2: Crear un superhéroe con IA")
    print("  3. Nivel 2 Avanzado: Crear varios superhéroes automáticamente")
    print("  4. Modo Aleatorio: Generar superhéroes aleatorios con IA (¡divertido!)")
    print("  5. Ver historias guardadas")
    print("  6. Ver estadísticas")
    print("  7. Ver información sobre el programa")
    print("  8. Salir")
    print()
    print("=" * 50)
    print()


def mostrar_estadisticas():
    """Muestra estadísticas simples del programa"""
    import os

    directorio_historias = "historias"
    mostrar_titulo()
    print("ESTADÍSTICAS")
    mostrar_separador()

    if not os.path.exists(directorio_historias):
        print("Aún no has guardado ninguna historia.")
        print("¡Crea tu primer superhéroe para comenzar!")
        return

    archivos = [f for f in os.listdir(directorio_historias) if f.endswith(".txt")]
    total_archivos = len(archivos)

    if total_archivos == 0:
        print("Aún no has guardado ninguna historia.")
        print("¡Crea tu primer superhéroe para comenzar!")
    else:
        print(f"📊 Total de historias guardadas: {total_archivos}")

        # Calcular tamaño total
        tamaño_total = 0
        for archivo in archivos:
            ruta = os.path.join(directorio_historias, archivo)
            tamaño_total += os.path.getsize(ruta)

        print(f"📁 Tamaño total: {tamaño_total} bytes ({tamaño_total/1024:.2f} KB)")
        print(f"📂 Ubicación: {os.path.abspath(directorio_historias)}")

        if total_archivos > 0:
            print(f"\n✨ ¡Has creado {total_archivos} superhéroe(s)! ¡Sigue así!")

    mostrar_separador()
    input("Presiona ENTER para volver al menú...")


def mostrar_informacion():
    """Muestra información educativa sobre el programa"""
    mostrar_titulo()
    print("INFORMACIÓN SOBRE EL PROGRAMA")
    mostrar_separador()

    print("Este programa te enseña:")
    print()
    print("  1. Cómo hacer preguntas al usuario")
    print("  2. Cómo guardar respuestas en variables")
    print("  3. Cómo combinar texto")
    print("  4. Cómo usar la IA dentro de un programa")
    print("  5. Cómo hacer que el programa repita algo automáticamente")
    print()
    mostrar_separador()

    print("Modos del programa:")
    print()
    print("  Opción 3 (Didáctico):")
    print("    - Tú defines los superhéroes")
    print("    - El programa procesa tus datos automáticamente")
    print("    - Muestra claramente: entrada → proceso → salida")
    print()
    print("  Opción 4 (Aleatorio con IA):")
    print("    - El programa genera superhéroes aleatorios")
    print("    - Usa IA para crear historias creativas")
    print("    - Más divertido, menos control")
    print("    - También demuestra automatización")
    print()
    mostrar_separador()

    print("¿Por qué es importante el Nivel 2 Avanzado?")
    print()
    print("  Sin programación:")
    print("    - Tendrías que pedir cada historia una por una")
    print("    - Tendrías que copiar y pegar cada vez")
    print("    - Sería muy lento y aburrido")
    print()
    print("  Con programación:")
    print("    - El programa lo hace automáticamente")
    print("    - Puedes crear muchas historias en segundos")
    print("    - Es rápido y divertido")
    print()
    print("  ¡Esto es lo que NO puedes hacer solo conversando con la IA!")
    print()
    mostrar_separador()

    input("Presiona ENTER para volver al menú...")


def main():
    """Función principal del programa"""
    # Mostrar bienvenida inicial
    mostrar_titulo()
    print("¡Bienvenido al Generador de Superhéroes con IA!")
    print()
    print("Este programa te enseña cómo usar la programación")
    print("para hacer que la IA trabaje para ti automáticamente.")
    print()
    input("Presiona ENTER para comenzar...")

    while True:
        mostrar_menu()
        opcion = input("  Elige una opción (1-8): ").strip()

        try:
            if opcion == "1":
                crear_superheroe_simple()
                input("\nPresiona ENTER para volver al menú...")

            elif opcion == "2":
                crear_superheroe_con_ia()
                input("\nPresiona ENTER para volver al menú...")

            elif opcion == "3":
                crear_varios_superheroes()
                input("\nPresiona ENTER para volver al menú...")

            elif opcion == "4":
                crear_superheroes_aleatorios()
                input("\nPresiona ENTER para volver al menú...")

            elif opcion == "5":
                listar_historias_guardadas()
                input("\nPresiona ENTER para volver al menú...")

            elif opcion == "6":
                mostrar_estadisticas()

            elif opcion == "7":
                mostrar_informacion()

            elif opcion == "8":
                confirmar = (
                    input("\n¿Estás seguro de que quieres salir? (s/n): ")
                    .strip()
                    .lower()
                )
                if confirmar == "s":
                    print("\n" + "=" * 50)
                    print("  ¡Gracias por usar el Generador de Superhéroes!")
                    print("  ¡Hasta pronto!")
                    print("=" * 50)
                    break
                else:
                    print("\n[INFO] Continuando en el programa...")
                    input("Presiona ENTER para volver al menú...")

            else:
                print(
                    "\n  [ERROR] Opción no válida. Por favor elige un número del 1 al 8."
                )
                input("\nPresiona ENTER para continuar...")
        except KeyboardInterrupt:
            print("\n\n[INFO] Operación cancelada por el usuario.")
            input("Presiona ENTER para volver al menú...")
        except Exception as e:
            print(f"\n  [ERROR] Ocurrió un error: {e}")
            print("  Por favor, intenta de nuevo.")
            input("\nPresiona ENTER para continuar...")


# ============================================
# EJECUTAR EL PROGRAMA
# ============================================
if __name__ == "__main__":
    main()
