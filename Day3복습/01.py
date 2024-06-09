## 문제 1 : 빅오 표기법
#1
import time
def example1(n):
	for i in range(n):
		for j in range(n):
			print(i, j)

#2
import time
def example2(lst):
    result = []
    for i in range(len(lst)):
        if not my_in(result, lst[i]):                
        #if lst[i] not in result:
            result.append(lst[i])
    return result

def my_in(arr, element):
    for a in arr:
        if a == element:
            return True
    return False    

start = time.time()
lst = list(range(1, 10000))
example2(lst)
end = time.time()
print(end - start)
print()
#3

#4


## 문제 2
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 3, 2, 4, 3, 5]))
print()

## 문제 3
def modify_list(lst):
    # 리스트에 값 추가
    lst.append(4)     # 1 2 3 1 2 3 4
    lst.insert(2, 5)  # 1 2 5 3 1 2 3 4

    # 리스트에서 값 제거
    lst.remove(1)    # 2 5 3 1 2 3 4
    lst.pop(3)       # 2 5 3

    lst[3] = 1
    return lst

# 예시 입력
lst = [1, 2, 3, 1, 2, 3]
print(modify_list(lst))
print()    # [2, 5, 3, 1, 3 ,4]   

## 문제 4


## 문제 5
print("문제5")
def word_count(string):
    words = string.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
			
print(word_count("apple banana apple orange banana"))
# {'apple': 2, 'banana': 2, 'orange': 1}     


print("문제6")
def print_dict(dct):
    for key, value in dct.items():
        print(f"키: {key}, 값: {value}")

# 예시 입력
dct = {'사과': 2, '바나나': 3, '오렌지': 1}
print_dict(dct)    


print("문제7")
def get_value(dct, key):
    pass
    

# 예시 입력
dct = {'name': 'Alice', 'age': 25, 'city': 'Seoul'}
print(get_value(dct, 'name'))
print(get_value(dct, 'age'))


print("문제8")
def add_entry(dct, key, value):
    pass 
    
# 예시 입력
dct = {'name': 'Alice', 'age': 25}
new_key = 'city'
new_value = 'Seoul'
print(add_entry(dct, new_key, new_value))