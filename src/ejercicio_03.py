import pandas as pd

def ejercicio_3():
    print("\n=== EJERCICIO 3: Operaciones matemáticas ===")
    precios = pd.Series([100, 150, 200])
    descuentos = pd.Series([10, 20, 15])
    
    print("Serie de precios:")
    print(precios)
    print("Serie de descuentos:")
    print(descuentos)
    
    precios_con_descuento = precios - descuentos
    print("Precios con descuento:")
    print(precios_con_descuento)
    
    precios_con_iva = precios * 1.16
    print("Precios con IVA:")
    print(precios_con_iva)