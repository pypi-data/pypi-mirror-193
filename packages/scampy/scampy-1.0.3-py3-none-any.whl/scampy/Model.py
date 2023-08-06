import numpy as np
import pickle

from scampy.Util import calculate_accuracy, to_sparse

class Sequential:
    def __init__(self, *layers):
        self.layers = layers
        self.forward_layers = [layer for layer in layers if not layer.train_only_layer]

    def forward(self, inputs):
        current_inputs = inputs

        for layer in self.forward_layers:
            current_inputs = layer.forward(current_inputs)

        return current_inputs

    def forward_train(self, inputs):
        current_inputs = inputs

        for layer in self.layers:
            current_inputs = layer.forward(current_inputs)

        return current_inputs

    def evaluate(self, output, labels, loss):
        data_loss = loss.forward(output, labels)

        regularization_loss = 0

        for layer in self.forward_layers:
            regularization_loss += loss.regularization_loss(layer)

        return data_loss + regularization_loss

    def train(self, inputs, labels, loss, optimizer, epochs=1, batch_size=None, print_every=1, print_first = False):
        if type(optimizer) == type:
            optimizer = optimizer()

        if batch_size != None:
            num_of_batches = np.ceil(inputs.shape[0] / batch_size).astype(int)
        else:
            num_of_batches = 1

        layers_reversed = self.layers[::-1]

        for epoch in range(epochs):
            for batch in range(num_of_batches):
                if batch_size != None:
                    batch_x = inputs[batch * batch_size:(batch + 1) * batch_size]
                    batch_y = labels[batch * batch_size:(batch + 1) * batch_size]
                else:
                    batch_x = inputs
                    batch_y = labels

                output = self.forward_train(batch_x)

                dvalues = loss.backward(output, batch_y)

                optimizer.pre_update_params()            

                for layer in layers_reversed:
                    dvalues = layer.backward(dvalues)
                    optimizer.update_params(layer)

                optimizer.post_update_params()

            if (epoch + 1) % print_every == 0 or (epoch == 0 and print_first):
                output = self.forward(inputs)
                evaluation = self.evaluate(output, labels, loss)
                accuracy = calculate_accuracy(output, labels, loss)
                
                print(f"Epoch #{epoch + 1}: Loss={evaluation:.3f}, Accuracy={accuracy:.3f}")

    def test(self, inputs, labels, loss):
        output = self.forward(inputs)
        test_evaluation = self.evaluate(output, labels, loss)
        test_accuracy = calculate_accuracy(output, labels, loss)

        print(f"Test dataset: Loss={test_evaluation:.3f}, Accuracy={test_accuracy:.3f}")

    def classify(self, input):
        output = self.forward(input)
        return to_sparse(output)

    def get_parameters(self):
        parameters = []
        for layer in self.forward_layers:
            parameters.append([layer.weights, layer.biases])

        return parameters

    def set_parameters(self, parameters):
        for layer in self.forward_layers:
            weights, biases = parameters.pop(0)
            layer.weights = weights
            layer.biases = biases

    def save_parameters(self, path):
        parameters = self.get_parameters()

        with open(path, "wb") as output_file:
            pickle.dump(parameters, output_file)

    def load_parameters(self, path):
        with open(path, "rb") as output_file:
            parameters = pickle.load(output_file)

        self.set_parameters(parameters)

    def save(self, path):
        with open(path, "wb") as output_file:
            pickle.dump(self, output_file)

        for layer in self.forward_layers:
            for property in ["dinputs", "dweights", "dbiases"]:
                layer.__dict__.pop(property, None)

    @staticmethod
    def load(path):
        with open(path, "rb") as output_file:
            return pickle.load(output_file)