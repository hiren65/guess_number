def squred(arg):
    if arg.isdigit()==True:
        num = int(arg)
        return num**2
    else:
        return arg*len(arg)

def squred1(arg):
    try:
        num = int(arg)**2
        return num
    except:
        return arg*len(arg)


tt = input("> ")

print(squred(tt))

print(squred1(tt))




