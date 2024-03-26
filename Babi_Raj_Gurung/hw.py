def task_menu():
    print("1. create file")
    print("2. add data to file")
    print("3. read file data")
    print("4. append data to file")
    print("5. delete file")
    print("6. exit")
    
def create_file(a):
    try:
        f=open(a,"x")
        print('file created successfully')
        f.close()
    except Exception as e:
        print(e)
  
def write_file(a,b):
    try:
        f=open(a,"w")
        f.write(b)
        print('file written successfully')
        f.close()
    except Exception as e:
        print(e)


def read_file(a): 
    try:
        f=open(a)
        print(f.readlines())
    except Exception as e:
        print(e)
    
def append_file(a,b):   
    try:
        f=open(a,"a")
        f.write(b)
        print('data appended successfully')
        f.close()
    except Exception as e:
        print(e)
    

def del_file(a):           
    try:
        import os
        os.remove(a)
        print('file deleted successfully')
    except Exception as e:
        print(e)

def main():
    while True:
        task_menu()
        choice = input('enter a choice:')
        if choice == '1':
            a = input('enter a filename to create(must be txt):')
            create_file(a)
        elif choice == '2':
            a = input('enter a filename to write to:')
            b = input('enter data to be written:')
            write_file(a,b)
        elif choice == '3':
            a = input('enter a filename to read:')
            read_file(a)
        elif choice == '4':
            a = input('enter a filename to append to:')
            b = input('enter data to be appended:')
            append_file(a,b)
        elif choice == '5':
            a = input('enter filename to delete:')
            del_file(a)
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
               
main()