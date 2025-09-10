import pandas as pd

def ejercicio_6():
    print("\n=== EJERCICIO 6: DataFrame desde lista de listas ===")
    datos_libros = [
        ['Cien años de soledad', 'Gabriel García Márquez', 1967],
        ['Don Quijote de la Mancha', 'Miguel de Cervantes', 1605],
        ['El amor en los tiempos del cólera', 'Gabriel García Márquez', 1985]
    ]
    
    nombres_columnas = ['Titulo', 'Autor', 'Año']
    df = pd.DataFrame(datos_libros, columns=nombres_columnas)
    
    print("DataFrame desde lista de listas:")
    print(df)
    print(f"Dimensiones: {df.shape}")