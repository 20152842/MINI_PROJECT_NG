import random
import pymysql

class Action :
    
    def UserInput():# 카드 통장 삽입
        user = input("카드나 통장을 삽입하세요.")
        return user
    
    def Input_Cash():
        return input("현금 또는 수표를 삽입하세요.")
    
    
        
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
        return int(input("거래를 계속하시려면 1을, 거래를 종료하시려면 0를 입력하세요.")
                   
    def recipt(): # 명세표 출력
                   
    def connection(text):   
        con = pymysql.connect(host='localhost', user='lastcoder', password='1234',
                       db='atm_db', charset='utf8',  autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        cur.execute(text)
        con.close()
        return Sort(cur)
                   
     def Call_Customer_Account(user_input):
        info = "select account_name, accounts_id, customer_id\
        from accounts \
        where accounts_id =(select accounts_id \
		from customer \
		where customer_id = '" + user_input + "');"
        #아이디 입력시 고객 id, 계좌 id , 계좌 이름           
        password = "select accounts_password\
        from accounts \
        where accounts_id = (select accounts_id \
		from customer \
        where customer_id = '" + user_input + "');"
        # 계좌 비밀번호           
        return [info, password]
                   

                   
     def Call_Branch():
   
                   
                   
                   
                   
                   
    def Sort(cur):
        tmp = list(cur)
        a = []
        b = []
        for i in range(len(tmp)):
            for j, k in tmp[i].items():
                a.append(j)
                b.append(k)
        new_a = []
        for i in a :
            if i not in new_a:
                new_a.append(i)
                        
        for i in new_a :
            print(i, end = '           ')
        print()
        for i in range(0, len(b)):
            print(b[i], end = '   /   ')
            if (i+1) % len(new_a) == 0 and i > 1:
                print()
