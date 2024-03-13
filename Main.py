# The Main comprises the GUI and takes functions from both the database and other modules
# to present a sophiscated system for Libray Management
# By StudentID: F221128

from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import bookSelect as sc #Modules
import database as db
import bookReturn as r
import bookSearch as s
import bookCheckout as c


#Functions

def save_memberID(): #Takes input from entry to verify the member id
    mgmntlog.delete(0,END)
    try:
        memberID = int(idMemEntry.get())
        if memberID<=9999 and memberID>=1000:
            mgmntlog.insert(END, "Member ID has been sucessfully saved")
            return memberID #if verified the function displays an appropriate message in a list box and returns the value
        else:
            mgmntlog.insert(END, "Error: Member ID was invalid")
            return False #if it is not verified it displays an appropriate message and returns False (which is used to stop other buttons from outputting)     
    except ValueError:   
        mgmntlog.insert(END, "Error: Member ID was invalidhi")
        return False


def save_bookID(): #Similar to save_member_id , this checks the input however, through a list of book ids taken from the book_info.txt file
    mgmntlog.delete(0,END)
    try:
        userbid = idBookEntry.get()
        infobid = db.get_book_id()
        if userbid in infobid:
            mgmntlog.insert(END, "Book ID has been sucessfully saved")
            return userbid
        else:
            mgmntlog.insert(END, "Error: Book ID unrecognised")
            return False
    except ValueError:
        mgmntlog.insert(END, "Error: Book ID unrecognised")
        return False

def search():
    # This function allows the user to input words/phrases and scans the book_info.txt to check whether the word matchsn any titles
    # if it does it appropriately displays the title, along with other useful information
    searchlog.delete(0, END)
    try:
        title = searchEntry.get()
        if len(title) == 0:
            searchlog.delete(0, END)
        else:
            books = s.searchBooks(title) 
            searchttl = ["Book ID", "Title","Genre","Author","Duplicate ID"]
            if books == False:
                searchlog.insert(END, "This book is not available at this time")
            else:
                for i in range(len(searchttl)):
                    searchinfo = searchttl[i]+": "+str(books[i]).capitalize()
                    searchlog.insert(END, searchinfo)
    except ValueError:
        searchlog.insert(END, "Error: Invalid Search, Please input one or more alphabet characters")
    except IndexError:
        return None

def purchase():
    # This function uses the save_bookid and save_memberid functions as parameters for the checkout function
    # If no correct value is inputed or nothing is inputed at all, the button doesn't show anything
    bid = save_bookID()
    mid = save_memberID()
    if bid == False or mid == False:
        mgmntlog.delete(0,END)
    else:
        mgmntlog.delete(0,END)
        purchaseMSG=c.checkout(bid,mid)
        mgmntlog.insert(END, purchaseMSG)
            


        
def reserve():
    # This function uses the save_bookid and save_memberid functions as parameters for the reserve function
    # If no correct value is inputed or nothing is inputed at all, the button doesn't show anything
    mgmntlog.delete(0,END)
    bid=save_bookID()
    mid=save_memberID()
    if bid == False or mid == False:
        mgmntlog.delete(0,END)
    else:
        mgmntlog.delete(0,END)
        reserveMSG = c.reserve(bid,mid)
        mgmntlog.insert(END, reserveMSG)

def returnB():
    # This function uses the save_bookid and save_memberid functions as parameters for the returnBook function
    # If no correct value is inputed or nothing is inputed at all, the button doesn't show anything
    mgmntlog.delete(0,END)
    bid= save_bookID()
    mid = save_memberID()
    if bid == False or mid == False:
        mgmntlog.delete(0,END)
    else:
        mgmntlog.delete(0,END)
        returnMSG = r.returnBook(bid,mid)
        mgmntlog.insert(END, returnMSG)

def display_budgetrecommendations(): # Uses the user inputed budget to calculate how much it the library should spend on books based on popularity
    budgetlstbx.delete(0,END)
    try:
        budgetvalue = budgetEntry.get()
        budgets= sc.get_genre_budget(budgetvalue)
        genrelist = ["Fantasy:", "Sci-fi:", "Horror:", "Romance:", "Non-Fiction:"]
        for i in range(len(genrelist)):
            recommendation = genrelist[i]+" £"+str(budgets[i])
            budgetlstbx.insert(END, recommendation)
    except ValueError:
        budgetlstbx.insert(END, "Error: Invalid Budget, please input numbers only")


def createGraphs(): # Uses the 5 genres and logfiles.txt info to create a graph showing the activity within them, new entries into the log will also be updated when the program is reloaded
    x_val1=["Fantasy", "Sci-fi", "Horror", "Romance", "Non-Fiction"]
    y_val1=sc.genreOccurences()
    sortedbyVal =sc.sort_titles()
    topListKeys=list(sortedbyVal.keys())[0:3]
    toplistVal=list(sortedbyVal.values())[0:3]
    x_val2=topListKeys
    y_val2=toplistVal

    ax1= plt.subplot(1, 2, 1)
    ax1.set_title(("Top Book Titles"))
    ax1.set_xlabel("Titles")
    ax1.set_ylabel("Log Activity")
    ax1.bar(width=0.6,x=x_val2,height=y_val2)
        
    ax2 = plt.subplot(1, 2, 2)
    ax2.set_title(("Bar chart of Popular Genres"))
    ax2.set_xlabel("Genres")
    ax2.set_ylabel("Log Activity")
    ax2.bar(x=x_val1,height=y_val1)

    plt.tight_layout()
    fig.set_visible(True)
    canvas.draw()


def closeGraphs(): # Closes/hides the graph
    fig.set_visible(False)
    canvas.draw()


##################
###### MAIN ######
##################

lib = Tk()
lib.geometry('1050x750')
lib.title("Library Management System")
lib.resizable(height=False,width=False)
lib.configure(bg="#6E260E")


notebook= ttk.Notebook(lib)
home = Frame(notebook, bg="#6E260E", width=1050, height=750)
libtools = Frame(notebook, bg="#6E260E", width=1050, height=750)
notebook.add(home, text="Home")
notebook.add(libtools, text="LibTools")
notebook.pack(expand=True, fill="both")
titlelbl= Label(home, text="Welcome to the Library!", font=('Times', 30), fg='#E1C16E', bg='#6E260E',padx=10, pady=20)
notice= Label(home, text="Please note: Before you can checkout,return or reserve, you must input the correct Book ID and membership ID", font=('Helvetica',9), fg='#FF0000', bg='#6E260E')

###HOME###
#Search GUI
searchlbl= Label(home, text="Find book:", font=('Times', 15), fg='#E1C16E', bg='#6E260E')
searchEntry = Entry(home,textvariable="" ,fg='#E1C16E',bg='#4A0404',width=15,font=(12))
searchlog=Listbox(home,fg='#F4BB44',bg='#4A0404',font=7, width=45, height=25)
searchbtn = Button(home,text="Search",fg='#E1C16E', bg='#6E260E',command=search)

#Saving ID GUI
mgmntlog= Listbox(home,fg='#F4BB44',bg='#4A0404',font=7, width=55, height=21, highlightcolor="#483C32")

idBooklbl = Label(home, text="Enter Book Id:",font=('Times', 15), fg='#E1C16E', bg='#6E260E')
idBookEntry = Entry(home,fg='#E1C16E',bg='#4A0404',width=15, font=(12))
saveBookbtn = Button(home,text="Save",fg='#E1C16E', bg='#6E260E',command=save_bookID)

idMemlbl = Label(home, text="Enter Member Id:",font=('Times', 15), fg='#E1C16E', bg='#6E260E',)
idMemEntry = Entry(home,fg='#E1C16E',bg='#4A0404',width=15, font=(12))
saveMembtn = Button(home,text="Save",fg='#E1C16E', bg='#6E260E',command=save_memberID)


#Checkout GUI
checkoutbtn = Button(home,text="Purchase Books",command=purchase,fg='#E1C16E', bg='#6E260E',width=15, height=4,font=7)

reservebtn = Button(home,text="Reserve Books",command=reserve,fg='#E1C16E', bg='#6E260E',width=15, height=4,font=7)

#Return GUI
returnbtn = Button(home,text="Return Books",command=returnB,fg='#E1C16E', bg='#6E260E',width=15, height=4,font=7)

###LIBTOOLS###
#Graph GUI
fig = plt.figure(figsize=(4,4))

canvas= FigureCanvasTkAgg(fig, master=libtools)
sketchbtn= Button(libtools,text="Show Graph",fg='white', bg='#6E260E',command=createGraphs)
closebtn= Button(libtools,text="Close Graph",fg='white', bg='#6E260E',command=closeGraphs)

#Budget GUI
budgetlbl= Label(libtools,text="Budget:",font=('Times', 25), fg='#E1C16E', bg='#6E260E')
budgetEntry= Entry(libtools,fg='#E1C16E',bg='#4A0404',width=15, font=(12))
budgetbtn = Button(libtools,text="Enter",fg='#E1C16E', bg='#6E260E',command=display_budgetrecommendations)
budgetlstbx= Listbox(libtools, fg='#E1C16E', bg='#4A0404',font=(50), width=50)



#defining locations
#HOME
notice.pack(padx=0.5,pady=1)
titlelbl.pack()
searchlbl.place(x=2, y=125)
searchEntry.place(x=5, y=150)
searchbtn.place(x=147, y=147)
searchlog.place(x=5, y=180)
mgmntlog.place(x=540, y=180)
idBooklbl.place(x=540, y=125)
idBookEntry.place(x=543, y=150)
saveBookbtn.place(x=685, y=147)
idMemlbl.place(x=822, y=125)
idMemEntry.place(x=825, y=150)
saveMembtn.place(x=967, y=147)
checkoutbtn.place(x=560, y=600)
reservebtn.place(x=725, y=600)
returnbtn.place(x=890, y=600)
#LIBTOOLS
canvas.get_tk_widget().place(x=22, y=80,width=1000)
sketchbtn.place(x=22, y=52)
closebtn.place(x=100, y=52)
budgetlbl.place(x=50, y=500)
budgetEntry.place(x=50, y=600)
budgetbtn.place(x=150, y=600)
budgetlstbx.place(x=250, y=500)


if __name__ == "__main__":
    lib.mainloop()