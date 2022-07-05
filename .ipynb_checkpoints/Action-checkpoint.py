import random

class Action :
    
    def UserInput():# 카드 통장 삽입
        user = input("카드나 통장을 삽입하세요.")
        return user
    
    def PassWord(): # 비밀번호 기입
        while(true):
            password = input("비밀번호를 입력하세요")
            if password not in '0123456789' and len(password) != 4:
                print("잘못 입력하셨습니다. 다시 입력하세요')
            elif password in '0123456789' and len(password) == 4 :
                return password
            
                       
    def Check_Fraud(): # 사기거래 조회
        list_fraud = [random.randint(1000,9999) for i in range(random.randint(10,20))]
        while(true):
            user_num = int(input("전화번호 마지막 4자리를 입력하세요.")
            if user_num not in '0123456789' and len(user_num) != 4:
                print("잘못 입력하셨습니다. 다시 입력하세요')
            elif user_num in '0123456789' and len(user_num) == 4 :
                break                                
                                
        if user_num in list_fraud :
            print("사기 거래 번호로 조회되었습니다.")
            print("거래를 종료합니다.")
            return 0
        elif user_num not in list_fraud:
            print("사기 거래 조회 되지 않았습니다. 거래를 계속합니다.")
                            
    def Continue(): # 거래 연속 or 종료
        return int(input("거래를 계속하시려면 1을, 거래를 종료하시려면 2를 입력하세요.")
                   
    def recipt(): # 명세표 출력
                   