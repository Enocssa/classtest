# This first line is provided for you
hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
r = float(rte)
def computepay(h,r):
    if h >40 :
        ot = h - 40
        norm = h - ot
        otf = float(ot)
        normf = float(norm)
        Pay = (normf*r) + (otf*(r*1.5))
        return (Pay)
    else :
        Pay = (h*r)
        return (Pay)
print(computepay(h,r))
