# 문제 1
def add_and_multiply(x, y):
    return x + y, x * y
result = add_and_multiply(5, 3)
print(result)  
# (8 , 15)

# 문제 2
def apply_callback(a, b, c):
    return c(a, b)

def add(a, b):
    return a + b

result = apply_callback(5, 3, add)
print(result)
# 8

# 문제 3
sum_lambda = lambda x, y: x + y
result = sum_lambda(5, 3)
print(result)

# 문제 4
def higher_order_function(a, b, c):
    return c(a, b)
def multiply(a, b):
    return a * b
result = higher_order_function(5, 3, multiply)
print(result)

# 문제 5
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
write_to_file('example.txt', 'Hello, world')