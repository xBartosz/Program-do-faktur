from tkinter import *

class App():
    def __init__(self):
        self.root = Tk()
        root=self.root
        root.title("Apka")
        root.configure(bg='#273746')
        # self.screen_width = int(self.root.winfo_screenwidth()/2)
        # self.screen_height = int(self.root.winfo_screenheight()/2)
        # self.root.geometry('{}x{}'.format(self.screen_width, self.screen_height))
        root.geometry('500x500')
        self.Menu()

    def Menu(self):
        self.Menu_frame = Frame(self.root, height=500, width=500, bg="#273746")
        Menu_frame = self.Menu_frame
        Menu_frame.grid()
        Menu_frame.grid_propagate(0)
        Invoice_but = Button(Menu_frame, text="Issue an invoice", font="Rockwell 13",fg='#CCD1D1', bg='#273746')
        Invoice_but.grid(column=4, row=0)

        Add_cont_but = Button(Menu_frame, text="Add Contractor", font="Rockwell 13",fg='#CCD1D1', bg='#273746')
        Add_cont_but.grid(column=4, row=1)

        Settings_But = Button(Menu_frame, text="Settings", font="Rockwell 13",fg='#CCD1D1', bg='#273746')
        Settings_But.grid(column=4, row=2)

        Back_But = Button(Menu_frame, text="Back", font="Rockwell 13",fg='#CCD1D1', bg='#273746', command=lambda:self.Raise_frame(self.root))
        Back_But.grid(column=4, row=3)

    #
    # def Raise_frame(self):
    #     self.frame.tkraise()

    def Login_frame(self):
        root = self.root
        # self.Menu_frame
        # Login_frame = self.Login_frame
        # Login_frame = Frame(master=root, height=500, width=500, bg='#273746')
        # Login_frame.grid(columnspan=8, rowspan=8)

        welcome_text = Label(master=root, text="Welcome in xxx", font="Rockwell 15 bold", fg='#CCD1D1', bg='#273746')
        welcome_text.grid(column=3, row=0,sticky=NS, pady=(0,40))

        Login_lab = Label(master=root, text="Login:", font="Rockwell", fg='#CCD1D1', bg='#273746')
        Login_lab.grid(column=3, row=2, sticky=NS, pady=5)

        Login_ent = Entry(master=root, width=20)
        Login_ent.grid(column=5, row=2, sticky=NS, pady=5)

        Pass_lab = Label(master=root, text="Password:", font="Rockwell", fg='#CCD1D1', bg='#273746')
        Pass_lab.grid(column=3, row=4, sticky=NS, pady=5)

        Pass_ent = Entry(master=root, width=20, show='*')
        Pass_ent.grid(column=5, row=4, sticky=NS, pady=5)

        Log_but_text=StringVar()
        Log_but=Button(master=root, textvariable=Log_but_text, font="Bebas 13", fg='#CCD1D1', bg='#273746', command=lambda:self.Raise_frame(self.Menu_frame))
        Log_but.grid(column=5, row=6, pady=(40,0))
        Log_but_text.set('Login')



    def __del__(self):
        self.root.mainloop()

App()