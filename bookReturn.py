# The Return module uses an assited datetime library to generate the current date.
# Alongside the user inputed book id and member id, this module checks the log
# for whether a book has been checked out, or reserved and outputs a specifc response
# By: F221128

import datetime as dt
import database as db


def returnBook(bid,mid):
    today = dt.datetime.today()
    todaystring=today.strftime('%d/%m/%Y')
    bookLogs=[]
    latestUpdate=[]
    pre_Latest=[]

    with open("logfiles.txt", "r") as f: # Generates a list which checks whether the book id is within a log, the lines that have this are added to a list
        for line in f:
            details = line.split(",")
            if str(bid) == details[0]:
                bookLogs.append(line)

    latestUpdate.append(bookLogs[-1].split(",")) # Takes the most recent line of the log which uses the bookid
    pre_Latest.append(bookLogs[-2].split(",")) # Takes the line before the most recent

    # This series of if, else, elif statements look for empty space and equivalent values
    # to write into the logfiles.txt and/or display an appropriate message which is displayed in the Gui
    if latestUpdate[0][1] == str(mid) and latestUpdate[0][2] != " ":
        with open("logfiles.txt", "a") as f:
            f.write(str(bid)+","+str(mid)+", ,"+todaystring+", \n")
        return "Book has succesfully been returned, thank you. :)"

    elif latestUpdate[0][1] != str(mid) and latestUpdate[0][4] == " \n":
        return "Error: User does not owe this book."

    elif latestUpdate[0][1] != str(mid) and latestUpdate[0][4] != " \n":
        if pre_Latest[0][1] == str(mid):
            with open("logfiles.txt", "a") as f:
                f.write(str(bid)+","+str(mid)+", ,"+todaystring+", \n")
            return "Book has succesfully been returned, thank you. :)"
        else:
           return "Error: User does not owe this book."

    elif latestUpdate[0][1] == str(mid) and latestUpdate[0][4] != " \n":
        if pre_Latest[0][1] == str(mid):
            with open("logfiles.txt", "a") as f:
                f.write(str(bid)+","+str(mid)+", ,"+todaystring+", \n")
            return "Book has succesfully been returned, thank you. :)"
        else:
           return "Error: User does not owe this book."

    else:
        return "Error: This book is already in the system."


def test_recents(bid):
    # displays list of most recent and 2nd recent log activity
    bookLogs=[]
    pre_latest=[]
    latestupdate=[]
    with open("logfiles.txt", "r") as f:
        for line in f:
            details = line.split(",")
            if str(bid) == details[0]:
                bookLogs.append(line)
    latestupdate.append(bookLogs[-1].split(","))
    pre_latest.append(bookLogs[-2].split(","))
    return print(pre_latest), print(latestupdate)

def test_checkout():
    # checks the return function is working properly
    x=int(input("Enter book Id:"))
    y=int(input("Enter member Id:"))
    get_return= returnBook(x,y)
    print(get_return)


    

if __name__ == "__main__":
    print(" Change returns to print('---') rather than just returning --- !")
    