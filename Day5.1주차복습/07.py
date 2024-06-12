# 다음은 학생들이 클래스를 구현하고, 생성자를 통해 필드를 주입하며, 원하는 메서드를 구현할 수 있는지 평가할 수 있는 문제입니다. 
# 이 문제는 `self` 키워드를 제대로 이해하고 사용하는지를 평가합니다. 또한, 만든 클래스로 여러 개의 객체를 생성하는 것을 출력 결과로 보여줍니다.
# ### 문제: 클래스 구현하기
# 다음은 `Book` 클래스를 구현하기 위한 요구사항입니다. 설명을 읽고 적절하게 클래스를 구현하세요.
# **요구사항:**
# `Book` 클래스는 `title`, `author`, `year`라는 세 개의 필드를 가집니다.
# 생성자 `__init__`를 통해 필드 값을 주입합니다.
# `description` 메서드를 구현하여 책의 제목, 저자, 출판 연도를 출력합니다.
# `is_classic` 메서드를 구현하여 책이 출판된 지 70년 이상 되었는지를 판단합니다. 70년 이상 되었으면 `True`, 아니면 `False`를 반환합니다.
# 다음과 같은 출력을 내기 위해 `Book` 클래스를 완성하세요.
class Book:
    def __init__(self, title, author, year):
        # 여기에 코드를 작성하세요
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        # 여기에 코드를 작성하세요
        return f"{self.title} by {self.author}, published in {self.year}"
    def is_classic(self):
        # 여기에 코드를 작성하세요
        if self.year + 70 < 2024:
            return True
        else:
            return False
# 객체 생성 및 사용 예시
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

print(book1.description())  # 출력: 1984 by George Orwell, published in 1949
print(book2.description())  # 출력: The Great Gatsby by F. Scott Fitzgerald, published in 1925
print(book3.description())  # 출력: To Kill a Mockingbird by Harper Lee, published in 1960

print(book1.is_classic())  # 출력: True
print(book2.is_classic())  # 출력: True
print(book3.is_classic())  # 출력: False
