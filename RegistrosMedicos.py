from datasets import load_dataset
import pandas as pd
import numpy as np

def cargar_dataset():
    dataset = load_dataset("mstz/heart_failure")
    data = dataset['train']
    return data
    
def promedio_edad(dataset)->float:
    edades=dataset['age']
    edades_np=np.array(edades)
    edad_promedio=np.mean(edades_np)
    return edad_promedio

def convertir_dataset(dataset)->pd.DataFrame:
    df=pd.DataFrame(dataset)
    print(df)
    return df

def separar_dtframe (df: pd.DataFrame)->pd.DataFrame:
    difuntos=df[df['is_dead']==1]
    aun_vivos=df[df['is_dead']!=1]
    return difuntos,aun_vivos

def imprimir_promedios(difuntos,vivos:pd.DataFrame):
    promedio_dif=np.mean(difuntos['age'])
    promedio_viv=np.mean(vivos['age'])
    print("edad promedio de muerte: " +str( promedio_dif))
    print("edad promedio de vivos: " +str( promedio_viv)) 
    
def cant_fumador_genero(df:pd.DataFrame):
    num_hombres_fum=df[df['is_male']]['is_smoker'].sum()
    num_mujeres_fum=df[df['is_male']==False]['is_smoker'].sum()
    print("numero de hombres fumadores: "+str(num_hombres_fum))
    print("numero de mujeres fumadoras: "+str(num_mujeres_fum))   
    
def verificar_datos_incorrectos(df, columna, tipo_deseado):
    try:
        df[columna] = df[columna].astype(tipo_deseado)
        print(f"Todos los datos en la columna '{columna}' son del tipo {tipo_deseado}.")
    except ValueError:
        print(f"Datos incorrectos en la columna '{columna}' (no son del tipo {tipo_deseado}).")
       
       
dataset=cargar_dataset()
df=convertir_dataset(dataset)
difuntos,aunvivos=separar_dtframe(df)
imprimir_promedios(difuntos,aunvivos)
verificar_datos_incorrectos(df, 'is_male', bool)  
cant_fumador_genero(df)


    
    
    

  

