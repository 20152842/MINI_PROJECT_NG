from Action import * as AC


class Deposit(action):
    
    user_imp = AC.UserInput()
    if (AC.Check_Fraud()):
        AC.Input_Cash()
    
    
    
    
def Deposit_Main