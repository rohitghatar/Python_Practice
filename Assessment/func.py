import datetime

log = open('logfile.txt', 'a')

def role():
        print('''\nWelcome to Banker's App
                                Operation Menu

                                1.) Add Customer
                                2.) View Customer
                                3.) Search Customer   
                                4.) View All Customer
                                5.) Total Amounts in Bank
                                6.) Back\n''')
        

def customer_role():
    print('''\nWelcome to Customer's App
                                Operation Menu

                                1.) Withdraw Amount
                                2.) Deposite Amount
                                3.) View Balance
                                4.) Back
                                ''')
        
       
# def role1(role):
#     customer_data2= {}
#     if role == 1:
#         # print('''Welcome to Banker's App
#         #                         Operation Menu

#         #                         1.) Add Customer
#         #                         2.) View Customer
#         #                         3.) Search Customer   
#         #                         4.) View All Customer
#         #                         5.) Total Amounts in Bank''')
    
#         # role1 = True
#         # while role1:
#         #     try:
#         #         Operation = int(input("Enter operation which you want to perform : "))
#         #         if Operation >= 1 and Operation <= 5 :
#         #             customer_data2.update(operation_1())
#         #             break
#         #         else:
#         #             print("Invalid input. Please enter a number between 1 to 5.")
#         #     except ValueError:
#         #         print("Invalid input. Please enter a valid number.")

#         #     role1=False

#         choice01 = True
#         while choice01:
#             choice1 = input("Do you want to perform more operation press 'y' for yes and press 'n' for no : ")
#             if choice1.lower() == 'y':
#                 customer_data2.update(operation_1())
                
#             elif choice1.lower() == 'n':
#                 choice1 = False
#                 break

#             else:
#                 print("Invalid choice. Please enter 'y' or 'n'.")
#             return customer_data2 


def operation_1():
    customer_data = {}
    temp_customer_data = {}
    ct_name = ['name']
    ct_balance = ['balance']
    ct_log = ['Opening Date']

    while True:
        try:
            account_no = int(input("\nEnter account No. : "))
            break

        except ValueError:
            print("\nInvalid input. Please enter a valid account number.")

    customer_name = input("\nEnter customer name : ")
    temp_customer_data[ct_name[0]] = customer_name

    while True:
        try:
            opening_balance = int(input("\nEnter opening balance. : "))
            temp_customer_data[ct_balance[0]] = opening_balance
            temp_customer_data[ct_log[0]] = log_data()
            customer_data[account_no] = temp_customer_data.copy()
            Data = log_data()
            log.write(f"customer name {customer_name}'s account opened with account no {account_no} and his opening balance is : {opening_balance} his account created at {Data}")
            temp_customer_data.clear()
            break

        except ValueError:
            print("\nInvalid input. Please enter a valid account number.")
    return customer_data
    

def operation_2(data):
    print(data)


def operation_3(data1) :
    while True:
        try:
            ac_no = int(input("\nEnter Customer's account no. : "))
            name = input("\nEnter Account Holder's Name : ")
            values = data1[ac_no]
            if ac_no in data1:
                if name in values.values():
                    print(f"\naccount no of {ac_no} \ncustomer's name is {values['name']} \nhis bank balance is : {values['balance']} \nhis Opening Date is {values['Opening Date']}")
                    break
                else:
                    print("\nEnter correct name")
                

            else:
                print("\nEnter valid account no and name.")
        except:
            print("\nEnter valid account no. ")


def operation_4(data2):
    ct_no = 1
    for i in data2:
        print("---------------------------------------------------------------------------------------------------")
        print(f"\ndetails of {ct_no} customer \n")
        print(f"customer's account no. is : {i}")
        ct_no += 1
        for j in data2[i].items():
            ct_str = tuple(str(i) for i in j)
            print(f'''customer's {" is ".join(ct_str)}''')
        print("---------------------------------------------------------------------------------------------------\n")
            

def operation_5(data3):
    bank_balance = {'balance':0}
    for b in data3.values():
        balance = b['balance']
        bank_balance['balance'] += balance
    
    return bank_balance


def withdraw(data4):
        customer_data = data4
        while True:
            try:
                ac_no = int(input("\nEnter Customer's account no. : "))
                if ac_no in data4:
                    amount = int(input("\nEnter withdraw amount : "))
                    customer_data[ac_no]['balance'] -= amount
                    Data = log_data()
                    log.write(f"\n {amount} withdraw by name : {customer_data[ac_no]['name']}, account no. {ac_no} at {Data}\n")
                    break

                else:
                    print("\nEnter valid account no.")
            except:
                print("\nEnter valid account no. ")
        return customer_data


def deposite(data4):
        customer_data = data4
        while True:
            try:
                ac_no = int(input("\nEnter Customer's account no. : "))
                if ac_no in customer_data:
                    amount = int(input("\nEnter deposite amount : "))
                    customer_data[ac_no]['balance'] += amount
                    Data = log_data()
                    log.write(f"\n {amount} deposite by name : {customer_data[ac_no]['name']}, account no. {ac_no} at {Data}\n")
                    break

                else:
                    print("\nEnter valid account no.")
            except:
                print("\nEnter valid account no. ")
        return customer_data


def view_balance(data5):
        customer_data = data5
        while True:
            try:
                ac_no = int(input("\nEnter Customer's account no. : "))
                if ac_no in customer_data:
                    balance =  customer_data[ac_no]
                    print(f"\nbalance of {balance['name']}'s is {balance['balance']}")
                    break

                else:
                    print("\nEnter valid account no.")
            except:
                print("\nEnter valid account no. ")   
            

def log_data():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime
