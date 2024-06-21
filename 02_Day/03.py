import random
print(random.randrange(0, 2))  # 0 이상 2 미만의 임의의 숫자 랜덤으로 하나 출력


import user.cal as cal  # user 패키지 안에있는 cal 모듈을 호출하고 cal 이라 별칭을 지음
print(cal.plus(4, 3))

from user import cal as c  # user 패키지에서 cal 모듈을 불러 사용하고 c 라 별칭을 지음
print(c.plus(4,3))