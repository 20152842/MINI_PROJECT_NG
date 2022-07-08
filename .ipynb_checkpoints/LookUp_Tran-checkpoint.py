from Action import *


class LookUp_Tran():
   
    user_id = Action.UserInput()
    user_input = Action.LookUp_Tran_UI()
    Action.Check_Password( int(Action.Call_Accounts_password( Action.Call_Customer_Account(user_id)['customer_id'] )['accounts_password'] ))
    
    
    

    
    

    
