# Print the multiplication table of following list using a loop.

table = int(input("Enter the number and print table: "))
num = 1 
while num <= 10:
    print(table,"*",num,"=",table*num)
    num += 1
    