"    *args and **kwargs  "
# *args function ko flexible number of arguments lene deta hai.

# 1. Multiple numbers ka sum
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))        # 6
print(sum_numbers(10, 20, 30, 40)) # 100
print(sum_numbers(5))              # 5
print(sum_numbers())               # 0

# 2. Multiple strings ko join karna
def join_strings(separator, *args):
    return separator.join(args)

print(join_strings("-", "a", "b", "c"))    # 'a-b-c'
print(join_strings(" ", "Hello", "World")) # 'Hello World'

#enumerate function

"enumerate(iterable, start=0)"
#           ↑           ↑
#    jis par loop lage  index kahan se start karna hai (default 0)

"for index, value in enumerate(iterable):"
    # index = position (0, 1, 2, ...)
    # value = actual item from iterable


# 3. ML example: Multiple layers ka sum
def create_model(*layers):
    print(f"Model has {len(layers)} layers")
    for i, layer in enumerate(layers, 1):
        print(f"Layer {i}: {layer} neurons")
    return layers

create_model(512, 256, 128, 64)
# Output:
# Model has 4 layers
# Layer 1: 512 neurons
# Layer 2: 256 neurons
# Layer 3: 128 neurons
# Layer 4: 64 neurons


# *kwargs function ko flexible number of keyword arguments (key=value) lene deta hai.


"""def function_name(**kwargs):
    # kwargs ek dictionary hai
    for key, value in kwargs.items():
        print(f"{key}: {value}")"""
 # Examplesss 
 # 1. Print all key-value pairs
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_details(name="Ali", age=25, city="Karachi")
# Output:
# name = Ali
# age = 25
# city = Karachi

# 2. ML Hyperparameters
def train_model(data, **hyperparams):
    print(f"Training on {len(data)} samples")
    for param, value in hyperparams.items():
        print(f"{param}: {value}")
    
    # Default values if not provided
    lr = hyperparams.get('lr', 0.001)
    epochs = hyperparams.get('epochs', 100)
    print(f"Using lr={lr}, epochs={epochs}")

# Call with different parameters
data = [1, 2, 3, 4, 5]
train_model(data, lr=0.01, epochs=50, batch_size=32)
# Output:
# Training on 5 samples
# lr: 0.01
# epochs: 50
# batch_size: 32
# Using lr=0.01, epochs=50

train_model(data)  # Default values use karega
# Output:
# Training on 5 samples
# Using lr=0.001, epochs=100

def trainingFunction(data,*args,**kwargs):
    print(f"applying function on {len(data)} length sample")
    for i , j in enumerate(args, 1):
        print(f"Layer:{1}, Nuerons:{j}")
    for parameter , value in kwargs.items():
        print(f"{parameter}: {value}")


trainingFunction([1,2,3,5,3,2,1,3,4,2,4,1,34,2,3,1,3],20,45,234,123,454,234,46,lr=0.001,epchos=2000)


"Lamda Function "
# lambda arguments: expression
print()
print()
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # 20

#Used constantly for custom sorting, filtering, mapping in data pipelines.