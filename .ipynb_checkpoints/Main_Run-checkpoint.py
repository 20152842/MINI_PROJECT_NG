
class Main_Run:
   # if __name__ == "__main__":
    print("이용하실 기능을 골라주세요.")
    print('-' *30)
    print("1. 입금")
    print("2. 출금")
    print("3. 계좌 송금")
    print("4. 조회 거래")
    print('-' *30)
   

    user_input = int(input())
    
    
    if(user_input == 1):
        import Deposit
    elif(user_input == 2):
        import Withdraw
    elif(user_input == 3):
        import Remittance
    elif(user_input == 4):
        import LookUp_Tran