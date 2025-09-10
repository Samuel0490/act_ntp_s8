import pandas as pd

def ejercicio_10():
    print("\n=== EJERCICIO 10: Simular datos de usuarios ===")
    datos_usuarios = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Juan Pérez', 'Ana García', 'Carlos López', 'María Rodríguez', 'Pedro Martín'],
        'email': ['juan@email.com', 'ana@email.com', 'carlos@email.com', 'maria@email.com', 'pedro@email.com'],
        'age': [25, 30, 28, 35, 22]
    }
    
    df = pd.DataFrame(datos_usuarios)
    print("DataFrame de usuarios:")
    print(df.head())
    print(f"Forma: {df.shape}")
    print("Tipos de datos:")
    print(df.dtypes)