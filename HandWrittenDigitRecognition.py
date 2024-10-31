from sklearn.datasets import load_digits

data_set = load_digits()

data = data_set.data
images = data_set.images    
target =  data_set.target

print("data shape : ", data.shape)
print("Images shape : ", images.shape)
print("data shape : ",target.shape )