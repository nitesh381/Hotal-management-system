from tkinter import *

from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector 
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Room booking")
        self.root.geometry("985x600+210+115")


        #=============varible============
        self.var_Contact=StringVar()
        self.var_Checkin=StringVar()
        self.var_Checkout=StringVar()
        self.var_Roomtype=StringVar()
        self.var_RoomAvailable=StringVar()
        self.var_Meal=StringVar()
        self.var_No_of_day=StringVar()
        self.var_Paidtax=StringVar()
        self.var_Sub_total=StringVar()
        self.var_Total_cost=StringVar()
        

        #============title=========================
        lbl_title=Label(self.root,text="Roombooking Detail" ,font=("times new roman",40,"bold"),bg="gray",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=10,y=0,width=950,height=55)

        #===========left frame====
        left_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="Roombookig Detail" ,font=("times new roman",10,"bold"),fg="black")
        left_frame.place(x=10,y=55,width=400,height=500)

        #==========label and entrys=========

         #contact
        
        lbl_cust_contact=Label(left_frame,text="Customer Contact",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_cust_contact.place(x=10,y=5)

        enter_cont=ttk.Entry(left_frame,width=10,textvariable=self.var_Contact,font=("times new roman",10,"bold"))
        enter_cont.place(x=150,y=10)

        #button for fetch
        btn_fetch=Button(left_frame,text="Fetch Data",command=self.Fetch_contact,font=("arial",8,"bold"),bg="gray",fg="white",width=8)
        btn_fetch.place(x=232,y=8)


        
        # cust check in data
        lbl_cust_name=Label(left_frame,text="Check in date",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_cust_name.place(x=10,y=30)

        enter_in_date=ttk.Entry(left_frame,width=20,textvariable=self.var_Checkin,font=("times new roman",10,"bold"))
        enter_in_date.place(x=150,y=35)

        # cust check out data
        lbl_out_date=Label(left_frame,text="Check out date",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_out_date.place(x=10,y=55)

        enter_out_date=ttk.Entry(left_frame,width=20,textvariable=self.var_Checkout,font=("times new roman",10,"bold"))
        enter_out_date.place(x=150,y=60)

             #room type
        lbl_type=Label(left_frame,text="Room type",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_type.place(x=10,y=80)

        conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
        my_cursor=conn.cursor()
        my_cursor.execute("select room_type from details")
        rows1=my_cursor.fetchall()

        

        combo_gender=ttk.Combobox(left_frame,textvariable=self.var_Roomtype,font=("times new roman",10,"bold"),width=17,state="readonly")
        combo_gender["value"]=rows1
        combo_gender.current(0)
        combo_gender.place(x=150,y=85)


        # room available
        lbl_available=Label(left_frame,text="Avialable",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_available.place(x=10,y=105)

        # enter_available=ttk.Entry(left_frame,width=20,textvariable=self.var_RoomAvailable,font=("times new roman",10,"bold"))
        # enter_available.place(x=150,y=110)
        conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
        my_cursor=conn.cursor()
        my_cursor.execute("select room_no from details")
        rows=my_cursor.fetchall()
        
        combo_room_no=ttk.Combobox(left_frame,textvariable=self.var_RoomAvailable,font=("times new roman",10,"bold"),width=17,state="readonly")
        combo_room_no["value"]=rows
        combo_room_no.current(0)
        combo_room_no.place(x=150,y=110)


        # meal
        lbl_meal=Label(left_frame,text="Meal",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_meal.place(x=10,y=130)

        enter_meal=ttk.Entry(left_frame,width=20,textvariable=self.var_Meal,font=("times new roman",10,"bold"))
        enter_meal.place(x=150,y=135)

        # number of day
        lbl_of_day=Label(left_frame,text="No of day",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_of_day.place(x=10,y=155)

        enter_of_day=ttk.Entry(left_frame,width=20,textvariable=self.var_No_of_day,font=("times new roman",10,"bold"))
        enter_of_day.place(x=150,y=160)

        # paid tax
        lbl_paid_tax=Label(left_frame,text="Paid Tax",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_paid_tax.place(x=10,y=180)

        enter_Paid_tax=ttk.Entry(left_frame,width=20,textvariable=self.var_Paidtax,font=("times new roman",10,"bold"))
        enter_Paid_tax.place(x=150,y=185)

        # sub total
        lbl_sub_tol=Label(left_frame,text="Sub Total",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_sub_tol.place(x=10,y=205)

        enter_sub_tol=ttk.Entry(left_frame,width=20,textvariable=self.var_Sub_total,font=("times new roman",10,"bold"))
        enter_sub_tol.place(x=150,y=210)

        # total cost
        lbl_total_cost=Label(left_frame,text="Total Cost",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_total_cost.place(x=10,y=230)

        enter_tol_cost=ttk.Entry(left_frame,width=20,textvariable=self.var_Total_cost,font=("times new roman",10,"bold"))
        enter_tol_cost.place(x=150,y=235)

        #============button Bill====================
        btn_bil=Button(left_frame,text="Bill",command=self.total,font=("arial",11,"bold"),bg="gray",fg="white",width=6)
        btn_bil.place(x=10,y=255)

        #==========button=========
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=300,height=110,width=380)

        #button Add
        btn_Add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="gray",fg="white",width=10)
        btn_Add.grid(row=0,column=0,padx=30,pady=10)

        #button update
        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="gray",fg="white",width=10)
        btn_update.grid(row=0,column=1,padx=30,pady=10)

        #button Delete
        btn_delete=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",11,"bold"),bg="gray",fg="white",width=10)
        btn_delete.grid(row=1,column=0,padx=30,pady=10)

        #button Reset
        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="gray",fg="white",width=10)
        btn_reset.grid(row=1,column=1,padx=30,pady=10)


        #=============table frame=======
        table_frame=LabelFrame(self.root,bd=5,relief=RIDGE,text="View Detials and Search System",font=("arial",10,"bold"),padx=2)
        table_frame.place(x=420,y=250,width=540,height=330)

        lblsearchby=Label(table_frame,font=("arial",12,"bold"),text="Search By:",bg="gray",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_id_proof=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",11,"bold"),width=12,state="readonly")
        combo_id_proof["value"]=("Contact","roomavailable")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=0,column=1 ,padx=2)

        self.txt_search=StringVar()
        textSearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",11,"bold"),width=15)
        textSearch.grid(row=0,column=2,padx=2)

        btn_Search=Button(table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="gray",fg="white",width=8)
        btn_Search.grid(row=0,column=3,padx=2)

        btn_Show_all=Button(table_frame,text="Show all",command=self.fatch_data,font=("arial",11,"bold"),bg="gray",fg="white",width=8)
        btn_Show_all.grid(row=0,column=4,padx=2)


        #show data table

        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=1,y=35,width=520,height=260)


        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("Contact","Checkin","Checkout","Roomtype","RoomAvailable","Meal","No_of_day"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
   
        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("Checkin",text="Checkin")
        self.room_table.heading("Checkout",text="Checkout")
        self.room_table.heading("Roomtype",text="Roomtype")
        self.room_table.heading("RoomAvailable",text="RoomAvailable")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("No_of_day",text="No_of_day")
      
        

        self.room_table["show"]="headings"
        self.room_table.column("Contact",width=100)
        self.room_table.column("Checkin",width=100)
        self.room_table.column("Checkout",width=100)
        self.room_table.column("Roomtype",width=100)
        self.room_table.column("RoomAvailable",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("No_of_day",width=100)

        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fatch_data()



        #=============add data=============


    def add_data(self):
        if self.var_Contact.get()=="" or self.var_Checkin.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_Contact.get(),
                                                                self.var_Checkin.get(),
                                                                self.var_Checkout.get(),
                                                                self.var_Roomtype.get(),
                                                                self.var_RoomAvailable.get(),
                                                                self.var_Meal.get(),
                                                                self.var_No_of_day.get()
                                                                
                                                            
                ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("success","room booked",parent=self.root)
            except Exception as es:
    
    
                messagebox.showwarning("warning",f"some thing want wrong:{str(es)}",parent=self.root)        

     #=======fetch data===
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

#===============get cuersor======

    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]


        self.var_Contact.set(row[0]),
        self.var_Checkin.set(row[1])
        self.var_Checkout.set(row[2])
        self.var_Roomtype.set(row[3])
        self.var_RoomAvailable.set(row[4])
        self.var_Meal.set(row[5])
        self.var_No_of_day.set(row[6])

 #=====================update================== 
    def update(self):
        if self.var_Contact=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
            my_cursor=conn.cursor()
            my_cursor.execute("update room set contact=%s,check_in=%s,check_out=%s,roomtype=%s,meal=%s,no_of_days=%s where roomavailable=%s",(
                                            
                                            self.var_Contact.get(),
                                            self.var_Checkin.get(),
                                            self.var_Checkout.get(),
                                            self.var_Roomtype.get(),
                                            self.var_Meal.get(),
                                            self.var_No_of_day.get(),
                                            self.var_RoomAvailable.get(),
                                        ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("upadat","Room details has been updated successfully",parent=self.root)    
        
 #=====delete================

    def mdelete(self):
        mdelete=messagebox.askyesno("hotal management system","Do you want to delete this room data",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_Contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return    
        conn.commit()
        self.fatch_data()  
        conn.close()  

  #==================reset===================
    def reset(self): 
        self.var_Contact.set(""),
        self.var_Checkin.set("")
        self.var_Checkout.set("")
        #self.var_Roomtype.set("")
        self.var_RoomAvailable.set("")
        self.var_Meal.set("")
        self.var_No_of_day.set("")
        self.var_Paidtax.set("")
        self.var_Sub_total.set("")
        self.var_Total_cost.set("")



     #===========================all data fetch============

    def Fetch_contact(self):
        if self.var_Contact.get()=="":
            messagebox.showerror("Error","please Enter Contact Number ",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
            my_cursor=conn.cursor()   
            query=("select Name from customer where Mobile=%s")
            value=(self.var_Contact.get(),)
            my_cursor.execute(query,value) 
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)
            else:
                conn.commit()
                conn.close()


                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=440,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold")) 
                lblName.place(x=0,y=0)


                lbl=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                lbl.place(x=90,y=0)
                
     #==========father===========
                conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
                my_cursor=conn.cursor()   
                query=("select Father from customer where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()

                lblfather=Label(showDataframe,text="father:",font=("arial",12,"bold")) 
                lblfather.place(x=0,y=30)


                lbl1=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                lbl1.place(x=90,y=30)

      #==================gender===============
                conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
                my_cursor=conn.cursor()   
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()

                lblgender=Label(showDataframe,text="Gander:",font=("arial",12,"bold")) 
                lblgender.place(x=0,y=60)


                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                lbl2.place(x=90,y=60)

     #=================nationality============
                conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
                my_cursor=conn.cursor()   
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()

                lblnat=Label(showDataframe,text="Nationality:",font=("arial",12,"bold")) 
                lblnat.place(x=0,y=90)


                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                lbl3.place(x=90,y=90)

    #===================address=========
                conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
                my_cursor=conn.cursor()   
                query=("select Address from customer where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold")) 
                lblAddress.place(x=0,y=120)


                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                lbl4.place(x=90,y=120)

    #==============Search system=================== 

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
        my_cursor=conn.cursor()


        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()          


    #=================total==========
    def total(self):
        inDate=self.var_Checkin.get()     
        outDate=self.var_Checkout.get() 
        inDate=datetime.strptime(inDate,"%d/%m/%Y")     
        outDate=datetime.strptime(outDate,"%d/%m/%Y") 
        self.var_No_of_day.set(abs(outDate-inDate).days)   

        if (self.var_Meal.get()=="breakfast" and self.var_Roomtype.get()=="Single Room"):
            q1=float(300)   
            q2=float(500)
            q3=float(self.var_No_of_day.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%(q5))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_Paidtax.set(Tax)
            self.var_Sub_total.set(ST)
            self.var_Total_cost.set(TT)

        elif (self.var_Meal.get()=="launch" and self.var_Roomtype.get()=="Family Room"):
            q1=float(300)   
            q2=float(900)
            q3=float(self.var_No_of_day.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%(q5))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_Paidtax.set(Tax)
            self.var_Sub_total.set(ST)
            self.var_Total_cost.set(TT)


        elif (self.var_Meal.get()=="breakfast" and self.var_Roomtype.get()=="Family Room"):
            q1=float(300)   
            q2=float(110)
            q3=float(self.var_No_of_day.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%(q5))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_Paidtax.set(Tax)
            self.var_Sub_total.set(ST)
            self.var_Total_cost.set(TT)    
    






        
        


if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
