from tkinter import *
from tkinter import ttk
import time
from view.new_b import newbookings
from view.bookings_ import bookings
from Driver.add_new_driver import addnew_driver
from account.create_new_account import new_account


def close_tab(event):
    index = notebook.index("@%d,%d" % (event.x, event.y))
    if index != -1:
        notebook.forget(index)

def show_menu(event):
    menu = Menu(notebook, tearoff=0)
    menu.add_command(label="Close", command=lambda: close_tab(event))
    menu.post(event.x_root, event.y_root)


def home():
    main_frame = Frame(notebook, width=screen_width, height=screen_height)
    notebook.add(main_frame, text="Home")
    display_canvas = Canvas(main_frame, width=(screen_width - 45), height=(screen_height - 207), background="yellow")
    display_canvas.grid(row=1, column=0)
    # frames_ onjob _______________________________________________________________________
    onjob_frame = Frame(display_canvas, bg="red")
    onjob_frame.place(x=10, y=10, width=((screen_width // 3) - 10), height=300)
    onjobs_frame = ttk.Frame(onjob_frame)
    onjobs_frame.config(borderwidth=2, relief="sunken")

    # Add a scrollbar to the frame
    scrollbar = ttk.Scrollbar(onjobs_frame)
    scrollbar.pack(side="right", fill=Y)

    onjobs_table = ttk.Treeview(onjobs_frame, show="headings", yscrollcommand=scrollbar.set)
    onjobs_table["columns"] = (
        "driver_no", "customer_name", "pickup_point", "driver_position", "job_status")
    onjobs_table.heading("driver_no", text="Driver No")
    onjobs_table.heading("customer_name", text="Customer Name")
    onjobs_table.heading("pickup_point", text="Pickup Point")
    onjobs_table.heading("driver_position", text="Driver Position")
    onjobs_table.heading("job_status", text="Job Status")

    # set the width of columns and make them resizable
    onjobs_table.column("driver_no", width=60, stretch=NO, minwidth=20, anchor='center')
    onjobs_table.column("customer_name", width=70, stretch=NO, minwidth=50, anchor='center')
    onjobs_table.column("pickup_point", width=100, stretch=NO, minwidth=50, anchor='center')
    onjobs_table.column("driver_position", width=100, stretch=NO, minwidth=50, anchor='center')
    onjobs_table.column("job_status", width=100, stretch=NO, minwidth=50, anchor='center')

    onjobs_table.pack(expand=True, fill=BOTH)

    # attach the scrollbar to the table
    scrollbar.config(command=onjobs_table.yview)

    onjobs_frame.pack(expand=True, fill=BOTH)
    # ________________________________________________________________
    availables_frame = Frame(display_canvas, bg="green")
    availables_frame.place(x=(screen_width // 3) + 10, y=10, width=((screen_width // 3) - 10), height=300)
    available_frame = ttk.Frame(availables_frame)
    available_frame.config(borderwidth=2, relief="sunken")
    # adding scroll bar
    available_scrollbar = ttk.Scrollbar(available_frame, orient="vertical")
    # Table
    available_table = ttk.Treeview(available_frame, show="headings", yscrollcommand=available_scrollbar.set)
    available_table["columns"] = ("driver_no", "driver_name", "driver_position", "waiting_time")
    available_table.heading("driver_no", text="Driver No")
    available_table.heading("driver_name", text="Driver Name")
    available_table.heading("driver_position", text="Driver Position")
    available_table.heading("waiting_time", text="Waiting Time")
    # set the width of columns and make them resizable
    available_table.column("driver_no", width=60, stretch=NO, minwidth=20, anchor='center')
    available_table.column("driver_name", width=70, stretch=NO, minwidth=50, anchor='center')
    available_table.column("driver_position", width=100, stretch=NO, minwidth=50, anchor='center')
    available_table.column("waiting_time", width=100, stretch=NO, minwidth=50, anchor='center')
    # pack the table and scrollbar
    available_table.pack(side="left", expand=True, fill=BOTH)
    available_scrollbar.pack(side="right", fill=Y)
    # attach the scrollbar to the table
    available_scrollbar.config(command=available_table.yview)
    # pack the frame
    available_frame.pack(side="left", expand=True, fill=BOTH)
    # ____________________________PLOTING______________________________________
    plotting_frame = Frame(display_canvas, bg="blue")
    plotting_frame.place(x=((screen_width // 3) * 2) + 10, y=10, width=((screen_width // 3) - 60), height=300)

    # Create an empty list to store column names
    columns = []

    # Retrieve plot names from the database
    plot_names = ["Plot1", "Plot2", "Plot3", "Plot4"]

    # Create a treeview with columns
    table = ttk.Treeview(plotting_frame, columns=plot_names, show="headings")
    table.pack(side="left", fill="both", expand=True)

    # Set the column headings
    for i in range(len(plot_names)):
        table.heading("#" + str(i + 1), text=plot_names[i])

    # set the width of columns and make them resizable
    for i in range(len(plot_names)):
        table.column("#" + str(i + 1), width=100, stretch=NO, minwidth=50, anchor='center')

    # Add a scrollbar to the treeview
    scrollbar = ttk.Scrollbar(plotting_frame, orient="vertical", command=table.yview)
    scrollbar.pack(side="right", fill="y")
    table.configure(yscrollcommand=scrollbar.set)

    # Retrieve driver data for each plot from the database
    plot1_drivers = [("Driver1", "Driver2"), ("Driver3", "Driver4")]
    plot2_drivers = [("Driver5", "Driver6"), ("Driver7", "Driver8")]
    plot3_drivers = [("Driver9", "Driver10"), ("Driver11", "Driver12")]
    plot4_drivers = [("Driver13", "Driver14"), ("Driver15", "Driver16")]

    # Insert the driver data into the treeview
    for i in range(len(plot1_drivers)):
        table.insert("", "end",
                     values=(plot1_drivers[i][0], plot2_drivers[i][0], plot3_drivers[i][0], plot4_drivers[i][0]))
    # _________________________________________________________________________
    jobs_button = ttk.Frame(display_canvas, border=15, borderwidth=15, relief=SUNKEN)
    jobs_button.configure(style='My.TFrame')
    s = ttk.Style()
    s.configure('My.TFrame', background='red')
    jobs_button.place(x=10, y=312, width=(screen_width - 30), height=(screen_height - 855))
    index = 1
    for i in range(8):
        button1 = Button(jobs_button, text="button1", padx=30)
        button1.grid(row=0, column=index, padx=(10, 0), sticky=E)
        index += 1
    # _________________________________________________________________________
    jobs_rect = ttk.Frame(display_canvas, border=5, borderwidth=5, relief=SUNKEN)
    jobs_rect.place(x=10, y=360, width=(screen_width - 30), height=(screen_height - 570))


global current_time


def timer():
    global current_time
    current_time = time.time()
    convert_time = time.strftime("%Y-%m-%d:%H:%M:%S")
    time_label.config(text=convert_time)
    time_label.after(1, timer)


# Main root
global root
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("{}x{}".format(int(screen_width * 0.75), int(screen_height * 0.75)))
root.resizable(width=True, height=True)
root.title("Cabhook By Junaid")
root.config(bg="green")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# _____________________________________________creating menu bar___________________________
main_menu = Menu(root, bg="blue")
root.config(menu=main_menu)
# cascade menu
file = Menu(main_menu)
view = Menu(main_menu)
# booking = Menu(main_menu)
accounts = Menu(main_menu)
drivers = Menu(main_menu)
plotting = Menu(main_menu)
reports = Menu(main_menu)
general = Menu(main_menu)
help = Menu(main_menu)
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Accounts", menu=accounts)
main_menu.add_cascade(label="Drivers", menu=drivers)
main_menu.add_cascade(label="Plotting & Maps", menu=plotting)
main_menu.add_cascade(label="Reports", menu=reports)
main_menu.add_cascade(label="General", menu=general)
main_menu.add_cascade(label="Help", menu=help)
# File Menu
logout = Menu(file)
master_exit = Menu(file)
file.add_command(label="Log out")
file.add_command(label="Quit", command=lambda: root.destroy())

# view menu
view.add_command(label="Bookings", command=lambda: bookings(notebook, screen_width, screen_height))
view.add_command(label="Show Pre Booking")
view.add_command(label="Show Web Booking")
view.add_command(label="Show Cancelled")
view.add_command(label="Show No pickup")
view.add_command(label="Show Account Booking")
view.add_command(label="Show Card Booking")
view.add_command(label="Show All")
view.add_command(label="Show Regular")
# Account menu
accounts.add_command(label="View all Accounts")
accounts.add_command(label="Create New Account",command=lambda: new_account(notebook, screen_width, screen_height))
accounts.add_command(label="Edit Account")
accounts.add_command(label="Create Account invoices")
accounts.add_command(label="Create Job invoice")

master = root
drivers.add_command(label="Driver List")
drivers.add_command(label="Add New Driver", command=lambda: addnew_driver(notebook, screen_width, screen_height))
drivers.add_command(label="Company Driver")
drivers.add_command(label="Other Drivers")
drivers.add_command(label="Driver PDA Settings")
# plotting
plotting.add_command(label="View Maps")
plotting.add_command(label="Localization")
plotting.add_command(label="Airports")
plotting.add_command(label="Stations")
plotting.add_command(label="Shops")
plotting.add_command(label="Hospitals & Surgeries")
plotting.add_command(label="Schools & Colleges")
plotting.add_command(label="Religious Places")
plotting.add_command(label="Hotels")
# reports
reports.add_command(label="Driver Earning Reports")
reports.add_command(label="Job list Report")
reports.add_command(label="Call History")
reports.add_command(label="Log_time")
# General
general.add_command(label="Colors")
general.add_command(label="Shortcuts")
# Help
help.add_command(label="Help")
# _______________________-- Buttons --____________________________________________
# buttons Bar(Frame) master_canvas

button_frame = Canvas(root, width=screen_width*0.2, height=screen_height*0.1, bg="black")
button_frame.place(x=0, y=screen_height*0.00, width=screen_width, height=screen_height*0.05)
home_btn = Button(button_frame, text="Home", padx=10, pady=5)

new_booking_btn = Button(button_frame, text="New Booking", padx=10, pady=5,
                         command=lambda: newbookings(notebook, screen_width, screen_height,root))
bookings_btn = Button(button_frame, text="Booking", padx=10, pady=5)
sms_btn = Button(button_frame, text="SMS", padx=10, pady=5)
emails_inbox_btn = Button(button_frame, text="emails", padx=10, pady=5)
call_hist_btn = Button(button_frame, text="Call history", padx=10, pady=5)
home_btn.grid(row=0, column=0, sticky=NW, padx=(5, 0))
new_booking_btn.grid(row=0, column=2, padx=(5, 0))
sms_btn.grid(row=0, column=3, padx=(5, 0))
emails_inbox_btn.grid(row=0, column=4, padx=(5, 0))
call_hist_btn.grid(row=0, column=5, padx=(5, 0))
time_label = Label(button_frame, text="", fg="white",bg="#000000")
time_label.grid(row=0, column=10, pady=3, padx=5,sticky="W")
timer()
# ____________________________________________ create Master Canvas_____________________________________
master_canvas1 = Canvas(root, width=screen_width, height=screen_height, background="blue")
master_canvas1.place(x=5, y=screen_height*0.05, width=(screen_width - 30), height=(screen_height-(screen_height*0.16)))
root.config(bg="#F8E17F", padx=5, pady=5)
# _________________ creating notebook___________
global notebook
notebook = ttk.Notebook(master_canvas1)
notebook.grid()
home()

# ________________________________________ footer ----------------------------------------------------------------


root.mainloop()
