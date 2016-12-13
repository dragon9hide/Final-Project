'''
Created on Nov 29, 2016

@author: ah208044
'''
from tkinter import *

class Recipe:
    def __init__(self, cat, na, num):
        self.catagory = cat
        self.name = na
        self.ingrednt = []
        Ingreds(num, self.ingrednt).mainloop()

    def toPrint(self):
        print(self.name, "\n", self.catagory, "\n", self.ingrednt)
        
class Ingreds(Frame):
    def __init__(self, num, ingredients):
        Frame.__init__(self)
        self.cookBook = ingredients
        self.ammount = StringVar()
        self.ammount.set('')
        self.measure =StringVar()
        self.measure.set('')
        self.item = StringVar()
        self.item.set('')
        for i in range(0,num):
            self.master.title("What is the Ingredient")
            self.grid()
            
            ingred = Toplevel(self)
            #ingred.grid(row = 0, column = 0)
            a1 = Label(ingred, text = 'how much is there just the number')
            a1.grid(row = i, column = 0)
            #a1.pack()
            a2 = Entry(ingred, textvariable = self.ammount)
            a2.grid(row = (i+1), column = 0)
            #a2.pack()
            b1 = Label(ingred, text = 'What is the unit of measure')
            b1.grid(row = i, column = 1)
            #b1.pack()
            b2 = Entry(ingred, textvariable = self.measure)
            b2.grid(row = (i+1), column = 1)
            #b2.pack()
            c1 = Label(ingred, text = 'what is the name of the ingredient')
            c1.grid(row = i, column = 2)
            #c1.pack()
            c2 = Entry(ingred, textvariable = self.item)
            c2.grid(row = (i+1), column = 2)
            #c2.pack()
            self.cookBook.append([]) 
            self.cookBook[i].append(self.ammount.get())
            self.cookBook[i].append(self.measure.get())
            self.cookBook[i].append(self.item.get())
            d1 = Button(ingred, text = "Next", command = ingred.destroy)
            d1.grid(row = (i+2), column = 0)
            #d1.pack()
           
            

class recipieBook(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("The Book of recipes")
        self.grid()
        
        #pull recipiers from a file and enter them into a book
        '''
        pull from a file
        split on key term ,
        on evert mutiple of 3 ex 3,6,9,... split on dif key |
        so you get [name,cat,[ing1|ing2]]
        split once again on diff key \
        get [name, cat,[[ammount, measure, name of ingred1],[ammount, measure, name of ingred2]]]]
        assign as necisssary in a while loop
        '''
        self.ingredR = IntVar()
        self.nameR = StringVar()
        self.catR = StringVar()
        self.startF = StringVar()
        self.startC = StringVar()
        self.startF.set('')
        self.startC.set('')
        self.nameR.set('')
        self.catR.set('')
        self.ingredR.set(0)
        self.book = []
        
        #Add in a section for adding a new entry to the book
                
        #LOGIC
        def algo():
            print("WIP")
            self.book[0].toPrint()
                
        def new():
            
            self.book.append(Recipe(self.catR.get(), self.nameR.get(), self.ingredR.get()))
            self.nameR.set('')
            self.catR.set('')
            self.ingredR.set(0)
            self.book[0].toPrint()
        
        #GUI
        self.recBook = Frame(self)
        self.recBook.grid(row = 0, column = 0)
        
        
        self.l1 = Label(self.recBook, text = 'Keyword')
        self.l1.grid(row = 0, column = 0)
        
        self.l2 = Entry(self.recBook, textvariable = self.startF)
        self.l2.grid(row = 1, column = 0)
        
        self.r3 = Button(self.recBook, text = 'Search', command = algo)
        self.r3.grid(row = 2, column = 1)
        
        
        self.r1 = Label(self.recBook, text = 'Search Type')
        self.r1.grid(row = 0, column = 1)
        
        self.r2 = Entry(self.recBook, textvariable = self.startC)
        self.r2.grid(row = 1, column = 1)
        
        self.r4 = Label(self.recBook, text = 'Recipe')
        self.r4.grid(row = 3, column = 0)
        
        self.r5 = Entry(self.recBook, textvariable = self.nameR)
        self.r5.grid(row = 4, column = 0)
        
        self.m4 = Label(self.recBook, text = 'Category')
        self.m4.grid(row = 3, column = 1)
        
        self.m5 = Entry(self.recBook, textvariable = self.catR)
        self.m5.grid(row = 4, column = 1)
        
        self.r4 = Label(self.recBook, text = 'Ingrediants')
        self.r4.grid(row = 3, column = 2)
        
        self.r5 = Entry(self.recBook, textvariable = self.ingredR)
        self.r5.grid(row = 4, column = 2)
        
        self.r7 = Button(self.recBook, text = 'New Entry', command = new)
        self.r7.grid(row = 6, column = 1)
        
        
        
def main():
    recipieBook().mainloop()
    
    
main()