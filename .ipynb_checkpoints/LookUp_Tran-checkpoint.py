from Action import *


class LookUp_Tran():
    cnt = 1
    while(cnt):
        user_id = Action.UserInput()
        Action.Check_Password( int(Action.Call_Accounts_password( Action.Call_Customer_Account(user_id)['customer_id'] )['accounts_password'] ))
        total = Action.LookUp_Tran_UI(user_id)
        print(total)
        Action.update_accounts_minus(total, user_id)
        cnt = Action.Continue()
    
    

    
    

    
