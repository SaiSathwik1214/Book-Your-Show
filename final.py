from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import random
import cx_Oracle
import tempfile

class BillApp:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("BOOK YOUR SHOW")

        

        # ====================Variable==================
        
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000, 99999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.product=StringVar()
        self.sub_tot=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.price=IntVar()
        self.qty=IntVar()
        self.search_bill=StringVar()
        self.Tax=10
        self.subcategor=StringVar()
        
        


        # =================Product==========================
        self.Language=["select option","ENGLISH","TELUGU","HINDI"]
        #==================snacks===========================
        self.subcatENGLISH=["select option","AVATAR","AVENGERS","JOHN_WICK"]

        self.AVATAR=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200

        self.AVENGERS=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200

        self.JOHN_WICK=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200
        #===================lifestyle==============================
        self.subcatTELUGU=["select option","RRR","JERSEY","DASARA","VIKRAM"]

        self.RRR=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200


        self.JERSEY=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200


        self.DASARA=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200


        self.VIKRAM=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200


       
        self.subcatHINDI=["select option","PATHAAN","KRISH","DANGAL"]

        self.PATHAAN=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200


        self.KRISH=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200




        self.DANGAL=["select option","IMAX","INOX","CINEPOLIS"]
        self.price_IMAX=100
        self.price_INOX=150
        self.price_CINEPOLIS=200






        
        

        lbl_tit=Label(self.root,text="BOOK YOUR SHOW",font=("times new roman",25,"bold"),bg="black",fg="white" )
        lbl_tit.place(x=-50,y=0,width=1730,height=100)

        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="red")
        Main_frame.place(x=0,y=100,width=1730,height=900)



        #Customer label frame
        cust_frame=LabelFrame(Main_frame,text="Customer",font=("times new roman",15,"bold"),bg="white",fg="red" )
        cust_frame.place(x=10,y=5,width=540,height=200)
       
        # For Mobile number
        self.lbl_mob=Label(cust_frame,text="Mobile Number:",font=("times new roman",15,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=5,column=0,sticky=W,padx=5,pady=2) 
        self.enter_mob=ttk.Entry(cust_frame,textvariable=self.c_phon,font=("times new roman",15,"bold"),width=24)
        self.enter_mob.grid(row=5,column=1)
       
        # For Name
        self.lbl_name=Label(cust_frame,text="Customer Name:",font=("times new roman",15,"bold"),bg="white",fg="black")
        self.lbl_name.grid(row=3,column=0,sticky=W,padx=5,pady=2) 
        self.enter_name=ttk.Entry(cust_frame,textvariable=self.c_name,font=("times new roman",15,"bold"),width=24)
        self.enter_name.grid(row=3,column=1)
       
        #For Email
        self.lbl_email=Label(cust_frame,text="Customer Email:",font=("times new roman",15,"bold"),bg="white",fg="black")
        self.lbl_email.grid(row=4,column=0,sticky=W,padx=5,pady=2) 
        self.enter_email=ttk.Entry(cust_frame,textvariable=self.c_email,font=("times new roman",15,"bold"),width=24)
        self.enter_email.grid(row=4,column=1)

        #Product Label Frame
        prod_frame=LabelFrame(Main_frame,text="Product",font=("times new roman",15,"bold"),bg="white",fg="red" )
        prod_frame.place(x=10,y=206,width=540,height=270)
        
        # Category Selection
        self.lbl_Language=Label(prod_frame,text="Select Language",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_Language.grid(row=1,column=0,sticky=W,padx=5,pady=2) 
        self.combo_categ=ttk.Combobox(prod_frame,font=("arial",12,"bold"),value=self.Language,width=14,state="readonly")
        self.combo_categ.current(0)
        self.combo_categ.grid(row=1,column=1,sticky=W,padx=5,pady=5)
        self.combo_categ.bind("<<ComboboxSelected>>",self.Languagefun)
        
        # sub Category Selection
        self.lbl_subLanguage=Label(prod_frame,text="Select Movie",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_subLanguage.grid(row=2,column=0,sticky=W,padx=5,pady=2) 
        self.combo_subcateg=ttk.Combobox(prod_frame,values=[''],textvariable=self.subcategor,font=("arial",12,"bold"),width=14,state="readonly")
        self.combo_subcateg.grid(row=2,column=1,sticky=W,padx=5,pady=5)
        self.combo_subcateg.bind("<<ComboboxSelected>>",self.productfun)
        
        
        # product Selection
        self.lbl_product=Label(prod_frame,text="Select Theatre",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_product.grid(row=3,column=0,sticky=W,padx=5,pady=2) 
        self.combo_product=ttk.Combobox(prod_frame,textvariable=self.product,font=("arial",12,"bold"),width=14,state="readonly")
        self.combo_product.grid(row=3,column=1,sticky=W,padx=6,pady=5)
        self.combo_product.bind("<<ComboboxSelected>>",self.pricefun)
        #======================================================================================================================================================
         # sub Time Selection
        #self.lbl_subLanguage=Label(prod_frame,text="Select Time",font=("arial",12,"bold"),bg="white",fg="black")
        #self.lbl_subLanguage.grid(row=4,column=0,sticky=W,padx=5,pady=2) 
        #self.combo_subcateg=ttk.Combobox(prod_frame,values=[''],font=("arial",12,"bold"),width=14,state="readonly")
        #self.combo_subcateg.grid(row=4,column=1,sticky=W,padx=5,pady=5)
        #self.combo_subcateg.bind("<<ComboboxSelected>>",self.productfun)

        # price
        self.lbl_price=Label(prod_frame,text="Price(1 ticket)",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_price.grid(row=6,column=0,sticky=W,padx=5,pady=2) 
        self.combo_price=ttk.Combobox(prod_frame,textvariable=self.price,font=("arial",12,"bold"),width=10,state="readonly")
        self.combo_price.grid(row=6,column=1,sticky=W,padx=5,pady=5)
        
        # Quantity
        self.lbl_quant=Label(prod_frame,text="Quantity",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_quant.grid(row=5,column=0,sticky=W,padx=5,pady=2) 
        self.combo_quant=ttk.Entry(prod_frame,textvariable=self.qty,font=("arial",12,"bold"),width=10)
        self.combo_quant.grid(row=5,column=1,sticky=W,padx=5,pady=5)

        # search
        #search_frame=Frame(Main_frame,bd=5,bg="white")
        #search_frame.place(x=910,y=5,width=500,height=300)


        # self.lbl_bill=Label(search_frame,font=("arial",12,"bold"),bg="red",fg="white",text="Bill number")
        # self.lbl_bill.grid(row=0,column=0,sticky=W,padx=1)

        #self.txt_search=ttk.Entry(search_frame,textvariable=self.search_bill,font=("arial",12,"bold"),width=20)
        #self.txt_search.grid(row=0,column=0,padx=2)

        #self.btnSearch=Button(search_frame,text="Search bill",command=self.searchfun,font=("arial",15,"bold"),width=10,bg="red",fg="white")
        #self.btnSearch.grid(row=0,column=1,sticky=W)

        # Right Frame Bill Area
        Right_label_Frame=LabelFrame(Main_frame,text="Bill Area",font=("times new roman",15,"bold"),bg="white",fg="red")
        Right_label_Frame.place(x=570,y=10,width=400,height=450)
        
        # Scroll bar
        
        scrol_y=Scrollbar(Right_label_Frame,orient=VERTICAL)
        self.textarea=Text(Right_label_Frame,yscrollcommand=scrol_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview())
        self.textarea.pack(fill=BOTH,expand=1) 

        #Billcounter Label Frame
        #Billcounter Label Frame
        
        billcount_frame=LabelFrame(Main_frame,text="bill counter",font=("times new roman",15,"bold"),bg="black",fg="orange" )
        billcount_frame.place(x=0,y=500,width=1520,height=840)
        
        #Sub total
        
        #self.lbl_subtotal=Label(billcount_frame,text="Sub Total",font=("arial",12,"bold"),bg="black",fg="purple")
        #self.lbl_subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2) 
        #enty_quant=ttk.Entry(billcount_frame,font=("arial",12,"bold"),width=10)
        #enty_quant.grid(row=0,column=1,sticky=W,padx=5,pady=5)
        
        # TAX
        
        #self.lbl_tax=Label(billcount_frame,text="Tax",font=("arial",12,"bold"),bg="black",fg="purple")
        #self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2) 
        #enty_tax=ttk.Entry(billcount_frame,font=("arial",12,"bold"),width=10,)
        #enty_tax.grid(row=1,column=1,sticky=W,padx=5,pady=5) 

        # Amount
        #self.lbl_amntotal=Label(billcount_frame,text="Total Amount",font=("arial",12,"bold"),bg="black",fg="purple")
        #self.lbl_amntotal.grid(row=2,column=0,sticky=W,padx=5,pady=2) 
        ##enty_amount=ttk.Entry(billcount_frame,font=("arial",12,"bold"),width=10)
        #enty_amount.grid(row=2,column=1,sticky=W,padx=5,pady=5) 

        
        btn_frame=Frame(billcount_frame,bd=5,bg="white")
        btn_frame.place(x=300,y=0)

        self.btnAddtocart=Button(btn_frame,command=self.Additemfun,height=2,text="Add to cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnAddtocart.grid(row=0,column=0 )
        
        self.btnGenBill=Button(btn_frame,command=self.genbillfun,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnGenBill.grid(row=0,column=1 )

        self.btnsavebil=Button(btn_frame,command=self.savebillfun,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnsavebil.grid(row=0,column=2 )

        self.btnPrint=Button(btn_frame,command=self.iprintfun,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnPrint.grid(row=0,column=3 )

        self.btnClear=Button(btn_frame,height=2,command=self.clearfun,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnClear.grid(row=0,column=4 )

        self.btnExit=Button(btn_frame,height=2,text="Exit",command=root.quit,font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnExit.grid(row=0,column=5)
        self.welcomefun()
        self.lis=[]
        # =========================FUNCTIONS==========================================
    def Additemfun(self,event=""):
        
        self.n=self.price.get()
        self.m=self.qty.get()*self.n
        self.lis.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error,Please select theatre name")
        else:
            #self.textarea.insert(f"\n {self.product.get()}\t\t\t{self.qty.get()}\t{self.m}")
            self.sub_tot.set(str('Rs.%.2f'%(sum(self.lis)-100)))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.lis))-(self.price.get()))*self.Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.lis))+((((sum(self.lis))-(self.price.get()))*self.Tax)/100)))))
    def genbillfun(self):
        
        self.n=self.price.get()
        self.m=self.qty.get()*self.n
        self.lis.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error,Please select product name")
        else:
            self.textarea.insert(END, f"\n {self.product.get()}\t{self.qty.get()}\t{self.m}")
            self.sub_tot.set(str('Rs.%.2f'%((self.m))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.lis))-(self.price.get()))*self.Tax)/100)))
            self.total.set(str('Rs.%.2f'%((((self.m))+((((sum(self.lis))-(self.price.get())-100)*self.Tax)/100)))))
        if self.product.get()=="":
            messagebox.showerror("Error, please add to cart")
        
        text=self.textarea.get(10.0,(10.0+float(len(self.lis))))
        self.welcomefun()
        self.n=self.price.get()
        self.m=self.qty.get()*self.n
        self.lis.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error,Please select product name")
        else:
            self.textarea.insert(END, f"\n {self.subcategor.get()}\t\t{self.product.get()}\t{self.qty.get()}\t{self.m}")
            self.sub_tot.set(str('Rs.%.2f'%((self.m))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.lis))-(self.price.get()))*self.Tax)/100)))
            self.total.set(str('Rs.%.2f'%((((self.m))+((((sum(self.lis))-(self.price.get()))*self.Tax)/100)))))
        self.textarea.insert(END,f"\n==================================")
        self.textarea.insert(END, f"\n Sub Amount:\t\t{self.sub_tot.get()}")
        self.textarea.insert(END, f"\n Tax Amount:\t\t{self.tax_input.get()}")
        self.textarea.insert(END, f"\n Total Amount:\t\t{self.total.get()}")
        self.textarea.insert(END,f"\n==================================")

    def welcomefun(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\tWelcome to Book Your Show")
        self.textarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number: {self.c_phon.get()}")
        self.textarea.insert(END,f"\n Email ID: {self.c_email.get()}")
        self.textarea.insert(END,f"\n==================================")
        self.textarea.insert(END,f"\n Movie\t\tTheatre\tQTY\tPrice")
        self.textarea.insert(END,f"\n==================================")
        

    def Languagefun(self,event=""):
        if self.combo_categ.get()=="ENGLISH":
            self.combo_subcateg.config(value=self.subcatENGLISH)
            self.combo_subcateg.current(0)

        if self.combo_categ.get()=="TELUGU":
            self.combo_subcateg.config(value=self.subcatTELUGU)
            self.combo_subcateg.current(0)
        
        if self.combo_categ.get()=="HINDI":
            self.combo_subcateg.config(value=self.subcatHINDI)
            self.combo_subcateg.current(0)


    def productfun(self,event=""):
        if self.combo_subcateg.get()=="AVATAR":
            self.combo_product.config(values=self.AVATAR)
            self.combo_product.current(0)

        if self.combo_subcateg.get()=="AVENGERS":
            self.combo_product.config(values=self.AVENGERS)
            self.combo_product.current(0)

        if self.combo_subcateg.get()=="JOHN_WICK":
            self.combo_product.config(values=self.JOHN_WICK)
            self.combo_product.current(0)
# ===========lifestyle===============
        if self.combo_subcateg.get()=="VIKRAM":
            self.combo_product.config(values=self.VIKRAM)
            self.combo_product.current(0)
        
        if self.combo_subcateg.get()=="RRR":
            self.combo_product.config(values=self.RRR)
            self.combo_product.current(0)

        if self.combo_subcateg.get()=="JERSEY":
            self.combo_product.config(values=self.JERSEY)
            self.combo_product.current(0)
        
        if self.combo_subcateg.get()=="KGF":
            self.combo_product.config(values=self.KGF)
            self.combo_product.current(0)
#================milk products=================
        if self.combo_subcateg.get()=="PATHAAN":
            self.combo_product.config(values=self.PATHAAN)
            self.combo_product.current(0)

        if self.combo_subcateg.get()=="KRISH":
            self.combo_product.config(values=self.KRISH)
            self.combo_product.current(0)
        if self.combo_subcateg.get()=="DANGAL":
            self.combo_product.config(values=self.DANGAL)
            self.combo_product.current(0)
    def pricefun(self,event=""):
        #snacks
        if self.combo_product.get()=="IMAX":
            self.combo_price.config(values=self.price_IMAX)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="INOX":
            self.combo_price.config(values=self.price_INOX)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.combo_product.get()=="CINEPOLIS":
            self.combo_price.config(values=self.price_CINEPOLIS)
            self.combo_price.current(0)
            self.qty.set(1)
    def savebillfun(self):
        c1_name=self.c_name.get()
        c1_email=self.c_email.get()
        c1_phon=self.c_phon.get()
        total1=self.total.get()
        billno1=self.bill_no.get()
        try:
            con=cx_Oracle.connect("system/system@localhost:1521/orcl")
            self.cursor=con.cursor()
            self.cursor.execute("insert into customer values(eid_seq.nextval,:1,:2,:3)",(c1_name,c1_email,c1_phon))
            con.commit()
            self.cursor.execute("select * from customer")
            e=self.cursor.fetchall()
            eid=e[-1]
            eid1=eid[0]
            self.cursor.execute("insert into bill values(:1,:2,:3)",(billno1,total1,eid1))
            con.commit()
        except cx_Oracle.DatabaseError as e:
            print("there is a problem with oracle",e)
        finally:
            if self.cursor:
                self.cursor.close() 
            if con:
                con.close()
    def searchfun(self):
        try:
            con=cx_Oracle.connect("system/system@localhost:1521/orcl")
            self.cursor=con.cursor()
            search1=self.search_bill.get()
            self.cursor.execute("select c.cid,c.cname,c.cmail,c.cmob,b.total from customer c,bill b where c.cid=b.cid and b.bid=:value",{'value':search1})
            ans=self.cursor.fetchone()
            
        except cx_Oracle.DatabaseError as e:
            print("there is a problem with oracle",e)
        finally:
            if self.cursor:
                self.cursor.close() 
            if con:
                con.close()
        q1=ans[0]
        q2=ans[1]
        q3=ans[2]
        q4=ans[3]
        q5=ans[4]
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\tDetails of customer")
        self.textarea.insert(END,f"\n==================================")
        self.textarea.insert(END, f"\nCUSTOMER ID            :{q1}")
        self.textarea.insert(END, f"\nCUSTOMER NAME          :{q2}")
        self.textarea.insert(END, f"\nCUSTOMER MAIL          :{q3}")
        self.textarea.insert(END, f"\nCUSTOMER PHONE NUMBER  :{q4}")
        self.textarea.insert(END, f"\nTOTAL BILL             :{q5}")
        self.textarea.insert(END,f"\n==================================")

    def iprintfun(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def clearfun(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        self.bill_no.set(random.choice(list(range(1000))))
        self.search_bill.set("")
        self.product.set("")
        self.price.set(0)
        self.qty.set(0)
        self.lis=[0]
        self.total.set("")
        self.sub_tot.set("")
        self.tax_input.set("")
        self.welcomefun()

        
if __name__=='__main__':
    root=Tk()
    obj=BillApp(root)
    root.mainloop()        




