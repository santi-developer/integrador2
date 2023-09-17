from datasets import load_dataset
import numpy as np

def cargar_dataset():
    dataset = load_dataset("mstz/heart_failure")
    return dataset
    
def promedio_edad(dataset)->float:
    data=dataset['train']
    edades=data['age']
    edades_np=np.array(edades)
    edad_promedio=np.mean(edades_np)
    print(edad_promedio)
    return edad_promedio

promedio_edad(cargar_dataset())

