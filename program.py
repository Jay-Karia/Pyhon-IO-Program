import os
print("Welcome to Python IO Program Developed -- By Jay")
sel = input("\n1) Custom Directory\n2) Default Directory\n")

# Methods
def list(directory):
    li = os.listdir(directory)
    print("\nItems:\n")
    for items in li:
        print(items)

def read(directory):
    pass

if sel == "1":
    print("\nSelected 1) Custom Directory\n")
    str = "Enter you Directory: "
    dir = input(str)
    cDir = dir+"\\"
    print(f"Directory is set to: " + cDir)
    
    opt = input("\nEnter what do you want do:\n1) List the items in the Directory\n2) Read a file\n3) Write into a file\n4) Append to a file\n5) Create a new file\n6) Delete a File\n")

    if opt == "1":
        list(cDir)