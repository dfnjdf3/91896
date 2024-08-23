#Author: Jai Irudayarjan
#Date: 17th May 2024
#Purpose: To make a Ui for sort out pary pantry information using the tkinter standerd

from tkinter import *
import tkinter as tk#Import tkinter for GUI components
from tkinter import messagebox#Import message box for error messages
from tkinter import ttk
import random#Import random for generating random numbers
from PIL import Image,ImageTk#Import PIL for image handling
import random
class JuilesApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Julie's Party Pantry")#Set title of window
        self.root.iconbitmap('favicon.ico')#Changes the defalt feather icon to custom icon
        self.details_list=[]#Initialize empty list to store details
        self.total_count=0#Initialize count of entries
        self.current_id=random.randint(100000,999999)#Generate random receipt ID
        self.setup_ui()#Call method to setup user interface
        self.root.geometry("1024x768")
    
    def setup_ui(self):
        #Set up the background image
        bg_image=Image.open('pic8.png')#Open background image file
        bg_image=bg_image.resize((self.root.winfo_screenwidth(),self.root.winfo_screenheight()))#Resize image to fit screen
        self.bg_photo=ImageTk.PhotoImage(bg_image)#Convert image to PhotoImage
        bg_label=tk.Label(self.root,image=self.bg_photo)#Create label to hold background image
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)#Place label at top left corner, stretch to fill window

        # Create and place entry widgets
        tk.Label(self.root,text="Customer Name", font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=0,row=0,sticky=tk.E)#Label for customer name
        tk.Label(self.root,text="Item Hired", font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=0,row=1,sticky=tk.E)#Label for item hired
        tk.Label(self.root,text="Quantity", font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=0,row=2,sticky=tk.E)#Label for quantity
        tk.Label(self.root,text="Row #", font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=2,row=2,sticky=tk.E)#Label for row number

        self.customer_entry=tk.Entry(self.root)#Entry widget for customer name
        self.customer_entry.grid(column=1,row=0)#Place entry widget
        self.hired_entry=tk.Entry(self.root)#Entry widget for item hired
        self.hired_entry.grid(column=1,row=1)#Place entry widget
        self.quantity_entry=ttk.Combobox(self.root,values=[str(i) for i in range(1, 501)]) 
        self.quantity_entry.grid(column=1,row=2)#Place entry widget
        self.quantity_entry.set("1")
        self.row_entry=tk.Entry(self.root)#Entry widget for row number
        self.row_entry.grid(column=2,row=3)#Place entry widget

        #Create and place buttons with images
        self.create_button("Append","pic1.png",self.validate_and_add, font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=2,row=1)
        self.create_button("Print","pic2.png", self.show_details, font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=3,row=1)
        self.create_button("Delete row","pic3.png", self.remove_row, font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=3,row=3)
        self.create_button("Quit","pic4.png",self.root.quit, font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=4,row=0)
        self.create_button("Save Info","pic9.png", self.save_to_file, font=("SpaceGrotesk-Bold",12,"bold", "italic")).grid(column=4,row=1) 


    def create_button(self, text,image_path,command, font=("Helveltica", 12)):
        image=Image.open(image_path)#Open image file
        image=image.resize((30, 30))
        photo=ImageTk.PhotoImage(image)
        button=tk.Button(self.root,text=text,image=photo,compound='left',command=command, font=font)
        button.photo=photo#Keep reference to image to prevent garbage collection
        return button#Return created button
     
    def validate_and_add(self):# creats a error control

        allowed_chars=set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")#make's sure if the customer only enters the alpha bets and space
        customer_name=self.customer_entry.get()#gets customer information
        item_hired=self.hired_entry.get()#gets item hired information
        quantity=self.quantity_entry.get()#gets how much the customer bought
        
        if not customer_name or not item_hired or not quantity:#check if customer name, item hired and quantity is filled in
            messagebox.showerror("Error", "Please fill in all fields")#shows message box if all entry fields are not entered
        elif not set(customer_name).issubset(allowed_chars) or not set(item_hired).issubset(allowed_chars):#makes sure that the customer only enters alpahabets and spaces
            messagebox.showerror("Error", "Enter a your name and item hired please")#shows if the customer entered special characters, numbers in special entery fields.
        elif not quantity.isdigit() or not 1<int(quantity)<500:#makes sure that customer enters a quantity between 1 and 500 if. If chosen as 1 gives a error or if chosen as 500 also gives an error
            messagebox.showerror("Error", "Quantity must be a number between 1 and 500")#Shows if the user choosed a number under 1(but can't) or 1 it self or if they choosed over 500(but can't) or 500 itself. This is because i made combobox
        else:
            self.add_entry()#Adds entries to the receipt
            self.clear_entries()#Deletes entries in the receipt
    
    def show_message(self, message):
        messagebox.showerror("Input Error",message)#Display error message in message box

    def add_entry(self):
        #Add new entry to details list
        self.details_list.append([
            self.customer_entry.get(),#Get customer name
            self.current_id,#Use current receipt ID
            self.hired_entry.get(),#Get item hired
            self.quantity_entry.get()#Get quantity
        ])
        self.save_to_file()#Save to file
        #Generate new random receipt ID
        self.current_id=random.randint(100000,999999)
        self.total_count+=1

    def save_to_file(self):
        #Save details list to file
        with open("details.txt","w") as file:
            for detail in self.details_list:
                file.write(f"Customer Name: {detail[0]}, Receipt Number: {detail[1]}, Item Hired: {detail[2]}, Quantity: {detail[3]}\n")
        print("Data has been saved successfully")

    def clear_entries(self):
        # Clear all entry fields
        self.customer_entry.delete(0,'end')#Clear customer name entry
        self.hired_entry.delete(0,'end')#Clear item hired entry
        self.quantity_entry.set("1")#Reset quantity entry to default value

    def show_details(self):
        #Display all details in the GUI
        for widget in self.root.grid_slaves():#Iterate over all widgets in grid
            if int(widget.grid_info()["row"])>7:#Check if widget is in rows greater than 7
                widget.grid_forget()#Hide widget
        
        Font_header=("SpaceGrotesk-Bold",12,"bold", "italic")
        #Create and place headers for details table
        tk.Label(self.root,text="Row",font=Font_header).grid(column=0,row=7)
        tk.Label(self.root,text="Customer Name",font=Font_header).grid(column=1,row=7)
        tk.Label(self.root,text="Receipt Number",font=Font_header).grid(column=2,row=7)
        tk.Label(self.root,text="Item Hired",font=Font_header).grid(column=3,row=7)
        tk.Label(self.root,text="Quantity",font=Font_header).grid(column=4,row=7)

        #Display each detail in the list
        detail_font=("SpaceGrotesk-Bold",12,"bold")
        for i,detail in enumerate(self.details_list):
            tk.Label(self.root,text=i,font=detail_font).grid(column=0,row=i+8)  # Display row number
            tk.Label(self.root,text=detail[0],font=detail_font).grid(column=1,row=i+8)#Display customer name
            tk.Label(self.root,text=detail[1],font=detail_font).grid(column=2,row=i+8)#Display receipt number
            tk.Label(self.root,text=detail[2],font=detail_font).grid(column=3,row=i+8)#Display item hired
            tk.Label(self.root,text=detail[3],font=detail_font).grid(column=4,row=i+8)#Display quantity

    def remove_row(self):
        #Remove row based on row number provided
        try:
            index=int(self.row_entry.get())#Get index from entry field
            if 0<=index<self.total_count:#Check if index is valid
                del self.details_list[index]#Delete entry at given index
                self.total_count-=1#Decrement total count
                self.save_to_file()#Save updated list to file
                self.show_details()#Update details display
            else:
                self.show_message("Invalid Row Number")#Show error message if index out of range
        except ValueError:
            self.show_message("Invalid Row Number")# Show error message if input not a number

if __name__=="__main__":
    root=tk.Tk()# Create the main window
    app=JuilesApp(root)# Instantiate JuilesApp class
    root.mainloop()# Run the application
