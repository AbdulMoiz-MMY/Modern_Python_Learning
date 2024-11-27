age = int(input("Enter the age: "))
if(age>=18):
    print("Apply the license")
else:
    print("You not eligible")

light_color =  str(input("Enter the color of traffic signal light: "))
Tra_signal =light_color.upper()

if(Tra_signal == "RED"):
    print("Please stop and Wait the Green light.")
elif(Tra_signal == "YELLOW

"):
    print("Ready to cross the signal.")
elif(Tra_signal == "GREEN"):
    print("Cross the signal.")
elif(Tra_signal == "BLINK"):
    print("Carefully crossing the Road")
