# WAP to find the sum of first natural number.

# n_num = int(input("enter number: "))


# sum = 0
# for i in range(1,n_num+1):
#     sum += i
# print("total sum = ",sum )


n_num = int(input("enter number: "))
sum = 0
ele = 1
while ele <= n_num:
    sum += ele
    ele +=1
print("total sum = ",sum )