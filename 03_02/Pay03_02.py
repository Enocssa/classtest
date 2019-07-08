# This first line is provided for you
hrs = input("Enter Hours:")
rte = input("Enter Rate")
h = float(hrs)
rate = float(rte)
if h >40 :
    ot = h - 40
    norm = h - ot
    otf = float(ot)
    normf = float(norm)
    Pay = (normf*rate) + (otf*(rate*1.5))
    print (Pay)
else :
    Pay = (h*rate)
    print (Pay)
