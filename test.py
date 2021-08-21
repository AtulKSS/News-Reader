print("Hi i am fitness trainer")
user = int(input("press 1 for exercise\n""press 2 for diet\n"))


def client_name():

    print(" 1 for rohan\n","2 for harry\n","3 for hammad\n")
    bachhe=int(input("enter your name here\n""also you can quit by pressing4"))
    if bachhe==1:
        print("you have selected rohan")
    elif bachhe==2:
        print("you have selected harry")
    elif bachhe==3:
        print("you have selected hammad")
    else:
        print("your choice is wrong")
        quit()


    if bachhe==1:
        def getdate():
            import datetime
            return datetime.datetime.now()

        rohans=input("Rohan Enter what exercise you did\n",)
        print(getdate())
        f=open("rohan food.txt","w")
        f.write(rohans)
        f.close()
        print("quit by pressing 4")
    if bachhe==2:
        harrys=input("Harry Enter what exercise you did\n")
        h=open("harry food.txt", "w")
        h.write(harrys)
        h.close()
        print("quit by pressing 4")
    if bachhe==3:
        hammads=input("hammad enter what exercise you did\n")
        m=open("hammad food.txt","w")
        m.write(hammads)
        m.close()
        print("quit by pressing 4")

    if user==4:
        quit()
        print("press 4 to quit")

    print(client_name())



def clients_diet():
    print(" 1 for rohan\n", "2 for harry\n", "3 for hammad\n")
    chokre=int(input("enter your name here"))
    if chokre==1:
        print("you have selected rohan")
    elif chokre==2:
        print("you have selected harry")
    elif chokre==3:
        print("you have selected hammad")
    else:
        quit()

    if chokre==1:
        rohanss=input("Rohan Enter what food you eat\n")
        f=open("rohan real food.txt","w")
        f.write(rohanss)
        f.close()
        print("quit by pressing 4")
    if chokre==2:
        harryss=input("harry Enter what food you eat\n")
        f=open("harry real food.txt","w")
        f.write(harryss)
        f.close()
        print("quit by pressing 4")
    if chokre==3:
        hammadss=input("hammad Enter what food you eat\n")
        f=open("hammad real food.txt","w")
        f.write(hammadss)
        f.close()
        print("quit by pressing 4")

    if user==4:
        quit()



    print(clients_diet())

while user:
    if user==1:
        print(client_name())
        break

    elif user==2:
     print(clients_diet())
     break

    else:
        quit()























