# Question no.1
# WAF to print the length of a list. ( list is the parameter)

list_country = ["Pakistan","USA",'Japan',"Saudi","Dubai"]

def len_list(list):
    print(len(list))
    return len_list
len_list(list_country)

# Question no.2
# WAF to print the elements of a list in a single line. ( list is the parameter).

def element(list):
    i = 1
    for i in list:
        print(i)
        
element(list_country)


# WAF to find the factorial of n. (n is the parameter)

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
        print(fact)
factorial(5)        
