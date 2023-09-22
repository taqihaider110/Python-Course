fileref = open("olympics.txt", "r")
## other code here that refers to variable fileref
f=fileref.read()
# for i in fileref:
    # print(i.strip())
print(len(f))
fileref.close()
