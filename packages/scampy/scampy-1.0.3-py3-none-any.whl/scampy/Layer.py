import numpy as np

class Layer:
    def __init__(self):
        self.train_only_layer = False

class Dense(Layer):
    def __init__(self, num_inputs, num_nodes, activation, l1_regularizers=None, l2_regularizers=None):
        super().__init__()

        self.num_inputs = num_inputs
        self.num_nodes = num_nodes
        self.activation = activation()

        self.l1_regularizers = l1_regularizers
        self.l2_regularizers = l2_regularizers

        self.weights = 0.01 * np.random.randn(self.num_inputs, self.num_nodes)
        self.biases = np.zeros((1, self.num_nodes))

        self.dweights = np.zeros_like(self.weights)
        self.dbiases = np.zeros_like(self.biases)

    def forward(self, inputs):
        self.inputs = inputs
        weighted_inputs = np.dot(inputs, self.weights) + self.biases
        return self.activation.forward(weighted_inputs)

    def backward(self, dvalues):
        dvalues = self.activation.backward(dvalues)

        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)

        if self.l1_regularizers:
            self.dweights += self.l1_regularizers[0] * np.sign(self.weights)
            self.dbiases += self.l1_regularizers[1] * np.sign(self.biases)

        if self.l2_regularizers:
            self.dweights += 2 * self.l2_regularizers[0] * self. weights
            self.dbiases += 2 * self.l2_regularizers[1] * self.biases

        dinputs = np.dot(dvalues, self.weights.T)

        return dinputs

class Dropout(Layer):
    def __init__(self, dropout_rate):
        super().__init__()

        self.dropout_rate = dropout_rate

        self.train_only_layer = True

    def forward(self, inputs):
        self.binary_mask = np.random.binomial(1, 1 - self.dropout_rate, inputs.shape) / (1 - self.dropout_rate)
        return inputs * self.binary_mask

    def backward(self, dvalues):
        return self.binary_mask * dvalues