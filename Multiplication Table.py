print("Multipication Table")

#A while loop statement that allows the user to input the desire multiplication length
while True:
    try:
        print("x to exit\n")
        user_input = input("Enter the Multipication Table length: ")
        q = int(user_input) + 1
        z = 1
#A for loop statement that allows i and a ranges interact and create multiplication tables with the stop barrier
        for i in range(1,q):
            print(z,"Times")
            z+=1
            for a in range (1,q):
                print (i,"x",a,"=",i*a)
#A bar that separates the different tables                
            print("_____________________________")
#A break statement that allows the user to end the process on choice using letter 'x'
    except:
        if user_input == "x":
            break
        print("***pls enter a number*** \n")


