import math

class Neuron:
    def __init__(self, weights, bias=0):
        if len(weights) < 1 or len(weights) > 10:
            raise ValueError("Количество весов должно быть от 1 до 10")
        self.weights = weights
        self.bias = bias

    def _matrix_multiply(self, inputs):

        if len(inputs) != len(self.weights):
            raise ValueError("Размеры матриц не совместимы!")
        # Представляем веса как матрицу 1xN, а входы как Nx1
        result = 0
        for i in range(len(self.weights)):
            result += self.weights[i] * inputs[i]
        return result

    def weighted_sum(self, inputs):
        return self._matrix_multiply(inputs) + self.bias

    def activate(self, inputs, activation='sigmoid'):
        x = self.weighted_sum(inputs)
        if activation == 'sigmoid':
            return 1 / (1 + math.exp(-x))
        elif activation == 'relu':
            return max(0, x)
        elif activation == 'tanh':
            return math.tanh(x)
        elif activation == 'step':
            return 1 if x >= 0 else 0
        else:
            raise ValueError(f"Неизвестная функция активации: {activation}")
        
neuron = Neuron(weights=[0.5, -0.3, 0.1], bias=1)

inputs = [1, 2, 3]


print("Взвешенная сумма:", neuron.weighted_sum(inputs))  
print("Sigmoid:", neuron.activate(inputs, 'sigmoid'))  
print("ReLU:", neuron.activate(inputs, 'relu'))          
print("Step:", neuron.activate(inputs, 'step'))          
