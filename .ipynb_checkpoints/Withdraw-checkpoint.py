from Action import *


class Withdraw():
    cnt = 1
    while(cnt):
        user_id = Action.UserInput()
        check = Action.Check_Fraud()
        Action.Check_Password( int(Action.Call_Accounts_password( Action.Call_Customer_Account(user_id)['customer_id'] )['accounts_password'] ))
        Action.Withdraw_Cash(Action.Withdraw_UI())
        cnt = Action.Continue()