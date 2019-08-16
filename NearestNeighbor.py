# -*- coding: utf-8 -*-
#***************************************************#
#CPSC-51100 [Semester] [Year]                       #   
#NAME: Nisha George                                 #
#PROGRAMMING ASSIGNMENT #3                          #
#***************************************************#

if __name__ == "__main__":
    print("CPSC-51100, Summer 2019")
    print("NAME: Nisha George")
    print("NearestNeighbor.py")

import numpy as np
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
open(r'C:\Users\Nishiji\Desktop\iris-testing-data.csv') #full path
open(r'C:\Users\Nishiji\Desktop\iris-training-data.csv') #full path

train_file = 'iris-training-data.csv'
test_file = 'iris-testing-data.csv'


# gather necessary data
train_data = np.loadtxt(train_file, delimiter = ",", usecols = (0, 1, 2, 3))
train_classes = np.loadtxt(train_file, delimiter = ",", usecols = (4,),
                           dtype = str)
test_data = np.loadtxt(test_file, delimiter = ",", usecols = (0, 1, 2, 3))
test_classes = np.loadtxt(test_file, delimiter = ",", usecols = (4,),
                          dtype = str)
predicted_classes = []

def distance(x, y):
    """
    Computes the distance between two vectors, x and y.
    
    params:
        x: vector, floats
        y: vector, floats
    
    return:
        float
    """
    
    return np.sqrt(np.sum((x-y)**2)) # euclidean distance

for row in test_data:
    # find distance between this row and every row in training
    distances = [distance(row, x) for x in train_data]
    predicted_class = np.argmin(distances) 
    predicted_classes.append(train_classes[predicted_class])

accuracy = ((sum(predicted_classes == test_classes) / float(test_classes.shape[0])) 
                * 100)

print("#, True, Predicted")

for x, y, z in zip(range(1, 76), test_classes, predicted_classes):
    print(x, y, z)
    
print("Accuracy: %f%% " % accuracy)


