def cal_minutes(days):
    if days > 0:
        print(days)  # Access of Global variable
        return f'Number of minutes in {days} days are {days * 24 * 60}'  # Need to put return explicitly
    elif days == 0:
        return "It's a zero as input"
    else:
        return "Input is a -ve number"


def validate_and_execute(num_of_days):
    # num_of_days will be string. we need to cast it to int by calling function named int
    try:
        number_of_day_number = int(num_of_days)
        print(cal_minutes(number_of_day_number))

    except ValueError:
        print(f'Wrong Input: {num_of_days} is not a number')


# num_of_days = 20  # Python is dynamically typed...  Don't put Integer in front of variable
num_of_days_ip = ''
while num_of_days_ip != 'exit':
    num_of_days_ip = input("Enter nu of days or [exit]: ")
    validate_and_execute(num_of_days_ip)

# Scope in python
# Global -- defined outside any function
# Local -- defined inside any function
