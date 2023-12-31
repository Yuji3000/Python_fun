# exercise 03 - 01/02 
# https://www.youtube.com/watch?v=crLerB4ZxMI

# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours
# worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# hours = input("Enter Hours: ")
# rate = input("Enter Rate: ")

# rate_float = float(rate)
# hour_float = float(hours)

# if hour_float > 40 :
#     print("Overtime")
#     over_time_pay = (hour_float - 40.0) * (rate_float * 1.5)
#     regular_pay = 40.0 * rate_float
#     # print(regular_pay, over_time_pay)
#     pay = regular_pay + over_time_pay
# else:
#     print("regular")
#     pay = hour_float * rate_float
# print("Pay:",pay)

# EXERCISE 02 - Do the same as above but with TRY / EXCEPT
# input can be a string this time

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    rate_float = float(rate)
    hour_float = float(hours)
except:
    print("Error, please enter numeric input")
    quit()
    # must put quit() so the code stops running
    
if hour_float > 40 :
    print("Overtime")
    over_time_pay = (hour_float - 40.0) * (rate_float * 1.5)
    regular_pay = 40.0 * rate_float
    # print(regular_pay, over_time_pay)
    pay = regular_pay + over_time_pay
else:
    print("regular")
    pay = hour_float * rate_float
print("Pay:",pay)