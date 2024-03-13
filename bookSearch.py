#The Search function allows ther user to take their input, the book title, 
# from the gui and check if that inpout is similar to the title within books_info.txt
# it allows the user to input one word that might be within the book title and output a book with similar characters or words
#By: F221128

from tkinter import *
import database as db



def searchBooks(title):
    flag= False #Flag is needed to return the list of relevant information, if the user input does not match the txt file, it registers it as false and returns a False bool.
    searchResults=[]
    title = str(title).strip().lower()
    allbooks=[]
    with open("books_info.txt", "r") as f:
        for booksInfo in f:
            cleanRecord = booksInfo.rstrip()
            lCase = cleanRecord.lower()
            allbooks.append(lCase.split(","))
    for book in allbooks:
        if title in book[2]:
            searchResults.append(book[0]) #Appending the relevant info; title, id, genre, author
            searchResults.append(book[1])
            searchResults.append(book[2])
            searchResults.append(book[3])
            flag = True
    c = 0
    while c < len(searchResults): #This code allows us to add a 5th element which takes the id of any duplicate books and appends it
        d = c + 1
        while d < len(searchResults):
            if searchResults[c] == searchResults[d]:
                del searchResults[d]
            else:
                d += 1
        c += 1
        
    if flag:
        return searchResults
    else:
        return False
         

def test_search():
    x=input("enter title:")
    a= searchBooks(x)
    print(a)

if __name__ == "__main__":
    print("Testing book search")
    test_search()
