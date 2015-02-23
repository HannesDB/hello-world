def name():
    ur_name = raw_input("What's your name? ")
    if len(ur_name) <= 5:
        print ur_name + ", your name is short and sweet!"
    else:
        print ur_name + ", your name is long and difficult!"

name()
