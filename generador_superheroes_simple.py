"""
Generador de Superhéroes - Versión MUY SIMPLE
Para empezar paso a paso
"""

# ============================================
# PASO 1: Hacer preguntas y guardar respuestas
# ============================================
print("=" * 50)
print("    GENERADOR DE SUPERHÉROES")
print("=" * 50)
print()

# Hacer preguntas
nombre = input("¿Cómo se llama tu superhéroe? ")
poder = input("¿Qué poder especial tiene? ")
origen = input("¿De dónde viene su poder? ")

print()
print("-" * 50)
print()

# ============================================
# PASO 2: Crear el texto combinando las respuestas
# ============================================
texto = f"Mi superhéroe se llama {nombre}.\n"
texto += f"Tiene el poder de {poder}.\n"
texto += f"Su poder viene de {origen}.\n"

# ============================================
# PASO 3: Mostrar el resultado
# ============================================
print("RESULTADO:")
print("=" * 50)
print()
print(texto)
print("=" * 50)

print()
print("¡Listo! Has creado tu primer superhéroe con programación.")
print()
