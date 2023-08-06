import numpy as np

from scampy.Util import to_one_hot, to_sparse

class Loss:
    is_categorical = False
    is_binary = False
    is_regression = False

    def regularization_loss(layer):
        regularization_loss = 0

        if layer.l1_regularizers:
            regularization_loss += layer.l1_regularizers[0] * np.sum(np.abs(layer.weights))
            regularization_loss += layer.l1_regularizers[1] * np.sum(np.abs(layer.biases))

        if layer.l2_regularizers:
            regularization_loss += layer.l2_regularizers[0] * np.sum(np.square(layer.weights))
            regularization_loss += layer.l2_regularizers[1] * np.sum(np.square(layer.biases))

        return regularization_loss

class CategoricalCrossentropy(Loss):
    is_categorical = True

    def forward(y_pred, y_true):
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
        correct_confidences = []

        dimensions = len(y_true.shape)
        if dimensions == 1:
            correct_confidences = y_pred_clipped[range(len(y_pred_clipped)), y_true]
        elif dimensions == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)

        loss_per_sample = -np.log(correct_confidences)
        return np.mean(loss_per_sample)

    def backward(y_pred, y_true):
        samples = len(y_pred)

        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        if len(y_true.shape) == 1:
            y_true = to_one_hot(y_true)

        dinputs = -y_true / y_pred_clipped

        return dinputs / samples

    # TODO
    def backward_softmax(y_pred, y_true):
        samples = len(y_pred)

        if len(y_true.shape) == 2:
            y_true = to_sparse(y_true)

        dinputs = y_pred.copy()
        dinputs[range(samples), y_true] -= 1

        return dinputs / samples

class BinaryCrossentropy(Loss):
    is_binary = True

    def forward(y_pred, y_true):
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        sample_losses = -(y_true * np.log(y_pred_clipped) + (1 - y_true) * np.log(y_pred_clipped))
        mean_sample_losses = np.mean(sample_losses, axis=1)

        return np.mean(mean_sample_losses)

    def backward(y_pred, y_true):
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        samples = len(y_pred)
        classes = len(y_pred[0])

        dinputs = -(y_true / y_pred_clipped - (1 - y_true) / (1 - y_pred_clipped)) / classes

        return dinputs / samples

class MeanSquaredError(Loss):
    is_regression = True

    def forward(y_pred, y_true):
        return np.mean(np.square(y_pred - y_true))

    def backward(y_pred, y_true):
        samples = len(y_pred)
        classes = len(y_pred[0])

        dinputs = 2.0 * (y_pred - y_true) / classes
        
        return dinputs / samples

class MeanAbsoluteError(Loss):
    is_regression = True

    def forward(y_pred, y_true):
        return np.mean(np.abs(y_pred - y_true))

    def backward(y_pred, y_true):
        samples = len(y_pred)
        dinputs = np.sign(y_pred - y_true)

        return dinputs / samples