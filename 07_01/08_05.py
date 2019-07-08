#You will parse the From line using split()
#and print out the second word in the line
#(i.e. the entire address of the person who sent the message).
#Then print out a count at the end.

fname = input("Enter file name: ")

fh = open(fname)
count =0
for  line in fh:
    line =line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    count = count + 1
    print(words[1])


print("There were", count, "lines in the file with From as the first word")
