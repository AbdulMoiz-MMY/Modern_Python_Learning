# WAP to Find the greatest of 3 number entered by the user.

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

if(num_1 > num_2 and num_1 > num_3):
    print(num_1,": The number is greatest.")
elif(num_2 > num_1 and num_2 > num_3):
    print(num_2,": The number is greatest.")
elif(num_3 > num_2 and num_3 > num_1):
    print(num_3,": The number is greatest.")
else:
    print("Please enter the correct number.")