import random
import pymysql
import sys
import time

class Action :
    
    
    
    def UserInput():# 카드 통장 삽
        print("카드나 통장을 삽입하세요.")
        custom_id = str(random.randint(101,112))
        customer = 'C-' + custom_id
        time.sleep(1)
        return customer
    
        
    def Withdraw_UI():
        print("출금하실 종류를 선택하세요")
        print('-' *30)
        print("1. 전액 현금")
        print("2. 전액 수표")
        print("3. 현금 + 수표")
        print('-' *30)
        
        return int(input())
        
    def LookUp_Tran_UI(user_id):
        print("거래를 선택하세요")
        print('-' *30)
        print("1. 조회 후 출금")
        print("2. 최종일 거래내역 조회")
        print("3. 전체 거래내역 조회")
        print('-' *30)
        
        if(int(input()) == 1):
            print("현재 고객님의 계좌 잔액은 " + str(Action.Call_Accounts_desc(user_id)['accounts_desc']) + "입니다.")
            return Action.Withdraw_Cash(Action.Withdraw_UI())
            
    
    
    
    def Input_Cash():
        input_cash = {"1 만원권" : 0, "5 만원권" : 0, "10 만원권" : 0}
        
        for i in input_cash :
            input_cash[i] = int(input("입금하실 " + i + "의 갯수를 입력하세요."))
            
        for i in input_cash:
            print(i + " : " + str(input_cash[i]) + "장, ", end = '')
            
        total = input_cash["1 만원권"] * 1 + input_cash["5 만원권"] * 5 + input_cash["10 만원권"] * 10
        print("을 삽입하였습니다. 총 금액은 " + str(total) + "만원 입니다.")
        time.sleep(1)
        
        return total
    
    def Withdraw_Cash(user_input):
        if user_input == 1:
            out_cash = {"1 만원권" : 0, "5 만원권" : 0}
        elif user_input == 2:
             out_cash = {"10 만원권" : 0}
        elif user_input == 3:
             out_cash = {"1 만원권" : 0, "5 만원권" : 0, "10 만원권" : 0}
        
        while(True):
            try:
                for i in out_cash :
                    out_cash[i] = int(input("출금하실 " + i + "의 갯수를 입력하세요."))
            except KeyError:
                print("잘못 입력하셨습니다. 선택하신 돈의 종류를 맞춰주세요.")
            else:
                break
                
                
        for i in out_cash:
            print(i + " : " + str(out_cash[i]) + "장, ", end = '')

        if user_input == 1:        
            total = out_cash["1 만원권"] * 1 + out_cash["5 만원권"] * 5
        elif user_input == 2:
            total = out_cash["10 만원권"] * 10
        elif user_input == 3:
            total = out_cash["1 만원권"] * 1 + out_cash["5 만원권"] * 5 + out_cash["10 만원권"] * 10
            
            
        print("을 출금하였습니다. 총 금액은 " + str(total) + "만원 입니다.")
        time.sleep(1)
        
        return total
        
    
    
        
    def PassWord(): # 비밀번호 기입
        cnt = 1
        while(cnt):
            user_num = input("비밀번호 4자리를 입력하세요.")
            for i in range(len(user_num)):
                if user_num[i] not in '0123456789' or len(user_num) !=4:
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    break
                elif user_num[i] in '0123456789' and i == 3:
                    continue;
                    
            
    def Check_Fraud(): # 사기거래 조회
        list_fraud = [str(random.randint(1000,9999)) for i in range(random.randint(10,20))]
        cnt = 1
        while(cnt):
            user_num = input("전화번호 마지막 4자리를 입력하세요.")
            for i in range(len(user_num)):
                if user_num[i] not in '0123456789' or len(user_num) !=4:
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    break
                elif user_num[i] in '0123456789' and i == 3:
                    cnt = 0
                                       
        if user_num in list_fraud :
            print("사기 거래 번호로 조회되었습니다.")
            sys.exit("거래를 종료합니다.")
            
        elif user_num not in list_fraud:
            print("사기 거래 조회 되지 않았습니다. 거래를 계속합니다.")
        
                            
    def Continue(): # 거래 연속 or 종료
        return int(input("거래를 계속하시려면 1을, 거래를 종료하시려면 0를 입력하세요."))
                   
                   
                   
    def recipt(account, total): # 명세표 출력
        
        account_total = int(account) + int(total)
        print("계좌에 총 " + str(account_total) + "만원 있습니다.")
        print("카드/통장을 회수하세요")
        sys.exit("거래가 종료되었습니다. 안녕히 가세요.")
                
        
    def update(text):
        con = pymysql.connect(host='localhost', user='lastcoder', password='1234',
                       db='atm_db', charset='utf8',  autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        cur.execute(text)
        #result = cur.fetchall()
        con.close()
                   
    def connection(text):   
        con = pymysql.connect(host='localhost', user='lastcoder', password='1234',
                       db='atm_db', charset='utf8',  autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        cur.execute(text)
        #result = cur.fetchall()
        con.close()
        tmp_dict = {}
        tmp = list(cur)
        if not tmp:
            print("계좌 정보가 존재하지 않습니다.")
            return Action.recipt(0,0)
         
        #for i in range(len(tmp)):
        #   tmp_dict = {j : k for j, k in tmp[i].items()}
            
        for i in range(len(tmp)):
            for j,k in tmp[i].items():
                    tmp_dict[j] = k
                
        print("check_connec")
        time.sleep(1)
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
        print("check_cus")
        return Action.connection(info)
                   
                   
    def Call_Accounts_password(user_input):
        info = "select accounts_password, CU.customer_id \
                from accounts AC, customer CU \
                where CU.customer_id = AC.customer_id and CU.customer_id = '" + user_input + "';"
        print("계좌 비밀번호")
        return Action.connection(info)
                   
    
    def Call_Accounts_desc(user_input):#계좌 잔액 조회
        info = "select accounts_desc \
                from accounts \
                where accounts_id = (select accounts_id \
				from customer \
                where customer_id = '" + user_input +"');"
        print("계좌 desc")
        print("check_acc")
        return Action.connection(info)
                   
                   
    def Call_Branch(user_input):#은행 지점 이름, 은행 위치, 은행 id
        info = "select BR.branch_name, BR.branch_city, BR.branch_asserts, BR.branch_id \
        from branch BR, customer CU \
        where BR.customer_id = CU.customer_id and CU.customer_id = '" + user_input + "';"
                   
        print("목록 : 은행명, 은행 주소, 은행ID")
        return Action.connection(info)
    
    def Check_Password(password):
        cnt = 3
        while(cnt > 0):
            user_input = int(input("비밀번호를 입력하세요 : "))
            if user_input == password :
                break
            else:
                print("비밀번호가 다릅니다. 입력 횟수가 " + str(cnt) + "번 남았습니다.")
                cnt -= 1
            if cnt == 0 :
                sys.exit("입력 횟수를 초과하였습니다. 거래를 종료합니다.")
        
    def update_accounts_minus(value, account_id):
        info = "select accounts_desc \
            from accounts \
            where customer_id = '"+ account_id +"';"
        total = int(Action.connection(info)['accounts_desc']) - value
        if total < 0 :
            total = 0
            print("계좌의 잔액이 부족합니다.")
            return
        print("계좌의 잔액이 " + str(Action.Call_Accounts_desc(account_id)['accounts_desc']) + " 에서", end = '')
        info = "update accounts set accounts_desc = '"+ str(total) +"' where customer_id = '"+ account_id +"';"
        Action.update(info)
        print( str(Action.Call_Accounts_desc(account_id)['accounts_desc'] + "로 변경되었습니다.") )
        
    def update_accounts_plus(value, account_id):
        info = "select accounts_desc \
            from accounts \
            where customer_id = '"+ account_id +"';"
        total = value + int(Action.connection(info)['accounts_desc'])
        print("계좌의 잔액이 " + str(Action.Call_Accounts_desc(account_id)['accounts_desc']) + " 에서", end = '')
        info = "update accounts set accounts_desc = '"+ str(total) +"' where customer_id = '"+ account_id +"';"
        Action.update(info)
        print( str(Action.Call_Accounts_desc(account_id)['accounts_desc'] + "로 변경되었습니다.") )
        
                   
                   
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
