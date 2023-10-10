from matplotlib import pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from graficas import obtener_Dataframe
from sklearn.linear_model import LinearRegression

def eliminar_columnas(df):
    
    y = df['age']
    X=df.drop(['DEATH_EVENT', 'age'], axis=1)
    model = LinearRegression()

    # Ajustar el modelo a los datos
    model.fit(X, y)

    # Imprimir los coeficientes de la regresión lineal
    print("Coeficientes de la regresión lineal:")
    for feature, coef in zip(X.columns, model.coef_):
        print(f"{feature}: {coef}")

    # Predecir la edad utilizando el modelo ajustado
    predicted_age = model.predict(X)

    df['predicted_age'] = predicted_age

    # Calcular el MSE entre las edades reales y las edades predichas
    mse = mean_squared_error(df['age'], df['predicted_age'])
    
    # Datos reales y predichos
    y_real = df['age']
    y_pred = df['predicted_age']
    
    # Imprimir las edades predichas
    print("\nEdades predichas:")
    print(predicted_age)
    
     # Imprimir las edades reales y las edades predichas
    print("Edades reales vs. Edades predichas:")
    print(df[['age', 'predicted_age']])
    
     # Imprimir el MSE
    print(f"Error Cuadrático Medio (MSE): {mse}")

    # Crear un scatter plot para los datos reales
    plt.scatter(y_real, y_pred, c='blue', label='Datos reales vs. Predicciones')

    # Línea diagonal de referencia (y = x)
    plt.plot([min(y_real), max(y_real)], [min(y_real), max(y_real)], color='red', linestyle='-', lw=2, label='Línea de referencia (y=x)')

    # Etiquetas y título
    plt.xlabel('Edad Real')
    plt.ylabel('Edad Predicha')
    plt.title('Regresión Lineal: Edad Real vs. Edad Predicha')

    # Leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()
        
    
    
def main ():
    df=obtener_Dataframe()
    eliminar_columnas((df))
    
if __name__=="__main__":     
     main()       