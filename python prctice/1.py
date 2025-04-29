while True:
    num = input("enter a valid number")

    try:
        num = float(num)
        if num>0:
            print("number is valid:")
            break
        else:
            print("number isnot valid please try again :")
    except ValueError:
        print("enter a valid input:")


