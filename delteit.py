print("welcome to Atul Library")
allbooks = {"the jungle book", "Alice in the wonder land", "Buddha and his dhamma"}


class library:

    def __init__(self):
        pass

    def displaybook(self,displaybook):
        self.display = allbooks

        print(self.display)


    def lendbook(self,lendbook,books):
        self.lend=lendbook
        self.lend=books
        self.msg='which book do you want to lend'
        print(self.msg)
        self.input=input("")
        f=open('record for lending'"a")
        f.write(self.input)
        f.close()


    def addbook(self,addbook):
        self.addbook=addbook
        self.message='which book do you want to donate'
        print(self.message)
        self.inputs = input()
        f = open('records for donation'"a")
        f.write(self.inputs)
        f.close()

    def returnbook(self,returnbook):
        self.returns=returnbook
        self.returnss='which book do you want to return'
        print(self.returnss)
        self.take=input()
        f=open('record for return'"a")
        f.write(self.take)
        f.close()


d=library()
choice=''
while choice != 'q':

    print("\n[1] Enter 1 to lend a book.")
    print("[2] Enter 2 to return a book.")
    print("[3] Enter 3 to donate a book.")
    print("[4] Enter 4 to donate a book to quit.")
    print("[q] to quit the menu.")

    choice = input("\nWhat would you like to do? ")

    # Respond to the user's choice.
    if choice == '1':
        print(d.lendbook("",6))
    elif choice=='2':
        print(d.returnbook(""))
    elif choice=='3':
        print((d.addbook("")))
    elif choice=='4':
        print(d.displaybook(""))
    elif choice=='q':
        print("press q to exit")

    else:
        print("\nI don't understand that choice, please try again.\n")

