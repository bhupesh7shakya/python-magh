# f=open('hello.txt')
# print(f.read())



user_input= input("Enter the Text:")

f=open('hello.txt', 'a')
f.write(user_input + '\n')
f.read('hello i was written from the script', 'a')

print("Data written to the file.")
