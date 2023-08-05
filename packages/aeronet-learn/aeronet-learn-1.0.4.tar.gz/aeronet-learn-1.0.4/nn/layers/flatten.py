import numpy as np
from nn.layers.layer import Layer

class Flatten(Layer):
    def __init__(self, input_shape):
        self.input_shape = input_shape

    def forward(self, input):
        # Needs to be a single column 2d array not a 1d array.
        return np.reshape(input, (input.size, 1))

    def backward(self, output_gradient):
        return np.reshape(output_gradient, self.input_shape)

    # Modify string representation for network architecture printing
    def __str__(self):
        return self.__class__.__name__ + "()"