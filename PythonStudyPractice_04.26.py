import random

def generate_lotto_numbers():
    lotto_numbers = []

    while len(lotto_numbers) < 6 :
        # 1~45 까지 무작위 정수 생성
        number = random.randint(1, 45)

        #중복방지하기
        if number not in lotto_numbers : 
            lotto_numbers.append(number)
    
    return sorted(lotto_numbers)

if __name__ == "__main__" :
    lotto_numbers = generate_lotto_numbers()
    print("로또 번호: ", lotto_numbers)