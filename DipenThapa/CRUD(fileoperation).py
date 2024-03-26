# Homework:- 
# 1.take input from user so that which file user wants to create
# 2.insert content inside file by asking user
# 3.user needs to read file
# 4.New input add garna paryo
# 5.At last file must be deleted by asking user

def create(filename):
    try:
        file = open(filename, 'x')
        print("-------File Created Successfully-------")
        createfile = input("Enter content for the file: ")
        print('Contents added successfully.')
        file.write(createfile)
        
    except FileExistsError:
        print("File already exists.")
        
    except Exception as e:
        print("Enter valid filename.")

def read(filename):
    file = open(filename, 'r')
    readfile = file.readlines()
    print('Contents of the file: ', readfile)
        
def add(filename):
    file = open(filename, 'a')
    addcont = input("Add contents you like: ")
    file.write('\n' + addcont)
    print("Successfully added.")
        
def delete(filename):
    import os
    if os.path.exists(filename):
        os.remove(filename)
        print("Successfully deleted.")
    else:
        print("File not found!")
        
def main():
    filename = input("Enter filename you want to create: ")

    create(filename)
        
    while True:
        user = input("Do you want to add more contents inside the file? (yes/no): ").lower()
        if user == 'yes':
            add(filename)
        elif user == 'no':
            break
        else:
            print("Plz select either yes or no.")
            break
                
    while True:
        user = input("Do you want to look whats inside the file? (yes/no): ").lower()
        if user == 'yes':
            read(filename)
            break
        elif user == 'no':
            break
        else:
            print("Select either yes or no.")
            break
            
    while True:
        user = input("Do you want to delete the file? (yes/no): ").lower()
        
        if user == 'yes':
            delete(filename)
            break
        elif user == 'no':
            break
        else:
            print("Select either yes or no.")
            break
    
main()
        
            

