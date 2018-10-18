import numpy
from keras.models import model_from_json

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

x = "2;47;0;2;2;1;1;1;1;1;0;0;0;0;0;0;1;1;0;0;0;0;0;1"
#dataset = numpy.loadtxt(x, delimiter=';')
dataset = numpy.fromstring(x, sep=";")
dataset = numpy.vstack([dataset, dataset])

print(dataset.size)
print(dataset[0, 0:24])


salida = loaded_model.predict(dataset[:, 0:24])
print("")
print("salida")
print(salida)
