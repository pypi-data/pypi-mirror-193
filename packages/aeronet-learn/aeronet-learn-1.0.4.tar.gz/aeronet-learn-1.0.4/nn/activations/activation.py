import numpy as np
from nn.layers.layer import Layer

class Activation(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    def forward(self, input):
        self.input = input
        return self.activation(self.input)

    def backward(self, output_gradient):
        return np.multiply(output_gradient, self.activation_prime(self.input))
    
    # Modify string representation for network architecture printing
    def __str__(self):
        return self.__class__.__name__ + "()"