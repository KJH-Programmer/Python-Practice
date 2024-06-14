# 리스트를 절대값을 기준으로 정렬
numbers = [-5, -2, -1, 0, 1, 3, 7, 8, -9]
sorted_numbers = sorted(numbers, key=abs)  # key=lambda x: abs(x)
print("절대값 기준 정렬:", sorted_numbers)
print()

# 딕셔너리의 리스트를 특정 키를 기준으로 정렬
students = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 22},
    {"name": "Dave", "age": 23}
]

# 나이 기준으로 정렬
sorted_students = sorted(students, key=lambda x: x['age'])
print("나이 기준으로 정렬:", sorted_students)
print()

# 이름을 기준으로 정렬
sorted_students_name = sorted(students, key=lambda x: x['name'])
print("이름 기준으로 정렬:", sorted_students_name)
print()

## 딕셔너리의 리스트 정렬 ##
students = [
    {"name": "John", "age": 25, "grade": 85},
    {"name": "Jane", "age": 22, "grade": 90},
    {"name": "Anna", "age": 22, "grade": 91},
    {"name": "Dave", "age": 23, "grade": 88},
    {"name": "Alice", "age": 24, "grade": 95}
]
# 나이와 성적 기준으로 정렬 (먼저 나이, 그 다음 성적)
sorted_by_age_then_grade = sorted(students, key=lambda x: (x["age"], x["grade"]))
print("나이와 성적 기준 정렬:", sorted_by_age_then_grade)
print()

## 클래스 객체의 리스트 정렬 ##

