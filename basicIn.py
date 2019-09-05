def getNum(str):
    num = input(str)
    if num.isdigit(): # '''or isinstance(num,float)'''
        return int(num)
    else:
        return False