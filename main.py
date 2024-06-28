# File Copyright License adder
# Application by E-Coders Team

# Imports
import os, time

# Other things

# Code
print("File copyright license adder.")
time.sleep(3)

# Directory Changer
dirChange = input("Change directory (/Users/(username)/(folder)): ")
print("Changing directory...")
time.sleep(8)
try:
    print("Succesfully changed directory!")
    os.chdir(dirChange)
except Exception:
    print("Couldn't change directories. Please check the directory name or an error might have occured.")

# license adder
fileName_input = input("Enter file name (No whitespaces and must be empty before typing): ")
try:
    fileName = open(fileName_input, "w")
    print("Adding copyright license...")
    time.sleep(3)
    print(fileName.write("© 2024 (Name here)"))
    print("Added license!")
except FileNotFoundError:
    print("File not found!")