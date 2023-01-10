class Error(Exception):
    pass
class Rangesmall(Error):
    pass
class Rangelarge(Error):
    pass
while(True):
    n = int(input("enter a value 10-50 : "))
    try:
        if n<10:
            raise Rangesmall
        elif n>50:
            raise Rangelarge
        break
    except Rangesmall:
        print(" invalid value ")
    except Rangelarge:
        print('invalid value')
print("task completed")