# f=open('hello.txt','w')
# # print(f.readline()) 
# # for x in f:
# #    print(f.readline(4))
# f.write('k xa keta ho') 

def create_file():
   
    filename = input("Enter the filename: ")
    content = input("Enter the content: ")
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("File '{filename}' created successfully with the provided content.")
    except Exception as e:
        print("Error occurred: {e}")

if __name__ == "__main__":
    create_file()
