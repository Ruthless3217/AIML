from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

data=load_wine()
x=data.data
y=data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

y_pred=model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy:{acc:.2f}")

conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix:{conf_matrix}")