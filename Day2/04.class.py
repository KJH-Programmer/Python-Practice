# 절차지향 프로그래밍

sungjin_age = 21
sungjin_name = "성진"

def introduce(name, age):
    print(f"나는 {name}이고, {age}살이야")

introduce(sungjin_name, sungjin_age)
print()
# 객체지향 프로그래밍
# 위 절차지향보다는 더 단순하게 만들어준다.

# 클래스, 인스턴스, 필드, 메서드, 생성자 ★★★각각의 의미 알기★★★
class Human:
    # 필드(성질, 속성)
    def __init__(self, age, name):
        self.age = age
        self.name = name

    # 메서드(행동, 행위)
    # def exercise(self):
    #     print("스쿼시!")
    #     print(self.age, self.name)

    # 메서드(행동, 행위)
    def introduce(self):
        print(f"나는 {self.name}이고, {self.age}살이야")    

# a = Human(name="Bob", age=10)    
# a.exercise()

sungjin = Human(age=21, name='성진')
print(sungjin_name, sungjin_age)
sungjin.introduce()