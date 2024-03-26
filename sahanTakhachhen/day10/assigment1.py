import os
# Ask the user for the name of the file
filename = input("Please enter the name of the file you want to create: ")

# Open the file in write mode
file=open(filename, 'w')
print("Now you can start writing to the file. When you're done, type 'STOP'.")
    
    # Loop to get user input
while True:
        line = input()
        
        # If the user types 'STOP', stop asking for input
        if line.strip() == 'STOP':
            break
        
        # Write the user's input to the file
        file.write(line + '\n')

print("You've finished writing. Now I'll read the file.")

# Open the file in read mode and print its contents
file=open(filename, 'r')
print(file.read())
file.close()
os.remove("sahan.txt")
