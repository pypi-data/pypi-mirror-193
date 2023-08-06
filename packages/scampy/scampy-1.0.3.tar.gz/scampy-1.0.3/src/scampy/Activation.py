import numpy as np

class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        return np.maximum(self.inputs, 0)

    def backward(self, dvalues):
        dinputs = dvalues.copy()
        dinputs[self.inputs <= 0] = 0

        return dinputs

class Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        self.output = exp_values / np.sum(exp_values, axis=1, keepdims=True)

        return self.output

    def backward(self, dvalues):
        dinputs = np.empty_like(dvalues)

        for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
            single_output = single_output.reshape(-1, 1)
            jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)
            dinputs[index] = np.dot(jacobian_matrix, single_dvalues)

        return dinputs

class Sigmoid:
    def forward(self, inputs):
        self.output = 1 / (1 + np.exp(-inputs))
        return self.output

    def backward(self, dvalues):
        return dvalues * self.output * (1 - self.output)

class Linear:
    def forward(self, inputs):
        return inputs

    def backward(self, dvalues):
        return dvalues.copy()