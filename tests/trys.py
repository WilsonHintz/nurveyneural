import numpy
import pandas as pd


# dataset = numpy.loadtxt("dataset.csv", delimiter=",")
# # split into input (X) and output (Y) variables
# X = dataset[:, 0:8]
# Y = dataset[:, 8]
#
# print(X)
# print(Y)

s = pd.Series(list('1234'))
print(pd.get_dummies(s))