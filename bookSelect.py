# The Select modules is used to grab the ids of books in the book_info txt file and the logfile and 
# list the amount of times each bookid occurs in the log,
# this then generates a graph which the user can locate in the LIBTOOLS section of the Gui
#By: F221128

import matplotlib.pyplot as plt
from  tkinter import * 
import database as db

# Generates lists to be used in various parts of this module
db_bookInfo=db.get_books_lists()
db_bookid = db.get_book_id()
db_bookidLOG = db.get_book_id_LOG()

          
def titleOccurences():
    # Generates a dictionary associating book titles to the amount of times they've been logged
    titles= {}
    for bi in db_bookInfo:
        x=0
        for j in range(len(db_bookidLOG)):
            if str(bi[0]) == str(db_bookidLOG[j]):
                x += 1
                titles[bi[2]]=x
    return titles


def sort_titles():
    # This sorts titles by most occurences to least
    titles= titleOccurences()
    sortedbyVal ={k: v for k, v in sorted(titles.items(), key= lambda v: v[1],reverse=True)}
    return sortedbyVal

def idOccurences():
    # Generates a list  of the amount of times a certain bookid (from the book_info) has been logged in the logfiles
    occurence = []
    for i in range(len(db_bookid)): 
        x=0
        for j in range(len(db_bookidLOG)):
            if str(db_bookid[i]) == str(db_bookidLOG[j]):
                x += 1
        occurence.append(x)
    return occurence

def genreOccurences():
    # Generates a list that takes the order of occurences and sorts it by Genre
    occurence = idOccurences()
    total= []
    for i in range(len(occurence)):
        fantasy = occurence[0]+occurence[1]+occurence[3]+occurence[11]+occurence[16]
        sci_fi= occurence[8]+occurence[10]+occurence[18]+occurence[19]
        horror= occurence[2]+occurence[4]+occurence[7]+occurence[13]+occurence[15]
        romance= occurence[5]+occurence[14]+occurence[17]
        non_fiction= occurence[6]+occurence[9]+occurence[12]
        total.append(fantasy)
        total.append(sci_fi)
        total.append(horror)
        total.append(romance)
        total.append(non_fiction)
        return total



def get_genre_budget(budget):
    # Using the total number of lines in the logfile, this function takes the amount of occurnces by genre 
    # and calculates the amount to be spent on it based of both the budget inputed by the user and the log activity
    genre_popularity=genreOccurences()
    count = db.countlines()
    genre_budgetlist = []
    for value in genre_popularity:
        genre_ratio=value/count
        budgetForGenre= genre_ratio*int(budget)
        if budgetForGenre<0:
            genre_budgetlist.append(0)
        else:
            genre_budgetlist.append(round(budgetForGenre))
    return genre_budgetlist


def test_plotter():
    # Creates a bar chart labelling genres to the amount they've been logged in the logfiles.txt
    x_val=["Fantasy", "Sci-fi", "Horror", "Romance", "Non-Fiction"]
    y_val=genreOccurences()
    positions= [0, 1, 2, 3, 4]
    plt.bar(positions, y_val, width=0.5, color="yellow")
    plt.xticks(positions, x_val)
    plt.title("Bar chart of Popular Genres")
    plt.xlabel("Genres")
    plt.ylabel("Frequency")
    plt.show()

def test_plotter2():
    # Creates a bar chart which shows only the top 3 most logged books by book title
    sortedbyVal = sort_titles()
    topListKeys=list(sortedbyVal.keys())[0:3]
    toplistVal=list(sortedbyVal.values())[0:3]
    x_val= topListKeys
    y_val=toplistVal
    xpositions= [0, 1, 2,]
    ypositions= [0, 1, 2,]
    plt.bar(ypositions, y_val, width=0.5, color="yellow")
    plt.xticks(xpositions, x_val)
    plt.title("Top 3 Book Titles")
    plt.xlabel("Title")
    plt.ylabel("Log Activity")
    plt.show()

# These test whether their respective functions outputs an appropriate list or value
def test_TITLEoccurences():
    y=titleOccurences()
    print(y)

def test_sorted_dict():
    a = sort_titles()
    print(a)

def test_IDoccurences():
    y=idOccurences()
    print(y)

def test_GENREoccurences():
    y=genreOccurences()
    print(y)

def test_get_genre_budget():
    g=input("enter budget:")
    l = get_genre_budget(g)
    print(l)



if __name__ == "__main__":
    print("Testing:")
    #Input desired test function under: