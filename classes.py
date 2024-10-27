#program for classes and funtion
class xyz_bank:
    def __init__(self,c_name,acc_no,balance,acc_type):
        self.customer_name=c_name
        self.acc_no=acc_no
        self.balance=balance
        self.acc_type=acc_type
    def credit(self,amount):
        if amount>0:
            self.balance+=amount
            print('Money Credited..Available Balance:',self.balance)
        else:
            print('Invalid Amount')
    def debit(self,amount):
        if amount>0 and amount<=(self.balance-100):
            self.balance-=amount
            print('Money is debited..Available Balance:',self.balance)
        else:
            print('Insufficient Balance')
    def open_term_deposit(self,principle,year):
        if self.acc_type=='Sr.Citizen':
            interest=0.12
        else:
            interest=0.10
        si=principle*year*interest
        total_amount=principle+si
        print('Open Term Deposit Amount: ',total_amount)
    def display(self):
        print('Customer Name: ',self.customer_name,'\nAccount Number:',self.acc_no,'\nAccount Type:',self.acc_type,'\nAvailable Balance: ',self.balance)
        
c1=xyz_bank('vel',102201,50000,'Sr.Citizen')
c1.credit(500)
c1.debit(100)
c1.open_term_deposit(2000,5)
c1.display()
while True:
    print('.....Welcome to our bank.....\n Enter your details\n')
    n=input('Enter your Name:')
    ac=input('Enter Account Number')
    
    
