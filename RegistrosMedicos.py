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
    


dataset=cargar_dataset()
df=convertir_dataset(dataset)
difuntos,aunvivos=separar_dtframe(df)
imprimir_promedios(difuntos,aunvivos)
    
    
    

  

