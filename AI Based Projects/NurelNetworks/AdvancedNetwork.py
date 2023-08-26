import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

class Network:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.random.rand(self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.random.rand(self.output_size)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def feedforward(self, input_data):
        hidden_input = np.dot(input_data, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)
        
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        network_output = self.sigmoid(output_input)
        
        return network_output
    
    def train(self, input_data, target_data, learning_rate, epochs):
        epochs_list = []
        loss_list = []

        for epoch in range(epochs):
            total_loss = 0
            for i in range(len(input_data)):
                # Forward Pass
                hidden_input = np.dot(input_data[i], self.weights_input_hidden) + self.bias_hidden
                hidden_output = self.sigmoid(hidden_input)

                output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
                network_output = self.sigmoid(output_input)
                
                # Backpropagation
                output_error = target_data[i] - network_output
                output_delta = output_error * self.sigmoid_derivative(network_output)
                
                hidden_error = output_delta.dot(self.weights_hidden_output.T)
                hidden_delta = hidden_error * self.sigmoid_derivative(hidden_output)
                
                # Update Weights and Biases
                self.weights_hidden_output += np.outer(hidden_output, output_delta) * learning_rate
                self.bias_output += output_delta * learning_rate
                self.weights_input_hidden += np.outer(input_data[i], hidden_delta) * learning_rate
                self.bias_hidden += hidden_delta * learning_rate
                
                total_loss += 0.5 * np.sum((target_data[i] - network_output) ** 2)
            
            avg_loss = total_loss / len(input_data)
            epochs_list.append(epoch)
            loss_list.append(avg_loss)

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {avg_loss}")

        self.visualize_loss(epochs_list, loss_list)
    
    def visualize_loss(self, epochs_list, loss_list):
        plt.plot(epochs_list, loss_list)
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.title('Loss Over Epochs')
        plt.show()

data = pd.read_csv("data.csv")
input_columns = list(data.columns)[:-1]
target_column = list(data.columns)[-1]
input_data = data[input_columns].values
target_data = data[target_column].values.reshape(-1, 1)

input_size = len(input_columns)
output_size = 1
hidden_size = 4

nn = Network(input_size=input_size, hidden_size=hidden_size, output_size=output_size)

learning_rate = 0.5
epochs = 1000

nn.train(input_data, target_data, learning_rate, epochs)

for i in range(len(input_data)):
    predicted = math.round(nn.feedforward(input_data[i]))
    print("Input:", input_data[i], "Target:", target_data[i], "Predicted:", predicted)