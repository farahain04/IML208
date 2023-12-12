import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as MessageBox

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Book Tracking System")

#win.config(bg="blue")

title_label = tk.Label(win, text="Book Tracking System", font=("Arial", 25, "bold"), border=12, relief=tk.GROOVE,bg="lightgrey")
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 20), bd=12, relief=tk.GROOVE, bg="lightgrey")
detail_frame.place(x=20, y=90, width=420, height=575)

data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=475, y=90, width=810, height=575)

# Function

def add_book():
    title = booktitle.get()
    author_value = author.get()
    isbn_value = ISBN.get()
    availability_value = availability.get()

    if not title or not author_value or not isbn_value or not availability_value:
        MessageBox.showwarning("Warning", "Please fill in all the details.")
        return

    user_table.insert("", "end", values=(title, author_value, isbn_value, availability_value))

    # Clear the entry widgets
    clear_entries()

    # Append the book details to original_books
    original_books.append({"values": (title, author_value, isbn_value, availability_value)})
    
    MessageBox.showinfo("Success", "Book added successfully")

def update_book():
    selected_item = user_table.selection()
    if not selected_item:
        MessageBox.showwarning("Warning", "Please select a book to update.")
        return

    title = booktitle.get()
    author_value = author.get()
    isbn_value = ISBN.get()
    availability_value = availability.get()

    user_table.item(selected_item, values=(title, author_value, isbn_value, availability_value))
    clear_entries()
    MessageBox.showinfo("Success", "Book updated successfully")

def delete_book():
    selected_item = user_table.selection()
    if not selected_item:
        MessageBox.showwarning("Warning", "Please select a book to delete.")
        return

    # Get the book details
    book_details = user_table.item(selected_item, "values")

    # Remove the book from original_books
    original_books[:] = [book for book in original_books if book["values"] != book_details]

    # Remove the book from the Treeview
    user_table.delete(selected_item)

    clear_entries()
    MessageBox.showinfo("Success", "Book deleted successfully")

def read_book():
    selected_item = user_table.selection()
    if not selected_item:
        MessageBox.showwarning("Warning", "Please select a book to read.")
        return

    book_details = user_table.item(selected_item, "values")
    clear_entries()
    MessageBox.showinfo("Book Details", f"Title: {book_details[0]}\nAuthor: {book_details[1]}\nISBN: {book_details[2]}\nAvailability: {book_details[3]}")

# Function to calculate average and show total availability
def calculate_average_and_total():
    total_availability = 0
    total_books = 0

    for book in original_books:
        values = book["values"]
        if values and values[3]:
            total_availability += int(values[3])
            total_books += 1

    average_availability = total_availability / total_books if total_books > 0 else 0

    MessageBox.showinfo("Availability Summary", f"Total Availability: {total_availability}\nTotal Books: {total_books}\nAverage Availability: {average_availability:.2f}")

original_books = [{"values": ("The Grass is Always Greener", "Jeffrey Archer", "1-86092-049-7", "1")},
                  {"values": ("Murder!", "Arnold Bennett", "1-86092-012-8", "1")},
                  {"values": ("A Boy at Seven", "John Bidwell", "1-86092-022-5", "1")},
                  {"values": ("The Higgler", "A. E. Coppard", "1-86092-010-1", "1")}]

def search_books():
    search_value = search_entry.get()

    if not search_value:
        MessageBox.showwarning("Warning", "Please enter a search value.")
        return

    found_books = []

    for book in original_books:
        if search_value.lower() in book["values"][0].lower():
            found_books.append(book)

    if not found_books:
        MessageBox.showinfo("No results found", "No books match your search term.")
        return

    display_search_results(found_books)

def show_all_books():
    display_search_results(original_books)

def display_search_results(results):
    user_table.delete(*user_table.get_children())  

    for result in results:
        user_table.insert("", "end", values=result["values"])

def clear_entries():
    booktitle.set("")
    author.set("")
    ISBN.set("")
    availability.set("")

#======== Variables ========#

booktitle = tk.StringVar()
author = tk.StringVar()
ISBN = tk.StringVar()
availability = tk.StringVar()

search_by = tk.StringVar()

#===============================#

# ========= ENTRY =========#

booktitle_lbl = tk.Label(detail_frame, text="Title :", font=("Arial", 17), bg="lightgrey")
booktitle_lbl.grid(row=0, column=0, padx=2, pady=2)

booktitle_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=booktitle, state='normal')
booktitle_ent.grid(row=0, column=1, padx=2, pady=2)

# Repeat the above pattern for other entry widgets (author, ISBN, availability)

author_lbl = tk.Label(detail_frame, text="Author :", font=("Arial", 17), bg="lightgrey")
author_lbl.grid(row=1, column=0, padx=2, pady=2)

author_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15),textvariable=author)
author_ent.grid(row=1, column=1, padx=2, pady=2)

ISBN_lbl = tk.Label(detail_frame, text="ISBN :", font=("Arial", 17), bg="lightgrey")
ISBN_lbl.grid(row=2, column=0, padx=2, pady=2)

ISBN_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15),textvariable=ISBN)
ISBN_ent.grid(row=2, column=1, padx=2, pady=2)

availability_lbl = tk.Label(detail_frame, text="Availability :", font=("Arial", 17), bg="lightgrey")
availability_lbl.grid(row=3, column=0, padx=2, pady=2)

availability_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15),textvariable=availability)
availability_ent.grid(row=3, column=1, padx=2, pady=2)

# =========================#

# ====== Buttons ==========#

btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=22, y=250, width=340, height=160)  # Increased the y coordinate

add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=15)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=15)
update_btn.grid(row=0, column=1, padx=3, pady=2)

delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=15)
delete_btn.grid(row=1, column=0, padx=2, pady=2)

read_btn = tk.Button(btn_frame, bg="lightgrey", text="Read", bd=7, font=("Arial", 13), width=15)
read_btn.grid(row=1, column=1, padx=3, pady=2)

availability_summary_btn = tk.Button(btn_frame, bg="lightgrey", text="Total Book", bd=7, font=("Arial", 13), width=20, command=calculate_average_and_total)
availability_summary_btn.grid(row=5, column=0, padx=3, pady=2, columnspan=2, sticky=tk.W+tk.E) 

# ======= Search =======#

search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="lightgrey", font=("Arial", 14))
search_lbl.grid(row=0, column=0, padx=12, pady=2)

# Entry widget for the search criteria
search_entry = tk.Entry(search_frame, font=("Arial", 14), textvariable=search_by)
search_entry.grid(row=0, column=1, padx=12, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=search_books)
search_btn.grid(row=0, column=2, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=show_all_books)
showall_btn.grid(row=0, column=3, padx=12, pady=2)

# =======================


# ====== database frame ====

main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

''' Title, Author, ISBN, Availability '''

user_table = ttk.Treeview(main_frame, columns=("Title", "Author", "ISBN", "Availability"), yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=user_table.yview)
x_scroll.config(command=user_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

user_table.heading("Title", text="Title")
user_table.heading("Author", text="Author")
user_table.heading("ISBN", text="ISBN")
user_table.heading("Availability", text="Availability")

user_table['show'] = 'headings'

user_table.column("Title", width=100)
user_table.column("Author", width=100)
user_table.column("ISBN", width=100)
user_table.column("Availability", width=100)

user_table.pack(fill=tk.BOTH, expand=True)

# ======================

def on_treeview_select(event):
    selected_item = user_table.selection()
    if selected_item:
        # Get the values of the selected item
        values = user_table.item(selected_item, "values")

        # Set the values to the StringVar variables
        booktitle.set(values[0])
        author.set(values[1])
        ISBN.set(values[2])
        availability.set(values[3])

# Bind the TreeviewSelect event to the on_treeview_select function
user_table.bind("<<TreeviewSelect>>", on_treeview_select)


# Configure button commands

add_btn.config(command=add_book)
update_btn.config(command=update_book)
delete_btn.config(command=delete_book)
read_btn.config(command=read_book)
search_btn.config(command=search_books)
showall_btn.config(command=show_all_books)

# Display the books in original_books in the Treeview
display_search_results(original_books)

#============================
win.mainloop()



