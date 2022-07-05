import sys

filename = "../name.txt"

while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r')
    except:
        print("Inside EXCEPT")
        print("Error found!")
        print(sys.exc_info()[1])
        filename = input("Enter Correct file name:")
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()
