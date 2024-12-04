# Search for a number x in this tuple using loop.
# [1,2,9,16,25,36,49,64,81,100]


print("([1,2,9,16,25,36,49,64,81,100]")
x = int(input("Search the index from given list: "))
num_list = (1,2,9,16,25,36,49,64,81,100)
idx = 0
while idx <= len(num_list)-1:
    if(num_list[idx] == x):
        print("FOUND at index: ",idx)
        break
    else:
        print("Finding--")
    idx += 1