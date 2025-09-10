import pandas as pd

def ejercicio_7():
    print("\n=== EJERCICIO 7: Crear y guardar CSV ===")
    datos_cursos = {
        'curso': ['Python para Principiantes', 'JavaScript Avanzado', 'Machine Learning'],
        'instructor': ['Ana Martínez', 'Carlos Ruiz', 'Laura Gómez'],
        'duracion': ['40 horas', '60 horas', '80 horas']
    }
    
    df = pd.DataFrame(datos_cursos)
    print("DataFrame de cursos:")
    print(df)
    
    df.to_csv('cursos.csv', index=False)
    print("Archivo 'cursos.csv' creado")
    
    df_leido = pd.read_csv('cursos.csv')
    print("DataFrame leído desde CSV:")
    print(df_leido)