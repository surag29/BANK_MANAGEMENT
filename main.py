import json
import random
import string
from pathlib import Path


class bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)

    except Exception as err:
        print(f"AN EXCEPTION HAS OCCURRED AS {err}")


    
    @classmethod
    def __update(cls):

        with open(bank.database,'w') as fs:
            fs.write(json.dumps(cls.data))


    
    @classmethod
    def __accountgenerate(cls):
        alpha  = random.choices(string.ascii_letters,k= 3)
        num = random.choices(string.digits, k= 3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)




    def createaccount(self):

        info = {
            "NAME"  :  input("ENTER YOUR NAME  : -"),
            "AGE" : int(input("ENTER YOUR AGE ;- ")),
            "EMAIL" : input("ENTER YOUR EMAIL : - "),
            "PIN" : int(input("ENTER YOUR 4 NO  PIN : - ")),
            "ACCOUNTNO." : bank.__accountgenerate(),
            "BALANCE" : 0
        }
        if info['AGE'] < 18 or len(str(info['PIN'])) != 4 :
            print("SORRY YOU CANNOT CREATE YOUR ACCOUNT ")
        else:
            print("ACCOUNT CREATED SUCCESSFULLY")
            for i in info :
                print(f"{i},{info[i]}")
            print("PLEASE NOTE DOWN YOUR ACCOUNT NUMBER ")

            bank.data.append(info) 

            bank.__update()


    
    def depositmoney(self):
        accnumber  = input("please tell your account number :")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in bank.data if i['ACCOUNTNO.'] == accnumber and i['PIN'] == pin]

        if userdata == False:
            print("oops sorry no data found ")
        
        else:
            amount = int(input("enter how much you want to deposit"))
            if amount > 10000:
                print("sorry the amount is too much you can deposit below 10000")

            else :
                userdata[0]['BALANCE'] += amount
                bank.__update()
                print(userdata)
                print("amount deposited successfully")


        

    def withdrawmoney(self):
            accnumber  = input("please tell your account number :")
            pin = int(input("please tell your pin as well "))

            userdata = [i for i in bank.data if i['ACCOUNTNO.'] == accnumber and i['PIN'] == pin]

            if userdata == False:
                print("oops sorry no data found ")
            
            else:
                amount = int(input("enter how much you want to withdraw"))
                if userdata[0]['BALANCE'] < amount:
                    print("SORRY YOU DONT HAVE ENOUGH BALANCE ")

                else :
                    userdata[0]['BALANCE'] -= amount
                    bank.__update()
                    print(userdata)
                    print("amount WITHDREW successfully")

    

    def checkdetails(self):
         accnumber  = input("please tell your account number :")
         pin = int(input("please tell your pin as well "))

         userdata = [i for i in bank.data if i['ACCOUNTNO.'] == accnumber and i['PIN'] == pin]

         print("your information are \n\n\n")

         for i in userdata[0]:
             print(f"{i} : - {userdata[0][i]}")
    



    def updatedetails(self):
         accnumber  = input("please tell your account number :")
         pin = int(input("please tell your pin as well "))


         userdata = [i for i in bank.data if i['ACCOUNTNO.'] == accnumber and i['PIN'] == pin]

         if userdata == False:
                print("oops sorry no data found ")
        
         else:
             print("you cannot change the  age ,account number ,and balance ")

             print(" fill the details for change  or leave it empty for no change ")

             newdata =  {
                 "NAME"  : input("please enter the new name or press enter : -"),
                 "EMAIL" :  input("please enter the new email or press enter : -"),
                 "PIN"  : input("please enter the new pin or press enter to skip : -")
                 
             }

             if newdata['NAME'] == "":
                 newdata['NAME'] = userdata[0]['NAME']

             if newdata['EMAIL'] == "":
                 newdata['EMAIL'] = userdata[0]['EMAIL']

             if newdata['PIN'] == "":
                 newdata['PIN'] = userdata[0]['PIN']
             
             newdata['AGE'] = userdata[0]['AGE']
             newdata['ACCOUNTNO.'] = userdata[0]['ACCOUNTNO.']
             newdata['BALANCE'] = userdata[0]['BALANCE']

             if type(newdata['PIN']) == str:
                 newdata['PIN'] = int(newdata['PIN'])
            
             for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     
                     userdata[0][i] = newdata[i]
             
             bank.__update()
             print("DETAILS UPDATED SUCCESSFULLY")
             
    
    def delete(self):
         accnumber  = input("please tell your account number :")
         pin = int(input("please tell your pin as well "))


         userdata = [i for i in bank.data if i['ACCOUNTNO.'] == accnumber and i['PIN'] == pin]

         if userdata == False:
                print("oops sorry no data found ")
         
         else:
             
             check =   input("press y if you actually want to delete the account or press n ")

             if check == 'n' or check == "N":
                 print("bypassed")
             
             else:
                 index = bank.data.index(userdata[0])
                 bank.data.pop(index)
                 print("account deleted successfully")
                 bank.__update()
        

        







            



    


        
        

    



user = bank()

print("PRESS 1 FOR CREATING AN ACCOUNT ")
print("PRESS 2 FOR DEPOSITING THE MONEY IN ACCOUNT ")
print("PRESS 3 FOR WITHDRWAING THE MONEY FROM ACCOUNT ")
print("PRESS 4 FOR DETAILS")
print("PRESS 5 FOR UPDATING DETAILS")
print("PRESS 6 FOR DELETING ACCOUNT")

check = int(input("tell your response : - "))

if check ==1 :

    user.createaccount()

if check == 2:

    user.depositmoney()

if check == 3:

    user.withdrawmoney()

if check ==4:

    user.checkdetails()

if check == 5:

    user.updatedetails()

if check == 6:

    user.delete()