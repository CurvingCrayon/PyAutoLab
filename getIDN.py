import visa
#import importlib
import basicIn as b
rm = visa.ResourceManager()
print("Connected instruments")
print(rm.list_resources())
#inst = rm.open_resource(rm.list_resources()[0])
#print(inst.query("*IDN?"))
#print(inst.write("C1: BSWV FRQ, 100"))
run = True
while(run):
    start = b.getNum("Enter start frequency: ")
    step = b.getNum("Enter step size: ")
    num = b.getNum("Enter # of steps: ")
    if  start and step and num:
        if start > 0:
            cycles = 10
            for cyc in range(10):
                freq = start + step * num
                print("Setting frequency: "+ str(freq))
                #inst.write("C1: BSWV FRQ, "+str(freq))
    else:
        print("Invalid num")
        run = False

