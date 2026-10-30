balance = 10000
correct_pin = 2026
withdrawl = True
deposit = True

pin = int(input("enter the pin to unlock account :"))
if (correct_pin != pin):
    print ("login failed :")
else :
    print("login successfully :")
    while True :
        print("banking management system :")
        print("1. withdrawl :")
        print("2. deposit :")
        print("3. check balance :")
        print("4. exit :")
        
        choice = int(input("enter your choice :"))
        if choice == 1:
            amount = int(input("enter the withdrawl amount :"))
            if (amount <= balance and amount >= 0):
                print("amount debited successful:")
                balance = balance - amount 
                print("rest balance :",balance)
            else :
                print ("insufficient balance:")

        elif choice == 2:
            amount = int(input("enter the amount to be deposit :"))
            print("amount credit successful:")
            balance = balance + amount
            print ("total balance",balance)
        
        elif choice == 3:
            print ("current balance :",balance)

        elif choice == 4:
            print ("thankyou for using my banking management system :")
            break 

        else :
            print ("invalid choice :")

