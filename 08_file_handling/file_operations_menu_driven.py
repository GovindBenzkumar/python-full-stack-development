import os

def create():
    file_name=input("Enter the file name: ")
    if os.path.exists(file_name):
        print("File already exists")
    else:
        open(file_name,"x")
        print("New File created")

def write():
    file_name=input("Enter the file name: ")
    if os.path.exists(file_name):
        print("File already exists")
    else:
        data= input("Enter the data to write: ")
        x= open(file_name,"w")
        x.write(data)
        print("File written")

def display():
    file_name=input("Enter the file name: ")
    if os.path.exists(file_name):
        x=open(file_name, "r")
        print("File content\n:-")
        print(x.read())
    else:
        print("File does not exist")

def delete():
    file_name=input("Enter the file name: ")
    if os.path.exists(file_name):
        os.remove(file_name)
        print("File got deleted")
    else:
        print("File does not exist")

while True:
    print("\t File Operations:-\n\n 1. Create file\n2. Write file\n3. Display file\n4. Delete file\n5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        create()
    elif choice==2:
        write()
    elif choice==3:
        display()
    elif choice==4:
        delete()
    elif choice==5:
        print("Program got Exited\nThank you for using this program")
        break
    else:
        print("Please enter a valid choice")









