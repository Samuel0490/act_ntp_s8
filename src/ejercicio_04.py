import pandas as pd

def ejercicio_4():
    print("\n=== EJERCICIO 4: DataFrame desde diccionario ===")
    diccionario_productos = {
        'Producto': ['Laptop', 'Smartphone', 'Tablet', 'Monitor'],
        'Precio': [15000, 8000, 6000, 4500],
        'Categoria': ['Computadoras', 'Móviles', 'Computadoras', 'Accesorios']
    }
    
    df = pd.DataFrame(diccionario_productos)
    print("DataFrame completo:")
    print(df)
    
    print("Columna 'Precio':")
    print(df['Precio'])
