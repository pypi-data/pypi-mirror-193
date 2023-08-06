import numpy as np

WEIGHTS = 0
BIASES = 1

class Optimizer:
    def __init__(self, learning_rate, decay):
        self.learning_rate = learning_rate
        self.decay = decay

        self.current_learning_rate = learning_rate
        self.iterations = 0

    def pre_update_params(self):
        if self.decay:
            self.current_learning_rate = self.learning_rate * (1.0 / (1.0 + self.decay * self.iterations))

    def post_update_params(self):
        self.iterations += 1

class StochasicGradientDescent(Optimizer):
    def __init__(self, learning_rate=1.0, decay=0.0, momentum=0.0):
        super().__init__(learning_rate, decay)
        self.momentum = momentum

    def update_params(self, layer):
        if self.momentum and not hasattr(layer, "prev_updates"):
            layer.prev_updates = [
                np.zeros_like(layer.weights),
                np.zeros_like(layer.biases)
            ]
            
        layer.weights += self.__calculate_updates(WEIGHTS, layer, layer.dweights)
        layer.biases += self.__calculate_updates(BIASES, layer, layer.dbiases)

    def __calculate_updates(self, parameter_type, layer, gradients):
        updates = self.current_learning_rate * -gradients

        if self.momentum:
            updates = self.momentum * layer.prev_updates[parameter_type] + updates
            layer.prev_updates[parameter_type] = updates

        return updates
    
class AdaGrad(Optimizer):
    def __init__(self, learning_rate=1.0, decay=0.0, epsilon=1e-7):
        super().__init__(learning_rate, decay)
        self.epsilon = epsilon

    def update_params(self, layer):
        if not hasattr(layer, "gradient_cache"):
            layer.gradient_cache = [
                np.zeros_like(layer.weights),
                np.zeros_like(layer.biases)
            ]

        layer.weights += self.__calculate_updates(WEIGHTS, layer, layer.dweights)
        layer.biases += self.__calculate_updates(BIASES, layer, layer.dbiases)

    def __calculate_updates(self, parameter_type, layer, gradients):
        cache = layer.gradient_cache[parameter_type]
        cache += gradients ** 2
        
        return self.current_learning_rate * -gradients / (np.sqrt(cache) + self.epsilon)

class RMSProp(Optimizer):
    def __init__(self, learning_rate=0.001, decay=0.0, rho=0.9, epsilon=1e-7):
        super().__init__(learning_rate, decay)

        self.rho = rho
        self.epsilon = epsilon

    def update_params(self, layer):
        if not hasattr(layer, "gradient_cache"):
            layer.gradient_cache = [
                np.zeros_like(layer.weights),
                np.zeros_like(layer.biases)
            ]

        layer.weights += self.__calculate_updates(WEIGHTS, layer, layer.dweights)
        layer.biases += self.__calculate_updates(BIASES, layer, layer.dbiases)

    def __calculate_updates(self, parameter_type, layer, gradients):
        cache = self.rho * layer.gradient_cache[parameter_type] + (1 - self.rho) * gradients ** 2
        layer.gradient_cache[parameter_type] = cache

        return self.current_learning_rate * -gradients / (np.sqrt(cache) + self.epsilon)

class Adam(Optimizer):
    def __init__(self, learning_rate=0.001, decay=0.0, beta1=0.9, beta2=0.999, epsilon=1e-7):
        super().__init__(learning_rate, decay)

        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

    def update_params(self, layer):
        if not hasattr(layer, "prev_updates"):
            layer.prev_updates = [
                np.zeros_like(layer.weights),
                np.zeros_like(layer.biases)
            ]

            layer.gradient_cache = [
                np.zeros_like(layer.weights),
                np.zeros_like(layer.biases)
            ]

        layer.weights += self.__calculate_updates(WEIGHTS, layer, layer.dweights)
        layer.biases += self.__calculate_updates(BIASES, layer, layer.dbiases)

    def __calculate_updates(self, parameter_type, layer, gradients):
        prev_updates = self.beta1 * layer.prev_updates[parameter_type] + (1 - self.beta1) * gradients
        layer.prev_updates[parameter_type] = prev_updates

        cache = self.beta2 * layer.gradient_cache[parameter_type] +  (1 - self.beta2) * gradients ** 2
        layer.gradient_cache[parameter_type] = cache

        weight_cache_corrected = cache / (1 - self.beta2 ** (self.iterations + 1))

        momentums = prev_updates * (1 - self.beta1 ** (self.iterations + 1))
        return self.current_learning_rate * -momentums /  (np.sqrt(weight_cache_corrected) + self.epsilon)