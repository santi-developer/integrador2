from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargamos el dataset
iris = datasets.load_iris(as_frame=True)
X = iris.data
y = iris.target #

# Creamos la gráfica de distribución de clases
plt.figure(figsize=(8, 6))
plt.hist(y, bins=3, alpha=0.7, rwidth=0.85)
plt.xticks(range(3), iris.target_names)
plt.title('Distribución de Clases en el Iris Dataset')
plt.xlabel('Especies')
plt.ylabel('Frecuencia')
plt.show()


# se Realiza la partición del dataset en conjunto de entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# se crea una instancia del clasificador de árbol de decisión
clf = DecisionTreeClassifier(random_state=50)

# se ajusta el modelo a los datos de entrenamiento
clf.fit(X_train, y_train)

# se realiza predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# se calcula la precisión del modelo en el conjunto de prueba
accuracy = accuracy_score(y_test, y_pred)

print(f'Precisión en el conjunto de prueba: {accuracy:.2f}')