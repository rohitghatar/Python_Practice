# Here we import UDF func module for reusability of same function and sys func for exit programme and save data in log file
import func, sys

# this object will store all customer's data in dictionary format
customer_data = {101: {'name': 'rohit', 'balance': 5000, 'Opening Date': '2023-07-01 19:25:38'}}
# this object will get balance from all cstomer's then store in dictionary format
bank_balance = {'balance':0}


# if check is True this while loop will looping until user overwrite with False 
check = True
while check:
    print('''\n               WELCOME TO PYTHON BANK MANAGEMENT SYSTEM
                            SELECT YOUR ROLE
                                1.) Banker
                                2.) Customer
                                
                                3.) Exit \n''')

# this loop ask for integer value between 1 to 3 after right input it'll jump to next code
    check01 = True
    while check01:
# here we use try and except block with while loop, due to while loop it'll run try block until user gives valid input
        try:   
            role = int(input("\nChoose Your Role : "))
            if role >= 1 and role <= 3 :
                if role == 1:
                    print("\nBanker's roll selected Successfully")
                elif role == 2:
                    print("\nCustomer's roll selected Successfully")
                check01 = False # if user gives valid input this while loop will stop
                check02 = True # it'll jump user to check02 while loop's code
            else:
                print("\nInvalid input. Please enter a number between 1 to 3.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

# after right input between 1 to 3 this loop will run until we overwrite with False
    check02 = True
    while check02:
            

        if role == 1:  # if role's value is one this code will run
            # print("\nBanker's roll selected Successfully")
            func.role() # this function will print baker's app menu

            role1 = True
            while role1: # we use this loop for get valid input for perform operation
                try:
                    Operation = int(input("\nEnter operation which you want to perform : "))
                    if Operation >= 1 and Operation <= 6 :
                        break
                    else:
                        print("\nInvalid input. Please enter a number between 1 to 6.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")

            if Operation == 1:
                customer_data.update(func.operation_1())  # it'll get data and update dictionary
                choice01 = True
                while choice01:  # we use this loop for getting multiple times data if user wants
                    choice1 = input("\nDo you want to perform more operation press 'y' for yes and press 'n' for no : ")
                    if choice1.lower() == 'y': 
                        customer_data.update(func.operation_1())
                            
                    elif choice1.lower() == 'n':
                        print("\nOperation 1 performed successfully")
                        choice1 = False # it'll stop this loop and go back to check02 while loop
                        break

                    else:
                        print("\nInvalid choice. Please enter 'y' or 'n'.")

            elif Operation == 2:
                print(customer_data)  # it'll will print customer data in dictionary form
                print("\nOperation 2 performed Successfully")
                # func.operation_2(customer_data)  # this function will print customer data in dictionary form

            elif Operation == 3:
                func.operation_3(customer_data)  # it'll search customer and if it's exist it'll show data of that customer
                
            
            elif Operation == 4:
                func.operation_4(customer_data)  # it'll show all customer with his details
                print("\nOperation 4 performed Successfully")
            
            elif Operation == 5:
                bank_balance.update(func.operation_5(customer_data))  # it'll update balance dictionary which data function returns
                print(f"\nTotal Amount in Bank is {bank_balance['balance']}")
                print("\nOperation 5 performed Successfully")

            elif Operation == 6: # if users choose 6 it'll stop check02 while loop and jump to check01 while loop
                print("\nOperation 6 performed Successfully")
                check02 = False
                check01 = True



# if user input 2 while choses a role this code will run
        elif role == 2:
            # print("\nCustomer's roll selected Successfully")
            func.customer_role() # this func will print custome's app

            role2 = True
            while role2:
                try:
                    Operation = int(input("\nEnter operation which you want to perform : "))
                    if Operation >= 1 and Operation <= 4 :
                        break
                    else:
                        print("\nInvalid input. Please enter a number between 1 to 4.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")

            if Operation == 1:
                customer_data.update(func.withdraw(customer_data))  # this func will withdraw amt of user then update it in customer_data
                bank_balance.update(func.operation_5(customer_data)) # it'll update bank_balance after withdraw

            elif Operation == 2:
                customer_data.update(func.deposite(customer_data)) # this func will deposite amt of user then update it in customer_data
                bank_balance.update(func.operation_5(customer_data)) # it'll update bank_balance after deposite

            elif Operation == 3:
                func.view_balance(customer_data)  # we use this func to show particular users bank balance

            elif Operation == 4:
                check02 = False # it'll stop this while loop
                check01 = True # it'll jump user to check01 again

        elif role == 3:
            print("\nProgramme Exited Successfully")
            print("\nVisit Again\n")
            sys.exit()  # it'll terminate the programme after this log data will be saved in log file


          
