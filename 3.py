class Bankacount:
    def __init__(self, bal):
        self.__balance=bal
    def deposit(self, amount):
        self.__balance+=amount
    def withdrow(self,amount):
        if self.__balance>=amount:

            self.__balance-=amount
        else:
            print('error')
    def get_balance(self):
        return self.__balance
import bankacount
def main():
    start_bal=int(input('enter your starting balance:'))
    saving=bankacount.Bankacount(start_bal)
    pay=int(input('how much would you pay this week?'))
    print('i  will deposit pay!')
    saving.deposit(pay)
    print('your balance is:', saving.get_blance())
    cash=int(input('how much would you like throw'))
    print('i will withdrow!')
    saving.withdrow(cash)
    print('your balance is:', saving.get_blance())
main()