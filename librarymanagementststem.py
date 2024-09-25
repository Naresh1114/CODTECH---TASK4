from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # Sample Data Storage
        self.data = []

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # ============================= DataFrameLeft ============================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=12,
                                   relief=RIDGE, font=("times new roman", 14, "bold"))
        DataFrameLeft.place(x=0, y=5, width=860, height=350)

        self.member_type = StringVar()
        self.prn_no = StringVar()
        self.id_no = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.address1 = StringVar()
        self.address2 = StringVar()
        self.post_code = StringVar()
        self.mobile = StringVar()
        self.book_id = StringVar()
        self.book_title = StringVar()
        self.author = StringVar()
        self.date_borrowed = StringVar()
        self.date_due = StringVar()
        self.days_on_book = StringVar()
        self.late_return_fine = StringVar()
        self.date_overdue = StringVar()
        self.actual_price = StringVar()

        lblMember = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Member Type", padx=2, pady=6, bg="powder blue")
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_type, state="readonly", font=("arial", 12, "bold"), width=27)
        comMember["value"] = ("Admin staff", "Student", "Lecturer", "Principal")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        self.create_label_entry(DataFrameLeft, "PRN No:", self.prn_no, 1)
        self.create_label_entry(DataFrameLeft, "ID No:", self.id_no, 2)
        self.create_label_entry(DataFrameLeft, "First Name:", self.first_name, 3)
        self.create_label_entry(DataFrameLeft, "Last Name:", self.last_name, 4)
        self.create_label_entry(DataFrameLeft, "Address1:", self.address1, 5)
        self.create_label_entry(DataFrameLeft, "Address2:", self.address2, 6)
        self.create_label_entry(DataFrameLeft, "Post Code:", self.post_code, 7)
        self.create_label_entry(DataFrameLeft, "Mobile:", self.mobile, 8)

        self.create_label_entry(DataFrameLeft, "Book ID:", self.book_id, 0, 2)
        self.create_label_entry(DataFrameLeft, "Book Title:", self.book_title, 1, 2)
        self.create_label_entry(DataFrameLeft, "Author Name:", self.author, 2, 2)
        self.create_label_entry(DataFrameLeft, "Date Borrowed:", self.date_borrowed, 3, 2)
        self.create_label_entry(DataFrameLeft, "Date Due:", self.date_due, 4, 2)
        self.create_label_entry(DataFrameLeft, "Days On Book:", self.days_on_book, 5, 2)
        self.create_label_entry(DataFrameLeft, "Late Return Fine:", self.late_return_fine, 6, 2)
        self.create_label_entry(DataFrameLeft, "Date Overdue:", self.date_overdue, 7, 2)
        self.create_label_entry(DataFrameLeft, "Actual Price:", self.actual_price, 8, 2)

        # ========================== DataFrame Right =========================
        DataFrameRight = LabelFrame(frame, bd=12, padx=20, relief=RIDGE, bg="powder blue", font=("arial", 12, "bold"),
                                    text="Book Details")
        DataFrameRight.place(x=870, y=5, width=580, height=350)

        self.textBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.textBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        ListBooks = ['Head First Book', 'Learn Python the Hard Way', 'Python Programming', 'Secret Rahshy', 'Cookbook',
                     'Intro to Machine Learning', 'Web Development', 'Machine Learning', 'Machine Python', 'My Python',
                     'Intro Python', 'Advanced Python']

        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in ListBooks:
            listBox.insert(END, item)

        # ================================ Buttons Frame ==========================
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(FrameButton, text="Add Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.add_data)
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(FrameButton, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.show_data)
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(FrameButton, text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(FrameButton, text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.delete_data)
        btnDelete.grid(row=0, column=3)

        btnReset = Button(FrameButton, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.reset_data)
        btnReset.grid(row=0, column=4)

        btnExit = Button(FrameButton, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=root.quit)
        btnExit.grid(row=0, column=5)

        # ================================ Information Frame ==========================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1510, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, columns=("membertype", "prnno", "idno", "firstname", "lastname",
                                                                "address1", "address2", "postid", "mobile", "bookid",
                                                                "booktitle", "author", "dateborrowed", "datedue", "days",
                                                                "latereturnfine", "dateoverdue", "finalprice"),
                                           xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN NO.")
        self.library_table.heading("idno", text="ID No.")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author Name")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Overdue")
        self.library_table.heading("finalprice", text="Actual Price")
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table["show"] = "headings"

        # Bind the select event to the table
        self.library_table.bind("<ButtonRelease-1>", self.select_data)

    def create_label_entry(self, parent, label_text, variable, row, column=0):
        lbl = Label(parent, font=("arial", 12, "bold"), text=label_text, padx=2, pady=6, bg="powder blue")
        lbl.grid(row=row, column=column, sticky=W)
        entry = Entry(parent, font=("arial", 12, "bold"), textvariable=variable, width=30)
        entry.grid(row=row, column=column + 1)

    def add_data(self):
        member_data = (
            self.member_type.get(),
            self.prn_no.get(),
            self.id_no.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.address1.get(),
            self.address2.get(),
            self.post_code.get(),
            self.mobile.get(),
            self.book_id.get(),
            self.book_title.get(),
            self.author.get(),
            self.date_borrowed.get(),
            self.date_due.get(),
            self.days_on_book.get(),
            self.late_return_fine.get(),
            self.date_overdue.get(),
            self.actual_price.get()
        )
        self.data.append(member_data)
        self.reset_data()
        messagebox.showinfo("Success", "Data Added Successfully!")

    def show_data(self):
        for row in self.library_table.get_children():
            self.library_table.delete(row)
        for item in self.data:
            self.library_table.insert("", "end", values=item)

    def update_data(self):
        selected_item = self.library_table.focus()
        if not selected_item:
            messagebox.showwarning("Select Item", "Please select an item to update.")
            return
        updated_data = (
            self.member_type.get(),
            self.prn_no.get(),
            self.id_no.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.address1.get(),
            self.address2.get(),
            self.post_code.get(),
            self.mobile.get(),
            self.book_id.get(),
            self.book_title.get(),
            self.author.get(),
            self.date_borrowed.get(),
            self.date_due.get(),
            self.days_on_book.get(),
            self.late_return_fine.get(),
            self.date_overdue.get(),
            self.actual_price.get()
        )
        self.data[self.library_table.index(selected_item)] = updated_data
        self.reset_data()
        messagebox.showinfo("Success", "Data Updated Successfully!")

    def delete_data(self):
        selected_item = self.library_table.focus()
        if not selected_item:
            messagebox.showwarning("Select Item", "Please select an item to delete.")
            return
        self.data.pop(self.library_table.index(selected_item))
        self.reset_data()
        messagebox.showinfo("Success", "Data Deleted Successfully!")

    def reset_data(self):
        self.member_type.set("")
        self.prn_no.set("")
        self.id_no.set("")
        self.first_name.set("")
        self.last_name.set("")
        self.address1.set("")
        self.address2.set("")
        self.post_code.set("")
        self.mobile.set("")
        self.book_id.set("")
        self.book_title.set("")
        self.author.set("")
        self.date_borrowed.set("")
        self.date_due.set("")
        self.days_on_book.set("")
        self.late_return_fine.set("")
        self.date_overdue.set("")
        self.actual_price.set("")

    def select_data(self, event):
        selected_item = self.library_table.focus()
        if selected_item:
            values = self.library_table.item(selected_item, 'values')
            self.member_type.set(values[0])
            self.prn_no.set(values[1])
            self.id_no.set(values[2])
            self.first_name.set(values[3])
            self.last_name.set(values[4])
            self.address1.set(values[5])
            self.address2.set(values[6])
            self.post_code.set(values[7])
            self.mobile.set(values[8])
            self.book_id.set(values[9])
            self.book_title.set(values[10])
            self.author.set(values[11])
            self.date_borrowed.set(values[12])
            self.date_due.set(values[13])
            self.days_on_book.set(values[14])
            self.late_return_fine.set(values[15])
            self.date_overdue.set(values[16])
            self.actual_price.set(values[17])

if __name__ == "__main__":
    root = Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
    
