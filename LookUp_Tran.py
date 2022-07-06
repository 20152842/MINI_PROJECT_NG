from Action import * as AC







class LookUp_Tran(action):
    def __init__(self):
        
    UI(AC.UserInput())
    LookupMain() 
    
    
    
    

    
    

    
    
    
    
    
def LookupMain(func):
        
    while(cnt)
        if tmp == 1 :
            Lookup_Withdraw()
            func(#Action 참조후 함수 대입) # 클래스 매개변수)
                #계좌 정보 가져온 후 출금 연동
                # 출금 클래스 호출 후 연동
                
            
        elif tmp == 2 :
            Last_Tran()
             func() # 클래스 매개변수)
                #마지막 거래일자 조회
            
        elif tmp == 3 :
            All_Tran()
            func()# 클래스 매개변수)
                #전체 거래내역 조회
        cnt = Continue()
        
    if int(input("거래를 종료하였습니다. 명세표를 출력하시려면 1을, 아니라면 2를 입력하세요.") == 1:
        recipt()
    else :
        print("안녕히가세요")
           
@LookupMain
def LM_PassWord(Action):
    return Action.PassWord()
                    
    
def UI(user):
    print(user + "을(를) 삽입하셨습니다. 거래를 선택하세요")
    print('-' *30)
    print("1. 조회 후 출금")
    print("2. 최종일 거래내역 조회")
    print("3. 전체 거래내역 조회")
    print('-' *30)
        
    return int(input())
        
    
    
def Lookup_Withdraw(PassWord):
        
            
            
def Last_Tran(PassWord):
        
        
def All_Tran(PassWord):
        
   
    
    