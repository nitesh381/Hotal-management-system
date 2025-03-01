from tkinter import *

from tkinter import ttk
import mysql.connector 
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Details")
        self.root.geometry("985x600+210+115")


    #============title=========================
        lbl_title=Label(self.root,text="Rooms Details" ,font=("times new roman",40,"bold"),bg="gray",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=10,y=0,width=950,height=55)

    #===========left frame====
        left_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="New Rooms Add" ,font=("times new roman",10,"bold"),fg="black")
        left_frame.place(x=10,y=55,width=450,height=400) 

         #==========label and entrys=========

         #floor
        
        lbl_floor=Label(left_frame,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.place(x=10,y=5)

        self.var_floor=StringVar()
        enter_floor=ttk.Entry(left_frame,textvariable=self.var_floor,width=20,font=("times new roman",12,"bold"))
        enter_floor.place(x=100,y=10)      

        
         #Room No
        
        lbl_room_no=Label(left_frame,text="Room no",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_room_no.place(x=10,y=35)

        self.var_room_no=StringVar()
        enter_room_no=ttk.Entry(left_frame,textvariable=self.var_room_no,width=20,font=("times new roman",12,"bold"))
        enter_room_no.place(x=100,y=40) 

        
         #Room type
        
        lbl_room_type=Label(left_frame,text="Room type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_room_type.place(x=10,y=65)

        self.var_room_type=StringVar()
        enter_room_ty=ttk.Entry(left_frame,textvariable=self.var_room_type,width=20,font=("times new roman",12,"bold"))
        enter_room_ty.place(x=100,y=70) 

        #==========button=========
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=150,height=110,width=380)

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
        table_frame=LabelFrame(self.root,bd=5,relief=RIDGE,text="Show Room Details System",font=("arial",10,"bold"),padx=2)
        table_frame.place(x=460,y=55,width=500,height=400)   

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(table_frame,columns=("floor","room_no","room_type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="floor")
        self.room_table.heading("room_no",text="room_no")
        self.room_table.heading("room_type",text="room_type")
      
      
        
        self.room_table["show"]="headings"
        self.room_table.column("floor",width=100)
        self.room_table.column("room_no",width=100)
        self.room_table.column("room_type",width=100)
       

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fatch_data()

        #=============add data=============


    def add_data(self):
        if self.var_floor.get()=="" or self.var_room_type.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                self.var_floor.get(),
                                                                self.var_room_no.get(),
                                                                self.var_room_type.get(),
                                                                
                                                                
                                                            
                ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("success","New room add successfully",parent=self.root)
            except Exception as es:
    
    
                messagebox.showwarning("warning",f"some thing want wrong:{str(es)}",parent=self.root)        
    
    
    #=======fetch data===
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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


        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1])
        self.var_room_type.set(row[2])


#=====================update================== 
    def update(self):
        if self.var_room_no=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,room_type=%s where room_no=%s",(
                                            
                                            self.var_floor.get(),
                                            self.var_room_type.get(),
                                            self.var_room_no.get(),
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
            query="delete from details where room_no=%s"
            value=(self.var_room_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return    
        conn.commit()
        self.fatch_data()  
        conn.close()  

  #==================reset===================
    def reset(self): 
        self.var_floor.set(""),
        self.var_room_no.set("")
        self.var_room_type.set("")
       


if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
