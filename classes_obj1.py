class laptop:
    processor = ""
    price = ""
    ram = ""


hp = laptop()
lenovo = laptop()
dell = laptop()

hp.processor = "i5"
lenovo.processor = "i6"
dell.processor = "i9"

hp.price = "40k"
lenovo.price = "50k"
dell.price = "80k"

hp.ram = "12gb"
lenovo.ram = "16gb"
dell.ram = "32gb"

print("hp:", hp.processor, hp.price, hp.ram)
print("lenovo:", lenovo.processor, lenovo.price, lenovo.ram)
print("dell:", dell.processor, dell.price, dell.ram)
