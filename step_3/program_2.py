#  WAP check if a list contains a palindrome of elements.(Hint: use copy()method)
# [1,2,3,2,1]                    [1,"abc","abc",1]

pal = []
print("To check the list is palindrome yes or not .")
word = input("Enter any 1st word or number: ")
pal.append(word)
word = input("Enter any 2nd word or number: ")
pal.append(word)
word = input("Enter any 3rd word or number: ")
pal.append(word)

copy_list = pal.copy()
copy_list.reverse()

if (copy_list == pal):
    print("This is palindrome list.")
else:
    print("This is non palindrome list.")
