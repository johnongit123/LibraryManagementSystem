# Database File for Library Management System
# used/acessed by (most)modules
# The main aim of this module is to make code more readable and synergetic
import datetime as dt

#Lists associated with functions below, useful for multiple modules
bookidLOG = []
bookid =[]
genre =[]
price=[]
title=[]


def get_books_lists():
    #This function allows us to convert the book_info txt file into a list with each element being each book with their associated info
    books=[]
    with open("books_info.txt", "r") as f:
        for booksInfo in f:
            cleanRecord = booksInfo.strip()
            lCase = cleanRecord.lower()
            books.append(lCase.split(","))
        f.close()
    return books
    

def get_logsVER2():
    #This function allows us to convert the logfiles txt file into a list with each element relating to the book id,member id, dates for checkouts and returns, and reservations
    logs=[]
    latest =[]
    with open("logfiles.txt", "r") as l: 
        for loginfo in l:
            logs.append(loginfo.split(","))
        latest=list(logs[-1])
    return latest


def get_logs():
    #This function allows us to convert the logfiles txt file into a list with each element relating to the book id,member id, dates for checkouts and returns, and reservations
    logs=[]
    with open("logfiles.txt", "r") as l: 
        for loginfo in l:
            logs.append(loginfo.split(","))
        
    return logs

#Using the above functions we are able to organise each element into a separate list for use in different modules
def get_book_id_LOG():
    logs = get_logs()
    for el in logs:
        bookidLOG.append(el[0])
    return bookidLOG

def get_book_id():
    books = get_books_lists()
    for el in books:
        bookid.append(el[0])
    return bookid

def get_genre():
    books = get_books_lists()
    for el in books:
        genre.append(el[1])
    return genre

def get_price():
    books = get_books_lists()
    for el in books:
        price.append(el[4])
    return price

def get_title():
    books=get_books_lists()
    for el in books:
       title.append(el[2])
    return title



def test_lists():
    # Checks to see if each function displays appropriate list
    a=get_book_id()
    b=get_genre()
    c=get_price()
    d= get_book_id_LOG()
    e= get_title()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)




def countlines():
    # Counts the amount of lines that exists in the log file, this is useful for the budget functionality
    count=0
    with open("logfiles.txt", "r") as l:
        for line in enumerate(l): 
            count+=1
        return count

if __name__ == "__main__":
    print("Testing:")
    test_lists()