
# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    """Display a greeting"""
    print("hello_" + user_name.upper() + "!")

hello_name("username")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds(values):
    """Display only odd numbers below 100"""
    for value in values:
        if value % 2 != 0:
            print(value)

first_odds(range(1,100))

# Question 3
# Please write a python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """Returns the maximum value within a list"""
    return max(a_list)
    

practice_list = [1, 100, 1000, 100000, 5, 10]
print(max_num_in_list(practice_list))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisble by 4,
# but not divisble by 100, unless it is also divisible by 400. The return should be boolean type (True/False)

def is_leap_year(a_year):
    """Proves if a given year is a leap year"""
    if (a_year % 4 == 0) or (a_year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2020))
print(is_leap_year(2021))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. The return should be boolean type.

def is_consecutive(a_list):
    """Checks to see if a list is in consecutive order"""
    for n in a_list:
        if a_list[n] + 1 == a_list[n+1]:
            return True
        else:
            return False

sample_list_1 = [2,3,4,5,6,7]
sample_list_2 = [1,2,4,5]

print(is_consecutive(sample_list_1))
print(is_consecutive(sample_list_2))

