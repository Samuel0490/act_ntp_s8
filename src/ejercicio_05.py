import pandas as pd

def ejercicio_5():
    print("\n=== EJERCICIO 5: DataFrame desde lista de diccionarios ===")
    lista_empleados = [
        {'empleado': 'Juan Pérez', 'salario': 35000, 'departamento': 'Ventas'},
        {'empleado': 'Ana García', 'salario': 42000, 'departamento': 'IT'},
        {'empleado': 'Carlos López', 'salario': 38000, 'departamento': 'Marketing'}
    ]
    
    df = pd.DataFrame(lista_empleados)
    print("DataFrame desde lista de diccionarios:")
    print(df)
    
    print("Fila con índice 1:")
    print(df.iloc[1])