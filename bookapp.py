while True:
    print("select an option from the menu")
    print("""             1. add book
             2. view all books
             3. search a book
             4. update the book
             5. delete a book
             6. exit   
                 """)   
    choice =int(input("Enter your option : "))
    if choice==1:
        print("book entry selected")
    elif choice==2:
        print("view all books selected ")
    elif choice==3:
        print("search the  books : ")
    elif choice==4:
        print("update the book  ")
    elif choice==5:
        print("delete the book  ")
    elif choice==6:
        break