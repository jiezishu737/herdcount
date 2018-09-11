'''This script displays the UCF CC 50 dataset'''

#!python
#!/usr/bin/env python
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# image input
x = mpimg.imread('11.jpg')
imgplot = plt.imshow(x)

# reading annPoints variable from the Mat data file
y = loadmat('11_ann.mat')['annPoints']
outputX = y[:,0]
outputY = y[:,1]

# displaying the crowd count
plt.text(0.2, 0.2, "Count: " + str(outputY.size), fontsize=12)

data_Plot = plt.scatter(outputX,outputY, s=3, c='r')

# displaying data
plt.show(data_Plot)
