clients=["Harry","Rohan","hammad"]
print("Hi i am fitness trainer")
user = int(input("press 1 for diet\n""press 2 for exercise\n"))

if user==1:
    print("you have selected for diet")
elif user==2:
    print("you have selected for Exercise")

else:
    print("you cannot procces")


def client_name():
    print(" 1 for rohan\n","2 for harry\n","3 for hammad\n")
    bachhe=int(input("enter your name here"))
    if bachhe==1:
        print("you have selected rohan")
    elif bachhe==2:
        print("you have selected harry")
    elif bachhe==3:
        print("you have selected hammad")
    else:
        print("your choice is wrong")
        return 0
    if bachhe==1:
        rohans=input("Rohan Enter what exercise you did\n")
        f=open("rohan food.txt","w")
        f.write(rohans)
        f.close()
    if bachhe==2:
        harrys=input("Harry Enter what exercise you did\n")
        h=open("harry food.txt", "w")
        h.write(harrys)
    if bachhe==3:
        hammads=input("hammad enter what exercise you did\n")
        m=open("hammad food.txt","w")
        m.write(hammads)

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
        print("your choice is wrong")

    if chokre==1:
        rohanss=input("Rohan Enter what food you eat\n")
        f=open("rohan real food.txt","w")
        f.write(rohanss)
        f.close()
    if chokre==2:
        harryss=input("harry Enter what food you eat\n")
        f=open("harry real food.txt","w")
        f.write(harryss)
        f.close()
    if chokre==3:
        hammadss=input("Rohan Enter what food you eat\n")
        f=open("hammad real food.txt","w")
        f.write(hammadss)
        f.close()


print(clients_diet())

















