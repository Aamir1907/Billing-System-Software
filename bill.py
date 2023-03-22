from tkinter import *
import math,random,os
from tkinter import messagebox


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title=("Billing Software")
        bg_color = ("#074463")  ##074463
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #variable
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.loshan=IntVar()

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.dal=IntVar()
        self.atta=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()

        self.coco_cola=IntVar()
        self.maza=IntVar()
        self.sprite=IntVar()
        self.pepsi=IntVar()
        self.nimka=IntVar()
        self.nimbuzz=IntVar()

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()




        #customer details frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text = Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_text = Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl = Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text = Entry(F1,width=10,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn = Button(F1,text="Search",command=self.find_bill,width=10,font="arial 12",bd=7).grid(row=0,column=6,padx=10,pady=10)
        #cosmetics frame

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl = Label(F2,text="Bath Shop",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_text = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        Face_cream_lbl = Label(F2,text="Face cream",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_text = Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        Face_w_lbl = Label(F2,text="Face Wash",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_text = Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        Hair_s_lbl = Label(F2,text="Hair Spray",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_text = Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        Hair_g_lbl = Label(F2,text="Hair Gel",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_text = Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        Body_lbl = Label(F2,text="Body Loshan",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_text = Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)


        #Grocery frame

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl = Label(F3,text="Rice",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_text = Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        g2_lbl = Label(F3,text="Food Oil",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_text = Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        g3_lbl = Label(F3,text="Dal",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_text = Entry(F3,width=10,textvariable=self.dal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        g4_lbl = Label(F3,text="Atta",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_text = Entry(F3,width=10,textvariable=self.atta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        g5_lbl = Label(F3,text="Wheat",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_text = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        g6_lbl = Label(F3,text="Sugar",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_text = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)


        #Cold Drink frame

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl = Label(F4,text="Coco Cola",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_text = Entry(F4,width=10,textvariable=self.coco_cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        c2_lbl = Label(F4,text="Maza",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_text = Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        c3_lbl = Label(F4,text="Sprite",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_text = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        c4_lbl = Label(F4,text="Pepsi",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_text = Entry(F4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        c5_lbl = Label(F4,text="Nimka",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_text = Entry(F4,width=10,textvariable=self.nimka,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        c6_lbl = Label(F4,text="Nimbuzz",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_text = Entry(F4,width=10,textvariable=self.nimbuzz,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        #Bill Frame

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=340,height=380)
        bill_title=Label(F5,text="Bill Area",bd=7,relief=GROOVE,font="arial 15 bold").pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #Button Frame
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl = Label(F6,text="Total Cosmetic Price",bg=bg_color,fg='white',font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F6,width=18,textvariable=self.cosmetic_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)

        m2_lbl = Label(F6,text="Total Grocery Price",bg=bg_color,fg='white',font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt = Entry(F6,width=18,textvariable=self.grocery_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,pady=1,padx=10)

        m3_lbl = Label(F6,text="Total Cold Drink Price",bg=bg_color,fg='white',font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt = Entry(F6,width=18,textvariable=self.cold_drink_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,pady=1,padx=10)

        c1_lbl = Label(F6,text="Cosmetic Tax",bg=bg_color,fg='white',font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt = Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,pady=1,padx=10)

        c2_lbl = Label(F6,text="Grocery Tax",bg=bg_color,fg='white',font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt = Entry(F6,width=18,textvariable=self.grocery_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,pady=1,padx=10)

        c3_lbl = Label(F6,text="Cold Drink Tax",bg=bg_color,fg='white',font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt = Entry(F6,width=18,textvariable=self.cold_drink_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,pady=1,padx=10)

        btn_F = Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn = Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_F,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn = Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn = Button(btn_F,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*90
        self.c_fw_p=self.face_wash.get()*110
        self.c_hs_p=self.spray.get()*30
        self.c_hg_p=self.gel.get()*20
        self.c_bl_p=self.loshan.get()*70

        self.total_cosmetic_price=float(
                                        self.c_s_p+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_hs_p+
                                        self.c_hg_p+
                                        self.c_bl_p
                                        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.g_r_p=self.rice.get()*60
        self.g_f_p=self.food_oil.get()*125
        self.g_d_p=self.dal.get()*110
        self.g_a_p=self.atta.get()*250
        self.g_w_p=self.wheat.get()*40
        self.g_s_p=self.sugar.get()*45

        self.total_grocery_price=float(
                                       self.g_r_p+
                                       self.g_f_p+
                                       self.g_d_p+
                                       self.g_a_p+
                                       self.g_w_p+
                                       self.g_s_p
                                       )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.d_cc_p=self.coco_cola.get()*85
        self.d_m_p=self.maza.get()*55
        self.d_s_p=self.sprite.get()*110
        self.d_pe_p=self.pepsi.get()*150
        self.d_n_p=self.nimka.get()*40
        self.d_ni_p=self.nimbuzz.get()*45

        

        self.total_cold_drink_price=float(
                                          self.d_cc_p+
                                          self.d_m_p+
                                          self.d_s_p+
                                          self.d_pe_p+
                                          self.d_n_p+
                                          self.d_ni_p 
                                   )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(
                                self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.cd_tax
                            )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome To Delhi Store\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n ====================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n ====================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details Are Must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")

        
        else:
            self.welcome_bill()
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gel.get()}\t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.dal.get()!=0:
                self.txtarea.insert(END,f"\n Dal\t\t{self.dal.get()}\t\t{self.g_d_p}")
            if self.atta.get()!=0:
                self.txtarea.insert(END,f"\n Atta\t\t{self.atta.get()}\t\t{self.g_a_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.coco_cola.get()!=0:
                self.txtarea.insert(END,f"\n Coco Cola\t\t{self.coco_cola.get()}\t\t{self.d_cc_p}")
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_pe_p}")
            if self.nimka.get()!=0:
                self.txtarea.insert(END,f"\n Nimka\t\t{self.nimka.get()}\t\t{self.d_n_p}")
            if self.nimbuzz.get()!=0:
                self.txtarea.insert(END,f"\n Nimbuzz\t\t{self.nimbuzz.get()}\t\t{self.d_ni_p}")

            self.txtarea.insert(END,f"\n ------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

                self.txtarea.insert(END,f"\n Total Bill\t\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n ------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want To Bave Bill?")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No : {self.bill_no.get()} Saved Successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do You want To Clear Data?")
        if op>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.loshan.set(0)

            self.rice.set(0)
            self.food_oil.set(0)
            self.dal.set(0)
            self.atta.set(0)
            self.wheat.set(0)
            self.sugar.set(0)

            self.coco_cola.set(0)
            self.maza.set(0)
            self.sprite.set(0)
            self.pepsi.set(0)
            self.nimka.set(0)
            self.nimbuzz.set(0)

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do You want To Exit?")
        if op>0:
            self.root.destroy()


             







            






 














root=Tk()
obj= Bill_App(root)
root.mainloop()

 