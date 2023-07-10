import func, sys

customer_data = {101: {'name': 'rohit', 'balance': 5000, 'Opening Date': '2023-07-01 19:25:38'}}
bank_balance = {'balance':0}
temp_customer_data = {}

check = True
while check:
    print('''\n               WELCOME TO PYTHON BANK MANAGEMENT SYSTEM
                            SELECT YOUR ROLE
                                1.) Banker
                                2.) Customer
                                
                                3.) Exit \n''')


    check01 = True
    while check01:
        try:
            role = int(input("\nChoose Your Role : "))
            if role >= 1 and role <= 3 :
                check01 = False
                check02 = True
            else:
                print("\nInvalid input. Please enter a number between 1 to 3.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

    check02 = True
    while check02:
            

        if role == 1:
            func.role()

            role1 = True
            while role1:
                try:
                    Operation = int(input("\nEnter operation which you want to perform : "))
                    if Operation >= 1 and Operation <= 6 :
                        break
                    else:
                        print("\nInvalid input. Please enter a number between 1 to 6.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")

            if Operation == 1:
                customer_data.update(func.operation_1())
                choice01 = True
                while choice01:
                    choice1 = input("\nDo you want to perform more operation press 'y' for yes and press 'n' for no : ")
                    if choice1.lower() == 'y':
                        customer_data.update(func.operation_1())
                            
                    elif choice1.lower() == 'n':
                        choice1 = False
                        break

                    else:
                        print("\nInvalid choice. Please enter 'y' or 'n'.")

            elif Operation == 2:
                func.operation_2(customer_data)

            elif Operation == 3:
                func.operation_3(customer_data)
            
            elif Operation == 4:
                func.operation_4(customer_data)
            
            elif Operation == 5:
                bank_balance.update(func.operation_5(customer_data))
                print(f"Total Amount in Bank is {bank_balance['balance']}")

            elif Operation == 6:
                check02 = False
                check01 = True




        elif role == 2:
            func.customer_role()

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
                customer_data.update(func.withdraw(customer_data))
                bank_balance.update(func.operation_5(customer_data))

            elif Operation == 2:
                customer_data.update(func.deposite(customer_data))
                bank_balance.update(func.operation_5(customer_data))

            elif Operation == 3:
                func.view_balance(customer_data)

            elif Operation == 4:
                check02 = False

        elif role == 3:
            print("\nVisit Again\n")
            sys.exit()


          
