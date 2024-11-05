# model

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
import joblib


data_set = load_digits()

data = data_set.data
images = data_set.images    
target =  data_set.target

print("data shape : ", data.shape)
print("Images shape : ", images.shape)
print("target shape : ",target.shape )

plt.imshow(images[0], cmap = 'gray')
# plt.show()

print(images[0])

train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.2)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(train_data, train_target)

predicted_target = model.predict(test_data)

accuracy = accuracy_score(test_target, predicted_target)
print("Acuracy : ", accuracy)

joblib.dump(model, "KNN-digit_recongnition.sav")