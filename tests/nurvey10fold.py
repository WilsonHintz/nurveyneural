from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
import numpy

# Function to create model, required for KerasClassifier

def create_model():
    # create model
    model = Sequential()
    model.add(Dense(24, input_dim=24, activation='relu'))
    model.add(Dense(12, activation='relu'))
    model.add(Dense(12, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load dataset
dataset = numpy.loadtxt("ConNSE(clasificado123).csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:, 0:24]
Y = dataset[:, 24]

# SinmiembrosniaportanteniedadconNSEclasificado 21
# ConNSE(clasificado123) 24


# create model
model = KerasClassifier(build_fn=create_model, epochs=50, batch_size=10)
# evaluate using 10-fold cross validation
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())