# Q. Write python program that user to enter only odd numbers, else will raise an exception. 

#-------------------- Method 1 -------------------------

try:
    n = int(input("Enter odd no. only : "))
    if n % 2 == 0:
        raise Exception("You entered an even no") # it will jump your code to except Exception block
    else:
        print(f"you entered odd no. {n}")
except ValueError: # always set all error before Exception b'coz exception can handle all errors so after exception remaining except block wouldn't execute
    print("please enter digits only")
except Exception as e: # you can print your message here also if u don't want give when u raise
    print(e)

#------------------------ Method 2 -----------------------------------

class EvenNumberException(Exception):
    pass

while True:
    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            raise EvenNumberException("EvenNumberException: Even number entered.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except EvenNumberException as e:
        print(str(e))

print(f"The entered odd number is: {number}")
