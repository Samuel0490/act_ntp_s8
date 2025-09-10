import pandas as pd

def ejercicio_9():
    print("\n=== EJERCICIO 9: DataFrame desde datos 2D ===")
    datos_ventas = [
        [1200, 1500, 1800],
        [980, 1300, 1650],
        [1450, 1750, 2000]
    ]
    
    df = pd.DataFrame(datos_ventas, columns=['Q1', 'Q2', 'Q3'])
    print("DataFrame de ventas trimestrales:")
    print(df)
    print("Tipos de datos:")
    print(df.dtypes)