# 문제 4
def multiply(x, y=1):
	return x * y
result1 = multiply(3, 4)
result2 = multiply(3)

print(result1)
print(result2)

# 문제 5
def print_info(name, age):
	print(f"Name: {name}, Age: {age}")
	
print_info(name="Alice", age=30)
print_info(age=25, name="Bob")

# 심화 1
def add_and_multiply(a, b):
	return a + b, a * b
sum_result, product_result = add_and_multiply(5, 3)
print(f"Sum: {sum_result}, Product: {product_result}") 

# 심화 2
def print_kwargs(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}") 
print_kwargs(name="Alice", age=30, city="New York")

# 심화 3
def mixed_params(a, b, c=0, *args, **kwargs):
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")	

mixed_params(1, 2)
mixed_params(1, 2, 3, 4, 5, 6, key1="value1", key2="value2")

# 호출, 매개변수, 리턴값, 가변 매개변수, 기본 매개변수
#%%
def add(a, b):      # 함수 호출
	return a + b     
add(4, 3)
# %%
#%%
def add(*values):
	result = 0
	for value in values:
		result += value
		# result = result + value
	return result	