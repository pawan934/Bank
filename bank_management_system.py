import sqlite3
import random as r
class Bank:
    print('\t\t\t=====================================')
    print('')
    print('\t\t\t---->>>>WELCOME TO THE BANK<<<<------')
    print('')
    print('\t\t\t=====================================')
    def __init__(self):
        self.con = sqlite3.connect('Bank.db')
        self.c = self.con.cursor()

    def CreateAccount(self):
        self.c.execute('''create table if not exists Bank(
            account_name text,
            acc_num integer,
            balance integer
        )''')

        n1 = input('Enter Your First Name :- ').upper()
        n2 = input('Enter Your Last Name :- ').upper()

        if n1.isalpha() and not n1.isspace() and n2.isalpha() and not n2.isspace():
            name = n1+' '+n2
            num = r.randint(100000, 999999)
            amount = 0

            self.c.execute("insert into Bank values(?,?,?)",(name, num, amount))
            print('')
            print('====Congratulations {} Your Account Sucessfully Created===='.format(name))
            print('')
            print('')
            print('**** Please note down {} Your Account No. ****'.format(num))
            print('')
            self.con.commit()
            self.con.close()
            # self.c.execute("select * from Bank")
            # c = self.c.fetchall()
            # print(c)


        else:
            print('Enter invalid Name, Try Again.......')

    def OpenAccount(self):
        a_num = int(input('Enter Your Account No.'))
        check = True
        flag = False
        for a,b,c in self.c.execute("select * from Bank"):
            if b == a_num:
                check = False
                flag = True
                val = c
                na = a
                print("(d) -Deposit")
                print("(w) -Withdraw")
                print("(c) -Check Balance")
                ope = input('Enter any of the Operation (c)/(w)/(d)..:- ')
        if flag and (ope == 'd' or ope == 'D'):
            dep = int(input('Enter the Amount to Deposite :- '))
            deposite = dep + val
            self.c.execute("update Bank set balance = ? where acc_num = ? ", (deposite, a_num))
            self.con.commit()
            print('Sucessfully deposited Amount ₹ {}.00 Avl Balance ₹ {}.00'.format(dep, deposite))
            self.con.close()
        
        if flag and (ope == 'w' or ope == 'W'):
            wid = int(input('Enter the Amount to Withdraw :- '))
            if val >0 and val >=wid:
                withdraw = val - wid
                self.c.execute("update Bank set balance = ? where acc_num = ? ", (withdraw, a_num))
                self.con.commit()
                print('Dabited for Amount ₹ {}.00 Avl Balance ₹ {}.00'.format(wid, withdraw))
                self.con.close()
            else:
                print('Balance is Low')

        if flag and (ope == 'c' or ope =='C'):
            print('Hello! Mr.{} Your Total Balance is ₹ {}.00.'.format(na, val))
            print('__________________________________________________________')

        if check:
            print('Invalid Account No.')



bk= Bank()
print ('(c) -Create Account')
print ('(l) -Open Account')
op = input('Enter choice Operation (c)/(l) :-')
if op == 'c' or op == 'C':
    bk.CreateAccount()
if op == 'l' or op == 'L':
    bk.OpenAccount()

