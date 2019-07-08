score = input("Enter Score: ")
try:
    sc=float(score)
except:
    print("Error not a number")
    quit()

if sc >1 :
        print("Please input a number between 1.0 and 0.0")
        quit()

elif sc < 0.6 :
    print("F")
elif sc >= 0.9 :
    print ("A")
elif sc >= 0.8 :
    print("B")
elif sc >= 0.7 :
    print("C")
elif sc >= 0.6 :
    print("D")
