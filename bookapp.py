import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root', password = '',database = 'librarydb')

mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print("""             1. add book
             2. view all books
             3. search a book by category
             4. update the book
             5. delete a book
             6. Diplay the total amount for each book depending on the return date
             7. Display the total number of books in each category of book table
             8. Display the book details where book name starting character contain 
             9. Exit
              
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
        sql = "SELECT * FROM `books` "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        #for i in result:
        print(result)
        
    elif choice==3:
        print("search the  books by category : ")
        category = input("Enter the book category you needed : ")
        sql = "SELECT `id`, `bookname`, `bookauthor`, `bookcategory`, `book_rentprice` FROM `books` WHERE `bookcategory`='"+category+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif choice==4:
        print("update the book  ")
        perday = input("Enter the price for each day to be get updated : ")
        name = input('Enter the book name : ')
        AuthorName = input('Enter the author name : ')
        category = input('Enter the category of the book : ')
        sql = "UPDATE `books` SET `bookname`='"+name+"',`bookauthor`='"+AuthorName+"',`bookcategory`='"+category+"',`book_rentprice`='"+perday+"' WHERE `book_rentprice`="+perday
        mycursor.execute(sql)
        mydb.commit()
        print(" data updated ")
    elif choice==5:
        print("delete the book  ")
        price = input("Enter the book price to be deleted : ")
        sql = " DELETE FROM `books` WHERE `book_rentprice`="+price
        mycursor.execute(sql)
        mydb.commit()
        print("deleted successfully")
    elif choice==6:
        print("Get the total amount for each book depending on the return date : ")
        sql = 'SELECT i.`user_id`, i.`book_id`, i.`issue_date`, i.`return_date`, DATEDIFF(i.`return_date`,i.`issue_date`)AS DATEdiffrence,DATEDIFF(i.`return_date`,i.`issue_date`) * b.book_rentprice AS TOTAL FROM issue_book i JOIN books b ON i.book_id = b.`id`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif choice==7:
            print("Display the total number of books in each category of book table")
            sql = "SELECT COUNT(id),`bookcategory` FROM `books` GROUP BY `bookcategory`"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(result)
    elif choice==8:
        print("")
    elif choice==9:
        print("")
        break