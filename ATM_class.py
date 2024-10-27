class ATMCard:
    def __init__(self, card_number,name, pin, balance):
        self.card_number = card_number
        self.name =name
        self.pin = pin
        self.balance = balance
        self.attempts = 0

    def swipe_card(self, entered_pin, amount):
        if self.attempts >= 3:
            self.calling_police()
            return "Account is locked due to too many wrong PIN attempts. Police have been notified."
        
        if entered_pin == self.pin:
            if amount > self.balance:
                return "Insufficient balance."
            self.balance -= amount
            return "Withdrew ",amount," from your account. Available balance: ",self.balance
        else:
            self.attempts += 1
            return "Wrong PIN!!!. Attempts remaining: ",3 - self.attempts

    def check_balance(self, entered_pin):
        if entered_pin == self.pin:
            return "Your account balance is ",self.balance
        else:
            return "Wrong PIN. Please enter the correct PIN to check your balance."

    def calling_police(self):
        print("!!!..Calling the police to report... a potential ATM card theft or misuse!!!.")




try:
    print('Enter your details..')
    no=input('Enter your account NO: ')
    name=input('Enter your name: ')
    pin=int(input('Set a pin number(4digit): '))
    balance=int(input('Enter the balance amount: '))
    atm_card = ATMCard(no,name,pin,balance)# Create an ATM card instance
        
    while True:
        ch=int(input('\nEnter your choice: \n1.Swipe card \n2.check balance \n3.Exit'))
        if ch==1:
            apin=int(input('Enter your pin no: '))
            abalance=int(input('Enter amount you want to withdraw: '))
            print(atm_card.swipe_card(apin,abalance))
        elif ch==2:
            apin=int(input('Enter your pin no: '))
            print(atm_card.check_balance(apin))
        elif ch==3:
            exit()
        else:
            print('Entet valid choice...')
except IOError:
    print('Somethink wants to wrong..')
