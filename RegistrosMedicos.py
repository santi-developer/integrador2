from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")

data=dataset['train']

edades=data['age']

edades_np=np.array(edades)

edad_promedio=int(np.mean(edades_np))

print(edad_promedio)


