## 1단계
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        return self.balance  # 남은 잔고 반환
    
    def withdraw(self, money):
        if money > self.balance:
            return "Insufficient funds"
        self.balance -= money
        return self.balance  # 남은 잔고 반환

    def __str__(self):
        return f"owner={self.owner}, balance={self.balance}"

# 테스트 코드
acc = BankAccount("Charlie", 500)
print(acc)
print(acc.deposit(100))
print(acc.withdraw(200))
print(acc.withdraw(500))
print()

## 2번
class SavingsAccount(BankAccount):
    def add_interest(self, num):
        self.balance += self.balance * num
        return self.balance

# 테스트 코드
savings = SavingsAccount("Dana", 1000)
print(savings)
print(savings.add_interest(0.05))
print(savings)
print()

## 3번
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=0):
        # self.owner = owner
        # self.balance = balance
        super().__init__(owner, balance)  # super() : 기존에 있던 부모class에 있던 메소드를 가져와서 사용, 위에 두줄을 따로 쓸 필요 없음
        self.overdrft_limit = overdraft_limit

    def withdraw(self, money):
        if money > self.balance + self.overdrft_limit:
            return "Insufficient funds, overdraft limit reached"     
        self.balance -= money
        return self.balance
    
# 테스트 코드
checking = CheckingAccount("Eve", 500, 200)
print(checking)
print(checking.withdraw(600))
print(checking.withdraw(150))
print(checking)
