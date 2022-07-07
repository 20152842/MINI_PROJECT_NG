from Action import *
class Deposit():
    
    user_id = Action.UserInput()
    check = Action.Check_Fraud()
    cash = Action.Input_Cash()
    Action.recipt(Action.Call_Accounts_desc( Action.Call_Customer_Account(user_id)['customer_id'] )['accounts_desc'], cash)
    
    
