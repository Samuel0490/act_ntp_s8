import pandas as pd

def ejercicio_8():
    print("\n=== EJERCICIO 8: Crear y guardar JSON ===")
    datos_vehiculos = {
        'marca': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],
        'modelo': ['Corolla', 'Civic', 'Focus', 'Cruze'],
        'año': [2022, 2021, 2020, 2023]
    }
    
    df = pd.DataFrame(datos_vehiculos)
    print("DataFrame de vehículos:")
    print(df)
    
    df.to_json('vehiculos.json', orient='records', indent=2)
    print("Archivo 'vehiculos.json' creado")
    
    df_leido = pd.read_json('vehiculos.json')
    print("DataFrame leído desde JSON:")
    print(df_leido)
    print("Tipos de datos:")
    print(df_leido.dtypes)