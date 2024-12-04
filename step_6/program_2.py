# Search for a number x in this tuple using loop.
#  [1,4,9,16,25,36,49,64,81,100]

print("[1,4,9,16,25,36,49,64,81,100]")
x = int(input("enter the each number: "))
tup =(1,4,9,16,25,36,49,64,81,100) 
idx = 0
for found in tup:
    if(found == x):
        print("Fond at index: ",idx )
    idx += 1
