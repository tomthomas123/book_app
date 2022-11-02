import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root', password = '',database = 'librarydb')

mycursor = mydb.cursor()
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
        name = input("enter the name of the book :")
        author =input("Enter the author name :  ")
        category = input("Enter the category : ")
        price =input("Enter the price per day : ")
        sql = 'INSERT INTO `books`(`bookname`, `bookauthor`, `bookcategory`, `book_rentprice`) VALUES  (%s,%s,%s,%s)'
        data = (name,author,category,price)
        mycursor.execute(sql,data)
        mydb.commit()
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