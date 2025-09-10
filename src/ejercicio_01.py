import pandas as pd

def ejercicio_1():
    print("=== EJERCICIO 1: Serie de ventas diarias ===")
    ventas_diarias = [150, 200, 180, 220, 175, 190, 165]
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    serie_ventas = pd.Series(ventas_diarias, index=dias_semana)
    
    print("Serie de ventas diarias:")
    print(serie_ventas)
    
    valor_indice_3 = serie_ventas[3]
    print(f"\nValor en el índice 3: {valor_indice_3}")
    
    promedio_ventas = serie_ventas.mean()
    print(f"Promedio de ventas: {promedio_ventas:.2f}")
    
    serie_ordenada = serie_ventas.sort_values()
    print("Ventas ordenadas:")
    print(serie_ordenada)