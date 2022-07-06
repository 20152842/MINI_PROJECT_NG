import random
import pymysql

class Action :
    
    
    
    def UserInput():# 카드 통장 삽
        print("카드나 통장을 삽입하세요.")
        custom_id = str(random.randint(101,112))
        customer = 'C-' + custom_id
    
        return customer
    
    def Input_Cash():
        input_cash = {"1 만원권" : 0, "5 만원권" : 0, "10 만원권" : 0}
        
        for i in input_cash :
            input_cash[i] = int(input("입금하실 " + i + "의 갯수를 입력하세요."))
            
        for i in input_cash:
            print(i + " : " + str(input_cash[i]) + "장, ", end = '')
            
        total = input_cash["1 만원권"] * 1 + input_cash["5 만원권"] * 5 + input_cash["10 만원권"] * 10
        print("을 삽입하였습니다. 총 금액은 " + str(total) + "만원 입니다.")
        
        return total
        
    
    
        
    def PassWord(): # 비밀번호 기입
        while(True):
            password = input("비밀번호를 입력하세요")
            if password not in '0123456789' and len(password) != 4:
                print("잘못 입력하셨습니다. 다시 입력하세요")
            elif password in '0123456789' and len(password) == 4:
                return password
            
                       
    def Check_Fraud(): # 사기거래 조회
        list_fraud = [str(random.randint(1000,9999)) for i in range(random.randint(10,20))]
        cnt = 1
        while(cnt):
            user_num = input("전화번호 마지막 4자리를 입력하세요.")
            for i in range(len(user_num)):
                if user_num[i] not in '0123456789':
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                elif user_num[i] in '0123456789' and i == 3:
                    cnt = 0
                    break
            
                                
        if user_num in list_fraud :
            print("사기 거래 번호로 조회되었습니다.")
            print("거래를 종료합니다.")
            return 0
        elif user_num not in list_fraud:
            print("사기 거래 조회 되지 않았습니다. 거래를 계속합니다.")
            return 1
                            
    def Continue(): # 거래 연속 or 종료
        return int(input("거래를 계속하시려면 1을, 거래를 종료하시려면 0를 입력하세요."))
                   
                   
                   
    def recipt(account, total): # 명세표 출력
        
        account_total = int(account) + int(total)
        print("계좌에 총 " + str(account_total) + "원 있습니다.")
        print("카드/통장을 회수하세요")
        print("입금이 완료되었습니다. 안녕히 가세요.")
        
                
        
                   
                   
    def connection(text):   
        con = pymysql.connect(host='localhost', user='lastcoder', password='1234',
                       db='atm_db', charset='utf8',  autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        cur.execute(text)
        #result = cur.fetchall()
        con.close()
        tmp_dict = {}
        tmp = list(cur)
        for i in range(len(tmp)):
            for j,k in tmp[i].items():
                tmp_dict[j] = k
        print(tmp_dict)
        return tmp_dict   # Select col 들을 딕셔너리 반환
                   
                
    def Call_Customer_Account(user_input):
        info = "select AC.accounts_name, CU.customer_name, CU.customer_street, CU.customer_city, AC.accounts_id, AC.customer_id \
        from accounts AC, customer CU \
        where AC.accounts_id = (select CU.accounts_id \
		from customer CU \
		where CU.customer_id = '" + user_input + "')  \
        and CU.customer_id = '" + user_input + "';"
        tmp_dict = {}
        print("목록 : 계좌명, 고객명, 고객 주소, 계좌 ID, 고객 ID")        
        #아이디 입력시 고객 id, 계좌 id , 계좌 이름     
        return Action.connection(info)
                   
                   
    def Call_Accounts_password(user_input):
        password = "select accounts_password\
        from accounts \
        where accounts_id = (select accounts_id \
		from customer \
        where customer_id = '" + user_input + "');"
        print("계좌 비밀번호")
        return connection(info)
                   
    
    def Call_Accounts_desc(user_input):#계좌 잔액 조회
        info = "select accounts_desc \
                from accounts \
                where accounts_id = (select accounts_id \
				from customer \
                where customer_id = '" + user_input +"');"
        print("계좌 desc")

        return Action.connection(info)
                   
                   
    def Call_Branch(user_input):#은행 지점 이름, 은행 위치, 은행 id
        info = "select BR.branch_name, BR.branch_city, BR.branch_asserts, BR.branch_id \
        from branch BR, customer CU \
        where BR.customer_id = CU.customer_id and CU.customer_id = '" + user_input + "';"
                   
        print("목록 : 은행명, 은행 주소, 은행ID")
        return connection(info)
                   
                   
                   
                   
                   
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
