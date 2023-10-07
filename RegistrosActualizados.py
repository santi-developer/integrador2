from datasets import load_dataset
import pandas as pd
import numpy as np
import sys

#descargar dataset  1
def cargar_dataset(url):
    dataset = load_dataset(url)
    data = dataset['train']
    return data

#convertir la columna edades en un arreglo numpy y calcular promedio 1
def promedio_edad(dataset)->float:
    edades=dataset['age']
    edades_np=np.array(edades)
    edad_promedio=np.mean(edades_np)
    return edad_promedio
    
# convertir el Dataset en un DataFrame   -- carga de datos    2
def convertir_dataset(dataset)->pd.DataFrame:
    df=pd.DataFrame(dataset)
    print(df)
    return df

#partir dataframe en dos        2
def separar_dtframe (df: pd.DataFrame)->pd.DataFrame:
    difuntos=df[df['is_dead']==1]
    aun_vivos=df[df['is_dead']!=1]
    return difuntos,aun_vivos

#promedios de los dataframes vivos y muertos       2
def imprimir_promedios(difuntos,vivos:pd.DataFrame):
    promedio_dif=np.mean(difuntos['age'])
    promedio_viv=np.mean(vivos['age'])
    print("edad promedio de muerte: " +str( promedio_dif))
    print("edad promedio de vivos: " +str( promedio_viv)) 
    
#verificacion de datos -- calculando analitica de datos    3 
def verificar_datos_incorrectos(df):
   for columnas in df.columns:
    df[columnas] = pd.to_numeric(df[columnas], errors='coerce')
    return df

#cantidad de fumadores por genero      3 
def cant_fumador_genero(df:pd.DataFrame):
    num_hombres_fum=df[df['is_male']]['is_smoker'].sum()
    num_mujeres_fum=df[df['is_male']==False]['is_smoker'].sum()
    print("numero de hombres fumadores: "+str(num_hombres_fum))
    print("numero de mujeres fumadoras: "+str(num_mujeres_fum))
          
           
def main():
    
    # automatizacion del proceso con argvs
    dataset = cargar_dataset(sys.argv[1])
    df = convertir_dataset(dataset)
    difuntos, aunvivos = separar_dtframe(df)
    imprimir_promedios(difuntos, aunvivos)
    verificar_datos_incorrectos(df)
    cant_fumador_genero(df)
    
    

if __name__ == "__main__":
    main()

    
    
    

  

