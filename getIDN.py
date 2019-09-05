import visa
rm = visa.ResourceManager()
print("Connected instruments")
print(rm.list_resources())
inst = rm.open_resource(rm.list_resources()[0])
print(inst.query("*IDN?"))
print(inst.write("C1: BSWV FRQ, 100"))
