# while True:
#     try:
#         a=int(input("number:"))
#         b=int(input("next number:"))  
#         if b==6:
#             raise Exception("5 number is not valid")
#         print(a/b)
        
#     except  ZeroDivisionError:
#         print('zero le divide jadain bro')
#     except Exception as e:
#         print("kehi mistake vo:",e)
                  

while True:  
    try:
        a=[8,9,6,5,4]
        index=int(input("enter any number:"))
        if index >=len(a):
            raise Exception("jpt nahann")
        print(a[index])
        
    except Exception as e:
        print("mistake vo kehi",e)
    

              