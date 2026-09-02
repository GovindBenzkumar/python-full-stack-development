x= int(input("Enter the mark scored by the student:\t"))
if x>100 or x<0:
    print("INVALID DATA!")
elif x<=100 and x>=80:
    print("Grade: A+")
elif x<80 and x>=60:
    print("Grade: B+")
elif x<60 and x>=40:
    print("Grade: C+")
elif x<40 and x>=20:
    print("Grade: D+")
else:
    print("Grade: F")
    
