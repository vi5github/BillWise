from tkinter import *               #importing tkinter module
from tkinter import messagebox
import math,random,os
class Bill_App:
    def __init__(self,root):        #calling initialized function
        self.root=root              #initializing root
        self.root.geometry("1350x700+0+0")      
        self.root.title("Billing Software")         #giving title otherwise tk was coming
        bg_color="purple"
        title=Label(self.root,text="Billing Software",bd=24,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=============Variables======================
        #=============Cocolate======================
        self.silk=IntVar()
        self.perk=IntVar()
        self.five_star=IntVar()
        self.kinder_joy=IntVar()
        self.munch=IntVar()
        self.kit_kat=IntVar()
        #=============Grocery========================
        self.rice=IntVar()
        self.food_oil=IntVar() 
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #=============Cold Drinka====================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        #=============Total Product Price and Tax variables====================
        self.cocolate_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cocolate_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        #=============Customer Detail================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #=============Customer Detail================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=90,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",fg="white",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=0,padx=10,pady=5)
        cname_txt=Entry(F1,width=11,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone No.",fg="white",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=2,padx=10,pady=5)
        cphn_txt=Entry(F1,width=11,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        cbill_lbl=Label(F1,text="Bill Number",fg="white",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=4,padx=10,pady=5)
        cbill_txt=Entry(F1,width=11,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=9,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=5)
        
        #=============Cocolate Frame================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cocolate",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=400,height=380)
        silk_lbl=Label(F2,text="Silk",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        silk_txt=Entry(F2,width=10,textvariable=self.silk,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        perk_lbl=Label(F2,text=" Perk",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        perk_txt=Entry(F2,width=10,textvariable=self.perk,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        five_star_lbl=Label(F2,text="Five Star",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        five_star_txt=Entry(F2,width=10,textvariable=self.five_star,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        kinder_joy_lbl=Label(F2,text="Kinder Joy",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        kinder_joy_txt=Entry(F2,width=10,textvariable=self.kinder_joy,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        munch_lbl=Label(F2,text="Munch",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        munch_txt=Entry(F2,width=10,textvariable=self.munch,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        kit_kat_lbl=Label(F2,text="Kit Kat",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        kit_kat_txt=Entry(F2,width=10,textvariable=self.kit_kat,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============Grocery Frame================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=335,height=380)
        g1_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        g4_lbl=Label(F3,text="Wheat",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        g5_lbl=Label(F3,text="Suger",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============Cold Drink Frame================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=677,y=180,width=343,height=380)
        c1_lbl=Label(F4,text="Maza",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        c2_lbl=Label(F4,text="Cock",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        c3_lbl=Label(F4,text="Frooti",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        c4_lbl=Label(F4,text="ThumbsUp",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        c5_lbl=Label(F4,text="Limca",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        c6_lbl=Label(F4,text="Sprite",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #=============Bill Area Frame================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1025,y=180,width=500,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",fg="gold",bg=bg_color,bd=17,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=============Button Frame================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=3,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Cocolate Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="w")
        m1_txt=Entry(F6,width=15,textvariable=self.cocolate_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=10,pady=1,sticky="w")
        m2_txt=Entry(F6,width=15,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=10,pady=1,sticky="w")
        m3_txt=Entry(F6,width=15,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=1)

        c1_lbl=Label(F6,text="Cocolate Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=3,padx=10,pady=1,sticky="w")
        c1_txt=Entry(F6,width=15,textvariable=self.cocolate_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=4,padx=5,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=3,padx=10,pady=1,sticky="w")
        c2_txt=Entry(F6,width=15,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=4,padx=5,pady=1)

        c3_lbl=Label(F6,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=3,padx=10,pady=1,sticky="w")
        c3_txt=Entry(F6,width=15,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=4,padx=5,pady=1)
#=================Button====================
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=650,width=340,height=100)
        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=5,width=15,bd=4,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",pady=5,width=15,bd=4,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=5,width=15,bd=4,font="arial 10 bold").grid(row=1,column=0,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=5,width=15,bd=4,font="arial 10 bold").grid(row=1,column=1,padx=5,pady=5)
        self.welcome_bill()
#======================Total======================        
    def total(self):
        self.c_s_p=self.silk.get()*140
        self.c_fc_p=self.perk.get()*10
        self.c_fw_p=self.five_star.get()*30
        self.c_spr_p=self.kinder_joy.get()*50
        self.c_g_p=self.munch.get()*15
        self.c_l_p=self.kit_kat.get()*60
        self.total_cocolate_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_spr_p+
                                    self.c_g_p+
                                    self.c_l_p
                                  )
        self.cocolate_price.set("Rs. "+str(self.total_cocolate_price))
        self.c_tax=round(self.total_cocolate_price*0.05,2)
        self.cocolate_tax.set("Rs. "+str(self.c_tax))
        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.food_oil.get()*180
        self.g_w_p=self.wheat.get()*60
        self.g_d_p=self.daal.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_w_p+
                                    self.g_d_p+
                                    self.g_s_p+
                                    self.g_t_p
                                  )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round(self.total_grocery_price*0.1,2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        self.cd_m_p=self.maza.get()*60
        self.cd_c_p=self.cock.get()*60
        self.cd_f_p=self.frooti.get()*50
        self.cd_th_p=self.thumbsup.get()*45
        self.cd_l_p=self.limca.get()*40
        self.cd_s_p=self.sprite.get()*60
        self.total_cold_drink_price=float(
                                    self.cd_m_p+
                                    self.cd_c_p+
                                    self.cd_f_p+
                                    self.cd_th_p+
                                    self.cd_l_p+
                                    self.cd_s_p
                                   )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round(self.total_cold_drink_price*0.05,2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))
        self.total_bill=float(
            self.total_cocolate_price+
            self.total_grocery_price+
            self.total_cold_drink_price+
            self.c_tax+
            self.g_tax+
            self.cd_tax
        )
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome Our Retail")
        self.textarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number :{self.c_phon.get()}")
        
        self.textarea.insert(END,f"\n==============================")
        self.textarea.insert(END,f"\n Product\t\tQTY\tPrice")
        self.textarea.insert(END,f"\n==============================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are Required")
        elif self.cocolate_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Selected")
        else:
            self.welcome_bill()
            #===cocolate=====
            if self.silk.get()!=0:
                self.textarea.insert(END,f"\n Silk\t\t{self.silk.get()}\t{self.c_s_p}")
            if self.perk.get()!=0:
                self.textarea.insert(END,f"\n Perk\t\t{self.perk.get()}\t{self.c_fc_p}")
            if self.five_star.get()!=0:
                self.textarea.insert(END,f"\n Five Star \t\t{self.five_star.get()}\t{self.c_fw_p}")
            if self.kinder_joy.get()!=0:
                self.textarea.insert(END,f"\n Kinder Joy\t\t{self.kinder_joy.get()}\t{self.c_s_p}")
            if self.munch.get()!=0:
                self.textarea.insert(END,f"\n Hair Gell \t\t{self.munch.get()}\t{self.c_g_p}")
            if self.kit_kat.get()!=0:
                self.textarea.insert(END,f"\n kit kat\t\t{self.kit_kat.get()}\t{self.c_l_p}")
            #===Grocery=====
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice   \t\t{self.rice.get()}\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t{self.g_fo_p}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal   \t\t{self.daal.get()}\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat  \t\t{self.wheat.get()}\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Suger  \t\t{self.sugar.get()}\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea   \t\t{self.tea.get()}\t{self.g_t_p}")
            
            #===Cold Drink=====
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza   \t\t{self.maza.get()}\t{self.cd_m_p}")
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock   \t\t{self.cock.get()}\t{self.cd_c_p}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti  \t\t{self.frooti.get()}\t{self.cd_f_p}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t{self.cd_th_p}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t{self.cd_l_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite  \t\t{self.sprite.get()}\t{self.cd_s_p}")
            self.textarea.insert(END,f"\n==============================")
            if self.cocolate_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cocolate Tax \t{self.cocolate_tax.get()}")
            
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax \t{self.grocery_tax.get()}")
                
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n ColdDrink Tax\t{self.cold_drink_tax.get()}")
            self.textarea.insert(END,f"\n Total Bill  \t Rs. {self.total_bill}")
            self.textarea.insert(END,f"\n==============================")
        self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("C:\\Users\\gaura\\Desktop\\Project\\BILL\\"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfull")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("C:\\Users\\gaura\\Desktop\\Project\\BILL"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"C:\\Users\\gaura\\Desktop\\Project\\BILL\{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear_data(self):
        op=messagebox.askyesno("clear","Do you want to Reset Entries?")
        if op>0:
            #=============Cocolate======================
            self.silk.set(0)
            self.perk.set(0)
            self.five_star.set(0)
            self.kinder_joy.set(0)
            self.munch.set(0)
            self.kit_kat.set(0)
            #=============Grocery========================
            self.rice.set(0)
            self.food_oil.set(0) 
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #=============Cold Drinka====================
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            #=============Total Product Price and Tax variables====================
            self.cocolate_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cocolate_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #=============Customer Detail================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()





root=Tk()               #making an object of tkinter
obj=Bill_App(root)      #making object of bill app

root.mainloop()         #calling using root.mainloop

