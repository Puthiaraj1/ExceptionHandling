import sys


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid Number entered, please try again")
            print("Invalid Number entered, please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally block always execute")


first_number = get_int("Please enter first number:")
second_number = get_int("Please enter second number:")
try:
    print("{} divied by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("Number cann't be divied by 0")
    sys.exit(2)
finally:
    print("Division performed successfully")
