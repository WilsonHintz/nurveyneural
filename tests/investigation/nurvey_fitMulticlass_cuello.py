import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# load dataset

dataset = numpy.loadtxt('nurvey7214.csv', delimiter=';')
X = dataset[:, 0:24]
Y = dataset[:, 24]

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# se convierten las variables de enteros a variables ficticias
dummy_y = np_utils.to_categorical(encoded_Y)

model = Sequential()
model.add(Dense(24, input_dim=24, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(8, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X, dummy_y, validation_split=0.25, epochs=250, batch_size=7, verbose=1)
scores = model.evaluate(X, dummy_y, verbose=0)

#impresion de resultados
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()