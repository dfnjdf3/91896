#import tkinter so we can make a GUI
from tkinter import *
from tkinter import messagebox

#quit subroutine
def quit():
    main_window.destroy()

#print details of customers
def print_shop_details ():
    name_count = 0
    #Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),text="Row").grid(column=0,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Customer Name").grid(column=1,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Receipt Number").grid(column=2,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Item Hired").grid(column=3,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Number Hired").grid(column=4,row=7)
    #add each item in the list into its own row
    while name_count < counters['total_entries'] :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(shop_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(shop_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(shop_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(shop_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1
        counters['name_count'] = name_count
        
#Check the inputs are all valid


#add the next customer to the list
def append_name ():
    #append each item to its own area of the list
    shop_details.append([entry_customer.get(),entry_receipt.get(),entry_hired.get(),entry_number_hired.get()])
    #clear the boxes
    entry_customer.delete(0,'end')
    entry_receipt.delete(0,'end')
    entry_hired.delete(0,'end')
    entry_number_hired.delete(0,'end')
    counters['total_entries'] += 1

#delete a row from the list

#create the buttons and labels
def setup_buttons():
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, text="Customer Name") .grid(column=0,row=0,sticky=E)
    Label(main_window, text="Receipt Number") .grid(column=0,row=1,sticky=E)
    Button(main_window, text="Quit",command=quit,width = 10) .grid(column=4, row=0,sticky=E)
    Button(main_window, text="Print Details",command=print_shop_details,width = 10) .grid(column=4,row=1,sticky=E)
    Label(main_window, text="Item Hired") .grid(column=0,row=2,sticky=E)
    Label(main_window, text="Number Hired") .grid(column=0,row=3,sticky=E)
    Label(main_window, text="Row #") .grid(column=3,row=2,sticky=E)
    Label(main_window, text="               ") .grid(column=2,row=0)

#start the program running
def main():
    #Start the GUI it up
    main_window.title("Julies party pantry")
    setup_buttons()
    main_window.iconbitmap('favicon.ico')
    main_window.mainloop()
    
#create empty list for customer details and empty variable for entries in the list
counters = {'total_entries':0,'name_count':0}
shop_details = []    
main_window =Tk()    
entry_customer = Entry(main_window)
entry_customer.grid(column=1,row=0)
entry_receipt = Entry(main_window)
entry_receipt.grid(column=1,row=1)
entry_hired = Entry(main_window)
entry_hired.grid(column=1,row=2)
entry_number_hired = Entry(main_window)
entry_number_hired.grid(column=1,row=3)
delete_item = Entry(main_window)
delete_item .grid(column=3,row=3)    
main()
