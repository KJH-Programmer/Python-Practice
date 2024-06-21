class Human:
    def __init__(self, name, age, location, hobby):  # 예를들어 hobby = "게임" 이라고 지정하면 hobby="게임" 이라고 고정이됨
        self.name= name
        self.age = age
        self.location = location
        self.hobby = hobby

    def introduce(self):
        print(f"나는 {self.name}이고, {self.age}살이야")
    
    def eat(self):
        print(f"{self.name}은 밥을 먹는다.")

    def exerices(self):
        print(f"{self.name}은 밖에서 뛰고있어")    

    def sleep(self):
        print(f"{self.name}은 잠을 자고있어")

    def do_hobby(self):
        print(f"{self.name}의 취미는 축구야")

sungjin = Human(name = "성진", age=21, location = "광주", hobby = "게임")
jihun = Human(name = "지훈", age=28, location = "광주", hobby = "게임")
sungjin.do_hobby()
jihun.sleep()
print()

## 상속
class Programmer(Human):
    def coding(self):
        print(f"개발자 {self.name}은 코딩을 한다.")

sungjin = Programmer(name = "성진", age=21, location = "광주", hobby = "게임")
sungjin.do_hobby()    # do_hobby 라는 함수는 없지만, 위에 Human이라는 class 를 상속받아서 사용이 가능하다. 
sungjin.coding()      
print()

class Programer(Human):
    def coding(self):
        print(f"개발자 {self.name}은 코딩을 한다.")

    # __str__ 메서드
    def __str__(self):
        return f"Programmer(age={self.age}, name={self.name}, location={self.location}, hobby={self.hobby})"
sungjin = Human(name = "성진", age=21, location = "광주", hobby = "게임")
#sungjin.do_hobby()  -> sungjin.coding() Human 이라는 클래스에는 coding 이라는 함수가 없기에 오류 발생