from tkinter import *
import mysql.connector
from tkcalendar import DateEntry
from datetime import timedelta, datetime
from tkinter import ttk
from DbConnector import DbConnector

class App():
    def __init__(self):
        self.dbConnector = DbConnector()
        self.background_color = '#273746'
        self.foreground_color = '#CCD1D1'
        self.basic_font = 'Rockwell 13'
        self.root = Tk()
        self.root.title("Apka")
        # self.root.configure(bg=self.background_color)
        self.screen_width = int(self.root.winfo_screenwidth() / 2)
        self.screen_height = int(self.root.winfo_screenheight() / 2)
        self.root.geometry('{}x{}'.format(self.screen_width, self.screen_height))
        self.login()
        self.root.resizable(width=False, height=False)
        self.root.mainloop()


    def darkmode(self):
        self.background_color = '#273746'
        self.foreground_color = '#CCD1D1'

    def lightmode(self):
        self.background_color = '#EAEDED'
        self.foreground_color = '#424949'

    def logowanie(self):
        entered_login = self.Login_ent.get()
        entered_password = self.Pass_ent.get()
        if entered_login and entered_password != "":
            query = f"SELECT * FROM acc WHERE login='{entered_login}' and password='{entered_password}'"
            self.dbConnector.get_cursor().execute(query)
            self.Empty = None
            if self.Empty != None:
                self.Empty.grid_forget()
            wrong = Label(self.Login_frame, text="Wrong Data", font=self.basic_font, fg=self.foreground_color,
                          bg=self.background_color)
            wrong.grid(row=8, column=5, sticky=NS, pady=30)
            for i in self.dbConnector.get_cursor():
                if i != "":
                    success = Label(self.Login_frame, text="Login Successfull", font="Bebas 13",
                                    fg=self.foreground_color,
                                    bg=self.background_color)
                    success.grid(row=8, column=5, sticky=NS, pady=30)
                    self.Login_frame.grid_forget()
                    self.menu()
                else:
                    print("nie")

        else:
            self.Empty = Label(self.Login_frame, text="Enter your data", font=self.basic_font, fg=self.foreground_color,
                               bg=self.background_color)
            self.Empty.grid(row=8, column=5, sticky=NS, pady=30)

    def add_cont_func(self):
        self.cont_list = [self.Name_ent.get(), self.Address_ent.get(), self.Nip_ent.get(), self.Email_ent.get(), self.Phone_ent.get(), self.Bank_ent.get()]
        if len(self.cont_list) == 6:
            query = f"Insert Into Contrahents(Company_name, Address, Nip, Email, Phone, Bank_number) Values('{self.cont_list[0]}', '{self.cont_list[1]}', " \
                    f"'{self.cont_list[2]}', '{self.cont_list[3]}', '{self.cont_list[4]}', '{self.cont_list[5]}')"
            print(self.cont_list)
            print(query)
            self.dbConnector.get_cursor().execute(query)
            self.dbConnector.commit()
            success = Label(self.Contrahent_frame, text="Contrahent has been added successfully", font=self.basic_font,
                            fg=self.foreground_color, bg=self.background_color)
            success.grid(column=4, row=9)


    def showing_contrahents(self):
        self.show_cont_list = []
        query = "Select * from contrahents"
        self.dbConnector.get_cursor().execute(query)
        result = self.dbConnector.get_cursor().fetchall()
        for row in result:
            self.show_cont_list.append(row[0])


    def Autoincrementmysql(self, e):
        query = f"Select * from contrahents where Company_name='{self.Contrahents_box.get()}'"
        self.dbConnector.get_cursor().execute(query)

        result = self.dbConnector.get_cursor().fetchall()
        for row in result:
            self.Address.set(row[1])
            self.Nip.set(row[2])
            self.Email.set(row[3])
            self.Phone.set(row[4])
            self.Bank.set(row[5])


    def login(self):
        self.Login_frame = Frame(self.root, height=self.screen_height, width=self.screen_width,
                                 bg=self.background_color)
        self.Login_frame.grid()
        self.Login_frame.grid_propagate(0)

        welcome_text = Label(master=self.Login_frame, text="Welcome in xxx", font="Rockwell 15 bold",
                             fg=self.foreground_color, bg=self.background_color)
        welcome_text.grid(columnspan=3, column=0, row=0, sticky=NS, pady=(0, 40))

        Login_lab = Label(master=self.Login_frame, text="Login:", font=self.basic_font, fg=self.foreground_color,
                          bg=self.background_color)
        Login_lab.grid(column=0, row=1, sticky=NS, pady=5)
        tak = StringVar()
        tak.set("and")
        self.Login_ent = Entry(master=self.Login_frame, width=20, textvariable=tak)
        self.Login_ent.grid(column=1, row=1, sticky=NS, padx=(0, 0), pady=5)

        Pass_lab = Label(master=self.Login_frame, text="Password:", font=self.basic_font, fg=self.foreground_color,
                         bg=self.background_color)
        Pass_lab.grid(column=0, row=2, sticky=NS, pady=5)

        tak1 = StringVar()
        tak1.set("sd")
        self.Pass_ent = Entry(master=self.Login_frame, width=20, show='*', textvariable=tak1)
        self.Pass_ent.grid(column=1, row=2, sticky=NS, pady=5)

        Log_but_text = StringVar()
        Log_but = Button(master=self.Login_frame, textvariable=Log_but_text, font=self.basic_font,
                         fg=self.foreground_color, bg=self.background_color, command=self.logowanie)
        Log_but.grid(column=1, row=3, pady=(40, 0))
        Log_but_text.set('Login')

    def menu(self):
        self.Menu_frame = Frame(self.root, height=self.screen_height, width=self.screen_width, bg=self.background_color)
        self.Menu_frame.grid()
        self.Menu_frame.grid_propagate(0)
        Invoice_but = Button(self.Menu_frame, text="Issue an invoice", font=self.basic_font, fg=self.foreground_color,
                             bg=self.background_color,
                             command=lambda: [(self.Menu_frame.grid_forget(), self.issue_an_invoice())])
        Invoice_but.grid(column=4, row=0)

        Add_cont_but = Button(self.Menu_frame, text="Add Contrahent", font=self.basic_font, fg=self.foreground_color,
                              bg=self.background_color,
                              command=lambda: [(self.Menu_frame.grid_forget(), self.addcont())])
        Add_cont_but.grid(column=4, row=1)

        Add_item_but = Button(self.Menu_frame, text="Add item", font=self.basic_font, fg=self.foreground_color,
                              bg=self.background_color, command=lambda:[(self.Menu_frame.grid_forget(), self.additem())])
        Add_item_but.grid(column=4, row=2)

        Settings_But = Button(self.Menu_frame, text="Settings", font=self.basic_font, fg=self.foreground_color,
                              bg=self.background_color,
                              command=lambda: [(self.Menu_frame.grid_forget(), self.settings())])
        Settings_But.grid(column=4, row=3)

        Back_But = Button(self.Menu_frame, text="Log out", font=self.basic_font, fg=self.foreground_color,
                          bg=self.background_color,
                          command=lambda: [(self.Menu_frame.grid_forget(), self.login())])
        Back_But.grid(column=4, row=4)

    def issue_an_invoice(self):
        def my_upd(*args):  # triggered when value of string varaible changes
            dt = sel.get()  # cal.selection_get() # minmum date
            if (len(dt) > 3):  # when dt is having date selection
                dt1 = datetime.strptime(dt, '%d-%m-%Y')  # create date type
                dt2 = dt1 + timedelta(days=10)  # maximum date, added 10 days
                Invoice_sell_cal.config(mindate=dt1)  # set minimum date
                Invoice_sell_cal.config(maxdate=dt2)  # set maximum date

        sel = StringVar()
        self.Address = StringVar()
        self.Nip = StringVar()
        self.Email = StringVar()
        self.Phone = StringVar()
        self.Bank = StringVar()

        def clear():
            self.Address.set("")
            self.Nip.set("")
            self.Email.set("")
            self.Phone.set("")
            self.Bank.set("")

        self.showing_contrahents()

        self.Invoice_frame = Frame(self.root, height=self.screen_height, width=self.screen_width,
                                   bg=self.background_color)
        self.Invoice_frame.grid()
        self.Invoice_frame.grid_propagate(0)

        Invoice_name_text = Label(self.Invoice_frame, text="Invoice name: ", font=self.basic_font,
                                  fg=self.foreground_color,
                                  bg=self.background_color)
        Invoice_name_text.grid(column=0, row=0, pady=(30, 0))

        self.Invoice_name_ent = Entry(self.Invoice_frame, width=30)
        self.Invoice_name_ent.grid(column=1, row=0, pady=(30, 0))

        Invoice_issue_date_text = Label(self.Invoice_frame, text="Date of issue:", font=self.basic_font,
                                        fg=self.foreground_color,
                                        bg=self.background_color)
        Invoice_issue_date_text.grid(column=0, row=1, pady=20)

        Invoice_issue_cal = DateEntry(self.Invoice_frame, date_pattern='dd-mm-y', textvariable=sel)
        Invoice_issue_cal.grid(column=1, row=1)

        Invoice_sell_date_text = Label(self.Invoice_frame, text="Date of sell:", font=self.basic_font,
                                       fg=self.foreground_color,
                                       bg=self.background_color)
        Invoice_sell_date_text.grid(column=0, row=2, pady=20)

        Invoice_sell_cal = DateEntry(self.Invoice_frame, date_pattern='dd-mm-y', selectmode='day')
        Invoice_sell_cal.grid(column=1, row=2)

        Contrahents_text = Label(self.Invoice_frame, text="Contrahents:", font=self.basic_font, fg=self.foreground_color,
                                 bg=self.background_color)
        Contrahents_text.grid(column=2, row=0, padx=10)

        self.Contrahents_box = ttk.Combobox(self.Invoice_frame, value=self.show_cont_list)
        self.Contrahents_box.grid(column=3, row=0)

        self.Contrahents_box.bind("<<ComboboxSelected>>", self.Autoincrementmysql)

        Contrahent_address_text = Label(self.Invoice_frame, text="Address", font=self.basic_font,
                                        fg=self.foreground_color,
                                        bg=self.background_color)
        Contrahent_address_text.grid(column=2, row=1)

        Contrahent_address = Entry(self.Invoice_frame, width=30, textvariable=self.Address)
        Contrahent_address.grid(column=3, row=1)

        Contrahent_nip_text = Label(self.Invoice_frame, text="Nip", font=self.basic_font, fg=self.foreground_color,
                                    bg=self.background_color)
        Contrahent_nip_text.grid(column=2, row=2)

        Contrahent_nip = Entry(self.Invoice_frame, width=30, textvariable=self.Nip)
        Contrahent_nip.grid(column=3, row=2)

        Contrahent_email_text = Label(self.Invoice_frame, text="E-mail", font=self.basic_font, fg=self.foreground_color,
                                      bg=self.background_color)
        Contrahent_email_text.grid(column=2, row=3)

        Contrahent_email = Entry(self.Invoice_frame, width=30, textvariable=self.Email)
        Contrahent_email.grid(column=3, row=3)

        Contrahent_Phone_text = Label(self.Invoice_frame, text="Phone Number", font=self.basic_font,
                                      fg=self.foreground_color,
                                      bg=self.background_color)
        Contrahent_Phone_text.grid(column=2, row=4)

        Contrahent_Phone = Entry(self.Invoice_frame, width=30, textvariable=self.Phone)
        Contrahent_Phone.grid(column=3, row=4)

        Contrahent_Bank_text = Label(self.Invoice_frame, text="Account number", font=self.basic_font,
                                     fg=self.foreground_color,
                                     bg=self.background_color)
        Contrahent_Bank_text.grid(column=2, row=5)

        Contrahent_Bank = Entry(self.Invoice_frame, width=30, textvariable=self.Bank)
        Contrahent_Bank.grid(column=3, row=5)

        Invoice_back_but = Button(self.Invoice_frame, text="Back", font=self.basic_font, fg=self.foreground_color,
                                  bg=self.background_color,
                                  command=lambda: [(self.Invoice_frame.grid_forget(), self.menu())])
        Invoice_back_but.grid(column=3, row=6, pady=(20, 0), padx=0)

        Invoice_clear_but = Button(self.Invoice_frame, text="Clear", font=self.basic_font, fg=self.foreground_color,
                                   bg=self.background_color, command=clear)
        Invoice_clear_but.grid(column=4, row=6, pady=(20, 0), padx=0)

        sel.trace('w', my_upd)

        # nazwa faktury, data wystawienia/sprzedaży, ile vatu, contrahent's autoincrement, przedmioty

    def settings(self):
        self.Settings_frame = Frame(self.root, height=self.screen_height, width=self.screen_width,
                                    bg=self.background_color)
        self.Settings_frame.grid()
        self.Settings_frame.grid_propagate(0)

        dark_mode = Button(master=self.Settings_frame, text="Dark mode", font=self.basic_font, fg=self.foreground_color,
                           bg=self.background_color,
                           command=lambda: [(self.Settings_frame.grid_forget(), self.darkmode(), self.settings())])
        dark_mode.grid(column=3, row=0, sticky=NS, pady=5)

        light_mode = Button(master=self.Settings_frame, text="Light mode", font=self.basic_font, fg=self.foreground_color,
                            bg=self.background_color,
                            command=lambda: [(self.Settings_frame.grid_forget(), self.lightmode(), self.settings())])
        light_mode.grid(column=3, row=1, sticky=NS, pady=5)

        Back_But = Button(self.Settings_frame, text="Back to menu", font=self.basic_font, fg=self.foreground_color,
                          bg=self.background_color,
                          command=lambda: [self.Settings_frame.grid_forget(), self.menu()])
        Back_But.grid(column=3, row=2)

    def addcont(self):
        self.Contrahent_frame = Frame(self.root, height=self.screen_height, width=self.screen_width,
                                      bg=self.background_color)
        self.Contrahent_frame.grid()
        self.Contrahent_frame.grid_propagate(0)

        Contrahent_text = Label(self.Contrahent_frame, text="Adding Contrahent", font="Rockwell 15 bold",
                                fg=self.foreground_color, bg=self.background_color)
        Contrahent_text.grid(column=5, row=0)

        # Nazwa, adres, nip, e-mail, Telefon
        Name_text = Label(self.Contrahent_frame, text="Name", font=self.basic_font, fg=self.foreground_color,
                          bg=self.background_color)
        Name_text.grid(column=3, row=1)

        self.Name_ent = Entry(self.Contrahent_frame, width=30)
        self.Name_ent.grid(column=4, row=1)

        Address_text = Label(self.Contrahent_frame, text="Address", font=self.basic_font, fg=self.foreground_color,
                             bg=self.background_color)
        Address_text.grid(column=3, row=2)

        self.Address_ent = Entry(self.Contrahent_frame, width=30)
        self.Address_ent.grid(column=4, row=2)

        Nip_text = Label(self.Contrahent_frame, text="Nip", font=self.basic_font, fg=self.foreground_color,
                         bg=self.background_color)
        Nip_text.grid(column=3, row=3)

        self.Nip_ent = Entry(self.Contrahent_frame, width=30)
        self.Nip_ent.grid(column=4, row=3)

        Email_text = Label(self.Contrahent_frame, text="E-mail address", font=self.basic_font, fg=self.foreground_color,
                           bg=self.background_color)
        Email_text.grid(column=3, row=4)

        self.Email_ent = Entry(self.Contrahent_frame, width=30)
        self.Email_ent.grid(column=4, row=4)

        Phone_text = Label(self.Contrahent_frame, text="Phone number", font=self.basic_font, fg=self.foreground_color,
                           bg=self.background_color)
        Phone_text.grid(column=3, row=5)

        self.Phone_ent = Entry(self.Contrahent_frame, width=30)
        self.Phone_ent.grid(column=4, row=5)

        Bank_text = Label(self.Contrahent_frame, text="Bank Account", font=self.basic_font, fg=self.foreground_color,
                          bg=self.background_color)
        Bank_text.grid(column=3, row=6)

        self.Bank_ent = Entry(self.Contrahent_frame, width=30)
        self.Bank_ent.grid(column=4, row=6)

        Add_but = Button(self.Contrahent_frame, text="Add", font=self.basic_font, fg=self.foreground_color,
                         bg=self.background_color, command=self.add_cont_func)
        Add_but.grid(column=4, row=7)

        Cont_back_but = Button(self.Contrahent_frame, text="Back", font=self.basic_font, fg=self.foreground_color,
                               bg=self.background_color,
                               command=lambda: [(self.Contrahent_frame.grid_forget(), self.menu())])
        Cont_back_but.grid(column=4, row=8)

    def additem(self):

        #kategorie
        categories = ["Biżuteria", "Broń", "Kosmetyki", "Meble", "Narzędzia", "Sprzęt RTV", "Odzież", "Elektronika"]


        #quantity, kategoria, Nazwa prezdmiotu, cena
        self.Additem_frame = Frame(self.root, width=self.screen_width, height=self.screen_height, bg=self.background_color)
        self.Additem_frame.grid()
        self.Additem_frame.grid_propagate(0)

        Item_Name_text = Label(self.Additem_frame, text="Name:", font=self.basic_font, fg=self.foreground_color, bg=self.background_color)
        Item_Name_text.grid(column=0, row=0)

        self.Item_Name_Ent = Entry(self.Additem_frame, width=30)
        self.Item_Name_Ent.grid(column=1, row=0)

        Category_text = Label(self.Additem_frame, text="Category: ", font=self.basic_font, fg=self.foreground_color, bg=self.background_color)
        Category_text.grid(column=0, row=1)

        self.Category_Box = ttk.Combobox(self.Additem_frame, value=categories)
        self.Category_Box.grid(column=1, row=1)

        Quantity_text = Label(self.Additem_frame, text="Quantity:", font=self.basic_font, fg=self.foreground_color, bg=self.background_color)
        Quantity_text.grid(column=0, row=2)

        self.Quantity_ent = Entry(self.Additem_frame, width=30)
        self.Quantity_ent.grid(column=1, row=2)

        Price_text = Label(self.Additem_frame, text="Price:", font=self.basic_font, fg=self.foreground_color, bg=self.background_color)
        Price_text.grid(column=0, row=3)

        self.Price_ent = Entry(self.Additem_frame, width=30)
        self.Price_ent.grid(column=1, row=3)

        Back = Button(self.Additem_frame, text="Back", font=self.basic_font, fg=self.foreground_color,
                      bg=self.background_color, command=lambda:[(self.Additem_frame.grid_forget(), self.menu())])
        Back.grid(column=1, row=4)

        Add = Button(self.Additem_frame, text="Add", font=self.basic_font, fg=self.foreground_color, bg=self.background_color, command=self.item_to_base)
        Add.grid(column=2, row=4)


    def item_to_base(self):
        query = f"Insert Into items(Item_name, Category, Quantity, Price) Values('{self.Item_Name_Ent.get()}', '{self.Category_Box.get()}', '{self.Quantity_ent.get()}', '{self.Price_ent.get()}')"
        self.dbConnector.get_cursor().execute(query)
        self.dbConnector.commit()
        Label(self.Additem_frame, text="Added successfully", font=self.basic_font, fg=self.foreground_color, bg=self.background_color)

    def __del__(self):
        self.dbConnector.get_cursor().close()
        self.dbConnector.close()

App()


