import pandas as pd

def ejercicio_2():
    print("\n=== EJERCICIO 2: Serie de calificaciones ===")
    serie_calificaciones = pd.Series([85, 92, 78], index=['Matemáticas', 'Ciencias', 'Historia'])
    
    print("Serie de calificaciones:")
    print(serie_calificaciones)
    
    calificacion_ciencias = serie_calificaciones['Ciencias']
    print(f"Calificación en Ciencias: {calificacion_ciencias}")
    
    suma_total = serie_calificaciones.sum()
    promedio = serie_calificaciones.mean()
    print(f"Suma total: {suma_total}")
    print(f"Promedio: {promedio:.2f}")