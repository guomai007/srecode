def calc():
    try:
            x=input('enter first num:')
            y=input('enter second num:')
            return x/y
    except Exception,e:
            print e


calc()
