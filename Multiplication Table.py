print("Multipication Table")


while True:
    try:
        print("x to exit \n")
        user_input = input("Enter the Multipication Table lenght: ")
        q = int(user_input) + 1
        z = 1

        for i in range(1,q):
            print(z,"Times")
            z+=1
            for a in range (1,q):
                print (i,"x",a,"=",i*a)
            print("_____________________________")

    except:
        if user_input == "x":
            break
        print("***pls enter a number*** \n")


