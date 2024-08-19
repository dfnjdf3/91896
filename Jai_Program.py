import tkinter as tk#Import tkinter for GUI components
from tkinter import messagebox#Import message box for error messages
from tkinter import ttk
import random#Import random for generating random numbers
from PIL import Image,ImageTk#Import PIL for image handling

class JuilesApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Julie's Party Pantry")#Set title of window
        self.root.iconbitmap('favicon.ico')
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
        tk.Label(self.root,text="Customer Name").grid(column=0,row=0,sticky=tk.E)#Label for customer name
        tk.Label(self.root,text="Item Hired").grid(column=0,row=1,sticky=tk.E)#Label for item hired
        tk.Label(self.root,text="Quantity").grid(column=0,row=2,sticky=tk.E)#Label for quantity
        tk.Label(self.root,text="Row #").grid(column=2,row=2,sticky=tk.E)#Label for row number

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
        self.create_button("Append","pic1.png", self.validate_and_add).grid(column=2,row=1)
        self.create_button("Print","pic2.png", self.show_details).grid(column=3,row=1)
        self.create_button("Delete","pic3.png", self.remove_row).grid(column=3,row=3)
        self.create_button("Quit","pic4.png", self.root.quit).grid(column=4,row=0)
        self.create_button("Save Info","pic9.png", self.save_to_file).grid(column=4,row=1) 


    def create_button(self, text,image_path,command):
        image=Image.open(image_path)#Open image file
        image=image.resize((30, 30))
        photo=ImageTk.PhotoImage(image)
        button=tk.Button(self.root,text=text,image=photo,compound='left',command=command)
        button.photo=photo#Keep reference to image to prevent garbage collection
        return button#Return created button

    def validate_and_add(self):
        #Validate input and add details if valid
        if not self.customer_entry.get().isalpha():#Check if customer name is alphabetic
            self.show_message("Customer Name must be letters only")#Show error message
        elif not self.hired_entry.get().isalpha():#Check if item hired is alphabetic
            self.show_message("Item Hired must be letters only")#Display error message
        elif not self.quantity_entry.get().isdigit() or not 1<= int(self.quantity_entry.get())<= 500:#Check if quantity is number between 1 and 500
            self.show_message("Quantity must be between 1 and 500")#Show error message
        else:
            self.add_entry()#Add entry to the list
            self.clear_entries()#Clear input fields
    
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

        #Create and place headers for details table
        tk.Label(self.root,text="Row",font=("Helvetica",10,"bold")).grid(column=0,row=7)
        tk.Label(self.root,text="Customer Name",font=("Helvetica",10,"bold")).grid(column=1,row=7)
        tk.Label(self.root,text="Receipt Number",font=("Helvetica",10,"bold")).grid(column=2,row=7)
        tk.Label(self.root,text="Item Hired",font=("Helvetica",10,"bold")).grid(column=3,row=7)
        tk.Label(self.root,text="Quantity",font=("Helvetica",10,"bold")).grid(column=4,row=7)

        #Display each detail in the list
        for i,detail in enumerate(self.details_list):
            tk.Label(self.root,text=i).grid(column=0,row=i+8)  # Display row number
            tk.Label(self.root,text=detail[0]).grid(column=1,row=i+8)#Display customer name
            tk.Label(self.root,text=detail[1]).grid(column=2,row=i+8)#Display receipt number
            tk.Label(self.root,text=detail[2]).grid(column=3,row=i+8)#Display item hired
            tk.Label(self.root,text=detail[3]).grid(column=4,row=i+8)#Display quantity

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
