# WAP to find the factorial of first natural number.

num_1 =  int(input("Enter the number: "))

fact = 1
for i in range(1,num_1+1):
    fact *= i
print("Total factorial: ",fact )

num_2 =  int(input("Enter the number: "))
fact_2 = 1

count = 1
while (count <= num_2):
    fact_2 *= count
    count += 1
print("Total factorial", fact_2)