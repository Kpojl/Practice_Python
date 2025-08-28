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


neuron = Neuron(weights=[0.4, 0.3, 0.2, 0.1], bias=-0.5)

print("=== ЗАДАЧА: СТОИТ ЛИ ИДТИ НА ПРОГУЛКУ? ===")
print("Входные параметры (1-хорошо/0-плохо, время в часах):")
print("Погода, Свободное время, Настроение, Физическая активность")
print()


inputs1 = [1, 3, 1, 1]  
print("Ситуация 1 - Идеальные условия:", inputs1)
print("Взвешенная сумма:", neuron.weighted_sum(inputs1))
print("Sigmoid (вероятность):", neuron.activate(inputs1, 'sigmoid'))
print("ReLU:", neuron.activate(inputs1, 'relu'))
print("Tanh:", neuron.activate(inputs1, 'tanh'))
print("Step (решение):", "ИДТИ" if neuron.activate(inputs1, 'step') == 1 else "НЕ ИДТИ")
print()


inputs2 = [0, 1, 0, 0]  
print("Ситуация 2 - Плохие условия:", inputs2)
print("Взвешенная сумма:", neuron.weighted_sum(inputs2))
print("Sigmoid (вероятность):", neuron.activate(inputs2, 'sigmoid'))
print("ReLU:", neuron.activate(inputs2, 'relu'))
print("Tanh:", neuron.activate(inputs2, 'tanh'))
print("Step (решение):", "ИДТИ" if neuron.activate(inputs2, 'step') == 1 else "НЕ ИДТИ")
print()


inputs3 = [1, 1, 1, 0]  
print("Ситуация 3 - Пограничный случай:", inputs3)
print("Взвешенная сумма:", neuron.weighted_sum(inputs3))
print("Sigmoid (вероятность):", neuron.activate(inputs3, 'sigmoid'))
print("ReLU:", neuron.activate(inputs3, 'relu'))
print("Tanh:", neuron.activate(inputs3, 'tanh'))
print("Step (решение):", "ИДТИ" if neuron.activate(inputs3, 'step') == 1 else "НЕ ИДТИ")
print()

inputs4 = [2, 1, 0, 0]  
print("Ситуация 4 - Пограничный случай:", inputs4)
print("Взвешенная сумма:", neuron.weighted_sum(inputs4))
print("Sigmoid (вероятность):", neuron.activate(inputs4, 'sigmoid'))
print("ReLU:", neuron.activate(inputs4, 'relu'))
print("Tanh:", neuron.activate(inputs4, 'tanh'))
print("Step (решение):", "ИДТИ" if neuron.activate(inputs4, 'step') == 1 else "НЕ ИДТИ")