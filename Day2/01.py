# 튜플, 콜백 함수, 람다, with 구문

#%% 튜플

a = (1, 2, 3)
print('튜플의 전체', a)
print('튜플의 첫 번째 원소', a[0])
# %% 리스트

a = [1, 2, 3]
print('리스트의 전체', a)
print('리스트의 첫 번째 원소', a[0])
# %% 튜플과 리스트의 차이
tuple_a = (1, 2, 3)
list_a = [1, 2, 3]

# 리스트는 변경 가능, 튜플은 변격 불가능

# 리스트에서 첫번째 원소를 변경하고 싶다
list_a[0] = 4
print(list_a)
# 리스트에 5를 추가
list_a.append(5)
print(list_a)
# %%

# 튜플은 원소를 변경 불가능
tuple_a[0] = 4
print(tuple_a)  
# tuple_a[0] = 4
print(tuple_a) 
# 에러 발생

tuple_a.append(5)
print(tuple_a)
# AttributeError: 'tuple' object has no attribute 'append'
# 에러 발생

# %%

# 리스트는 변경이 가능한 자료를 다룰 때 사용
#   ㄴ 고객목록 등

# 튜플은 변경이 불가능한 자료를 다룰 때 사용
#   ㄴ 고객목록(고정) , 설정값(고정)

# %% 튜플의 교환

a, b = 100, 200
# temp = a
# a = b
# b = temp

a, b = b, a
print(a, b)

# %% 튜플과 함수

def return_all(a, b, c):
    return a, b, c

print(return_all(10, 20, 30))
print(type(return_all(10, 20, 30)))  # 튜플로 인식하게된다.
#%%
def return_all(*values):
    print(f"values의 타입은 {type(values)}")
    return values

print(return_all(10, 20, 30))
print(type(return_all(10, 20, 30)))
# %%  콜백 함수 와 람다

# 매개변수로 받은 함수를 10번 호출
def call_10_times(func):
    for i in range(10):
        func()

# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")

# 조합하기
call_10_times(print_hello)        

# print_hello : 콜백함수 - 함수의 매개변수에 사용하는 함수

# %% 
list_input_a = [1, 2, 3, 4, 5]

def power(item):
    return item * item

# for문, enumerate 키워드
for i, value in enumerate(list_input_a):
    print(i, value)
    #print(list(enumerate(list_input_a)))
    list_input_a[i] = power(value)

print(list_input_a)

# %%
# map(함수, 리스트), 고차함수
list_input_a = [1, 2, 3, 4, 5]

def power(item):
    return item * item

output_a = map(power, list_input_a)
print(list(output_a))

#리스트 컴프리헨션
print([power(x) * x for x in list_input_a])
#%%
# filter()함수
list_input_a = [1, 2, 3, 4, 5]
def under_3(item):
    return item < 3
output_b = filter(under_3, list_input_a)
print(list(output_b))

output_b = filter(under_3, list_input_a)
# filter : 왼쪽에있는 원소들만 만족하는 값을 출력

#리스트 컨프리헨션
print([x * x for x in list_input_a if x < 3])

# %% 람다함수 = 익명함수

# filter() 함수를 변형
list_input_a = [100, 200, 300, 400, 500]
def under_3(item):
    return item < 300

output_b = filter(lambda x: x < 300, list_input_a)
print(list(output_b))

# map() 함수를 변형
list_input_a = [100, 200, 300, 400, 500]

def power(item):
    return item * item

output_a = map(lambda item: item * item, list_input_a)
print(list(output_a))
# %% with 함수 (파일 작업)

# with open() 함수 : 파일 열기
with open('basic.txt', 'r') as file:  # basic.txt 를 r : 읽어오다
    contents = file.read()

print(contents)

# %%
with open('basic.txt', 'w') as file:  # basic.txt 를 w : 쓰다
    file.write("adadad")

with open('basic.txt', 'r') as file:  # basic.txt 를 r : 읽어오다
    contents = file.read()

print(contents)   # basic.txt 파일에서 hello world 에서 adadad 로 바뀜
# %%
print("hello")
# %%
