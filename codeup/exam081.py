a = int(input(), 16)
b = 16

for i in range(1, b):
    print("%X" %a, "*%X" %i, "=%X" %(a * i), sep="")