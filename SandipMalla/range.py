                # range without using recursive function
# start=int(input("Enter the start number: "))
# stop=int(input("Enter the stop number :"))
# step=int(input("Enter the step value  :"))
# def my_range(start, stop, step):
#     while  start < stop:
#         print(start)
#         if step!=0:
#             start+=step
#         else:
#             start +=1
# my_range(start, stop, step)
                    # Range using recursion function
a = int(input('Start: ') )  
b = int(input('Stop: ') )  
c = int(input('Step: '))
def my_range(start, stop, step):
    print(start)
    start+=step
    if start>stop:
        return 0
    else:
        my_range(start,stop,step)     
my_range(a,b,c)