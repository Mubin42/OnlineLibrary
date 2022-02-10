#coding Segment
totalbook = ("Ami", "Himu Somogro", "Misir Ali Somogro", "Deyal", "Dorjar Opashe")
remainingbook = ["Ami", "Himu Somogro", "Misir Ali Somogro", "Deyal", "Dorjar Opashe"]

def viewall():
    for i in totalbook:
        print(i, end=" | ")
    print()
    print("Total Books: ", len(totalbook))
    print("Total Rented Books: ", len(totalbook) - len(remainingbook))

def view():
    for i in remainingbook:
        print(i, end=" | ")
    print()
    print("Total Available Books: ", len(remainingbook))
    print("Total Rented Books: ", len(totalbook) - len(remainingbook))

def rent(bookname):
    if(remainingbook.__contains__(bookname)):
        remainingbook.remove(bookname)
        print("Rent Successful:", bookname)
    else:
        print("Book Not Found.")

def rtn(bookname):
    if(remainingbook.__contains__(bookname)):
        print("Book Already Exists")
    else:
        remainingbook.append(bookname)
        print("Return Successful")


#Console UI Segment
while(True):
    mode = input('''---------------------------------------
Type "viewall" to view all books in the library
Type "view" to view all available books
Type "rent" to rent a book
Type "return" to return a rented book
Type "q" to exit
---------------------------------------''')
    if(mode=="q"):
        break
    elif(mode=="viewall"):
        viewall()
    elif(mode=="view"):
        view()
    elif(mode=="rent"):
        book = input("Input Bookname: ")
        rent(book)
    elif(mode=="return"):
        book = input("Input Bookname: ")
        rtn(book)

