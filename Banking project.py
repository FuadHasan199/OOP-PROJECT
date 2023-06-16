
class bank:
    bank_balance = 0
    cust_account_no = 5630
    no_of_customer_account = 0
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address 
        self.loan = 0
        self.loan_feature = True


    def create_account(self,name,NID_num):
        new_account = account(name,NID_num)
        print("Your account create successfully")
        return new_account
        
    def account_number(self,account):
        return account.account_num

    def deposit(self,account,amount):
        if amount < 0:
            print("Invalid amount transection aborted!")
        else:
            account.balance = account.balance + amount
            bank.bank_balance = bank.bank_balance + amount
            account.transection.append(f'deposit : {amount}')
    
    def withdraw(self,account,amount):
        if amount < account.balance and amount > 0:
            if bank.bank_balance < amount:
                print("The bank is bankrupt")
                return
            else:
                account.balance -= amount
                bank.bank_balance = bank.bank_balance - amount
                account.transection.append(f'credit : {amount}')
        else:
            print("Invalid amount transection aborted!")

    def check_balance(self,account):
        print('Your balance is: ',account.balance)
    
    def transfer(self,sender,receiver,amount):
        if amount > sender.balance:
            print("Insufficient balance transection aborted")
        else:
            sender.balance = sender.balance - amount 
            receiver.balance = receiver.balance + amount
            sender.transection.append(f'transfer {amount} from {sender.name} to {receiver.name}')
            

    # def transection_history(self):

    def stop_feature(self):
        if self.loan_feature == True:
            self.loan_feature = False

    def on_feature(self):
        if self.loan_feature == False:
            self.loan_feature = True
         
    def loan_take(self,account):
            get_loan = 2 * account.balance
            if get_loan > bank.bank_balance:
                self.loan_feature = False
            
            if self.loan_feature == True:
                account.balance = account.balance + get_loan
                self.loan = self.loan + get_loan
                bank.bank_balance = bank.bank_balance - get_loan
                print("Your loan is successfully taken")
                account.transection.append(f'loan take {get_loan} from bank')
            else:
                print("Sorry! loan feature is not currently available")
    
    def total_loan_given_by_bank(self):
        return self.loan
    
    def Total_bank_balance(self):
        return self.bank_balance
    
    def transection_record(self,account):
        print("Transection record for account: ",account.name)
        for item in account.transection:
            print(item)
        print("Your account have now: ",account.balance)
    
class account:
    def __init__(self,name,NID_num) -> None:
        self.name = name
        self.NID_num = NID_num
        self.balance = 0
        bank.no_of_customer_account += 1
        self.account_num = bank.cust_account_no + 1
        self.transection = []




Bank= bank('Dhaka','modina market')

user1 = Bank.create_account('fuad',1234)
user2 = Bank.create_account('jawad',3234)
user3 = Bank.create_account('Riad',1434)
user4 = Bank.create_account('Adil',1284)
Bank.deposit( user1,1500)
Bank.deposit(user2,200)
Bank.deposit(user3,500)
Bank.deposit(user4,700)
Bank.check_balance(user1)
Bank.withdraw(user1,400)
Bank.check_balance(user1)
Bank.check_balance(user3)
Bank.transfer(user1,user3,200)
Bank.check_balance(user1)
Bank.check_balance(user3)
Bank.loan_take(user1)
Bank.check_balance(user1)
Bank.account_number(user3)
print(Bank.total_loan_given_by_bank())
Bank.stop_feature()
Bank.loan_take(user3)
Bank.transection_record(user1)
tt = Bank.account_number(user4)
print(tt)
