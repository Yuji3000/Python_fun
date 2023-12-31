# Conditonal statements

# If statement can use:
# and, or, not


def if_example():
    if power_pellet_active is True and touching_ghost is True:
      return True
  # don't have to put else here
    return False

  # or can do
def return_bool():
    return bool(power_pellet_active and touching_ghost)


# if, else, elsif

def elif_example():
    if x < 2 :
        print('small')
    elif x < 10:
        print('big')
    else 
        print("something else")


# try / except structure
# it "tries" the code and if it blows up, it does something else
def try_except_example():
    temp = "5 degrees"
    cel = 0
    try:
        fahr = float(temp)
        cel = (fahr - 32.0) * 5.0 / 9.0
    except:
        cel = 100
    print(cel)