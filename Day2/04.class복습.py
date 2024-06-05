class Human:
    # 필드(성질, 속성)
    def __init__(self, age, name):   # self, age, name 을 매개변수로 받는다
        self.age = age               # self.age 를 age 로 초기화해준다.
        self.name = name             # self.name 를 name 로 초기화해준다.

    # 메서드(행동, 행위)
    def introduce(self):
	    print(f"내 이름은 {self.name}이고, 나이는 {self.age}살이야")

# 클래스 인스턴스 생성        
jihun = Human(age=28, name='김지훈')

# 인스턴스의 필드에 접근하여 값을 출력
print(jihun.name, jihun.age)

# 인스턴스 메서드 호출
jihun.introduce()       