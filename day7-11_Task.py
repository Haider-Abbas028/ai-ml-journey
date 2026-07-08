# Build a mini 'neural network' from scratch (no libraries):
# 1. Create a Matrix class with __init__, __mul__, __add__, __repr__
# 2. Create a Layer class that takes input_size, output_size, stores weights as Matrix
# 3. Create a Network class that chains multiple Layers
# 4. Implement a forward method that passes data through each layer
# 5. Generate random input data and pass it through your network
# This is basically what PyTorch does — you're building a toy version.


class matrix:
    def __init__(self, rows: int , cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def __repr__(self):
        result = "{"
        for row in self.data:
            result += " ".join(f"{val:.2f}" for val in row) + "} \n"
        return result
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add.")
        result = matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible matrix dimensions")
        result = matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result
    
    def randomize(self):
        import random
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random.uniform(0, 1)
    
    def transpose(self):
        result = matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result


class Layer:
    def __init__(self, input_size: int, output_size: int):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = matrix(input_size, output_size)
        self.weights.randomize()
        self.biases = matrix(1, output_size)
        biases.randomize()
    
    def forward(self, input_data: matrix) -> matrix:
        if input_data.cols != self.input_size:
            raise ValueError("Input data must have the same number of columns as the layer's input size.")
        
        output=input_data * self.weights
        output= output + self.biases
        return  output

    def __repr__(self):
        return f"Layer({self.input_size} → {self.output_size})"

