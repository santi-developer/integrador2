import requests
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
    
#4 procesando informacion en bruto   
# realizar las soicitudes http GET y obtencion del respectivo archivo.csv  
def obtener_csv(direccion,nombre_archivo):
    solicitud=requests.get(direccion)
    
    if solicitud.status_code==200:
        with open(nombre_archivo,'w',encoding='utf-8') as archivo:
        
            try:
               contenido=solicitud.content.decode('utf-8') 
               archivo.write(contenido)
            except:
                archivo.write(str(solicitud.content))
        print("los datos se descargaron")
    else:
        print("no se puede descargar los datos")  
        
        df=pd.DataFrame(archivo)
        return df
         
# limpieza y preparacion de los datos        5
def limpieza (df:pd.DataFrame,archivo):
    df=pd.read_csv(archivo)
    df.dropna()
    df.drop_duplicates()
    
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    # Define los límites para identificar valores atípicos
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    # Filtra y elimina filas con valores atípicos en todas las columnas
    df_sin_atipicos = df[(df >= limite_inferior) & (df <= limite_superior)].dropna()
    df_sin_atipicos['clas_edades']= df['age'].apply(categorizar_edades)
    # escribir el archivo resultante
    df_sin_atipicos.to_csv("resultado.csv")
    print(df_sin_atipicos)
    return df_sin_atipicos

  # funcion para categorizar edades   5
def categorizar_edades(edad):
    if edad <= 12:
        return 'Niño'
    elif 13 <= edad <= 19:
        return 'Adolescente'
    elif 20 <= edad <= 39:
        return 'Jóvenes adulto'
    elif 40 <= edad <= 59:
        return 'Adulto'
    else:
        return 'Adulto mayor' 
    
           
def main():
    # Automatizando el proceso #parte 6
    direccion = sys.argv[1]
    nombre_archivo = "datos.csv"
    obtener=obtener_csv(direccion, nombre_archivo)
    limpieza(obtener,nombre_archivo)
    print(sys.argv)

if __name__ == "__main__":
    main()
