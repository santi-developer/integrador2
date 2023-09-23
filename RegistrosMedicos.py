from datasets import load_dataset
import pandas as pd
import numpy as np
import requests

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
        
def obtener_csv(direccion,nombre_archivo):
    solicitud=requests.get(direccion)
    
    if solicitud.status_code==200:
        with open(nombre_archivo,'wb') as archivo:
             archivo.write(solicitud.content)
        print("los datos se descargaron")
    else:
        print("no se puede descargar los datos")  
        
        df=pd.DataFrame(archivo)
        return df
        
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
        
def limpieza (df:pd.DataFrame):
    df=pd.read_csv('datos.csv')
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
    df_sin_atipicos.to_csv("resultado.csv")
    print(df_sin_atipicos)
                
            
def main():
    dataset = cargar_dataset()
    df = convertir_dataset(dataset)
    difuntos, aunvivos = separar_dtframe(df)
    imprimir_promedios(difuntos, aunvivos)
    verificar_datos_incorrectos(df, 'is_male', bool)
    cant_fumador_genero(df)
    direccion = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
    nombre_archivo = "datos.csv"
    limpieza(obtener_csv(direccion, nombre_archivo))

if __name__ == "__main__":
    main()

    
    
    

  

