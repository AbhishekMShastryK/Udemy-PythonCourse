class Account():

    def __init__(self,filepath):
        self.file_path = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.balance)) 

class checking(Account):
    """This Class generates checking account objects"""

    type = "checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee

jim_checking = checking("jim_balance.txt",20)
jim_checking.transfer(300)
print(jim_checking.balance)
jim_checking.commit()
print(jim_checking.type)

jam_checking = checking("jam_balance.txt",20)
jam_checking.transfer(300)
print(jam_checking.balance)
jam_checking.commit()
print(jam_checking.type)

print(jam_checking.__doc__)