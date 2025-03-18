from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

def login():
    def check_credentials():
        username = user_entry.get()
        password = pass_entry.get()

        # Replace with your actual credentials
        if username == "admin" and password == "password":
            login_window.destroy()  # Close the login window
            main_window()  # Call the main application window
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    # Create login window
    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("400x250")
    login_window.resizable(0, 0)

    Label(login_window, text="Username", font=("Arial", 14)).pack(pady=10)
    user_entry = Entry(login_window, font=("Arial", 14))
    user_entry.pack(pady=5)

    Label(login_window, text="Password", font=("Arial", 14)).pack(pady=10)
    pass_entry = Entry(login_window, font=("Arial", 14), show='*')
    pass_entry.pack(pady=5)

    Button(login_window, text="Login", font=("Arial", 14), command=check_credentials).pack(pady=20)

    login_window.mainloop()
#fucntionality

def main_window():
    def clear():
        bathsoapEntry.delete(0, END)
        facepowderEntry.delete(0, END)
        facewashEntry.delete(0, END)
        foundationEntry.delete(0, END)
        hairgelEntry.delete(0, END)
        bodylotionEntry.delete(0, END)

        riceEntry.delete(0, END)
        sorghumEntry.delete(0, END)
        sugerEntry.delete(0, END)
        wheatEntry.delete(0, END)
        daalEntry.delete(0, END)
        oilEntry.delete(0, END)

        cupboardEntry.delete(0, END)
        bedEntry.delete(0, END)
        dresingtableEntry.delete(0, END)
        stoolEntry.delete(0, END)
        tableEntry.delete(0, END)
        showcaseEntry.delete(0, END)

        bathsoapEntry.insert(0, 0)
        facepowderEntry.insert(0, 0)
        facewashEntry.insert(0, 0)
        foundationEntry.insert(0, 0)
        hairgelEntry.insert(0, 0)
        bodylotionEntry.insert(0, 0)

        riceEntry.insert(0, 0)
        sorghumEntry.insert(0, 0)
        sugerEntry.insert(0, 0)
        wheatEntry.insert(0, 0)
        daalEntry.insert(0, 0)
        oilEntry.insert(0, 0)

        cupboardEntry.insert(0, 0)
        bedEntry.insert(0, 0)
        dresingtableEntry.insert(0, 0)
        stoolEntry.insert(0, 0)
        tableEntry.insert(0, 0)
        showcaseEntry.insert(0, 0)

        cosmeticpriceEntry.delete(0, END)
        grocerypriceEntry.delete(0, END)
        furniturepriceEntry.delete(0, END)

        cosmetictaxEntry.delete(0, END)
        grocerytaxEntry.delete(0, END)
        furnituretaxEntry.delete(0, END)

        nameEntry.delete(0, END)
        phoneEntry.delete(0, END)
        billnumberEntry.delete(0, END)

        textarea.delete(1.0, END)

    def send_email():
        def send_gmail():
            try:
                ob = smtplib.SMTP('smtp.gmail.com', 587)
                ob.starttls()
                ob.login(senderEntry.get(), passwordEntry.get())
                message = email_textarea.get(1.0, END)
                ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
                ob.quit()
                messagebox.showinfo('Success', 'Bill is successfully sent', parent=root1)
            except:
                messagebox.showinfo('Error', 'Somthing went wrong, Please try again', parent=root1)

        if textarea.get(1.0, END) == '\n':
            messagebox.showerror('Error', 'Bill is empty')
        else:

            root1 = Toplevel()
            root1.title('send Gmail')
            root1.config(bg='gray20')
            root1.resizable(0, 0)

            senderFrame = LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
            senderFrame.grid(row=0, column=0, padx=40, pady=20)

            senderLabel = Label(senderFrame, text="Sender's Email", font=('arial', 16, 'bold'), bg='gray20', fg='white')
            senderLabel.grid(row=0, column=0, padx=10, pady=8)

            senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
            senderEntry.grid(row=0, column=1, padx=10, pady=8)

            passwordLabel = Label(senderFrame, text="Password", font=('arial', 16, 'bold'), bg='gray20', fg='white')
            passwordLabel.grid(row=1, column=0, padx=10, pady=8, sticky='w')

            passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='#')
            passwordEntry.grid(row=1, column=1, padx=10, pady=8)

            recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20',
                                        fg='white')
            recipientFrame.grid(row=1, column=0, padx=40, pady=20)

            recieverLabel = Label(recipientFrame, text="Recipient's Email", font=('arial', 16, 'bold'), bg='gray20',
                                  fg='white')
            recieverLabel.grid(row=0, column=0, padx=10, pady=8, sticky='w')

            recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
            recieverEntry.grid(row=0, column=1, padx=10, pady=8)

            messageLabel = Label(recipientFrame, text="Message", font=('arial', 16, 'bold'), bg='gray20', fg='white')
            messageLabel.grid(row=1, column=0, padx=10, pady=8, sticky='w')

            email_textarea = Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN, width=48,
                                  height=18.3)
            email_textarea.grid(row=2, column=0, columnspan=2)
            email_textarea.delete(1.0, END)
            email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', ''))

            sendButton = Button(root1, text='SEND', font=('arial', 16, 'bold'), width=15, command=send_gmail)
            sendButton.grid(row=2, column=0, padx=10, pady=8)

    def print_bill():
        if textarea.get(1.0, END) == '\n':
            messagebox.showerror('Error', 'Bill is empty')
        else:
            file = tempfile.mktemp('.txt')
            open(file, 'w').write(textarea.get(1.0, END))
            os.startfile(file, 'print')



    def save_bill():
        global billnumber
        result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
        if result:
            bill_content = textarea.get(1.0, END)
            file = open(f'bills/ {billnumber}.txt', 'w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo('Success', f'Bill number {billnumber} is saved successfully')
            billnumber = random.randint(500, 1000)

    billnumber = random.randint(500, 1000)

    def bill_area():
        textarea.delete(1.0, END)
        if nameEntry.get() == '' or phoneEntry.get() == '':
            messagebox.showerror('Error', 'Customer Details Are Required')
        elif cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and furniturepriceEntry.get() == '':
            messagebox.showerror('Error', 'No Products Are Selected')
        elif cosmeticpriceEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and furniturepriceEntry.get() == '0 Rs':
            messagebox.showerror('Error', 'No Products Are Selected')

        else:
            textarea.insert(END, '\t\t**Welcome Customer**\n')
            textarea.insert(END, f'\nBill Number: {billnumber}')
            textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
            textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}')
            textarea.insert(END, '\n\n==========================================')
            textarea.insert(END, 'Product\t\tQuantity\t\tPrice')
            textarea.insert(END, '\n==========================================')
            if bathsoapEntry.get() != '0':
                textarea.insert(END, f'Bath Soap\t\t{bathsoapEntry.get()}\t\t{soapprice}')
            if facepowderEntry.get() != '0':
                textarea.insert(END, f'\nFace Powder\t\t{facepowderEntry.get()}\t\t{facepowderprice}')
            if facewashEntry.get() != '0':
                textarea.insert(END, f'\nFace Wash\t\t{facewashEntry.get()}\t\t{facewashprice}')
            if foundationEntry.get() != '0':
                textarea.insert(END, f'\nFoundation\t\t{foundationEntry.get()}\t\t{foundationprice}')
            if hairgelEntry.get() != '0':
                textarea.insert(END, f'\nHair Gel\t\t{hairgelEntry.get()}\t\t{hairgelprice}')
            if bodylotionEntry.get() != '0':
                textarea.insert(END, f'\nBody Lotion\t\t{bodylotionEntry.get()}\t\t{bodylotionprice}')

            if riceEntry.get() != '0':
                textarea.insert(END, f'\nRice\t\t{riceEntry.get()}\t\t{riceprice}')
            if oilEntry.get() != '0':
                textarea.insert(END, f'\nOil\t\t{oilEntry.get()}\t\t{oilprice}')
            if daalEntry.get() != '0':
                textarea.insert(END, f'\nDall\t\t{daalEntry.get()}\t\t{daalprice}')
            if sorghumEntry.get() != '0':
                textarea.insert(END, f'\nSorghum\t\t{sorghumEntry.get()}\t\t{sorghumprice}')
            if wheatEntry.get() != '0':
                textarea.insert(END, f'\nDall\t\t{wheatEntry.get()}\t\t{wheatprice}')
            if sugerEntry.get() != '0':
                textarea.insert(END, f'\nSugar\t\t{sugerEntry.get()}\t\t{sugarprice}')

            if tableEntry.get() != '0':
                textarea.insert(END, f'\nTable\t\t{tableEntry.get()}\t\t{tableprice}')
            if dresingtableEntry.get() != '0':
                textarea.insert(END, f'\nDressing Table\t\t{dresingtableEntry.get()}\t\t{dresingtableprice}')
            if bedEntry.get() != '0':
                textarea.insert(END, f'\nBed\t\t{bedEntry.get()}\t\t{bedprice}')
            if stoolEntry.get() != '0':
                textarea.insert(END, f'\nStool\t\t{stoolEntry.get()}\t\t{stoolprice}')
            if cupboardEntry.get() != '0':
                textarea.insert(END, f'\nCupboard\t\t{cupboardEntry.get()}\t\t{cupboardprice}')
            if showcaseEntry.get() != '0':
                textarea.insert(END, f'\nShowcase\t\t{showcaseEntry.get()}\t\t{showcaseprice}')
            textarea.insert(END, '\n\n------------------------------------------')

            if cosmetictaxEntry.get() != '0.0 Rs':
                textarea.insert(END, f'Cosmetic Tax\t\t{cosmetictaxEntry.get()}')
            if grocerytaxEntry.get() != '0.0 Rs':
                textarea.insert(END, f'\nGrocery Tax\t\t{grocerytaxEntry.get()}')
            if furnituretaxEntry.get() != '0.0 Rs':
                textarea.insert(END, f'\nFurniture Tax\t\t{furnituretaxEntry.get()}')
            textarea.insert(END, '\n------------------------------------------')
            textarea.insert(END, f'\nTotal Bill\t\t{totalbill}')
            save_bill()

    def total():
        global totalbill
        global tableprice, dresingtableprice, bedprice, stoolprice, cupboardprice, showcaseprice
        global riceprice, oilprice, daalprice, sorghumprice, wheatprice, sugarprice
        global facepowderprice, facewashprice, foundationprice, hairgelprice, bodylotionprice, soapprice
        # cosmeticprice calculation
        soapprice = int(bathsoapEntry.get()) * 20
        facepowderprice = int(facepowderEntry.get()) * 50
        facewashprice = int(facewashEntry.get()) * 60
        foundationprice = int(foundationEntry.get()) * 80
        hairgelprice = int(hairgelEntry.get()) * 70
        bodylotionprice = int(bodylotionEntry.get()) * 100

        totalcosmeticprice = soapprice + facepowderprice + facewashprice + foundationprice + hairgelprice + bodylotionprice
        cosmeticpriceEntry.delete(0, END)
        cosmeticpriceEntry.insert(0, f'{totalcosmeticprice} Rs')
        cosmetictax = totalcosmeticprice * 0.12
        cosmetictaxEntry.delete(0, END)
        cosmetictaxEntry.insert(0, f'{cosmetictax} Rs')

        # groceryprice calculation
        riceprice = int(riceEntry.get()) * 180
        oilprice = int(oilEntry.get()) * 220
        daalprice = int(daalEntry.get()) * 240
        sorghumprice = int(sorghumEntry.get()) * 200
        wheatprice = int(wheatEntry.get()) * 250
        sugarprice = int(sugerEntry.get()) * 150

        totalgroceryprice = riceprice + oilprice + daalprice + sorghumprice + wheatprice + sugarprice
        grocerypriceEntry.delete(0, END)
        grocerypriceEntry.insert(0, f'{totalgroceryprice} Rs')
        grocerytax = totalgroceryprice * 0.15
        grocerytaxEntry.delete(0, END)
        grocerytaxEntry.insert(0, f'{grocerytax} Rs')

        # Furnitureprice calculation
        tableprice = int(tableEntry.get()) * 500
        bedprice = int(bedEntry.get()) * 1000
        dresingtableprice = int(dresingtableEntry.get()) * 1500
        showcaseprice = int(showcaseEntry.get()) * 1200
        stoolprice = int(stoolEntry.get()) * 800
        cupboardprice = int(cupboardEntry.get()) * 1300

        totalfurnitureprice = tableprice + bedprice + dresingtableprice + showcaseprice + stoolprice + cupboardprice
        furniturepriceEntry.delete(0, END)
        furniturepriceEntry.insert(0, f'{totalfurnitureprice} Rs')
        furnituretax = totalfurnitureprice * 0.20
        furnituretaxEntry.delete(0, END)
        furnituretaxEntry.insert(0, f'{furnituretax} Rs')

        totalbill = totalfurnitureprice + totalcosmeticprice + totalgroceryprice + cosmetictax + grocerytax + furnituretax

    # GUI

    root = Tk()
    root.title('Retail Billing System')
    root.geometry('1270x685')
    headingLabel = Label(root, text='Billing System', font=('times new roman', 30, 'bold'), bg='gray20', fg='gold',
                         bd=12, relief=GROOVE)
    headingLabel.pack(fill=X)

    customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), fg='gold',
                                        bd=8, relief=GROOVE, bg='gray20')
    customer_details_frame.pack(fill=X)

    nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='gray20',
                      fg='white')
    nameLabel.grid(row=0, column=0, padx=20, )

    nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
    nameEntry.grid(row=0, column=1, padx=8)

    phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='gray20',
                       fg='white')
    phoneLabel.grid(row=0, column=2, padx=20, pady=2)

    phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
    phoneEntry.grid(row=0, column=3, padx=8)

    billnumberLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'),
                            bg='gray20', fg='white')
    billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

    billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
    billnumberEntry.grid(row=0, column=5, padx=8)

    searchButton = Button(customer_details_frame, text='CLEAR', font=('arial', 12, 'bold'), bd=7, width=10,
                          command=clear)
    searchButton.grid(row=0, column=6, padx=20, pady=8)

    productsFrame = Frame(root)
    productsFrame.pack(fill=X)

    cosmeticsFrame = LabelFrame(productsFrame, text='cosmetics', font=('times new roman', 15, 'bold'), fg='gold', bd=8,
                                relief=GROOVE, bg='gray20')
    cosmeticsFrame.grid(row=0, column=0)

    bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap ₹20', font=('times new roman', 12, 'bold'), bg='gray20',
                          fg='white')
    bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

    bathsoapEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    bathsoapEntry.grid(row=0, column=1, pady=9, padx=10)
    bathsoapEntry.insert(0, 0)

    facepowderLabel = Label(cosmeticsFrame, text='Face Powder ₹50', font=('times new roman', 12, 'bold'), bg='gray20',
                            fg='white')
    facepowderLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

    facepowderEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    facepowderEntry.grid(row=1, column=1, pady=9, padx=10)
    facepowderEntry.insert(0, 0)

    facewashLabel = Label(cosmeticsFrame, text='Face Wash ₹60', font=('times new roman', 12, 'bold'), bg='gray20',
                          fg='white')
    facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

    facewashEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    facewashEntry.grid(row=2, column=1, pady=9, padx=10)
    facewashEntry.insert(0, 0)

    foundationLabel = Label(cosmeticsFrame, text='Foundation ₹80', font=('times new roman', 12, 'bold'), bg='gray20',
                            fg='white')
    foundationLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

    foundationEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    foundationEntry.grid(row=3, column=1, pady=9, padx=10)
    foundationEntry.insert(0, 0)

    hairgelLabel = Label(cosmeticsFrame, text='Hair Gel ₹70', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

    hairgelEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
    hairgelEntry.insert(0, 0)

    bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion ₹100', font=('times new roman', 12, 'bold'), bg='gray20',
                            fg='white')
    bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

    bodylotionEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)
    bodylotionEntry.insert(0, 0)

    groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 15, 'bold'), fg='gold', bd=8,
                              relief=GROOVE, bg='gray20')
    groceryFrame.grid(row=0, column=1)

    riceLabel = Label(groceryFrame, text='Rice ₹180', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

    riceEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    riceEntry.grid(row=0, column=1, pady=9, padx=10)
    riceEntry.insert(0, 0)

    oilLabel = Label(groceryFrame, text='Oil ₹220', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

    oilEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    oilEntry.grid(row=1, column=1, pady=9, padx=10)
    oilEntry.insert(0, 0)

    daalLabel = Label(groceryFrame, text='Daal ₹240', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    daalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

    daalEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    daalEntry.grid(row=2, column=1, pady=9, padx=10)
    daalEntry.insert(0, 0)

    sorghumLabel = Label(groceryFrame, text='Sorghum ₹200', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    sorghumLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

    sorghumEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    sorghumEntry.grid(row=3, column=1, pady=9, padx=10)
    sorghumEntry.insert(0, 0)

    wheatLabel = Label(groceryFrame, text='Wheat ₹250', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    wheatLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

    wheatEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    wheatEntry.grid(row=4, column=1, pady=9, padx=10)
    wheatEntry.insert(0, 0)

    sugerLabel = Label(groceryFrame, text='Suger ₹150', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    sugerLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

    sugerEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    sugerEntry.grid(row=5, column=1, pady=9, padx=10)
    sugerEntry.insert(0, 0)

    furnitureFrame = LabelFrame(productsFrame, text='Furniture', font=('times new roman', 15, 'bold'), fg='gold', bd=8,
                                relief=GROOVE, bg='gray20')
    furnitureFrame.grid(row=0, column=2)

    tableLabel = Label(furnitureFrame, text='Table ₹500', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    tableLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

    tableEntry = Entry(furnitureFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    tableEntry.grid(row=0, column=1, pady=9, padx=10)
    tableEntry.insert(0, 0)

    bedLabel = Label(furnitureFrame, text='Bed ₹1000', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    bedLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

    bedEntry = Entry(furnitureFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    bedEntry.grid(row=1, column=1, pady=9, padx=10)
    bedEntry.insert(0, 0)

    dresingtableLabel = Label(furnitureFrame, text='Dressing Table ₹1500', font=('times new roman', 12, 'bold'), bg='gray20',
                              fg='white')
    dresingtableLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

    dresingtableEntry = Entry(furnitureFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    dresingtableEntry.grid(row=2, column=1, pady=9, padx=10)
    dresingtableEntry.insert(0, 0)

    showcaseLabel = Label(furnitureFrame, text='Showcase ₹1200', font=('times new roman', 12, 'bold'), bg='gray20',
                          fg='white')
    showcaseLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

    showcaseEntry = Entry(furnitureFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    showcaseEntry.grid(row=3, column=1, pady=9, padx=10)
    showcaseEntry.insert(0, 0)

    stoolLabel = Label(furnitureFrame, text='Stool ₹800', font=('times new roman', 12, 'bold'), bg='gray20', fg='white')
    stoolLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

    stoolEntry = Entry(furnitureFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    stoolEntry.grid(row=4, column=1, pady=9, padx=10)
    stoolEntry.insert(0, 0)

    cupboardLabel = Label(furnitureFrame, text='Cupboard ₹1300', font=('times new roman', 12, 'bold'), bg='gray20',
                          fg='white')
    cupboardLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

    cupboardEntry = Entry(furnitureFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    cupboardEntry.grid(row=5, column=1, pady=9, padx=10)
    cupboardEntry.insert(0, 0)

    billframe = Frame(productsFrame, bd=8, relief=GROOVE)
    billframe.grid(row=0, column=3, padx=10)

    billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=8, relief=GROOVE)
    billareaLabel.pack(fill=X)

    scrollbar = Scrollbar(billframe, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    textarea = Text(billframe, height=18.3, width=42, yscrollcommand=scrollbar.set)
    textarea.pack()

    scrollbar.config(command=textarea.yview)

    billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), fg='gold', bd=8,
                               relief=GROOVE, bg='gray20')
    billmenuFrame.pack(fill=X)

    cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic Price', font=('times new roman', 14, 'bold'), bg='gray20',
                               fg='white')
    cosmeticpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')

    cosmeticpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
    cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

    grocerypriceLabel = Label(billmenuFrame, text='Grocery Price', font=('times new roman', 14, 'bold'), bg='gray20',
                              fg='white')
    grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')

    grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
    grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

    furniturepriceLabel = Label(billmenuFrame, text='Furniture Price', font=('times new roman', 14, 'bold'),
                                bg='gray20', fg='white')
    furniturepriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')

    furniturepriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
    furniturepriceEntry.grid(row=2, column=1, pady=6, padx=10)

    cosmetictaxLabel = Label(billmenuFrame, text='Cosmetic Tax', font=('times new roman', 14, 'bold'), bg='gray20',
                             fg='white')
    cosmetictaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')

    cosmetictaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
    cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

    grocerytaxLabel = Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 14, 'bold'), bg='gray20',
                            fg='white')
    grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')

    grocerytaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
    grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

    furnituretaxLabel = Label(billmenuFrame, text='Furniture Tax', font=('times new roman', 14, 'bold'), bg='gray20',
                              fg='white')
    furnituretaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')

    furnituretaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
    furnituretaxEntry.grid(row=2, column=3, pady=6, padx=10)

    buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
    buttonFrame.grid(row=0, column=4, rowspan=3)

    totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                         pady=10, command=total)
    totalButton.grid(row=0, column=0, pady=20, padx=5)

    billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                        pady=10, command=bill_area)
    billButton.grid(row=0, column=1, pady=20, padx=5)

    emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                         pady=10, command=send_email)
    emailButton.grid(row=0, column=2, pady=20, padx=5)

    printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                         pady=10, command=print_bill)
    printButton.grid(row=0, column=3, pady=20, padx=5)

    clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                         pady=10, command=clear)
    clearButton.grid(row=0, column=4, pady=20, padx=5)

    root.mainloop()



login()
