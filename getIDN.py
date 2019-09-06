import visa
#import importlib
import basicIn as b
import time as t
rm = visa.ResourceManager()
print("Connected instruments")
print(rm.list_resources())
inst = rm.open_resource(rm.list_resources()[0])
print(inst.query("*IDN?"))
print(inst.write("C1: BSWV FRQ, 123"))
run = True
while(run):
    start = b.getNum("Enter start frequency: ")
    step = b.getNum("Enter step size: ")
    num = b.getNum("Enter # of steps: ")
    if  start and step and num:
        if start > 0:
            cycles = 10
            for cyc in range(num):
                freq = start + step * cyc
                print("Setting frequency: "+ str(freq))
                inst.write("C1: BSWV FRQ, "+str(freq))
                t.sleep(0.3)
    else:
        print("Invalid num")
        run = False

