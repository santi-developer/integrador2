
from sklearn.metrics import accuracy_score,f1_score
from clasificacion_1 import cargardataset,realizar_particion
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

irs,X,y=cargardataset()
X_train,X_test,y_train,y_test=realizar_particion(X,y)

# Crear el modelo Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=50)

# Entrenar el modelo
rf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = rf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)

# Calcular la matriz de confusión
confusion = confusion_matrix(y_test, y_pred)

print("Matriz de confusión:")
print(confusion)


# Calcular el F1-Score
f1 = f1_score(y_test, y_pred,average='micro')

print(f"Precisión (Accuracy): {accuracy:.2f}")
print(f"F1-Score: {f1:.2f}")





