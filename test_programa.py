"""
Script de prueba automática para verificar que el programa funciona
No requiere interacción del usuario
"""

import sys
import io
from contextlib import redirect_stdout

def test_imports():
    """Verifica que se pueden importar las funciones"""
    print("=" * 50)
    print("TEST 1: Verificar imports")
    print("=" * 50)
    try:
        # Simular importación del módulo
        import generador_superheroes as gs
        print("[OK] Modulo importado correctamente")
        return True
    except Exception as e:
        print(f"[ERROR] Error al importar: {e}")
        return False

def test_funciones_basicas():
    """Verifica que las funciones básicas existen"""
    print("\n" + "=" * 50)
    print("TEST 2: Verificar funciones básicas")
    print("=" * 50)
    try:
        import generador_superheroes as gs
        
        # Verificar que las funciones existen
        funciones_requeridas = [
            'mostrar_titulo',
            'mostrar_separador',
            'preguntar',
            'crear_superheroe_simple',
            'crear_superheroe_con_ia',
            'crear_varios_superheroes',
            'pedir_a_la_ia',
            'guardar_historias',
            'mostrar_menu',
            'main'
        ]
        
        for func_name in funciones_requeridas:
            if hasattr(gs, func_name):
                print(f"[OK] Funcion '{func_name}' existe")
            else:
                print(f"[ERROR] Funcion '{func_name}' NO existe")
                return False
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_pedir_a_la_ia():
    """Verifica que la función de IA funciona"""
    print("\n" + "=" * 50)
    print("TEST 3: Verificar función pedir_a_la_ia")
    print("=" * 50)
    try:
        import generador_superheroes as gs
        
        mensaje = "Crea una historia sobre un superhéroe"
        resultado = gs.pedir_a_la_ia(mensaje)
        
        if resultado and len(resultado) > 0:
            print("[OK] Funcion pedir_a_la_ia funciona")
            print(f"  Resultado: {resultado[:50]}...")
            return True
        else:
            print("[ERROR] Funcion no retorna resultado")
            return False
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        return False

def test_guardar_historias():
    """Verifica que se puede guardar archivos"""
    print("\n" + "=" * 50)
    print("TEST 4: Verificar guardar historias")
    print("=" * 50)
    try:
        import generador_superheroes as gs
        import os
        
        # Crear historias de prueba
        historias_test = [
            {"nombre": "Test Hero", "historia": "Esta es una historia de prueba"}
        ]
        
        archivo_test = "test_historias.txt"
        resultado = gs.guardar_historias(historias_test, archivo_test)
        
        if resultado:
            # Verificar que el archivo existe
            if os.path.exists(archivo_test):
                print("[OK] Archivo guardado correctamente")
                # Limpiar archivo de prueba
                os.remove(archivo_test)
                return True
            else:
                print("[ERROR] Archivo no se creo")
                return False
        else:
            print("[ERROR] Error al guardar")
            return False
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        return False

def test_estructura_programa():
    """Verifica la estructura general del programa"""
    print("\n" + "=" * 50)
    print("TEST 5: Verificar estructura del programa")
    print("=" * 50)
    try:
        import generador_superheroes as gs
        
        # Verificar que mostrar_titulo no da error
        f = io.StringIO()
        with redirect_stdout(f):
            gs.mostrar_titulo()
        salida = f.getvalue()
        
        if "GENERADOR" in salida.upper():
            print("[OK] Funcion mostrar_titulo funciona")
            return True
        else:
            print("[ERROR] Funcion mostrar_titulo no funciona correctamente")
            return False
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        return False

def main():
    """Ejecuta todos los tests"""
    print("\n" + "=" * 50)
    print("  PRUEBAS AUTOMÁTICAS DEL PROGRAMA")
    print("=" * 50 + "\n")
    
    tests = [
        test_imports,
        test_funciones_basicas,
        test_pedir_a_la_ia,
        test_guardar_historias,
        test_estructura_programa
    ]
    
    resultados = []
    for test in tests:
        try:
            resultado = test()
            resultados.append(resultado)
        except Exception as e:
            print(f"[ERROR] Error inesperado en test: {e}")
            resultados.append(False)
    
    # Resumen
    print("\n" + "=" * 50)
    print("  RESUMEN DE PRUEBAS")
    print("=" * 50)
    print(f"Tests pasados: {sum(resultados)}/{len(resultados)}")
    
    if all(resultados):
        print("\n[OK] TODOS LOS TESTS PASARON!")
        print("El programa esta listo para usar.")
        return 0
    else:
        print("\n[ERROR] Algunos tests fallaron.")
        print("Revisa los errores arriba.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
