from Action import * as AC


class Remittance(action):
    
    AC.UserInput()
    AC.Check_Fraud()
    AC.PassWord()
    
    AC.Input_Cash()
    AC.Call_Branch()