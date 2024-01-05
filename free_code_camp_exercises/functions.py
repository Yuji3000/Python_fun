
def computepay(hours, rate) :
    # hours = input("Enter Hours: ")
    # rate = input("Enter Rate: ")
    rate_float = float(rate)
    hour_float = float(hours)
        
    if hour_float > 40 :
        over_time_pay = (hour_float - 40.0) * (rate_float * 1.5)
        regular_pay = 40.0 * rate_float
        # print(regular_pay, over_time_pay)
        pay = regular_pay + over_time_pay
    else:
        pay = hour_float * rate_float
    return pay

x = computepay(50,10)

print("Pay is now",x)