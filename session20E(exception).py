class BankingError(Exception):
    pass
class BankAccount():
    def __init__(self):
        self.balance=10000
        self.minBalance=2000
        self.attempts=0
        print("Account activated and balance is \u20b9",self.balance)
    def withdraw(self,amount):
        self.balance-=amount
        if self.balance<self.minBalance:
            print("[F] withdraw failed")
            print("[F] the balance is LOW \u20b9",self.balance)
            self.attempts+=1
        else:
            print("[P]withdraw successfully done")
            print("[P]New balance is \u20b9",self.balance)

        if self.attempts==3:
            # error=IndexError("illegal Attempts")
            error=BankingError("Illegal attempts")
            raise error
print("Banking started")
johnAccount=BankAccount()
johnAccount.withdraw(3000)
johnAccount.withdraw(6000)
johnAccount.withdraw(2000)
for i in range(1,600):
    johnAccount.withdraw(5000)
print("Banking finished")



"""
    Nesting of try except finally :)
    try:
        try:

        except:

        finally:
    except:
        try:

        except:

        finally:
    finally:
        try:

        except:

        finally:

"""



