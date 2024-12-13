#Christopher Robles Serrano
#Module 11 Lab 1
#12/11/2024
#This program reads/validates user inputs and writes to a file. It reads student grades as a float and writes to a .txt file.



def validNum():
    #Boolean loop until inputs are a valid float.
    while True:
        myNum = input("What is the students grade?: ")
        
        try:
            myNum = float(myNum)
            return myNum
        except ValueError:
            print("Value must be a valid numerical value!")

def myContinue():
    #Boolean loop until inputs are 'y' or 'n'. Used to check if the user wants to continue.
    while True:
        myChoice = input("Would you like to continue? (y or n): ").lower()
        if myChoice in ['y', 'n']:
            return myChoice
        
        else:
            print("Not a valid choice!")


#Opening grades.txt and writing to the file using .write()
with open('grades.txt', 'w') as myFile:
    SENTINEL = 'y'
    while SENTINEL != 'n':
        myFile.write(f'{validNum()}\n')
        SENTINEL = myContinue()