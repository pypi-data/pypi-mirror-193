import numpy as np
import random

def to_one_hot(y):
    classes = y.max() + 1
    return np.eye(classes)[y]

def to_sparse(y):
    return np.argmax(y, axis=1)

def calculate_accuracy(y_pred, y, loss):
    if loss.is_categorical:
        return calculate_accuracy_categorical(y_pred, y)
    elif loss.is_binary:
        return calculate_accuracy_binary(y_pred, y)
    elif loss.is_regression:
        return calculate_accuracy_regression(y_pred, y)

def calculate_accuracy_categorical(y_pred, y):
    correct_classes = y
    predicted_classes = np.argmax(y_pred, axis=1)

    dimensions = len(correct_classes.shape)
    if dimensions == 2:
        correct_classes = np.argmax(y, axis=1)

    return np.mean(predicted_classes == correct_classes)

def calculate_accuracy_binary(y_pred, y):
    predictions = (y_pred > 0.5).astype(int)
    return np.mean(predictions == y)

def calculate_accuracy_regression(y_pred, y):
    precision = np.std(y) / 250
    return np.mean(np.abs(y_pred - y) < precision)

def get_classification(y_pred):
    return (y_pred > 0.5) * 1

def shuffle_dataset(X, y):
    indices = list(range(len(y)))
    random.shuffle(indices)
    return X[indices], y[indices]

def split_dataset(X, y, ratios):
    samples = len(y)
    split_sizes = tuple(int(samples * ratio) for ratio in ratios)
    
    datasets = []
    current_lower_bound = 0

    for size in split_sizes:
        upper_bound = current_lower_bound + size

        x_split = X[current_lower_bound:upper_bound]
        y_split = y[current_lower_bound:upper_bound]
        datasets.append((x_split, y_split))
        
        current_lower_bound = upper_bound

    return datasets

def split_dataset_random(X, y, ratios):
    X_random, y_random = shuffle_dataset(X, y)
    return split_dataset(X_random, y_random, ratios)