# The Checkout module is very similar to the functionalities of the Return Module,
# it generates the current date, makes use of the user inputed book and member ids,
# then checks the logs for the most appropriate info to either check-out, not-checkout or reserve
# By: F221128

import database as db
import datetime as dt


def reserve(bid,mid):
    # The function takes the user input (book id and member id)
    # it checks the most and 2nd most recent log information
    # if the log information matches certain events/parameters (if statements)
    # the function either writes into the log and returns a message or only returns a message
    # this message is then displayed in the Gui
    bookLogs=[]
    latestUpdate=[]
    pre_Latest=[]

    with open("logfiles.txt", "r") as f:
        for line in f:
            details = line.split(",")
            if str(bid) == details[0]:
                bookLogs.append(line)

    latestUpdate.append(bookLogs[-1].split(","))
    pre_Latest.append(bookLogs[-2].split(","))

    if latestUpdate[0][4] != " \n" and latestUpdate[0][1] == str(mid):
        return "You are already on the reserve list :)"

    elif latestUpdate[0][1] != str(mid) and latestUpdate[0][4] != " \n":
        if pre_Latest[0][1] == str(mid):
            return "Error: Book cannot be reserved as you currently own it"
        else:
            return "Error: This Book has already been reserved by another member"

    elif latestUpdate[0][1] == str(mid) and latestUpdate[0][4] != " \n":
        if pre_Latest[0][1] == str(mid):
            return "Error: Book cannot be reserved as you currently own it"

    elif latestUpdate[0][2] != " " and latestUpdate[0][3] == " " and latestUpdate[0][4] == " \n": 
            reserve = "Reserved by: "+str(mid)
            with open("logfiles.txt","a") as l:
                l.write(str(bid)+","+str(mid)+", , ,"+reserve+"\n")
            return "Book has succesfully been reserved. Have a nice day! :)"
    else:
        return "Error: This Book has already been reserved by another member"

def checkout(bid,mid):
    # This function, simiar to reserve, uses user inputs as bookid and memberid
    # running it through the logfile, it creates a list of the most recent and second most recent log data
    # this data is then examined to see whether a book is available for checkout or not
    # in both cases, the function will relay an appropriate message which is displayed in the Gui
    today = dt.datetime.today()
    todaystring=today.strftime('%d/%m/%Y')
    bookLogs=[]
    latestUpdate=[]
    pre_Latest=[]

    with open("logfiles.txt", "r") as f:
        for line in f:
            details = line.split(",")
            if str(bid) == details[0]:
                bookLogs.append(line)

    latestUpdate.append(bookLogs[-1].split(","))
    pre_Latest.append(bookLogs[-2].split(","))

    if latestUpdate[0][4] == " \n" and latestUpdate[0][2] != " " and mid != latestUpdate[0][1]:
        return "Error: This book is already in use, however you can RESERVE it"

    elif latestUpdate[0][4] == " \n" and latestUpdate[0][3] != " ":
        if pre_Latest[0][1] == str(mid) and pre_Latest[0][4] != " \n":
            with open("logfiles.txt", "a") as f:
                f.write(str(bid)+","+str(mid)+","+todaystring+", , "+"\n")
            return "Book successfully loaned. Enjoy! :)"
        elif pre_Latest[0][4] != " \n" and pre_Latest[0][1] != str(mid):
            return "As this book has already been reserved, you cannot purchase it."
        else:
            with open("logfiles.txt", "a") as f:
                f.write(str(bid)+","+str(mid)+","+todaystring+", , "+"\n")
            return "Book successfully loaned. Enjoy! :)"

    elif latestUpdate[0][4] == " \n" and latestUpdate[0][2] != " " and mid == latestUpdate[0][1]:
        with open("logfiles.txt", "a") as f:
            f.write(str(bid)+","+str(mid)+","+todaystring+", , "+"\n")
            return "Book successfully loaned. Enjoy! :)"

    elif latestUpdate[0][4] != " \n" and latestUpdate[0][1]!= str(mid):
        return "As this book has already been reserved, you cannot purchase it."

    elif latestUpdate[0][4] != " \n" and latestUpdate[0][1] == str(mid):
        return "Book can only be purchased once returned, please be patient :)"
    
    

def test_display_update(bid):
    # displays list of most recent and 2nd recent log activity
    bookLogs=[]
    latestupdate=[]
    pre_latest=[]
    with open("logfiles.txt", "r") as f:
        for line in f:
            details = line.split(",")
            if str(bid) == details[0]:
                bookLogs.append(line)
    latestupdate.append(bookLogs[-1].split(","))
    pre_latest.append(bookLogs[-2].strip(","))
    return print(pre_latest), print(latestupdate)

def test_checkout():
    # checks the chekout function is working properly
    x=int(input("Enter book Id:"))
    y=int(input("Enter member Id:"))
    get_checkout= checkout(x,y)
    print(get_checkout)

def test_reserve():
    # checks the reserve function is working properly
    x=int(input("Enter book Id:"))
    y=int(input("Enter member Id:"))
    get_checkout= reserve(x,y)
    print(get_checkout)


if __name__ == "__main__":
    print(" Change returns to print('---') rather than just returning --- !")
    test_display_update(20)


