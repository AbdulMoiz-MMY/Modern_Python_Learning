# WAP to check if a number entered by the user is odd or even.

user = int(input("Enter any number: "))

num = user%2
if(num == 0):
    print("This number is even")
elif(num != 0):
    print("This number is odd")
else:
    print("Please enter the correct number.")