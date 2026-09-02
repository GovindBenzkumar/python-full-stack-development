try:
    x= int(input("Enter a number"))
    y= int(input("Enter another number"))
    z= x/y
    print(z)
    print(k)

except ZeroDivisionError:
    print("Division by zero is not possible")

except NameError:
    print("Name Error")

except Exception as e:
    print(e)

else:
    print("Thank you")


