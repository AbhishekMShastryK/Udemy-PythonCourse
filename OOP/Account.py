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

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee

checking = checking("balance.txt",20)
checking.transfer(300)
print(checking.balance)
checking.commit()