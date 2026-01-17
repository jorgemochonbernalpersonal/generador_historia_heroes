# Desarrollo técnico del caso práctico: Generador de superhéroes con IA

**Versión adaptada para niños de 10 años**

Este documento describe un ejercicio simplificado pensado para alumnos de primaria (10 años). El enfoque es práctico, visual y progresivo, evitando conceptos abstractos o técnicos complejos.

## 0. Conceptos previos necesarios

Para realizar este ejercicio, el alumno solo necesita conocer:

- Cómo hacer una pregunta al usuario (por ejemplo: `input()` en Python)
- Cómo guardar una respuesta en una variable (por ejemplo: `nombre = input("¿Cuál es tu nombre?")`)
- Cómo mostrar texto en pantalla (por ejemplo: `print()` en Python)
- Cómo crear un texto combinando variables (concatenación o f-strings simples)

**Nota importante para niños de 10 años:** 
- **NO es necesario conocer funciones** - el código se puede escribir directamente, paso a paso.
- **NO es necesario entender APIs complejas** - el profesor proporcionará una función muy simple que solo hay que "llamar" como si fuera un comando mágico.
- El enfoque es **práctico y visual**, no teórico.

**Configuración previa:** El profesor habrá configurado el acceso a la IA y proporcionado una función helper **muy simple** que funciona así:

```python
# El profesor ya configuró esto - los niños solo lo usan
respuesta = pedir_a_la_ia("Escribe sobre un superhéroe llamado " + nombre)
```

Los niños no necesitan entender cómo funciona por dentro, solo cómo usarla.

## 1. Objetivo técnico del ejercicio

Crear una **herramienta sencilla** que:

- Recibe una entrada (una lista de superhéroes con sus características).
- **Utiliza la IA para procesar esa información** creando historias automáticamente.
- Produce una salida estructurada (las historias generadas).
- **Es reutilizable:** puedes ejecutarla varias veces con diferentes listas de superhéroes.

**Versión simplificada para empezar (Nivel 1):**
Primero haremos una versión sin IA que solo combina las respuestas. Esto ayuda a entender el proceso básico.

**Versión con IA (Nivel 2 - La importante):**
Luego añadimos la IA y hacemos que el programa cree **3-5 superhéroes automáticamente**. Esto es lo que **NO se puede hacer solo conversando** con la IA.

Desde el punto de vista técnico, el alumno debe entender que:
- El programa sigue siempre el mismo proceso, aunque cambien las respuestas.
- **Con la IA, el programa puede crear historias más creativas automáticamente.**
- **Lo más importante: el programa puede crear VARIOS superhéroes automáticamente, sin tener que hacerlo uno por uno.**
- **Esto es lo que demuestra el valor de la programación: automatizar tareas repetitivas.**
- **Es una herramienta reutilizable:** puedes cambiar la lista de superhéroes y ejecutar el programa de nuevo.

## 2. Estructura general del programa

Antes de escribir nada, se explica que todo el programa tiene cuatro partes, siempre en este orden:

1. **Entrada de datos**
2. **Proceso**
3. **Generación del resultado**
4. **Salida**

Este esquema se repite en cualquier programa, aunque sea más complejo.

### Estructura básica del código (pseudocódigo)

Para que el alumno visualice la estructura, se puede mostrar algo como:

**NIVEL 1 - Sin IA (para empezar):**
```
1. HACER PREGUNTAS
   - Preguntar: "¿Cómo se llama tu superhéroe?" → guardar en "nombre"
   - Preguntar: "¿Qué poder tiene?" → guardar en "poder"
   - Preguntar: "¿De dónde viene su poder?" → guardar en "origen"

2. CREAR EL TEXTO
   - Combinar todo: "Mi superhéroe se llama " + nombre + " y tiene el poder de " + poder

3. MOSTRAR
   - Imprimir el texto en pantalla
```

**NIVEL 2 - Con IA (más creativo y AUTOMÁTICO):**
```
1. PREPARAR VARIOS SUPERHÉROES
   - Crear una lista simple con 3-5 superhéroes (nombre, poder, origen)

2. PARA CADA SUPERHÉROE (hacer lo mismo automáticamente):
   - Construir el mensaje para la IA
   - Pedir a la IA que cree la historia: historia = pedir_a_la_ia("Crea una historia sobre " + nombre + " que tiene " + poder)
   - La IA crea una historia completa automáticamente
   - Mostrar la historia

3. RESULTADO
   - El programa ha creado 3-5 historias automáticamente
   - Sin programación, tendrías que hacerlo una por una manualmente
```

Esta estructura ayuda a entender que el programa sigue un orden lógico, paso a paso. **La IA es como un ayudante que crea historias cuando se le pide, y el programa puede pedirle que cree VARIAS historias automáticamente.**

## 3. Paso 1: Entrada de datos (preguntas al usuario)

### Qué hay que hacer

- Formular varias preguntas al usuario.
- Cada respuesta debe guardarse en una variable distinta.

### Qué debe quedar claro al alumno

- Una variable es una "caja" donde se guarda una respuesta.
- El programa recuerda esas respuestas para usarlas después.
- Si cambia la respuesta, cambia el resultado final.

### Decisión de diseño

Las preguntas deben ser coherentes entre sí (origen, motivación, poder, forma de actuar), porque el programa no inventa: combina lo que el usuario decide.

### Ejemplo de preguntas sugeridas (para niños de 10 años)

Para que el alumno tenga una referencia clara, se pueden usar preguntas simples como:

- "¿Cómo se llama tu superhéroe?"
- "¿Qué poder especial tiene? (ej: volar, super fuerza, invisibilidad)"
- "¿De dónde viene su poder? (ej: un accidente, nació con él, un experimento)"
- "¿Qué color de traje tiene?"
- "¿Tiene algún compañero o trabaja solo?"

**Nota:** Para niños de 10 años, es mejor usar 3-4 preguntas simples al principio. Pueden añadir más después si quieren.

## 4. Paso 2: Definir el proceso (función)

### Qué hay que hacer

- Crear una función que represente el proceso de creación del héroe.
- La función debe recibir como datos las respuestas del usuario.

**Nota para principiantes:** Si el alumno aún no conoce funciones, puede escribir el código directamente sin funciones. Una vez que funcione, se puede refactorizar usando una función para hacer el código más organizado y reutilizable.

### Qué debe quedar claro al alumno

- Una función es una "receta".
- La receta siempre es la misma.
- Los ingredientes cambian (las respuestas), pero el proceso no.

### Decisión de diseño

La función no debe preguntar nada al usuario. Solo debe usar los datos que recibe para construir el resultado.

## 5. Paso 3: Pedir a la IA que cree la historia

### Qué hay que hacer (NIVEL 1 - Sin IA)

Primero, crear un texto simple combinando las respuestas:

```python
texto = "Mi superhéroe se llama " + nombre
texto = texto + ". Tiene el poder de " + poder
texto = texto + ". Su poder viene de " + origen
print(texto)
```

### Qué hay que hacer (NIVEL 2 - Con IA para UN superhéroe)

Ahora, pedir a la IA que cree una historia más interesante:

```python
# Construir un mensaje simple para la IA
mensaje = "Crea una historia corta sobre un superhéroe llamado " + nombre
mensaje = mensaje + " que tiene el poder de " + poder
mensaje = mensaje + ". Su poder viene de " + origen

# Pedir a la IA que cree la historia (función que el profesor ya preparó)
historia = pedir_a_la_ia(mensaje)

# Mostrar lo que creó la IA
print(historia)
```

### Qué hay que hacer (NIVEL 2 AVANZADO - Con IA para VARIOS superhéroes)

**Este es el paso que demuestra el valor de la programación:**

```python
# Lista simple con varios superhéroes
superheroes = [
    {"nombre": "Rayo Veloz", "poder": "velocidad", "origen": "accidente"},
    {"nombre": "Sombra", "poder": "invisibilidad", "origen": "experimento"},
    {"nombre": "Fuerza", "poder": "super fuerza", "origen": "nacimiento"}
]

# Para cada superhéroe, hacer lo mismo automáticamente
for heroe in superheroes:
    mensaje = "Crea una historia sobre " + heroe["nombre"] + " que tiene " + heroe["poder"]
    historia = pedir_a_la_ia(mensaje)
    print("=== " + heroe["nombre"] + " ===")
    print(historia)
    print()  # línea en blanco
```

### Qué debe quedar claro al alumno

- **Sin IA:** El programa solo junta las palabras que escribiste.
- **Con IA (un superhéroe):** El programa le pide a la IA que cree una historia completa.
- **Con IA (varios superhéroes):** El programa crea VARIAS historias automáticamente.
- **Esto es lo importante:** Sin programación, tendrías que pedirle a la IA que cree cada historia una por una, manualmente. Con programación, el programa lo hace automáticamente.

### Para niños de 10 años

- No necesitan entender qué es un "prompt estructurado".
- Solo necesitan saber: "le digo a la IA qué quiero y ella lo crea".
- La función `pedir_a_la_ia()` es como un comando mágico que el profesor ya preparó.
- **Lo más importante:** Entienden que el programa puede hacer esto varias veces automáticamente.

### Ejemplo de salida esperada

**NIVEL 1 - Sin IA (simple):**
```
Mi superhéroe se llama Rayo Veloz. Tiene el poder de velocidad y electricidad. 
Su poder viene de un accidente con un rayo.
```

**NIVEL 2 - Con IA (más creativo):**
```
HISTORIA DE RAYO VELOZ

Rayo Veloz es un superhéroe increíble. Todo comenzó cuando un día estaba 
trabajando y un rayo muy poderoso lo alcanzó. En lugar de lastimarlo, 
el rayo le dio poderes especiales.

Ahora puede correr súper rápido y crear electricidad con sus manos. 
Usa sus poderes para ayudar a las personas y proteger la ciudad de los 
malvados. Le encanta trabajar con otros superhéroes porque sabe que 
juntos son más fuertes.

Cuando usa sus poderes, deja estelas de luz eléctrica cuando corre. 
Puede crear chispas pequeñas para asustar a los malos, o rayos grandes 
para detener peligros. También puede arreglar cosas eléctricas rotas, 
lo cual es muy útil para ayudar a la gente.
```

**Nota importante:** La versión con IA crea una historia más completa y divertida. Es como si tuvieras un ayudante que escribe historias por ti.

## 6. Paso 4: Ejecución del proceso

### Qué hay que hacer

- Llamar a la función creada.
- Pasarle las respuestas recogidas en el paso 1.

### Qué debe quedar claro al alumno

- Definir una función no hace nada por sí solo.
- El proceso solo ocurre cuando se ejecuta.
- El orden es importante.

## 7. Paso 5: Salida del programa

### Qué hay que hacer

- Mostrar en pantalla el resultado generado.
- (Opcional para niños avanzados) Guardar el resultado en un archivo para poder usarlo después.

### Qué debe quedar claro al alumno

- Un programa no solo calcula: comunica resultados.
- La salida es la parte visible del proceso.
- El usuario ve el resultado de sus decisiones.
- **La herramienta es reutilizable:** puedes ejecutar el programa varias veces con diferentes listas de superhéroes y obtener resultados diferentes cada vez.

## 7.1. Paso 6: La parte más importante - Crear VARIOS superhéroes automáticamente

### Por qué este paso es esencial

**Este es el paso que demuestra el valor real de la programación.**

Sin este paso, el ejercicio no cumple con el criterio del marco teórico: "crear algo que no se puede hacer solo conversando con la IA".

### Qué hay que hacer (versión simple para niños de 10 años)

El profesor puede proporcionar una lista predefinida o los niños pueden crear una lista simple:

```python
# Lista simple con 3 superhéroes
superheroes = [
    {"nombre": "Rayo Veloz", "poder": "velocidad", "origen": "accidente"},
    {"nombre": "Sombra", "poder": "invisibilidad", "origen": "experimento"},
    {"nombre": "Fuerza", "poder": "super fuerza", "origen": "nacimiento"}
]

# El programa hace esto para cada uno automáticamente
for heroe in superheroes:
    mensaje = "Crea una historia sobre " + heroe["nombre"] + " que tiene " + heroe["poder"]
    historia = pedir_a_la_ia(mensaje)
    print("=== " + heroe["nombre"] + " ===")
    print(historia)
    print()
```

### Por qué esto es importante

**Sin programación:**
- Tendrías que copiar y pegar cada superhéroe en el chat de la IA, uno por uno.
- Tendrías que esperar cada respuesta.
- Tendrías que copiar cada resultado manualmente.

**Con programación:**
- El programa hace todo automáticamente.
- Crea 3, 5 o 10 superhéroes en segundos.
- Todo queda guardado y organizado.

### Qué debe quedar claro al alumno

- **Esto NO se puede hacer solo conversando con la IA.**
- El programa trabaja para ti de forma automática.
- Puedes crear muchos superhéroes sin tener que hacerlo uno por uno.

### Nota para el profesor

Para niños de 10 años, el profesor puede:
- Proporcionar la lista de superhéroes predefinida.
- Explicar el bucle `for` de forma simple: "haz esto para cada uno".
- Enfocarse en que entiendan el concepto: "el programa lo hace automáticamente varias veces".
- No es necesario que entiendan toda la sintaxis, solo que funciona.
- **Enfatizar que es una herramienta:** Pueden cambiar la lista de superhéroes y ejecutar el programa de nuevo. Es como tener una herramienta que siempre funciona igual, pero con diferentes datos.

## 8. Relación con el uso de la IA

### Qué se explica al alumno (lenguaje simple)

- **Sin programación:** 
  - Tienes que escribir todo a mano o copiar y pegar en el chat de la IA cada vez.
  - Si quieres crear varios superhéroes, tienes que hacerlo **uno por uno, manualmente**.
  - Cada vez que quieres una historia, tienes que copiar y pegar los datos.

- **Con programación:** 
  - El programa hace el trabajo por ti:
    - Hace las preguntas automáticamente (o usa una lista)
    - Guarda las respuestas
    - Le pide a la IA que cree la historia
    - **Puede hacer esto VARIAS VECES automáticamente**
    - Te muestra todos los resultados

### Idea clave (para niños)

**El programa es una HERRAMIENTA que organiza todo y le pide a la IA que cree VARIAS historias automáticamente.**

- El programa **organiza** las preguntas y respuestas.
- La IA **crea** las historias divertidas.
- **Lo más importante:** El programa puede pedirle a la IA que cree **varias historias automáticamente**, sin tener que hacerlo una por una.
- **Es una herramienta reutilizable:** Puedes usar el programa muchas veces, cambiando la lista de superhéroes, y siempre funcionará igual.

### El cambio importante

**Antes:** 
- "Le pregunto cosas a la IA y ella me responde."
- "Si quiero varias historias, tengo que pedirlas una por una."

**Ahora:** 
- "Hago un programa que le pide a la IA que cree VARIAS historias automáticamente."
- "El programa hace el trabajo por mí varias veces."

**Esto es lo que NO se puede hacer solo conversando con la IA.**

**Es como tener un robot ayudante que hace el trabajo por ti, varias veces, automáticamente.**

## 9. Qué NO es necesario aprender

Es importante dejar explícito que no se evalúa:

- memorizar instrucciones,
- entender toda la sintaxis,
- escribir código perfecto.

El foco está en:

- entender el proceso,
- saber qué controla el usuario,
- y qué hace la herramienta.

## 9.1. Consejos para principiantes (especialmente niños de 10 años)

- **Empieza simple:** Comienza con solo 2-3 preguntas (nombre, poder, origen). Luego puedes añadir más.
- **Hazlo paso a paso:** Primero haz la versión sin IA (Nivel 1). Cuando funcione, añade la IA (Nivel 2).
- **No te preocupes si hay errores:** Es normal que no funcione a la primera. Prueba el programa paso a paso.
- **Pide ayuda:** Si te quedas atascado, pregunta al profesor. ¡No hay que saberlo todo!
- **Experimenta:** Cambia las respuestas varias veces y mira cómo cambia la historia que crea la IA.
- **Diviértete:** Este es un ejercicio creativo. ¡Disfruta creando tu superhéroe!

### Nota técnica sobre la implementación (para el profesor)

Para que el ejercicio sea accesible para niños de 10 años, el profesor debe proporcionar una función helper **muy simple**:

```python
def pedir_a_la_ia(mensaje):
    # Esta función ya está configurada por el profesor
    # Los niños solo la llaman así: historia = pedir_a_la_ia("Crea una historia sobre...")
    respuesta = openai_helper(mensaje)
    return respuesta
```

**Importante:** 
- Los niños NO necesitan entender cómo funciona por dentro.
- Solo necesitan saber cómo usarla: `resultado = pedir_a_la_ia("mensaje")`
- Es como un "comando mágico" que hace el trabajo.

## 10. Criterio de éxito técnico (adaptado para niños de 10 años)

El ejercicio se considera logrado cuando el alumno puede:

- **Hacer que el programa funcione:** El programa hace las preguntas, guarda las respuestas y muestra un resultado.
- **Entender las partes básicas:** Puede explicar (con palabras simples) qué parte hace las preguntas y qué parte muestra el resultado.
- **Usar la IA (Nivel 2):** Puede pedirle a la IA que cree una historia y mostrar el resultado.
- **Crear varios superhéroes automáticamente (ESENCIAL):** El programa puede crear 3-5 superhéroes automáticamente usando un bucle simple.
- **Reconocer el valor:** Entiende que crear varios superhéroes automáticamente es algo que **NO se puede hacer solo conversando** con la IA.

### Criterio de éxito simplificado

**Versión mínima (Nivel 1 - Sin IA):**
- El programa hace preguntas y muestra un texto combinando las respuestas.

**Versión completa (Nivel 2 - Con IA):**
- El programa hace preguntas, le pide a la IA que cree una historia, y muestra el resultado.

**Versión que cumple el marco teórico (Nivel 2 con procesamiento múltiple):**
- El programa crea **varios superhéroes automáticamente** (3-5) usando la IA.
- El alumno entiende que esto **no se puede hacer solo conversando** con la IA.

**No se evalúa:**
- Que el código sea perfecto
- Que entiendan toda la sintaxis del bucle `for`
- Que memoricen comandos

**Se evalúa:**
- Que entiendan el proceso (preguntar → guardar → procesar → mostrar)
- Que puedan hacer que funcione
- **Que entiendan que el programa puede hacer esto varias veces automáticamente**
- **Que reconozcan que esto es diferente a solo conversar con la IA**

## 11. Cierre pedagógico (adaptado para niños de 10 años)

### Qué aprendieron

Este ejercicio les muestra que:

1. **Pueden crear herramientas** (programas) que hacen cosas por ellos.
2. **Pueden usar la IA** como un ayudante que crea historias.
3. **El programa organiza todo** y le pide a la IA que trabaje.
4. **Lo más importante: el programa puede crear VARIAS historias automáticamente**, sin tener que hacerlo una por una.
5. **La herramienta es reutilizable:** Pueden ejecutarla varias veces con diferentes datos y siempre funcionará igual.

### El cambio importante (explicado de forma simple)

**Antes:**
- "Le pregunto cosas a la IA y ella me responde. Si quiero varias historias, tengo que pedirlas una por una."

**Ahora:**
- "Hago un programa que le pide a la IA que cree VARIAS historias automáticamente. El programa hace el trabajo por mí."

### Criterio de éxito pedagógico (para niños)

El ejercicio está logrado si el niño puede decir (con sus propias palabras):

**"Ahora puedo hacer que el programa cree varios superhéroes automáticamente. Sin el programa, tendría que pedirle a la IA que cree cada uno uno por uno, pero con el programa lo hace todo automáticamente."**

O incluso más simple:

**"El programa crea varios superhéroes automáticamente. Esto es diferente a solo hablar con la IA."**

### Conexión con el marco teórico

Este ejercicio cumple con el criterio del marco teórico porque:

- **Crea algo que NO se puede hacer solo conversando:** Procesar múltiples casos automáticamente.
- **Demuestra el salto de "oráculo" a "herramienta":** La IA deja de ser algo a lo que preguntas y se convierte en algo que trabaja para ti de forma sistemática.
- **El alumno pasa de "pedir cosas" a "hacer que trabaje para él":** Especialmente cuando crea varios superhéroes automáticamente.

### Nota para el profesor

Para niños de 10 años, el objetivo no es que entiendan conceptos abstractos como "automatización" o "procesos sistemáticos". El objetivo es que:

- Vean que pueden crear algo que funciona.
- Entiendan que el programa hace el trabajo por ellos **varias veces automáticamente**.
- Reconozcan que esto es diferente a solo conversar con la IA.
- Se diviertan creando y experimentando.
- Pierdan el miedo a la programación.

El cambio conceptual más profundo (de "oráculo" a "herramienta") se puede mencionar, pero no es necesario que lo comprendan completamente a esta edad. Lo importante es la experiencia práctica y que reconozcan que **crear varios superhéroes automáticamente es algo que no se puede hacer solo conversando**.
