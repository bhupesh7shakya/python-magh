 

# while True:
#     try:
#         a=int(input("Number"))
#         b=int(input("Arko number"))


#         if b==5:
#             raise Exception("5 number not accepted")
        

#         print(a/b)

#     except ZeroDivisionError:
#         print('A number cannot devided zero')

#     except Exception as e:
#         print("Something went wrong", e)




while True:
    try:
        a=[1,3,5,7,9]
        b=int(input("Enter any number"))
        print(a[b])
        
        
    except IndexError as e: 
            print("something wrong")

