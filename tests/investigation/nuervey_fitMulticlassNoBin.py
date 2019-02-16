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
# dataframe = pandas.read_csv("nurvey.csv", header=None)
# dataset = dataframe.values
dataset = numpy.loadtxt('LOLASO.txt', delimiter=',')
X = dataset[:, 0:14]
Y = dataset[:, 14]

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

model = Sequential()
model.add(Dense(14, input_dim=14, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(8, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X, dummy_y, validation_split=0.30, epochs=20, batch_size=7, verbose=1)

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

#estimator = KerasClassifier(build_fn=baseline_model, epochs=2, batch_size=5)
#kfold = KFold(n_splits=4, shuffle=True, random_state=seed)
#results = cross_val_score(estimator, X, dummy_y, cv=kfold)
#acc = []
#acc.append(results.mean()*100)
#print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
#print(acc)
