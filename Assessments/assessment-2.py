"""class hotelmanage:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',address='',cindate='',coutdate='',rno=1):

        print ("\n\n*****WELCOME TO HOTEl KING*****\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your Fullname:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")
        
    def roomrent(self):#sel1353

        print ("We have the following rooms for you:-")

        print ("1.  Class A---->4000")

        print ("2.  Class B---->3000")

        print ("3.  Class C---->2000")

        print ("4.  Class D---->1000")

        x=int(input("Enter the number of your choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("you have choose room Class A")

            self.s=4000*n

        elif (x==2):

            print ("you have choose room Class B")

            self.s=3000*n

        elif (x==3):

            print ("you have choose room Class C")

            self.s=2000*n

        elif (x==4):
            print ("you have choose room Class D")

            self.s=1000*n

        else:

            print ("please choose a room")

        print ("your choosen room rent is =",self.s,"\n")

    def foodpurchased(self):

        print("*****RESTAURANT MENU*****")

        print("1.Dessert----->100","2.Drinks----->50","3.Breakfast--->90","4.Lunch---->110","5.Dinner--->150","6.Exit")


        while (1):

            c=int(input("Enter the number of your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+100*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break
            else:
                print("You've Enter an Invalid Key")

        print ("Total food Cost=Rs",self.r,"\n")



    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total Purchased is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal Purchased is:",self.rt+self.a,"\n")
        self.rno+=1
    

def main():

    a=hotelmanage()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate Room Rent")

        print("3.Calculate Food Purchased")

        print("4.Show total cost")

        print("5.EXIT")

        b=int(input("\nEnter the number of your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.foodpurchased()

        if (b==4):

            a.display()

        if (b==5):

            quit()


main()"""





"""import tkinter as tk
from tkinter import messagebox

class HotelManage:
    def __init__(self, master):
        self.master = master
        master.title("Hotel King Management System")

        self.rt = 0
        self.s = 0
        self.p = 0
        self.r = 0
        self.t = 0
        self.a = 1000
        self.name = ''
        self.address = ''
        self.cindate = ''
        self.coutdate = ''
        self.rno = 1

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="*****WELCOME TO HOTEL KING*****").grid(row=0, columnspan=2)

        tk.Label(self.master, text="Customer Name:").grid(row=1)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Address:").grid(row=2)
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=2, column=1)

        tk.Label(self.master, text="Check-in Date:").grid(row=3)
        self.cindate_entry = tk.Entry(self.master)
        self.cindate_entry.grid(row=3, column=1)

        tk.Label(self.master, text="Check-out Date:").grid(row=4)
        self.coutdate_entry = tk.Entry(self.master)
        self.coutdate_entry.grid(row=4, column=1)

        tk.Button(self.master, text='Enter Customer Data', command=self.inputdata).grid(row=5, columnspan=2)

        tk.Button(self.master, text='Calculate Room Rent', command=self.roomrent).grid(row=6, columnspan=2)
        
        tk.Button(self.master, text='Calculate Food Purchased', command=self.foodpurchased).grid(row=7, columnspan=2)
        
        tk.Button(self.master, text='Show Total Cost', command=self.display).grid(row=8, columnspan=2)
        
        tk.Button(self.master, text='EXIT', command=self.master.quit).grid(row=9, columnspan=2)

    def inputdata(self):
        self.name = self.name_entry.get()
        self.address = self.address_entry.get()
        self.cindate = self.cindate_entry.get()
        self.coutdate = self.coutdate_entry.get()
        messagebox.showinfo("Info", f"Your room no.: {self.rno}\n")

    def roomrent(self):
        room_types = ["Class A---->4000", "Class B---->3000", "Class C---->2000", "Class D---->1000"]
        room_costs = [4000, 3000, 2000, 1000]

        def calculate_rent():
            try:
                x = int(room_choice.get())
                n = int(nights_entry.get())
                if 1 <= x <= 4:
                    self.s = room_costs[x - 1] * n
                    messagebox.showinfo("Info", f"You have chosen {room_types[x - 1]}\nYour chosen room rent is = {self.s}\n")
                else:
                    messagebox.showwarning("Warning", "Please choose a valid room type")
            except ValueError:
                messagebox.showwarning("Warning", "Invalid input, please enter a number")

        rent_window = tk.Toplevel(self.master)
        rent_window.title("Calculate Room Rent")

        tk.Label(rent_window, text="We have the following rooms for you:").pack()
        for i, room in enumerate(room_types):
            tk.Label(rent_window, text=f"{i + 1}.  {room}").pack()

        tk.Label(rent_window, text="Enter the number of your choice:").pack()
        room_choice = tk.Entry(rent_window)
        room_choice.pack()

        tk.Label(rent_window, text="For How Many Nights Did You Stay:").pack()
        nights_entry = tk.Entry(rent_window)
        nights_entry.pack()

        tk.Button(rent_window, text='Calculate', command=calculate_rent).pack()

    def foodpurchased(self):
        food_items = ["Dessert----->100", "Drinks----->50", "Breakfast--->90", "Lunch---->110", "Dinner--->150"]
        food_costs = [100, 50, 90, 110, 150]

        def add_food():
            try:
                c = int(food_choice.get())
                d = int(quantity_entry.get())
                if 1 <= c <= 5:
                    self.r += food_costs[c - 1] * d
                    messagebox.showinfo("Info", f"Added {d} of {food_items[c - 1]} to your bill.\nTotal food cost = Rs {self.r}\n")
                elif c == 6:
                    food_window.destroy()
                else:
                    messagebox.showwarning("Warning", "Invalid choice, please enter a number between 1 and 6.")
            except ValueError:
                messagebox.showwarning("Warning", "Invalid input, please enter a number")

        food_window = tk.Toplevel(self.master)
        food_window.title("Calculate Food Purchased")

        tk.Label(food_window, text="*****RESTAURANT MENU*****").pack()
        for i, item in enumerate(food_items):
            tk.Label(food_window, text=f"{i + 1}.  {item}").pack()

        tk.Label(food_window, text="Enter the number of your choice:").pack()
        food_choice = tk.Entry(food_window)
        food_choice.pack()

        tk.Label(food_window, text="Enter the quantity:").pack()
        quantity_entry = tk.Entry(food_window)
        quantity_entry.pack()

        tk.Button(food_window, text='Add', command=add_food).pack()

    def display(self):
        self.rt = self.s + self.t + self.p + self.r
        bill_text = (
            f"******HOTEL BILL******\n"
            f"Customer details:\n"
            f"Customer name: {self.name}\n"
            f"Customer address: {self.address}\n"
            f"Check-in date: {self.cindate}\n"
            f"Check-out date: {self.coutdate}\n"
            f"Room no.: {self.rno}\n"
            f"Your Room rent is: {self.s}\n"
            f"Your Food bill is: {self.r}\n"
            f"Your sub total is: {self.rt}\n"
            f"Additional service charges: {self.a}\n"
            f"Your grand total is: {self.rt + self.a}\n"
        )
        messagebox.showinfo("Hotel Bill", bill_text)
        self.rno += 1

def main():
    root = tk.Tk()
    hotel = HotelManage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
"""


import tkinter as tk
from tkinter import messagebox
import mysql.connector

class HotelManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Hotel Management System")
        self.master.geometry("500x400")

        self.rt = 0
        self.s = 0
        self.p = 0
        self.r = 0
        self.t = 0
        self.a = 1000
        self.rno = 1

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.master, text="Hotel Management System", font=("Arial", 24)).pack()

        # Customer Information
        tk.Label(self.master, text="Customer Information").pack()
        tk.Label(self.master, text="Name:").pack()
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack()

        tk.Label(self.master, text="Address:").pack()
        self.address_entry = tk.Entry(self.master)
        self.address_entry.pack()

        tk.Label(self.master, text="Check-in Date:").pack()
        self.cindate_entry = tk.Entry(self.master)
        self.cindate_entry.pack()

        tk.Label(self.master, text="Check-out Date:").pack()
        self.coutdate_entry = tk.Entry(self.master)
        self.coutdate_entry.pack()

        tk.Button(self.master, text="Enter Customer Data", command=self.inputdata).pack()

        # Room Rent
        tk.Button(self.master, text="Calculate Room Rent", command=self.roomrent).pack()

        # Food Purchased
        tk.Button(self.master, text="Calculate Food Purchased", command=self.foodpurchased).pack()

        # Show Total Cost
        tk.Button(self.master, text="Show Total Cost", command=self.display).pack()

    def inputdata(self):
        self.name = self.name_entry.get()
        self.address = self.address_entry.get()
        self.cindate = self.cindate_entry.get()
        self.coutdate = self.coutdate_entry.get()

        if not self.name or not self.address or not self.cindate or not self.coutdate:
            messagebox.showerror("Input Error", "Please fill all fields")
            return

        messagebox.showinfo("Success", f"Customer Data Entered:\nName: {self.name}\nAddress: {self.address}\nCheck-in Date: {self.cindate}\nCheck-out Date: {self.coutdate}")

    def roomrent(self):
        rent_window = tk.Toplevel(self.master)
        rent_window.title("Room Rent")
        rent_window.geometry("300x200")

        tk.Label(rent_window, text="We have the following rooms for you:").pack()
        tk.Label(rent_window, text="1. Class A---->4000").pack()
        tk.Label(rent_window, text="2. Class B---->3000").pack()
        tk.Label(rent_window, text="3. Class C---->2000").pack()
        tk.Label(rent_window, text="4. Class D---->1000").pack()

        tk.Label(rent_window, text="Enter the number of your choice:").pack()
        self.room_choice = tk.Entry(rent_window)
        self.room_choice.pack()

        tk.Label(rent_window, text="For How Many Nights Did You Stay:").pack()
        self.nights_stayed = tk.Entry(rent_window)
        self.nights_stayed.pack()

        tk.Button(rent_window, text="Submit", command=self.calculate_rent).pack()

    def calculate_rent(self):
        x = int(self.room_choice.get())
        n = int(self.nights_stayed.get())

        if x == 1:
            self.s = 4000 * n
        elif x == 2:
            self.s = 3000 * n
        elif x == 3:
            self.s = 2000 * n
        elif x == 4:
            self.s = 1000 * n
        else:
            messagebox.showerror("Input Error", "Please choose a valid room")

        messagebox.showinfo("Room Rent", f"Your chosen room rent is: {self.s}")

    def foodpurchased(self):
        food_window = tk.Toplevel(self.master)
        food_window.title("Food Purchased")
        food_window.geometry("300x300")

        tk.Label(food_window, text="*****RESTAURANT MENU*****").pack()
        tk.Label(food_window, text="1. Dessert----->100").pack()
        tk.Label(food_window, text="2. Drinks----->50").pack()
        tk.Label(food_window, text="3. Breakfast--->90").pack()
        tk.Label(food_window, text="4. Lunch---->110").pack()
        tk.Label(food_window, text="5. Dinner--->150").pack()
        tk.Label(food_window, text="6. Exit").pack()


        tk.Label(food_window, text="Enter the number of your choice:").pack()
        self.food_choice_entry = tk.Entry(food_window)
        self.food_choice_entry.pack()

        tk.Label(food_window, text="Enter the quantity:").pack()
        self.food_quantity_entry = tk.Entry(food_window)
        self.food_quantity_entry.pack()

        tk.Button(food_window, text="Add", command=self.add_food).pack()
        tk.Button(food_window, text="Finish", command=food_window.destroy).pack()

    def add_food(self):
        c = int(self.food_choice_entry.get())
        d = int(self.food_quantity_entry.get())

        if c == 1:
            self.r += 100 * d
        elif c == 2:
            self.r += 50 * d
        elif c == 3:
            self.r += 90 * d
        elif c == 4:
            self.r += 110 * d
        elif c == 5:
            self.r += 150 * d
        else:
            messagebox.showerror("Input Error", "Invalid food choice")

        messagebox.showinfo("Food Purchased", f"Total food cost so far: {self.r}")

    def display(self):
        self.rt = self.s + self.t + self.p + self.r
        grand_total = self.rt + self.a

        bill = (
            f"******HOTEL BILL******\n"
            f"Customer details:\n"
            f"Customer name: {self.name}\n"
            f"Customer address: {self.address}\n"
            f"Check in date: {self.cindate}\n"
            f"Check out date: {self.coutdate}\n"
            f"Room no.: {self.rno}\n"
            f"Your Room rent is: {self.s}\n"
            f"Your Food bill is: {self.r}\n"
            f"Your sub total Purchased is: {self.rt}\n"
            f"Additional Service Charges is: {self.a}\n"
            f"Your grandtotal Purchased is: {grand_total}\n"
        )

        messagebox.showinfo("Bill", bill)
        self.rno += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagement(master=root)
    root.mainloop()
