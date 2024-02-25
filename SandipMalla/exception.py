while True:
    try:
        a = [1,2,3,4,5]
        b = input("Enter the index you want to access: ")
        print(f"The  value at index {b} is {a[int(b)]}")
    except IndexError as e:
        print("Invalid index!", e)
        
    except ValueError as v:
        print("Invalid value, enter correct value",v)
    except Exception as e:
        print(e)