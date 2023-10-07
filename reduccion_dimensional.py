from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import plotly.graph_objects as go
from graficas import obtener_Dataframe

def exportar_matriz_datos(df:pd.DataFrame):
    array=df['DEATH_EVENT'].values
    df = df.drop('DEATH_EVENT', axis=1)
    matriz_numpy=df.values
    matriz_numpy_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(matriz_numpy)
    
    # extraer coordenadas
    x = [punto[0] for punto in matriz_numpy_embedded]
    y = [punto[1] for punto in matriz_numpy_embedded]
    z = [punto[2] for punto in matriz_numpy_embedded]
    
    # Crear una lista de colores basada en el arreglo estado
    colores = ['red' if s == 0 else 'green' for s in array]

    #creacion de grafico de dispersion 3D
    fig = go.Figure()  # Crear una figura vacía
    # Añadir el trazado de dispersión 3D a la figura
    fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,  # Datos de x, y y z
    mode='markers',  # Estilo de marcador
    marker=dict(
        size=5,  # Tamaño de los marcadores
        color=colores,  # Variable para la escala de colores
        opacity=0.8  # Opacidad de los marcadores
    )
))

# Personalizar el diseño de la gráfica
    fig.update_layout(
    title='Gráfica de Dispersión 3D',  # Título de la gráfica
    scene=dict(
        xaxis_title='X',  # Etiqueta del eje x
        yaxis_title='Y',  # Etiqueta del eje y
        zaxis_title='Z'  # Etiqueta del eje z
    )
)

# Mostrar la gráfica
    fig.show()
     
def main():
    df=obtener_Dataframe()
    exportar_matriz_datos(df) 
    
   
if __name__ == "__main__":
    main()        
    