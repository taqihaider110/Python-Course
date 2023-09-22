fileref = open("olympics.txt", "r")
## other code here that refers to variable fileref
for i in fileref:
    print(i.strip())
fileref.close()
