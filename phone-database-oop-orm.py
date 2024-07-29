from tkinter import *
from tkinter import messagebox
from peewee import *

db = SqliteDatabase('phone-contact.db')

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    contact_code = IntegerField(primary_key=True)
    contact_name = TextField()
    contact_family = TextField()
    contact_phone = TextField()

db.connect()
db.create_tables([Contact])

    

class PhotoGUI(Tk):
    def __init__(self, title, geometry):
        Tk.__init__(self)
        self.title(title)
        self.geometry(geometry)
        self.img = PhotoImage()

    def create_canvas(self, image):
        self.img = PhotoImage(file=image)
        c1 = Canvas(self, width=300, height=300)
        c1.create_image(150, 150, image=self.img)
        c1.pack()

    def create_buttons(self):
        add = Button(self,
             text='add contact to phone',
             cursor='hand2',
             font=('arial', 12, 'bold'),
             bg='#ff0000',
             fg='black',
             command=self.add_contact)
        add.place(x=2, y=302, width=298, height=30)

        delete = Button(self,
                    text='delete contact from phone',
                    cursor='hand2',
                    font=('arial', 12, 'bold'),
                    bg='#ff2323',
                    fg='black',
                    command=self.delete_contact)
        delete.place(x=2, y=334, width=298, height=30)

        search = Button(self,
                    text='search contact in phone',
                    cursor='hand2',
                    font=('arial', 12, 'bold'),
                    bg='#ff4646',
                    fg='black',
                    command=self.search_contact)
        search.place(x=2, y=366, width=298, height=30)

        show = Button(self,
                    text='show all contact in phone',
                    cursor='hand2',
                    font=('arial', 12, 'bold'),
                    bg='#ff6968',
                    fg='black',
                    command=self.show_contact)
        show.place(x=2, y=398, width=298, height=30)

        about = Button(self,
                    text='about me',
                    cursor='hand2',
                    font=('arial', 12, 'bold'),
                    bg='#ff8c8c',
                    fg='black',
                    command=self.about_contact)
        about.place(x=2, y=430, width=298, height=30)

        exit = Button(self,
                    text='Exit',
                    cursor='hand2',
                    font=('arial', 12, 'bold'),
                    bg='#ffafaf',
                    fg='black',
                    command=self.exit_contact)
        exit.place(x=2, y=462, width=298, height=30)
    
    def add_contact(self):
        top = Toplevel()
        top.config(bg='IndianRed')
        top.title('add contact')
        top.geometry('300x120')

        def destroy_top():
            top.destroy()

        def submit_contact(e1, e2, e3):
            try:
                name = e1.get()
                family = e2.get()
                phone = e3.get()
                
                new_contact = Contact(contact_name=name, contact_family=family, contact_phone=phone)
                new_contact.save()
                messagebox.showinfo("Information", "Contact added successfully!")
                e1.delete(0, 'end')
                e2.delete(0, 'end')
                e3.delete(0, 'end')
                e1.focus()
            except:
                messagebox.showwarning("warning", "I have some error!")
        

        l1 = Label(top, text='Name:',
                    fg='black',
                    bg='DarkSalmon',
                     font=('arial', 12, 'bold'))
        l1.grid(row=0, column=0)

        e1 = Entry(top,
                    bg='DarkSalmon',
                    font=('arial', 12, 'bold'),
                    bd=3,
                    fg='black',
                     width=20)
        e1.grid(row=0, column=1, padx=5)

        l2 = Label(top,
                    text='Family:',
                    fg='black', 
                    bg='DarkSalmon',
                    font=('arial', 12, 'bold'))
        l2.grid(row=1, column=0)

        e2 = Entry(top, 
                   bg='DarkSalmon', 
                   fg='black',
                   font=('arial', 12, 'bold'), 
                   bd=3, 
                   width=20)
        e2.grid(row=1, column=1, padx=5)

        l3 = Label(top, 
                   text='phone:', 
                   fg='black',
                    bg='DarkSalmon', 
                    font=('arial', 12, 'bold'))
        l3.grid(row=2, column=0)

        e3 = Entry(top, 
                   bg='DarkSalmon', 
                   fg='black', 
                   font=('arial', 12, 'bold'), 
                   bd=3, 
                   width=20)
        e3.grid(row=2, column=1, padx=5)

        b1 = Button(top, 
                    text='Submit', 
                    bg='DarkSalmon', 
                    fg='black', 
                    bd=3, 
                    cursor='hand2',
                    font=('arial', 12, 'bold'), 
                    command=lambda: submit_contact(e1, e2, e3))
        b1.grid(row=3, column=1)

        b2 = Button(top, 
                    text='Exit', 
                    bg='DarkSalmon', 
                    fg='black', 
                    cursor='hand2', 
                    bd=3, 
                    font=('arial', 12, 'bold'),
                    command=destroy_top)
        b2.grid(row=3, column=0)
    
    def delete_contact(self):
        top = Toplevel()
        top.config(bg='IndianRed')
        top.title('delete contact')
        top.geometry('300x120')

        def destroy_top():
            top.destroy()

        def submit_delete_contact(e1, e2):
            try:
                code = e1.get()
                phone = e2.get()
                contact = Contact.get_or_none(Contact.contact_code == code, Contact.contact_phone == phone)
                if contact:
                    contact.delete_instance()
                    messagebox.showinfo("Information", "Contact deleted successfully!")
                    e1.delete(0, END)
                    e2.delete(0, END)
                    e1.focus()
                    
                else:
                    messagebox.showwarning("Warning", "Contact not found!")
            except Exception as e:
                messagebox.showwarning("Warning", "An error occurred!")

        

        l1 = Label(top, text='Code:',
                    fg='black',
                    bg='DarkSalmon',
                     font=('arial', 12, 'bold'))
        l1.grid(row=0, column=0)

        e1 = Entry(top,
                    bg='DarkSalmon',
                    font=('arial', 12, 'bold'),
                    bd=3,
                    fg='black',
                     width=20)
        e1.grid(row=0, column=1, padx=5)

        l2 = Label(top,
                    text='Phone:',
                    fg='black', 
                    bg='DarkSalmon',
                    font=('arial', 12, 'bold'))
        l2.grid(row=1, column=0)

        e2 = Entry(top, 
                   bg='DarkSalmon', 
                   fg='black',
                   font=('arial', 12, 'bold'), 
                   bd=3, 
                   width=20)
        e2.grid(row=1, column=1, padx=5)

        b1 = Button(top, 
                    text='Submit', 
                    bg='DarkSalmon', 
                    fg='black', 
                    bd=3, 
                    cursor='hand2',
                    font=('arial', 12, 'bold'), 
                    command=lambda: submit_delete_contact(e1, e2))
        b1.grid(row=2, column=1)

        b2 = Button(top, 
                    text='Exit', 
                    bg='DarkSalmon', 
                    fg='black', 
                    cursor='hand2', 
                    bd=3, 
                    font=('arial', 12, 'bold'),
                    command=destroy_top)
        b2.grid(row=2, column=0)


    def search_contact(self):
        top = Toplevel()
        top.config(bg='IndianRed')
        top.title('search contact')
        top.geometry('300x120')

        def destroy_top():
            top.destroy()


        def submit_search_contact(e1, e2):
            try:
                name = e1.get()
                family = e2.get()
                all_contact = Contact.select()
                contact = all_contact.where(Contact.contact_name == name, Contact.contact_family == family)
                if contact:
                   
                    for entry in contact:
                         a = entry.contact_name
                         b = entry.contact_family
                         c = entry.contact_phone
                         messagebox.showinfo(f"{a} {b}", f"phone number : {c}    !")
                    e1.delete(0, END)
                    e2.delete(0, END)
                    e1.focus()
                    
                else:
                    messagebox.showwarning("Warning", "Contact not found!")
            except Exception as e:
                print(e)
                messagebox.showwarning("Warning", "An error occurred!")

        l1 = Label(top, text='Name:',
                    fg='black',
                    bg='DarkSalmon',
                     font=('arial', 12, 'bold'))
        l1.grid(row=0, column=0)

        e1 = Entry(top,
                    bg='DarkSalmon',
                    font=('arial', 12, 'bold'),
                    bd=3,
                    fg='black',
                     width=20)
        e1.grid(row=0, column=1, padx=5)

        l2 = Label(top,
                    text='Family:',
                    fg='black', 
                    bg='DarkSalmon',
                    font=('arial', 12, 'bold'))
        l2.grid(row=1, column=0)

        e2 = Entry(top, 
                   bg='DarkSalmon', 
                   fg='black',
                   font=('arial', 12, 'bold'), 
                   bd=3, 
                   width=20)
        e2.grid(row=1, column=1, padx=5)

        b1 = Button(top, 
                    text='Submit', 
                    bg='DarkSalmon', 
                    fg='black', 
                    bd=3, 
                    cursor='hand2',
                    font=('arial', 12, 'bold'), 
                    command=lambda: submit_search_contact(e1, e2))
        b1.grid(row=2, column=1)

        b2 = Button(top, 
                    text='Exit', 
                    bg='DarkSalmon', 
                    fg='black', 
                    cursor='hand2', 
                    bd=3, 
                    font=('arial', 12, 'bold'),
                    command=destroy_top)
        b2.grid(row=2, column=0)

    def show_contact(self):
        top = Toplevel()
        top.config(bg='IndianRed')
        top.title('show all contact')
        top.geometry('305x300')

        def destroy_top():
            top.destroy()   

        e = Listbox(top, background='DarkSalmon', width=50)
        e.grid(row=0, column=0)
        all_show_contact = Contact.select().execute()
        for contact in all_show_contact:
            e.insert(END, f'{contact.contact_name} {contact.contact_family} : {contact.contact_phone}')
        b2 = Button(top, 
                text='Exit', 
                bg='DarkSalmon', 
                fg='black', 
                cursor='hand2', 
                bd=3, 
                font=('arial', 12, 'bold'),
                command=destroy_top)
        b2.grid(row=1, column=0)

    def about_contact(self):
        top = Toplevel()
        top.config(bg='IndianRed')
        top.title('about contact')
        top.geometry('305x300')

        l1 = Label(top, text='Created by Saman Ghasemi',
                    fg='black',
                    bg='DarkSalmon',
                     font=('arial', 12, 'bold'))
        l1.pack()
        
        l2 = Label(top, text='python advance',
                    fg='black',
                    bg='DarkSalmon',
                     font=('arial', 12, 'bold'))
        l2.pack()

        l3 = Label(top, text='MFT ekbatan',
                    fg='black',
                    bg='DarkSalmon',
                     font=('arial', 12, 'bold'))
        l3.pack()

    def exit_contact(self):
        messagebox.showinfo('GoodBye', 'See you later')
        self.destroy()
            
        


        

        


    



p1 = PhotoGUI('phoneBook', '300x494')
p1.create_canvas('phone-image.png')
p1.create_buttons()
p1.mainloop()