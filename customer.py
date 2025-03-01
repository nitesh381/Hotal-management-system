from tkinter import *

from tkinter import ttk
import random
import mysql.connector 
from tkinter import messagebox


class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("CUSTOMER")
        self.root.geometry("985x600+210+115")

         #==========veriable=========
        self.var_ref=StringVar()
        x=random.randint(1000,10000)
        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()
        self.var_father=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()



           #title
        lbl_title=Label(self.root,text="Add Customer Detail" ,font=("times new roman",40,"bold"),bg="gray",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=10,y=0,width=950,height=50)

         #left frame
        cust_frame_left=Frame(self.root,bd=4,relief=RIDGE)
        cust_frame_left.place(x=10,y=50,width=400,height=500)

        #left frame title
        lbl_title_left=Label(cust_frame_left,text="Customer Detail" ,font=("times new roman",8,"bold"),fg="black",bd=4,relief=RIDGE)
        lbl_title_left.place(x=20,y=5)

        #label and entrys
        #ref 
        lbl_cust_ref=Label(cust_frame_left,text="Customer Ref",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.place(x=10,y=30)

        enter_ref=ttk.Entry(cust_frame_left,width=20,textvariable=self.var_ref,font=("times new roman",10,"bold"),state="readonly")
        enter_ref.place(x=150,y=35)

        # cust and name
        lbl_cust_name=Label(cust_frame_left,text="Customer Name",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_cust_name.place(x=10,y=60)

        enter_name=ttk.Entry(cust_frame_left,width=20,textvariable=self.var_cust_name,font=("times new roman",10,"bold"))
        enter_name.place(x=150,y=65)


        #father name
        lbl_cust_father_name=Label(cust_frame_left,text="Father Name",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_cust_father_name.place(x=10,y=90)

        enter_father_name=ttk.Entry(cust_frame_left,width=20,textvariable=self.var_father,font=("times new roman",10,"bold"))
        enter_father_name.place(x=150,y=95)

              #gender
        lbl_cust_gender=Label(cust_frame_left,text="Gender",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_cust_gender.place(x=10,y=120)

        combo_gender=ttk.Combobox(cust_frame_left,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=17,state="readonly")
        combo_gender["value"]=("male","female","other")
        combo_gender.current(0)
        combo_gender.place(x=150,y=125)







         # post code
        lbl_post_code=Label(cust_frame_left,text="Post Code",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_post_code.place(x=10,y=150)

        enter_post=ttk.Entry(cust_frame_left,width=20,textvariable=self.var_post,font=("times new roman",10,"bold"))
        enter_post.place(x=150,y=155)

        # mobile number
        lbl_mo_number=Label(cust_frame_left,text="Mobile Number",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_mo_number.place(x=10,y=180)

        enter_mo_number=ttk.Entry(cust_frame_left,textvariable=self.var_mobile,width=20,font=("times new roman",10,"bold"))
        enter_mo_number.place(x=150,y=185)

          # nationality
        lbl_nat=Label(cust_frame_left,text="Nationality",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_nat.place(x=10,y=210)


        
        combo_nat=ttk.Combobox(cust_frame_left,textvariable=self.var_nationality,font=("times new roman",10,"bold"),width=17,state="readonly")
        combo_nat["value"]=("India","USA","UK","Japan","other")
        combo_nat.current(0)
        combo_nat.place(x=150,y=215)

        


          # ID proof type
        lbl_Id_proof=Label(cust_frame_left,text="ID Proof Type",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_Id_proof.place(x=10,y=240)


        combo_id_proof=ttk.Combobox(cust_frame_left,textvariable=self.var_idproof,font=("times new roman",10,"bold"),width=17,state="readonly")
        combo_id_proof["value"]=("Adhar Card","Driving Licence","passport","other")
        combo_id_proof.current(0)
        combo_id_proof.place(x=150,y=245)




        #Id number
        lbl_id_number=Label(cust_frame_left,text="ID Number",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_id_number.place(x=10,y=270)

        enter_id_number=ttk.Entry(cust_frame_left,textvariable=self.var_idnumber,width=20,font=("times new roman",10,"bold"))
        enter_id_number.place(x=150,y=275)


        #address
        lbl_address=Label(cust_frame_left,text="Address",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_address.place(x=10,y=300)

        enter_add=ttk.Entry(cust_frame_left,width=20,textvariable=self.var_address,font=("times new roman",10,"bold"))
        enter_add.place(x=150,y=305)



        #==========button=========
        btn_frame=Frame(cust_frame_left,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=350,height=110,width=380)

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
        table_frame=LabelFrame(self.root,bd=5,relief=RIDGE,text="View Deatil and Search System",font=("arial",10,"bold"),padx=2)
        table_frame.place(x=420,y=50,width=540,height=530)

        lblsearchby=Label(table_frame,font=("arial",12,"bold"),text="Search By:",bg="gray",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_id_proof=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",11,"bold"),width=12,state="readonly")
        combo_id_proof["value"]=("Mobile","Ref")
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
        details_table.place(x=1,y=35,width=520,height=450)


        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,columns=("ref","name","father","gender","post","mobile","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
   
        self.cust_details_table.heading("ref",text="Ref No")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("father",text="Father")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("post",text="PostCode")
        self.cust_details_table.heading("mobile",text="Moblie No")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="Id proof")
        self.cust_details_table.heading("idnumber",text="Id Number")
        self.cust_details_table.heading("address",text="Address")

        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("father",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fatch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_father.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                            self.var_ref.get(),
                                            self.var_cust_name.get(),
                                            self.var_father.get(),
                                            self.var_gender.get(),
                                            self.var_post.get(),
                                            self.var_mobile.get(),
                                            self.var_nationality.get(),
                                            self.var_idproof.get(),
                                            self.var_idnumber.get(),
                                            self.var_address.get()
                ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
    
    
                messagebox.showwarning("warning",f"some thing want wrong:{str(es)}",parent=self.root)    

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()        

    def get_cuersor(self,event=""):
        cusrsor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cusrsor_row)
        row=content["values"]


        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1])
        self.var_father.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_nationality.set(row[6])
        self.var_idproof.set(row[7])
        self.var_idnumber.set(row[8])
        self.var_address.set(row[9])



        
    #=====================update================== 
    def update(self):
        if self.var_mobile=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Father=%s,Gender=%s,Postcode=%s,Mobile=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s ",(
                                            
                                            self.var_cust_name.get(),
                                            self.var_father.get(),
                                            self.var_gender.get(),
                                            self.var_post.get(),
                                            self.var_mobile.get(),
                                            self.var_nationality.get(),
                                            self.var_idproof.get(), 
                                            self.var_idnumber.get(),
                                            self.var_address.get(),
                                            self.var_ref.get()
                                        ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("upadat","customer details has been updated successfully",parent=self.root)



        #=====delete================

    def mdelete(self):
        mdelete=messagebox.askyesno("hotal management system","Do you want to delete this customer data",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return    
        conn.commit()
        self.fatch_data()  
        conn.close()  


     #==================reset===================
    def reset(self):
       # self.var_ref.set(""),
        self.var_cust_name.set("")
        self.var_father.set("")
        #self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        #self.var_nationality.set("")
        #self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_address.set("")


        x=random.randint(1000,10000)
        self.var_ref.set(str(x))

     #====================search=============
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="admin@8690930781",database="management")  
        my_cursor=conn.cursor()


        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()    






 



if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()

    