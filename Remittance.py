from Action import *

class Remittance():
    cnt = 1
    while(cnt):
        user_id = Action.UserInput()
        check = Action.Check_Fraud()
        Action.Check_Password( int(Action.Call_Accounts_password( Action.Call_Customer_Account(user_id)['customer_id'] )['accounts_password'] ))
        bank_id = Action.Call_Branch( Action.Call_Customer_Account(user_id)['customer_id'] )['branch_id']
        account_id = Action.Call_Customer_Account(user_id)['accounts_id'] 
        total = Action.Input_Cash()
        Action.update_accounts(total, account_id)
        cnt = Action.Continue()