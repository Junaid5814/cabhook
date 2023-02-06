from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

global account_invoice_fare_deduction_vr, account_invoice_fare_deduction_spin, account_discount_vr
global account_discount_spin, account_admin_fee_vr, account_admin_fee_spin
global account_type_combobox, account_type_vr, account_agent_vr, account_agent_check, account_commission_entry
global account_ccno_entry, account_payment_vr, account_payment_combobox, account_close_vr, account_close_check
global account_color_picker, blank_entry
global account_code_entry, account_mobile_entry, account_fax_entry, account_password_check, account_password_entry
global account_no_entry, account_notes_entry, account_password_vr
global account_name_entry, account_email_entry, account_tel_no_entry
global account_web_address_entry, account_contact_name_entry, account_address_entry


def saved():
    from account.account_data import save
    save()


def password_disabled():
    if account_password_vr == 1:
        account_password_entry.config(state="disabled")

    else:
        account_password_entry.config(state="enabled")


def colorp():
    c_code = colorchooser.askcolor()
    blank_entry.config(bg=c_code[1])


def new_account(root, screen_width, screen_height):
    top_new_acc = Toplevel(root)
    top_new_acc.geometry("{}x{}".format(int(screen_width * 0.78), int(screen_height * 0.65)))
    top_new_acc.title("New Account")
    top_new_acc.config(bg="#D5DBDB")
    top_new_acc.resizable(width=False, height=False)
    # _____________frame__________________
    new_account_frame = Frame(top_new_acc, bg="#206A7D")
    new_account_frame.place(x=0, y=0, height=(screen_height * 0.62), width=(screen_width * 0.75))
    head_frame = Frame(new_account_frame, bg="#48207D")
    head_frame.place(x=0, y=0, height=50, width=(screen_width * 0.74))
    head_title = Label(head_frame, text="Create A New Account", font=("Arial", 18, "bold"))
    head_title.pack(fill=BOTH, expand=1)
    # ____________ Account frame_____________
    account_info_frame = LabelFrame(new_account_frame, text="Account Information", bg="#A60AC0")
    account_info_frame.place(x=20, y=60, height=300, width=(screen_width * 0.73))
    # __________ Label____________

    account_name = Label(account_info_frame, text="Account Name", font=("Arial", 10, "bold"))
    account_email = Label(account_info_frame, text="Email")
    account_tel_no = Label(account_info_frame, text="Telephone Number")
    account_contact_name = Label(account_info_frame, text="Contact Name")
    account_web_address = Label(account_info_frame, text="Web Address")
    account_address = Label(account_info_frame, text="Address")
    account_code = Label(account_info_frame, text="code")
    account_mobile = Label(account_info_frame, text="Mobile")
    account_fax = Label(account_info_frame, text="Fax")
    account_password = Label(account_info_frame, text="Password")
    account_no = Label(account_info_frame, text="Account Number")
    account_type = Label(account_info_frame, text="Account Type")
    account_agent = Label(account_info_frame, text="Account Agent")
    account_commission = Label(account_info_frame, text="Account comm.")
    account_ccno = Label(account_info_frame, text="Credit card")
    account_amount = Label(account_info_frame, text="Amount")
    account_payment = Label(account_info_frame, text="Account Payment")

    # _________Action __________________
    # _____________Row 1__________________
    global account_name_entry, account_email_entry, account_tel_no_entry
    global account_web_address_entry, account_contact_name_entry, account_address_entry
    account_name.place(x=10, y=5, width=130)
    account_name_entry = Entry(account_info_frame)
    account_name_entry.place(x=150, y=5, width=200)
    account_email.place(x=10, y=35, width=130)
    account_email_entry = Entry(account_info_frame)
    account_email_entry.place(x=150, y=35, width=200)
    account_tel_no.place(x=10, y=65, width=130)
    account_tel_no_entry = Entry(account_info_frame)
    account_tel_no_entry.place(x=150, y=65, width=200)
    account_web_address.place(x=10, y=95, width=130)
    account_web_address_entry = Entry(account_info_frame)
    account_web_address_entry.place(x=150, y=95, width=200)
    account_contact_name.place(x=10, y=125, width=130)
    account_contact_name_entry = Entry(account_info_frame)
    account_contact_name_entry.place(x=150, y=125, width=200)
    account_address.place(x=10, y=155, width=130)
    account_address_entry = Entry(account_info_frame)
    account_address_entry.place(x=150, y=155, height=100, width=200)

    # ___________________Row 2_______________________
    global account_code_entry, account_mobile_entry, account_fax_entry, account_password_check, account_password_entry
    global account_no_entry, account_notes_entry, account_password_vr
    account_code.place(x=360, y=5, width=130)
    account_code_entry = Entry(account_info_frame)
    account_code_entry.place(x=500, y=5, width=150)
    account_mobile.place(x=360, y=35, width=130)
    account_mobile_entry = Entry(account_info_frame)
    account_mobile_entry.place(x=500, y=35, width=150)
    account_fax.place(x=360, y=65, width=130)
    account_fax_entry = Entry(account_info_frame)
    account_fax_entry.place(x=500, y=65, width=150)
    account_password.place(x=360, y=95, width=70)
    account_password_vr = IntVar()
    account_password_check = Checkbutton(account_info_frame, onvalue=1, offvalue=0, variable=account_password_vr)
    account_password_check.deselect()
    account_password_check.place(x=440, y=95)
    account_password_entry = Entry(account_info_frame, )
    account_password_entry.place(x=500, y=95, width=150)
    account_no.place(x=360, y=125, width=130)
    account_no_entry = Entry(account_info_frame)
    account_no_entry.place(x=500, y=125, width=150)
    account_notes = Label(account_info_frame, text="Notes")
    account_notes.place(x=360, y=155, width=130)
    account_notes_entry = Entry(account_info_frame)
    account_notes_entry.place(x=500, y=155, height=100, width=180)

    # ___________________Row 3___________________________
    global account_type_combobox, account_type_vr, account_agent_vr, account_agent_check, account_commission_entry
    global account_ccno_entry, account_payment_vr, account_payment_combobox, account_close_vr, account_close_check
    global account_color_picker, blank_entry
    account_type.place(x=680, y=5, width=100)
    account_type_vr = StringVar()
    account_type_combobox = ttk.Combobox(account_info_frame, textvariable=account_type_vr)
    account_type_combobox["value"] = ("Business", "Individual")
    account_type_combobox.set("Business")
    account_type_combobox.place(x=800, y=5, width=150)
    account_agent.place(x=680, y=35, width=100)
    account_agent_vr = IntVar()
    account_agent_check = Checkbutton(account_info_frame, onvalue=1, offvalue=0, variable=account_agent_vr)
    account_agent_check.deselect()
    account_agent_check.place(x=840, y=35, width=100)
    account_commission.place(x=680, y=65, width=100)
    account_commission_entry = Entry(account_info_frame)
    account_commission_entry.place(x=800, y=65, width=150)
    account_ccno.place(x=680, y=95, width=100)
    account_ccno_entry = Entry(account_info_frame)
    account_ccno_entry.place(x=800, y=95, width=150)
    account_payment.place(x=680, y=125, width=100)
    account_payment_vr = StringVar()
    account_payment_combobox = ttk.Combobox(account_info_frame, textvariable=account_payment_vr)
    account_payment_combobox["value"] = ("Weekly", "Monthly")
    account_payment_combobox.set("Monthly")
    account_payment_combobox.place(x=800, y=125, width=150)

    account_close_vr = IntVar()
    account_close_check = Checkbutton(account_info_frame, onvalue=1, offvalue=0, variable=account_close_vr,
                                      text=" Close", fg="RED")
    account_close_check.deselect()
    account_close_check.place(x=975, y=5)
    account_amount.place(x=975, y=35)
    account_color_picker = Button(account_info_frame, text="Pick Jobs Color", command=colorp, bg="#ffffff")
    global blank_entry
    blank_entry = Entry(account_info_frame)
    blank_entry.place(x=710, y=157)
    account_color_picker.place(x=850, y=155, width=100)

    # ______________ bottom Part _____________
    global account_invoice_fare_deduction_vr, account_invoice_fare_deduction_spin, account_discount_vr
    global account_discount_spin, account_admin_fee_vr, account_admin_fee_spin
    account_bottom_frame = LabelFrame(new_account_frame, text="Other Details", bg="Green")
    account_bottom_frame.place(x=20, y=380, height=150, width=(screen_width * 0.73))
    account_invoice_fare_deduction = Label(account_bottom_frame, text="Invoice Fare Deduction")
    account_invoice_fare_deduction.place(x=20, y=5)
    account_invoice_fare_deduction_vr = IntVar()
    account_invoice_fare_deduction_spin = ttk.Spinbox(account_bottom_frame, from_=0, to=999,
                                                      textvariable=account_invoice_fare_deduction_vr)
    account_invoice_fare_deduction_spin.place(x=150, y=5, width=100)
    account_discount = Label(account_bottom_frame, text="Discount")
    account_discount.place(x=260, y=5, width=100)
    account_discount_vr = IntVar()
    account_discount_spin = ttk.Spinbox(account_bottom_frame, from_=0, to=999, textvariable=account_discount_vr)
    account_discount_spin.place(x=370, y=5, width=100)
    account_admin_fee = Label(account_bottom_frame, text="Admin Fee")
    account_admin_fee.place(x=490, y=5, width=100)
    account_admin_fee_vr = IntVar()
    account_admin_fee_spin = ttk.Spinbox(account_bottom_frame, from_=0, to=999, textvariable=account_admin_fee_vr)
    account_admin_fee_spin.place(x=600, y=5, width=100)
    # ________________________Buttons______________________

    account_save_btn = Button(account_bottom_frame, text="Save Account", command=saved)
    account_update_btn = Button(account_bottom_frame, text="Update Account")
    account_clear_btn = Button(account_bottom_frame, text="Clear")
    account_email_invoice = Button(account_bottom_frame, text="Send Email")
    account_save_btn.place(x=270, y=45, width=100)
    account_update_btn.place(x=380, y=45, width=100)
    account_clear_btn.place(x=490, y=45, width=100)
    account_email_invoice.place(x=600, y=45, width=100)

    top_new_acc.mainloop()
