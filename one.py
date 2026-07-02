
# Create a menu using while loop for converting Decimal to Binary, Octal, Hexa

ch=1

while ch!=0:
    print("\nMenu : Number Conversion ")
    ch = int(input("1. Decimal to Binary\n2. Decimal to Octal\n3. Decimal to Hexadecimal\n0. Exit\n\nEnter Your Choice: "))

    if ch==1:
        num = int(input("Enter Decimal Number: "))
        print("Binary =", bin(num))

    elif ch==2:
        num = int(input("Enter Decimal Number: "))
        print("Octal =", oct(num))

    elif ch==3:
        num = int(input("Enter Decimal Number: "))
        print("Hexadecimal =", hex(num).upper())

    elif ch==0:
        print("\nExit!!!...")

    else:
        print("\nPlease Enter Valid Choice!")
Menu : Number Conversion 
Binary = 0b1010

Menu : Number Conversion 
Exit... Thank You!

# An Electricity Bill Program is a program that calculates 
# the total electricity charge based on the number 
# of units consumed and the predefined rate or slab.

# Electricity Bill Calculator

units = int(input("Enter Consumed Units: "))

if units<=100:
    bill=units*1.50

elif units<=200:
    bill=(100*1.50)+((units-100)*2.50)

elif units<= 300:
    bill=(100*1.50)+(100*2.50)+((units-200)*4.00)

else:
    bill=(100*1.50)+(100*2.50)+(100*4.00)+((units-300)*6.00)

print("\n----- Electricity Bill -----")
print("Total Units Consumed : ", units)
print("Total Bill Amount    : ", bill)
----- Electricity Bill -----
Total Units Consumed :  299
Total Bill Amount    :  796.0
 
