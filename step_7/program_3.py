#  WAP To find the factorial of n.(n is the parameter)

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
        print(fact)

num_1 = 8

factorial(5)
