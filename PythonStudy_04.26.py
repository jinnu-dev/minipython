# 캘린더 모듈로 윤년계산
import calendar
print(calendar.isleap(2024)) # --> True

# 윤년이 몇번 있는지 판단하기
print(calendar.leapdays(2019,2030)) # --> 3

# 어떤년도가 윤년인가?
print([y for y in range(2020,2030) if calendar.isleap(y)]) # 2020, 204, 2028

from datetime import datetime

# 현재 시각을 now 에 저장하기
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.date())
print(now.time())
print(now.weekday()) # 0=월 1=화 2-수 3=목 4=금 5=토 6=일

# 난수 사용법 학습
import random
# 특정범위 난수 생성
random_inpeger = random.randint(1,10)

# 특정범위의 난수 간격 지정하여 생성
random_num1 = random.randrange(1, 10, 2)  # 홀수만 강제 출력

# 리스트, 튜블 에서 무작위 요소 추출
ex_list = ["서울","부산","대구","대전","광주","울산","인천"]
random_element = random.choice(ex_list)

# 요소들을 무작위로 섞기
random.shuffle(ex_list)

print(ex_list)

