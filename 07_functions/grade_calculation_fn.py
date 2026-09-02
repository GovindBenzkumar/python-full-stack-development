def grade_calculation():
    mark=int(input("Enter the total mark out of 100:\n"))
    if mark<=100 and mark>=80:
        print("Grade: A+")
    elif mark<=80 and mark>=60:
        print("Grade: B+")
    elif mark<=60 and mark>=40:
        print("Grade: C+")
    elif mark<=40 and mark>=20:
        print("Grade: D+")
    else:
        print("Grade: F")
        return(mark)

grade_calculation()
        
