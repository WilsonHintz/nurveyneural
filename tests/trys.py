import numpy

dataset = numpy.loadtxt("dataset.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:, 0:8]
Y = dataset[:, 8]

print(X)
print(Y)