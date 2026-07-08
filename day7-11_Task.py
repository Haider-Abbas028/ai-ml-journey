# Build a mini 'neural network' from scratch (no libraries):
# 1. Create a Matrix class with __init__, __mul__, __add__, __repr__
# 2. Create a Layer class that takes input_size, output_size, stores weights as Matrix
# 3. Create a Network class that chains multiple Layers
# 4. Implement a forward method that passes data through each layer
# 5. Generate random input data and pass it through your network
# This is basically what PyTorch does — you're building a toy version.


class Matrix:
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
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible matrix dimensions")
        result = Matrix(self.rows, other.cols)
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
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result


class Layer:
    def __init__(self, input_size: int, output_size: int):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = Matrix(input_size, output_size)
        self.weights.randomize()
        self.biases = Matrix(1, output_size)
        self.biases.randomize()
    
    def forward(self, input_data: Matrix) -> Matrix:
        if input_data.cols != self.input_size:
            raise ValueError("Input data must have the same number of columns as the layer's input size.")
        
        output=input_data * self.weights
        output= output + self.biases
        return  output

    def __repr__(self):
        return f"Layer({self.input_size} → {self.output_size})"

class Network:
    """
    Neural network jo multiple layers ko chain karega.
    PyTork ka nn.Sequential ka toy version!
    """
    
    def __init__(self, layer_sizes: list):

        self.layer_sizes = layer_sizes
        self.layers = []
        
        # Har adjacent pair ke liye ek layer create karein
        for i in range(len(layer_sizes) - 1):
            input_size = layer_sizes[i]
            output_size = layer_sizes[i + 1]
            
            # Layer banayein aur list mein add karein
            layer = Layer(input_size, output_size)
            self.layers.append(layer)
    
    def forward(self, input_data: Matrix):
        print(f"\nStarting Forward Pass...")
        print(f"Input: {input_data}")
        
        current_data = input_data
        
        # Har layer se data pass karo
        for i, layer in enumerate(self.layers):
            print(f"\n  Layer {i+1}: {layer}")
            current_data = layer.forward(current_data)
            print(f"    Output: {current_data}")
        
        print(f"\nFinal Output: {current_data}")
        return current_data
    
    def __repr__(self):
        """Network ka representation."""
        result = f"Network({self.layer_sizes}) with {len(self.layers)} layers"
        return result


# ====================================================
# PART 4: Generate Random Input and Test
# ====================================================

def generate_random_input(size: int):
    """Random input vector banayein."""
    matrix = Matrix(1, size)
    matrix.randomize()
    return matrix


def main():

    print("=" * 60)
    print("BUILDING NEURAL NETWORK FROM SCRATCH")
    print("=" * 60)
    
    # Step 1: Network define karo
    # [2, 3, 2] means: 2 inputs → 3 hidden → 2 outputs
    network = Network([2, 3, 2])
    print(f"\nNetwork created: {network}\n")
    
    # Step 2: Random input generate karo
    input_data = generate_random_input(2)
    print(f"Input Data:\n{input_data}")
    
    # Step 3: Forward pass run karo
    output = network.forward(input_data)
    
    # Step 4: Final result
    print("\n" + "=" * 60)
    print(f"FINAL OUTPUT: {output}")
    print("=" * 60)


if __name__ == "__main__":
    main()