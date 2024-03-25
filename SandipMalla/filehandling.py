
while True:
    try:
        file = input("enter the file name you want to access: ")
        mode = input("enter 'r' if you want read mode , 'w' for write mode, 'a' for append mode 'x' for crete mode and 'd' for delete mode  :")
        f = open(file,f"{mode}" )
        if mode=='a':
            text = input("Enter the text you want to append: ")
            f.write('\n' + text+'\n')
            print("Text appended successfully!")        
            f.close()
        elif mode=='x':
            # text = input("Enter the fileName you want to crete: ")
            print("file created successfully!")        
            f.close()
        elif mode=='w':
            text = input("Enter the text you want to write(override): ")
            f.write('\n' + text+'\n')
            print("Text overriden successfully!")
            f.close()
        elif mode=='r':
            print(f.read())
            f.close()
        elif mode=='d':
            import os
            os.remove(f"{file}")
            print("File deleted successfully.")
        else:
            print("Choose the correct mode. ")
    
    except FileNotFoundError as e:
        print(f"File {file} not found.")
    