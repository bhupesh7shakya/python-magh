import os
def fileHandlingFunc():
   choice = int(input("select which operation you want to perform: \n 1. create file     2.write text into file   \n 3.Append data    4.delete file   \n 5.Read "))

   match choice:
      case 1:
         create_file()
         
        
      case 2:
         writeText()

      case 3:
         Append()
        
      case 4:
         delete()
      
      case 5:
         Read()



def create_file():
   filename = input("enter file name with extension: ")
   if(os.path.exists(filename)):
      print("\n")
      print("*"*10)
      print("file already exists!!!!!")
      print("*"*10)

      print("\n")
      fileHandlingFunc()  # calling the main function
   else:
      print(filename)
      f= open(filename,"x") 
      print("*"*10)

      print(f"file has been successfully created!!!! your file name is :  {f.name}") 
      print("*"*10)
      fileHandlingFunc()


def writeText():
   filename = input("enter the filename where you want to write text : ")
   try:
      f= open(filename,"w")
      content = input("enter the content text : ")
      f.write(content)
      f.close()
      print(f"content is added into your file : {content}")
      fileHandlingFunc()
   except Exception as e:
      print(f"error while writing text to file {e}")
      fileHandlingFunc()

    
def Append():
   filename  = input("enter the filename where you want to append data: ")
   try:
      f= open(filename, "a")
      content = input("enter the text to append into the file  : ")
      f.write(content)
      f.close()
      print("content successfully append to the file...")
      fileHandlingFunc()
   except Exception as e:
      print(f"error while appending text into a file {e}")
      fileHandlingFunc()



def delete():
   filename = input("enter the filename to delete: ")
   try:
     if not  os.path.exists(filename):
        raise FileNotFoundError("file does not exist,please enter the valid filename:::::)) ")
     os.remove(filename)
     print('file deleted successfullt!!!')
     fileHandlingFunc()
   except Exception as filenotFound:
      print(filenotFound)


   except Exception as e:
      print("error deleting file : ",e)


      


def Read():
   try:
      filename = input("enter the filename to read : ")
      if not os.path.exists(filename):
         raise FileNotFoundError("file not found please enter valid filename to read :)")
      f=open(filename,"r")
      print(f.read())   

   except Exception as filenotfound:
      print("\n")
      print("*"*10)
      print(filenotfound)
      print("*"*10)
      fileHandlingFunc()




fileHandlingFunc()