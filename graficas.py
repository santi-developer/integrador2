from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#integrador parte 7
def obtener_Dataframe()->pd.DataFrame:
    df=pd.read_csv("datos.csv")
    return df

# creacion de los Histogramas
def graficas_distribuciones(df:pd.DataFrame):
    
    #longitud de la columna edad
    longitud_muestra=len(df['age'])
    #determinar cantidad de bins por raiz cuadrada
    num_bins = int(np.sqrt(longitud_muestra))
    #Histograma distribucion de edades
    plt.hist(df['age'], bins=num_bins, color='skyblue', edgecolor='black')
    plt.title('Histograma de Distribucion Edades')
    plt.xlabel('Edad')
    plt.ylabel('Cantidad')
    
    #histograma agrupado por hombre y mujer
    # Filtrar datos por género (hombres y mujeres)
    mujeres = df[df['sex']==False]
    hombres = df[df['sex'] == True]

    # Calcular las cantidades de anémicos, diabéticos, fumadores y muertos por género
    cantidad_anemic_mujeres = mujeres['anaemia'].sum()
    cantidad_anemic_hombres = hombres['anaemia'].sum()
    cantidad_diabetes_mujeres = mujeres['diabetes'].sum()
    cantidad_diabetes_hombres = hombres['diabetes'].sum()
    cantidad_fumadores_mujeres = mujeres['smoking'].sum()
    cantidad_fumadores_hombres = hombres['smoking'].sum()
    cantidad_muertos_mujeres = mujeres['DEATH_EVENT'].sum()
    cantidad_muertos_hombres = hombres['DEATH_EVENT'].sum()

    # Etiquetas para las barras
    categorias = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

    # Datos de las barras
    mujeres_data = [cantidad_anemic_mujeres, cantidad_diabetes_mujeres, cantidad_fumadores_mujeres, cantidad_muertos_mujeres]
    hombres_data = [cantidad_anemic_hombres, cantidad_diabetes_hombres, cantidad_fumadores_hombres, cantidad_muertos_hombres]

    # Crear una figura de Matplotlib
    plt.figure(figsize=(10, 6))
    plt.title('Histograma de Grupos por Género', fontsize=16)

    ancho_barras=0.2
    # Posición de las barras en el eje x
    x = np.arange(len(categorias))

    # Crear las barras apiladas
    plt.bar(x, hombres_data, width=ancho_barras, label='Hombres', color='red', align='center', alpha=1)
    plt.bar(x+ ancho_barras/2, mujeres_data, width=ancho_barras, label='Mujeres', color='blue', align='edge', alpha=1)
   

    # Etiquetas de las barras
    plt.xticks(x, categorias)
    plt.xlabel('Categorías')
    plt.ylabel('Cantidad')

    # Leyenda
    plt.legend()
    plt.show()
    
        
           
def main():
   df=obtener_Dataframe()
   graficas_distribuciones(df)
    
if __name__ == "__main__":
    main()
