from tkinter import *
from tkinter import messagebox
from random import *
import pickle
from threading import *
from datetime import *
import time
class Food_items:
    def __init__(self):
        self.burger = ''
        self.fries = ''
        self.pizza = ''
        self.coke = ''
        self.icecream = ''
        self.ecomeal = ''
        self.deluxemeal = ''
        self.sgst=''
        self.cgst=''
class Customer(Food_items):
    cuslist=[]
def autoload1():
    fs=open('Cutomer_order_history.txt','rb')
    Customer.cuslist=pickle.load(fs)
    fs.close()
concat=''
def btnclick(number):
    global concat
    concat+=str(number)
    calc.set(concat)

def reset_func():
    calc.set('')
    global concat
    concat=''

def eval_func():
    try:
        global concat
        concat=str(eval(calc.get()))
        calc.set(concat)
    except Exception:
        messagebox.showerror('RESTAURANT BILLING SYSTEM','Syntax Error')
def exit_func():
    exit()
def res_func():
    ref_entry.delete(0,END)
    chk_bur.set('0')
    bur_entry.delete(0,END)
    burger.set('0')
    bur_entry.configure(state=DISABLED)
    chk_fries.set('0')
    fri_entry.delete(0,END)
    fries.set('0')
    fri_entry.configure(state=DISABLED)
    chk_pizza.set('0')
    pizz_entry.delete(0,END)
    pizza.set('0')
    pizz_entry.configure(state=DISABLED)
    chk_coke.set('0')
    cok_entry.delete(0,END)
    coke.set('0')
    cok_entry.configure(state=DISABLED)
    chk_icecream.set('0')
    ice_entry.delete(0,END)
    icecream.set('0')
    ice_entry.configure(state=DISABLED)
    chk_eco.set('0')
    eco_entry.delete(0,END)
    eco.set('0')
    eco_entry.configure(state=DISABLED)
    chk_deluxe.set('0')
    deluxe_entry.delete(0,END)
    deluxe.set('0')
    deluxe_entry.configure(state=DISABLED)
    cost_entry.delete(0,END)
    sgst_entry.delete(0,END)
    cgst_entry.delete(0,END)
    total_entry.delete(0,END)
    txt_reciept.delete('1.0', END)


now=datetime.now()
def ref_func():
    if(burger.get()!='' and fries.get()!='' and pizza.get()!=''and coke.get()!=''and icecream.get()!='' and eco.get()!=''and deluxe.get()!=''):
        x = randint(10000, 99999)
        refrence.set(str(x))
        fs=open('Rest_pricelist.txt','rb')
        obj=pickle.load(fs)
        fs.close()

        c=int(burger.get())*int(obj.burger)+int(fries.get())*int(obj.fries)+int(pizza.get())*int(obj.pizza)+\
          int(coke.get())*int(obj.coke)+int(icecream.get())*int(obj.icecream)+int(eco.get())*int(obj.ecomeal)+int(deluxe.get())*int(obj.deluxemeal)
        cost.set('Rs : '+str(c))
        st=(float(obj.sgst)*c)/100
        sgst.set('Rs : '+str(st))
        ct = (float(obj.cgst) * c)/100
        cgst.set('Rs : ' + str(ct))
        t=str(c+st+ct)
        total.set(t)
        cus=Customer()
        cus.ref=refrence.get()
        cus.date=now
        cus.burqty=int(burger.get())
        cus.buramt=int(burger.get())*int(obj.burger)
        cus.friqty=int(fries.get())
        cus.friamt=int(fries.get())*int(obj.fries)
        cus.pizzqty=int(pizza.get())
        cus.pizzamt=int(pizza.get())*int(obj.pizza)
        cus.cokqty=int(coke.get())
        cus.cokamt=int(coke.get())*int(obj.coke)
        cus.iceqty=int(icecream.get())
        cus.iceamt=int(icecream.get())*int(obj.icecream)
        cus.ecoqty=int(eco.get())
        cus.ecoamt=int(eco.get())*int(obj.ecomeal)
        cus.delqty=int(deluxe.get())
        cus.delamt=int(deluxe.get())*int(obj.deluxemeal)
        cus.subttl=c
        cus.sgsttax=st
        cus.cgsttax=ct
        cus.gdttl=t
        cus.burger=obj.burger
        cus.fries=obj.fries
        cus.pizza=obj.pizza
        cus.coke=obj.coke
        cus.icecream=obj.icecream
        cus.ecomeal=obj.ecomeal
        cus.deluxemeal=obj.deluxemeal
        cus.sgst=obj.sgst
        cus.cgst=obj.cgst
        Customer.cuslist.append(cus)
        fs=open('Cutomer_order_history.txt','wb')
        pickle.dump(Customer.cuslist,fs)
        fs.close()
    else:
        messagebox.showwarning('Warning','please fill the empty field')

def reciept_func():
    try:
        cus=Customer.cuslist[-1]

        txt_reciept.delete('1.0',END)
        txt_reciept.insert(END,'REF NO.\t\t'+cus.ref+'\t'+'DATE:\t'+f'{cus.date.day}/{cus.date.month}/{cus.date.year}\n')
        txt_reciept.insert(END,'------------------------------------------------\n')
        txt_reciept.insert(END,'ITEMS\t\tQTY\tRATE\tAMT\n')
        txt_reciept.insert(END, '------------------------------------------------\n')
        if(cus.burqty):
            txt_reciept.insert(END,'Burger\t\t '+str(cus.burqty)+'\t'+cus.burger+'\t'+str(cus.buramt)+'\n')
        if (cus.friqty):
            txt_reciept.insert(END, 'Fries\t\t ' + str(cus.friqty) + '\t' + cus.fries + '\t' + str(cus.friamt) + '\n')
        if (cus.pizzqty):
            txt_reciept.insert(END, 'Pizza\t\t ' + str(cus.pizzqty) + '\t' + cus.pizza + '\t' + str(cus.pizzamt) + '\n')
        if (cus.cokqty):
            txt_reciept.insert(END, 'Coke\t\t ' + str(cus.cokqty) + '\t' + cus.coke + '\t' + str(cus.cokamt) + '\n')
        if (cus.iceqty):
            txt_reciept.insert(END, 'Icecream\t\t ' + str(cus.iceqty) + '\t' + cus.icecream + '\t' + str(cus.iceamt) + '\n')
        if (cus.ecoqty):
            txt_reciept.insert(END, 'Ecomeal\t\t ' + str(cus.ecoqty) + '\t' + cus.ecomeal + '\t' + str(cus.ecoamt) + '\n')
        if (cus.delqty):
            txt_reciept.insert(END, 'Deluxemeal\t\t ' + str(cus.delqty) + '\t' + cus.deluxemeal + '\t' + str(cus.delamt) + '\n')
        txt_reciept.insert(END, 'SubTotal\t\t\t\t' + str(cus.subttl) + '\n')
        txt_reciept.insert(END, 'SGST\t\t\t' +str(cus.sgst)+'%' +'\t' + str(cus.sgsttax) + '\n')
        txt_reciept.insert(END, 'CGST\t\t\t' +str(cus.cgst)+'%'+'\t' + str(cus.cgsttax) + '\n')
        txt_reciept.insert(END, 'GrandTotal\t\t\t\t' + str(cus.gdttl) + '\n')


    except Exception:
        messagebox.showwarning('Warning','No Data')
def order_his():
    def delete_all():
        Customer.cuslist.clear()
        fs = open('Cutomer_order_history.txt', 'wb')
        fs.close()
        refval.set('')
        txt_shw.delete('1.0', END)
        res_func()
        messagebox.showinfo('Info','All Customer Deleted')
        sub.destroy()

    def delete():
        if(refval.get()!=''):

            for cus in Customer.cuslist:
                if (cus.ref == refval.get()):
                    Customer.cuslist.remove(cus)
                    fs = open('Cutomer_order_history.txt', 'wb')
                    pickle.dump(Customer.cuslist,fs)
                    refval.set('')
                    txt_shw.delete('1.0', END)
                    messagebox.showinfo('Info','Customer Deleted successfully')
                    sub.focus()
                    return
            messagebox.showinfo('Info','Customer not found of given Ref No.')
            sub.focus()
        else:
            messagebox.showwarning('Warning','Please Enter Ref No. ')
            sub.focus()

    def search():
        if(refval.get()!=''):
            for cus in Customer.cuslist:
                if(cus.ref==refval.get()):
                    txt_shw.delete('1.0',END)
                    txt_shw.insert(END,'REF NO.\t\t' + cus.ref + '\t' + 'DATE:\t' + f'{cus.date.day}/{cus.date.month}/{cus.date.year}\n')
                    txt_shw.insert(END, '-------------------------------------------------------------------\n')
                    txt_shw.insert(END, 'ITEMS\t\tQTY\tRATE\tAMT\n')
                    txt_shw.insert(END, '-------------------------------------------------------------------\n')
                    if (cus.burqty):
                        txt_shw.insert(END, 'Burger\t\t ' + str(cus.burqty) + '\t' + cus.burger + '\t' + str(
                            cus.buramt) + '\n')
                    if (cus.friqty):
                        txt_shw.insert(END, 'Fries\t\t ' + str(cus.friqty) + '\t' + cus.fries + '\t' + str(
                            cus.friamt) + '\n')
                    if (cus.pizzqty):
                        txt_shw.insert(END, 'Pizza\t\t ' + str(cus.pizzqty) + '\t' + cus.pizza + '\t' + str(
                            cus.pizzamt) + '\n')
                    if (cus.cokqty):
                        txt_shw.insert(END,
                                           'Coke\t\t ' + str(cus.cokqty) + '\t' + cus.coke + '\t' + str(cus.cokamt) + '\n')
                    if (cus.iceqty):
                        txt_shw.insert(END, 'Icecream\t\t ' + str(cus.iceqty) + '\t' + cus.icecream + '\t' + str(
                            cus.iceamt) + '\n')
                    if (cus.ecoqty):
                        txt_shw.insert(END, 'Ecomeal\t\t ' + str(cus.ecoqty) + '\t' + cus.ecomeal + '\t' + str(
                            cus.ecoamt) + '\n')
                    if (cus.delqty):
                        txt_shw.insert(END, 'Deluxemeal\t\t ' + str(cus.delqty) + '\t' + cus.deluxemeal + '\t' + str(
                            cus.delamt) + '\n')
                    txt_shw.insert(END, 'SubTotal\t\t\t\t' + str(cus.subttl) + '\n')
                    txt_shw.insert(END, 'SGST\t\t\t' + str(cus.sgst) + '%' + '\t' + str(cus.sgsttax) + '\n')
                    txt_shw.insert(END, 'CGST\t\t\t' + str(cus.cgst) + '%' + '\t' + str(cus.cgsttax) + '\n')
                    txt_shw.insert(END, 'GrandTotal\t\t\t\t' + str(cus.gdttl) + '\n')
                    return
            messagebox.showwarning('Warning','No Customer Found of given Ref.')
            sub.focus()
        else:
            messagebox.showwarning('Warning','Please fill Ref No.')
            sub.focus()
    sub=Toplevel(root)
    sub.focus()
    refval=StringVar()
    widg_ref=Frame(sub,bd=10,relief=RIDGE,width=500,height=100)
    widg_ref.pack(side=TOP)
    shw_dta=Frame(sub)
    shw_dta.pack(side=TOP)

    txt_shw = Text(shw_dta, font=1, bd=10, bg='white', relief=RIDGE, width=46, height=10)
    txt_shw.pack(side=TOP)

    lbl_ref=Label(widg_ref,text='Enter Ref. No.',font=1)
    lbl_ref.grid(row=0,column=0,padx=20,pady=20)
    ety_ref=Entry(widg_ref,textvariable=refval,width=20,bd=5,font=1)
    ety_ref.grid(row=0,column=1,columnspan=2,padx=20,pady=20)
    btn1 =Button(widg_ref,text='Search',width=10,font=1,bg='GreenYellow',bd=5,command=search)
    btn1.grid(row=1,column=0,padx=20,pady=20)
    btn2 = Button(widg_ref, text='Delete', width=10, font=1, bg='yellow', bd=5,command=delete)
    btn2.grid(row=1, column=1, padx=20, pady=20)
    btn3 = Button(widg_ref, text='Delete All', width=10, font=1, bg='red', bd=5,command=delete_all)
    btn3.grid(row=1, column=2, padx=20, pady=20)
def entery_box_bur():
    if(chk_bur.get()==1):
        bur_entry.configure(state=NORMAL)
        bur_entry.focus()
        bur_entry.delete(0,END)
        burger.set('')
    elif(chk_bur.get()==0):
        bur_entry.configure(state=DISABLED)
        burger.set('0')
def entery_box_fries():
    if(chk_fries.get()==1):
        fri_entry.configure(state=NORMAL)
        fri_entry.focus()
        fri_entry.delete(0,END)
        fries.set('')
    elif(chk_fries.get()==0):
        fri_entry.configure(state=DISABLED)
        fries.set('0')
def entery_box_pizza():
    if(chk_pizza.get()==1):
        pizz_entry.configure(state=NORMAL)
        pizz_entry.focus()
        pizz_entry.delete(0,END)
        pizza.set('')
    elif(chk_pizza.get()==0):
        pizz_entry.configure(state=DISABLED)
        pizza.set('0')
def entery_box_coke():
    if(chk_coke.get()==1):
        cok_entry.configure(state=NORMAL)
        cok_entry.focus()
        cok_entry.delete(0,END)
        coke.set('')
    elif(chk_fries.get()==0):
        cok_entry.configure(state=DISABLED)
        coke.set('0')
def entery_box_icecream():
    if(chk_icecream.get()==1):
        ice_entry.configure(state=NORMAL)
        ice_entry.focus()
        ice_entry.delete(0,END)
        icecream.set('')
    elif(chk_bur.get()==0):
        ice_entry.configure(state=DISABLED)
        icecream.set('0')
def entery_box_eco():
    if(chk_eco.get()==1):
        eco_entry.configure(state=NORMAL)
        eco_entry.focus()
        eco_entry.delete(0,END)
        eco.set('')
    elif(chk_eco.get()==0):
        eco_entry.configure(state=DISABLED)
        eco.set('0')
def entery_box_deluxe():
    if(chk_deluxe.get()==1):
        deluxe_entry.configure(state=NORMAL)
        deluxe_entry.focus()
        deluxe_entry.delete(0,END)
        deluxe.set('')
    elif(chk_deluxe.get()==0):
        deluxe_entry.configure(state=DISABLED)
        deluxe.set('0')

def pricelist_func():

    def autoload():
        fs=open('Rest_pricelist.txt','rb')
        obj=pickle.load(fs)
        burprice.set(obj.burger)
        friprice.set(obj.fries)
        pizzaprice.set(obj.pizza)
        cokeprice.set(obj.coke)
        icecreamprice.set(obj.icecream)
        ecoprice.set(obj.ecomeal)
        deluxeprice.set(obj.deluxemeal)
        sgstval.set(obj.sgst)
        cgstval.set(obj.cgst)
    def exfunc():
        root1.destroy()
    def save_list():
        obj = Food_items()
        fs = open('Rest_pricelist.txt', 'wb')

        obj.burger = burprice.get()
        obj.fries = friprice.get()
        obj.pizza = pizzaprice.get()
        obj.coke = cokeprice.get()
        obj.icecream = icecreamprice.get()
        obj.ecomeal = ecoprice.get()
        obj.deluxemeal = deluxeprice.get()
        obj.sgst = sgstval.get()
        obj.cgst = cgstval.get()

        pickle.dump(obj, fs)
        fs.close()

        messagebox.showinfo('RESTAURANT BILLING SYSTEM','Price Modified Successfully ')
        root1.destroy()

    root1 = Toplevel(root)
    burger_lbl = Label(root1, text='Burger', width=20, font=1)
    burger_lbl.grid(row=0, column=0)
    burprice = StringVar()
    burger_ety = Entry(root1, textvariable=burprice, width=20, font=1, bd=5)
    burger_ety.grid(row=0, column=1, padx=20)

    fries_lbl = Label(root1, text='Fries', width=20, font=1)
    fries_lbl.grid(row=1, column=0)
    friprice = StringVar()
    fries_ety = Entry(root1, textvariable=friprice, width=20, font=1, bd=5)
    fries_ety.grid(row=1, column=1, padx=20)

    pizza_lbl = Label(root1, text='Pizza', width=20, font=1)
    pizza_lbl.grid(row=2, column=0)
    pizzaprice = StringVar()
    pizza_ety = Entry(root1, textvariable=pizzaprice, width=20, font=1, bd=5)
    pizza_ety.grid(row=2, column=1, padx=20)

    coke_lbl = Label(root1, text='Coke', width=20, font=1)
    coke_lbl.grid(row=3, column=0)
    cokeprice = StringVar()
    coke_ety = Entry(root1, textvariable=cokeprice, width=20, font=1, bd=5)
    coke_ety.grid(row=3, column=1, padx=20)

    icecream_lbl = Label(root1, text='Ice Cream', width=20, font=1)
    icecream_lbl.grid(row=4, column=0)
    icecreamprice = StringVar()
    icecream_ety = Entry(root1, textvariable=icecreamprice, width=20, font=1, bd=5)
    icecream_ety.grid(row=4, column=1, padx=20)

    eco_lbl = Label(root1, text='Eco Meal', width=20, font=1, bd=5)
    eco_lbl.grid(row=5, column=0)
    ecoprice = StringVar()
    eco_ety = Entry(root1, textvariable=ecoprice, width=20, font=1, bd=5)
    eco_ety.grid(row=5, column=1, padx=20)

    deluxe_lbl = Label(root1, text='Deluxe Meal', width=20, font=1)
    deluxe_lbl.grid(row=6, column=0)
    deluxeprice = StringVar()
    deluxe_ety = Entry(root1, textvariable=deluxeprice, width=20, font=1, bd=5)
    deluxe_ety.grid(row=6, column=1, padx=20)

    sgst1_lbl = Label(root1, text='SGST (in %)', width=20, font=1)
    sgst1_lbl.grid(row=7, column=0)
    sgstval = StringVar()
    sgst_ety = Entry(root1, textvariable=sgstval, width=20, font=1, bd=5)
    sgst_ety.grid(row=7, column=1, padx=20)

    cgst1_lbl = Label(root1, text='CGST (in %)', width=20, font=1)
    cgst1_lbl.grid(row=8, column=0)
    cgstval = StringVar()
    cgst_ety = Entry(root1, textvariable=cgstval, width=20, font=1, bd=5)
    cgst_ety.grid(row=8, column=1, padx=20)

    save_btn = Button(root1, text='Save', width=15, bd=5, bg='GreenYellow', font=1,command=save_list)
    save_btn.grid(row=0,rowspan=3,column=2, padx=20)

    ex_btn = Button(root1, text='Exit', width=15, bd=5, bg='red', font=1,command=exfunc)
    ex_btn.grid(row=3, rowspan=3, column=2, padx=20)

    th1=Thread(target=autoload())
    th1.start()
try:
    th2=Thread(target=autoload1())
    th2.start()
except Exception:
    pass

root=Tk()
root.title('RESTAURANT BILLING SYSTEM')
root.geometry()

#title

title_frame=Frame(root)
title_frame.pack(side=TOP)
title_label=Label(title_frame,text='RESTAURANT BILLING SYSTEM',width=40,font=('arial',50,'bold'),fg='blue',bd=10,relief=RIDGE)
title_label.pack(side=TOP)

#frames

item_frame=Frame(root,bd=10,relief=RIDGE)
item_frame.pack(side=LEFT)

rec_calc_frame=Frame(root,bd=10,relief=RIDGE)
rec_calc_frame.pack(side=RIGHT)

cal_frame=Frame(rec_calc_frame,bd=10,relief=RIDGE)
cal_frame.pack(side=TOP)

rec_btn_frame=Frame(rec_calc_frame,bd=10,relief=RIDGE)
rec_btn_frame.pack(side=BOTTOM)

rec_frame=Frame(rec_calc_frame)
rec_frame.pack(side=BOTTOM)



#labels

ref_label=Label(item_frame,text='Refrence:',font=('lithograph',16,'bold'),fg='blue')
ref_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

cost_label=Label(item_frame,text='Cost of meal:',font=('lithograph',16,'bold'),fg='blue')
cost_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

sgst_label=Label(item_frame,text='SGST:',font=('lithograph',16,'bold'),fg='blue')
sgst_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)

cgst_label=Label(item_frame,text='CGST:',font=('lithograph',16,'bold'),fg='blue')
cgst_label.grid(row=4,column=2,padx=10,pady=10,sticky=W)

total_label=Label(item_frame,text='Total Cost:',font=('lithograph',16,'bold'),fg='blue')
total_label.grid(row=5,column=2,padx=10,pady=10,sticky=W)

#checkbutton
chk_bur=IntVar()
burger_chkbt=Checkbutton(item_frame,text='Burger:',font=('lithograph',16,'bold'),fg='blue',onvalue=1,offvalue=0,
                         variable=chk_bur,command=entery_box_bur)
burger_chkbt.grid(row=1,column=0,padx=10,pady=10,sticky=W)
chk_fries=IntVar()
fries_chkbtn=Checkbutton(item_frame,text='Fries:',font=('lithograph',16,'bold'),fg='blue',onvalue=1,offvalue=0,
                         variable=chk_fries,command=entery_box_fries)
fries_chkbtn.grid(row=2,column=0,padx=10,pady=10,sticky=W)

chk_pizza=IntVar()
pizza_chkbtn=Checkbutton(item_frame,text='Pizza:',font=('lithograph',16,'bold'),fg='blue',onvalue=1,offvalue=0,
                         variable=chk_pizza,command=entery_box_pizza)
pizza_chkbtn.grid(row=3,column=0,padx=10,pady=10,sticky=W)

chk_coke=IntVar()
coke_chkbtn=Checkbutton(item_frame,text='Coke:',font=('lithograph',16,'bold'),fg='blue',onvalue=1,offvalue=0,
                        variable=chk_coke,command=entery_box_coke)
coke_chkbtn.grid(row=4,column=0,padx=10,pady=10,sticky=W)

chk_icecream=IntVar()
icecream_chkbtn=Checkbutton(item_frame,text='Ice Cream:',font=('lithograph',16,'bold'),fg='blue',onvalue=1,offvalue=0,
                            variable=chk_icecream,command=entery_box_icecream)
icecream_chkbtn.grid(row=5,column=0,padx=10,pady=10,sticky=W)

chk_eco=IntVar()
eco_chkbtn=Checkbutton(item_frame,text='Eco Meal',font=('lithograph',16,'bold'),fg='blue',onvalue=1,offvalue=0,
                       variable=chk_eco,command=entery_box_eco)
eco_chkbtn.grid(row=0,column=2,padx=10,pady=10,sticky=W)

chk_deluxe=IntVar()
deluxe_chkbtn=Checkbutton(item_frame,text='Deluxe Meal',font=('lithograph',16,'bold'),fg='blue',onvalue=1,offvalue=0,
                          variable=chk_deluxe,command=entery_box_deluxe)
deluxe_chkbtn.grid(row=1,column=2,padx=10,pady=10,sticky=W)

#entery

refrence=StringVar()
ref_entry=Entry(item_frame,textvariable=refrence,width=30,bd=10,justify='right')
ref_entry.grid(row=0,column=1,padx=10,pady=10)

burger=StringVar()
bur_entry=Entry(item_frame,textvariable=burger,width=30,bd=10,justify='right',state=DISABLED)
bur_entry.grid(row=1,column=1,padx=10,pady=10)
burger.set('0')

fries=StringVar()
fri_entry=Entry(item_frame,textvariable=fries,width=30,bd=10,justify='right',state=DISABLED)
fri_entry.grid(row=2,column=1,padx=10,pady=10)
fries.set('0')

pizza=StringVar()
pizz_entry=Entry(item_frame,textvariable=pizza,width=30,bd=10,justify='right',state=DISABLED)
pizz_entry.grid(row=3,column=1,padx=10,pady=10)
pizza.set('0')

coke=StringVar()
cok_entry=Entry(item_frame,textvariable=coke,width=30,bd=10,justify='right',state=DISABLED)
cok_entry.grid(row=4,column=1,padx=10,pady=10)
coke.set('0')

icecream=StringVar()
ice_entry=Entry(item_frame,textvariable=icecream,width=30,bd=10,justify='right',state=DISABLED)
ice_entry.grid(row=5,column=1,padx=10,pady=10)
icecream.set('0')

eco=StringVar()
eco_entry=Entry(item_frame,textvariable=eco,width=30,bd=10,justify='right',state=DISABLED)
eco_entry.grid(row=0,column=3,padx=10,pady=10)
eco.set('0')

deluxe=StringVar()
deluxe_entry=Entry(item_frame,textvariable=deluxe,width=30,bd=10,justify='right',state=DISABLED)
deluxe_entry.grid(row=1,column=3,padx=10,pady=10)
deluxe.set('0')

cost=StringVar()
cost_entry=Entry(item_frame,textvariable=cost,width=30,bd=10,justify='right')
cost_entry.grid(row=2,column=3,padx=10,pady=10)

sgst=StringVar()
sgst_entry=Entry(item_frame,textvariable=sgst,width=30,bd=10,justify='right')
sgst_entry.grid(row=3,column=3,padx=10,pady=10)

cgst=StringVar()
cgst_entry=Entry(item_frame,textvariable=cgst,width=30,bd=10,justify='right')
cgst_entry.grid(row=4,column=3,padx=10,pady=10)

total=StringVar()
total_entry=Entry(item_frame,textvariable=total,width=30,bd=10,justify='right')
total_entry.grid(row=5,column=3,padx=10,pady=10)

calc=StringVar()
calc_entery=Entry(cal_frame,textvariable=calc,width=42,bd=7,font=('lithograph',12,'bold'),justify='right')
calc_entery.grid(row=0,columnspan=4,padx=5,pady=5)

#buttons

price_btn=Button(item_frame,text='PRICE\nLIST',width=8,bd=10,font=('lithograph',18,'bold'),bg='orange',command=pricelist_func)
price_btn.grid(row=6,column=0,padx=10,pady=10)

total_btn=Button(item_frame,text='TOTAL',bd=10,width=8,font=('lithograph',25,'bold'),bg='GreenYellow',command=ref_func)
total_btn.grid(row=6,column=1,padx=10,pady=10)

reset_btn=Button(item_frame,text='RESET',bd=10,width=8,font=('lithograph',25,'bold'),bg='yellow',command=res_func)
reset_btn.grid(row=6,column=2,padx=10,pady=10)

exit_btn=Button(item_frame,text='EXIT',bd=10,width=8,font=('lithograph',25,'bold'),bg='red',command=exit_func)
exit_btn.grid(row=6,column=3,padx=10,pady=10)

reci_btn=Button(rec_btn_frame,text='RECIEPT',width=16,font=('lithograph',10,'bold'),bg='GreenYellow',command=reciept_func)
reci_btn.grid(row=0,column=0)

print_btn=Button(rec_btn_frame,text='PRINT',width=16,font=('lithograph',10,'bold'),bg='red')
print_btn.grid(row=0,column=1)

ord_btn=Button(rec_btn_frame,text='ORDER HIS.',width=15,font=('lithograph',10,'bold'),bg='yellow',command=order_his)
ord_btn.grid(row=0,column=2)

btnlist=['7','8','9','+','4','5','6','-','1','2','3','x','0','C','=','/']
commandlist=[lambda :btnclick(7),lambda :btnclick(8),lambda :btnclick(9),lambda :btnclick('+'),
             lambda :btnclick(4),lambda :btnclick(5),lambda :btnclick(6),lambda :btnclick('-'),
             lambda :btnclick(1),lambda :btnclick(2),lambda :btnclick(3),lambda :btnclick('*'),
             lambda :btnclick(0),reset_func,eval_func,lambda :btnclick('/'),]
count=0
for i in range(1,5):
    for j in range(4):
        calc_btn=Button(cal_frame,text=btnlist[count],bd=7,width=10,height=1,font=('lithograph',10,'bold'),command=commandlist[count])
        calc_btn.grid(row=i,column=j)
        count+=1

#textwidget

txt_reciept=Text(rec_frame,bg='white',bd=10,relief=RIDGE)
txt_reciept.pack(side=BOTTOM)

root.mainloop()
