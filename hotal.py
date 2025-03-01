from tkinter import *

from customer import cust_win
from Room import Roombooking
from Details import DetailsRoom

class HotalManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotal Management System")
        self.root.geometry("1200x800+0+0")

        #title
        lbl_title=Label(self.root,text="Hotal Management System" ,font=("times new roman",40,"bold"),bg="gray",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=10,width=1200,height=70)

        #main frame
        main_frame=Frame(self.root,bd=5,relief=RIDGE)
        main_frame.place(x=0,y=80,width=1200,height=620)

        #menu
        lbl_menu=Label(self.root,text="MENU" ,font=("times new roman",20,"bold"),bg="gray",fg="black",bd=4,relief=RIDGE)
        lbl_menu.place(x=6,y=90,width=200,height=40)

            #button frame
        button_frame=Frame(self.root,bd=4,relief=RIDGE)
        button_frame.place(x=6,y=135,width=200,height=280)

        cust_button=Button(button_frame,text="CUSTOMER",command=self.cust_details,font=("times new roman",20,"bold"),bg="gray",bd=0)
        cust_button.grid(row=0,column=0,padx=8,pady=2)

        room_button=Button(button_frame,text="ROOM",command=self.Roombooking,font=("times new roman",20,"bold"),bg="gray",bd=0)
        room_button.grid(row=2,column=0,padx=8 ,pady=2)

        details_button=Button(button_frame,text="DETAILS",command=self.Details_room,font=("times new roman",20,"bold"),bg="gray",bd=0)
        details_button.grid(row=4,column=0,padx=8,pady=2)

        report_button=Button(button_frame,text="REPORT",font=("times new roman",20,"bold"),bg="gray",bd=0)
        report_button.grid(row=6,column=0,padx=8,pady=2)

        logout_button=Button(button_frame,text="LOGOUT",command=self.logout,font=("times new roman",20,"bold"),bg="gray",bd=0)
        logout_button.grid(row=8,column=0,padx=8,pady=2)

#==========customer fun=========
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)

#===========Room fun===========
    def Roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)    

#===========Details fun===========
    def Details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)     


        #==========logout======
    def logout(self):
        self.root.destroy()




        


if __name__=="__main__":
    root=Tk()
    obj=HotalManagementSystem(root)
    root.mainloop()