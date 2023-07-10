# we import inbuilt module datetime for get real-time log data of transaction
import datetime

# it'll create log file where we can save log data
log = open('logfile.txt', 'a')

# we create this func for show banker's app
def role():
        print('''\nWelcome to Banker's App
                                Operation Menu

                                1.) Add Customer
                                2.) View Customer
                                3.) Search Customer   
                                4.) View All Customer
                                5.) Total Amounts in Bank
                                6.) Back\n''')
        


# we create this func for show customer's app
def customer_role():
    print('''\nWelcome to Customer's App
                                Operation Menu

                                1.) Withdraw Amount
                                2.) Deposite Amount
                                3.) View Balance
                                4.) Back
                                ''')
        

# we create this func for add customer
def operation_1():
    customer_data = {}
    temp_customer_data = {}

    while True:
        try:
            account_no = int(input("\nEnter account No. : "))
            break

        except ValueError:
            print("\nInvalid input. Please enter a valid account number.")

    customer_name = input("\nEnter customer name : ")
    temp_customer_data['name'] = customer_name

    while True:
        try:
            opening_balance = int(input("\nEnter opening balance. : "))
            temp_customer_data['balance'] = opening_balance
            temp_customer_data['Opening Date'] = log_data()
            customer_data[account_no] = temp_customer_data.copy()
            Data = log_data()
            log.write(f"\ncustomer name {customer_name}'s account opened with account no {account_no} and his opening balance is : {opening_balance} his account created at {Data}")
            print("\nCustomer added Successfully")
            temp_customer_data.clear()
            break

        except ValueError:
            print("\nInvalid input. Please enter a valid account number.")
    return customer_data
    

# this function will get customer data then print it
def operation_2(data):
    print(data)
    print("\nOperation 2 performed Successfully")


# this function will search customer from customer_data then print it's details
def operation_3(data1) :
    # while True:
    try:
        ac_no = int(input("\nEnter Customer's account no. : "))
        name = input("\nEnter Account Holder's Name : ")
        values = data1[ac_no]
        if ac_no in data1:
            if name in values.values():
                print(f"\naccount no of {ac_no} \ncustomer's name is {values['name']} \nhis bank balance is : {values['balance']} \nhis Opening Date is {values['Opening Date']}")
                print("\nOperation 3 performed Successfully")
                # break
            else:
                print("\nEnter correct name")
            
        else:
            print("\nEnter valid account no and name.")
    except:
        print("\nEnter valid account no. ")


# this function will print all customers data 1 by 1
def operation_4(data2):
    ct_no = 1
    for i in data2:
        print("---------------------------------------------------------------------------------------------------")
        print(f"\ndetails of {ct_no} customer \n")
        print(f"\ncustomer's account no. is : {i}")
        ct_no += 1
        for j in data2[i].items():
            ct_str = tuple(str(i) for i in j)
            print(f'''\ncustomer's {" is ".join(ct_str)}''')
        print("---------------------------------------------------------------------------------------------------\n")
            

# it'll update bank_balance 
def operation_5(data3):
    bank_balance = {'balance':0}
    for b in data3.values():
        balance = b['balance']
        bank_balance['balance'] += balance
    
    return bank_balance


# it'll withdraw amount from customer's account
def withdraw(data4):
        customer_data = data4
        # while True:
        try:
            ac_no = int(input("\nEnter Customer's account no. : "))
            if ac_no in data4:
                balance = customer_data[ac_no]['balance']
                if balance > 5000:
                    amount = int(input("\nEnter withdraw amount : "))
                    if balance-amount >= 5000:
                        customer_data[ac_no]['balance'] -= amount
                        print("Amount withdrawal successfully")
                        Data = log_data()
                        log.write(f"\n {amount} withdraw by name : {customer_data[ac_no]['name']}, account no. {ac_no} at {Data}\n")
                    else:
                        print(f"you have to maintain minimum 5000 balance in your a/c \nyour a/c balance is {balance} \nyou can withdraw {balance-5000} rupees")
                    # break
                else:
                    print(f"insufficient balance \nyou have to maintain minimum 5000 balance in your a/c \nyour a/c balance is {balance}")
                    # break
            else:
                print("\nEnter valid account no.")
        except:
            print("\nEnter valid account no. ")
        return customer_data


# it'll deposit amount in customer's account
def deposite(data4):
        customer_data = data4
        # while True:
        try:
            ac_no = int(input("\nEnter Customer's account no. : "))
            if ac_no in customer_data:
                amount = int(input("\nEnter deposite amount : "))
                customer_data[ac_no]['balance'] += amount
                print("Amount deposited successfully")
                Data = log_data()
                log.write(f"\n {amount} deposite by name : {customer_data[ac_no]['name']}, account no. {ac_no} at {Data}\n")
                # break
            else:
                print("\nEnter valid account no.")
        except:
            print("\nEnter valid account no. ")
        return customer_data


# it'll desired customer's bank balance
def view_balance(data5):
        customer_data = data5
        # while True:
        try:
            ac_no = int(input("\nEnter Customer's account no. : "))
            if ac_no in customer_data:
                balance =  customer_data[ac_no]
                print(f"\nbalance of {balance['name']}'s is {balance['balance']}")
                print("view balance operation performed successfully")
                # break
            else:
                print("\nEnter valid account no.")
        except:
            print("\nEnter valid account no. ")   
            

# it'll create log time to get exact time 
def log_data():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime
