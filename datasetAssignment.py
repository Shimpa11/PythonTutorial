# Assignment for the day : Implement SVM ML Model on Cats and Dogs Image DataSet
# PreRequisite : Please change image into gray scale and into numpy Array. Create your own labels



import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_images
dataset = load_sample_images()
print(len(dataset.images))

first_img_data = dataset.images[0]
print(first_img_data.shape)

pos=1
for i in range(0,2):
    plt.subplot(1,2,pos)
    plt.imshow(dataset['images'][i],cmap=plt.cm.gray_r)
    pos+=1
plt.show()