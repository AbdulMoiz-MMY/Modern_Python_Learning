marks = float(input("Enter the marks: "))

if(marks >= 90):
    print("grade = 'A'")
elif(marks >= 80 and marks <= 90):
    print("grade = 'B'")
elif(marks >=70 and marks <= 80):
    print("grade = 'C'")
elif(marks >= 60 and marks <= 70):
    print("grade = 'C'")
elif(marks >= 50 and marks <= 60):
    print("grade = 'D'")
elif(marks >= 40 and marks <= 50):
    print("grade = 'E'")
else:
    print("grade = 'F'")