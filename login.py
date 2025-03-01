from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from hotal import HotalManagementSystem

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("600x550+350+100")

           #main frame
        main_frame=Frame(self.root,bd=5,relief=RIDGE)
        main_frame.place(x=100,y=80,width=400,height=400)

        
    #============title=========================
        lbl_title=Label(main_frame,text="Get Started" ,font=("times new roman",20,"bold"),bg="gray",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=100,y=0,width=200,height=40)


        #====lable user_name=======
        lbl_title=Label(main_frame,text="Username" ,font=("times new roman",15,"bold"),bg="gray",fg="black")
        lbl_title.place(x=40,y=100,width=100,height=20)

        self.enter_txt=ttk.Entry(main_frame,width=20,font=("times new roman",12,"bold"))
        self.enter_txt.place(x=40,y=125) 


        
        #====lable password=======
        lbl_title=Label(main_frame,text="Password" ,font=("times new roman",15,"bold"),bg="gray",fg="black")
        lbl_title.place(x=40,y=180,width=100,height=20)

        
        self.enter_pass=ttk.Entry(main_frame,width=20,font=("times new roman",12,"bold"))
        self.enter_pass.place(x=40,y=205)

         #button login
        btn_login=Button(main_frame,text="Login",command=self.login_1,font=("arial",11,"bold"),bg="lightblue",fg="black",width=10)
        btn_login.place(x=60,y=240)

        #------------------or--------------
        lbl_title=Label(main_frame,text="Or" ,font=("times new roman",8,"bold"),fg="black")
        lbl_title.place(x=100,y=280,width=20,height=15)

            #register button
        btn_reg=Button(main_frame,text="Register",font=("arial",10,"bold"),bg="white",fg="black",width=20)
        btn_reg.place(x=30,y=300)

         #button forget passwor
        btn_forgetpass=Button(main_frame,text="Forget password",font=("arial",10,"bold"),bg="white",fg="black",width=20)
        btn_forgetpass.place(x=30,y=340)

    def login_1(self):
        if self.enter_txt.get()=="" or self.enter_pass.get()=="":
            messagebox.showerror("Error","All fild required")
        elif self.enter_txt.get()=="nitesh" or self.enter_pass.get()=="123":
            self.new_window=Toplevel(self.root)
            self.app=HotalManagementSystem(self.new_window)          

            # messagebox.showinfo("Success","welcome my page")  
        else:
            messagebox.showerror("Invailed","invailed user& pass")    

  #=========== fun===========
    






if __name__=="__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()      