from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

global driver_no_entry, pda_password_entry, driver_no_entry, pda_password_entry, pda_vr, mobile_vr, driver_blocked_vr
global driver_first_name_entry, driver_last_name_entry, driver_gender_vr, driver_birthday_vr, driver_address_1_entry
global driver_address_2_entry
global driver_home_phone_entry, driver_mobile_entry, driver_date_joined_vr, driver_date_left_vr
global driver_national_insurance_entry, driver_license_entry, driver_penalties_vr, driver_pco_entry
global driver_pco_exp_vr, driver_town_entry, driver_postcode_entry
global insurance_premium_entry, insurance_ex_vr, road_expiry_vr, pco_number_entry, pco_expiry_vr
global veh_reg_entry, veh_make_entry, veh_model_entry, veh_color_entry, veh_category_vr, veh_ownership_vr
global type_vehicle_vr, deposit_entry, base_vr, radio_vr, outstanding_b_entry, commission_rate_vr
global commission_rate_acc_vr, rent_entry, salary_entry


def saver():
    from new_driver_database import save
    save()


def addnew_driver(notebook, screen_width, screen_height):
    driver_top = Frame(notebook, width=screen_width, height=screen_height)
    notebook.add(driver_top, text="New Driver")
    driver_top.update()

    # _________add_new_driver frame________
    add_new_driver_frame = Frame(driver_top, bg="red")
    add_new_driver_frame.place(x=0, y=0, height=(screen_height), width=(screen_width))
    add_new_driver_frame.update()
    frame_width = add_new_driver_frame.winfo_width()
    frame_height = add_new_driver_frame.winfo_height()

    # __________ Driver login information___________
    driver_login_info = LabelFrame(add_new_driver_frame, text="Login Information", bg="green", font=("Arial", 12))
    driver_login_info.place(x=frame_width * 0.05, y=frame_height * 0.01, height=frame_height * 0.2,
                            width=frame_width * 0.4)
    # ______Labels______
    driver_no = Label(driver_login_info, text="Driver NO", font=("Arial", 12))
    pda_password = Label(driver_login_info, text="PDA Password", font=("Arial", 12))
    device = Label(driver_login_info, text="Device", font=("Arial", 12))
    driver_blocked = Label(driver_login_info, text="Driver Blocked", font=("Arial", 12))
    driver_no.grid(row=0, column=0, pady=5, padx=5)
    pda_password.grid(row=0, column=3, pady=5, padx=5)
    device.grid(row=1, column=0, pady=5, padx=5)
    driver_blocked.grid(row=1, column=3, pady=5, padx=5)
    # _______Actions_________
    global driver_no_entry, pda_password_entry, driver_no_entry, pda_password_entry, pda_vr, mobile_vr, driver_blocked_vr
    driver_no_entry = Entry(driver_login_info)
    pda_password_entry = Entry(driver_login_info)
    driver_no_entry.grid(row=0, column=1, pady=5, padx=5, columnspan=2)
    pda_password_entry.grid(row=0, column=4, pady=5, padx=5)
    pda_vr = IntVar()
    pda_check_box = Checkbutton(driver_login_info, variable=pda_vr, font=("Arial", 12), onvalue=0, offvalue=1,
                                text="PDA")
    pda_check_box.deselect()
    pda_check_box.grid(row=1, column=1, pady=5, padx=5)
    mobile_vr = IntVar()
    mobile_box = Checkbutton(driver_login_info, font=("Arial", 12), variable=mobile_vr, onvalue=0, offvalue=1,
                             text="Mobile")
    mobile_box.deselect()
    mobile_box.grid(row=1, column=2, pady=5, padx=5)
    driver_blocked_vr = IntVar()
    driver_blocked_box = Checkbutton(driver_login_info, font=("Arial", 12), variable=driver_blocked_vr, onvalue=0,
                                     offvalue=1,
                                     text="Blocked")
    driver_blocked_box.deselect()
    driver_blocked_box.grid(row=1, column=4, pady=5, padx=5)

    # __________ Driver personal information___________
    driver_personal_info = LabelFrame(add_new_driver_frame, text="Personal Information", bg="blue")
    driver_personal_info.place(x=frame_width * 0.05, y=frame_height * 0.15, height=frame_height * 0.39,
                               width=frame_width * 0.4)

    # _ Labels and actions
    driver_first_name_label = Label(driver_personal_info, text="First Name", font=("Arial", 12))
    driver_last_name_label = Label(driver_personal_info, text="Last Name", font=("Arial", 12))
    driver_gender_label = Label(driver_personal_info, text="Gender", font=("Arial", 12))
    driver_birthday_label = Label(driver_personal_info, text="DOB", font=("Arial", 12))
    driver_address_1 = Label(driver_personal_info, text="Address ln1", font=("Arial", 12))
    driver_address_2 = Label(driver_personal_info, text="Address ln2", font=("Arial", 12))
    driver_town = Label(driver_personal_info, text="Town", font=("Arial", 12))
    driver_postcode = Label(driver_personal_info, text="Postcode", font=("Arial", 12))
    driver_home_phone = Label(driver_personal_info, text="Ho Phone", font=("Arial", 12))
    driver_mobile = Label(driver_personal_info, text="Mobile", font=("Arial", 12))
    driver_date_joined = Label(driver_personal_info, text="Date Joined", font=("Arial", 12))
    driver_date_left = Label(driver_personal_info, text="Date Left", font=("Arial", 12))
    driver_national_insurance = Label(driver_personal_info, text="N.I.C", font=("Arial", 12))
    driver_license = Label(driver_personal_info, text="Dri License", font=("Arial", 12))
    driver_penalties = Label(driver_personal_info, text="Penalties.Pts", font=("Arial", 12))
    driver_pco = Label(driver_personal_info, text="PCO No", font=("Arial", 12))
    driver_pco_exp = Label(driver_personal_info, text="PCO Exp", font=("Arial", 12))
    # _____________Actions________________
    driver_first_name_label.grid(row=0, column=0, pady=(5, 2), padx=5)
    global driver_first_name_entry, driver_last_name_entry, driver_gender_vr, driver_birthday_vr, driver_address_1_entry
    global driver_address_2_entry, insurance_ex_vr
    global driver_home_phone_entry, driver_mobile_entry, driver_date_joined_vr, driver_date_left_vr
    global driver_national_insurance_entry, driver_license_entry, driver_penalties_vr, driver_pco_entry
    global driver_pco_exp_vr, driver_town_entry, driver_postcode_entry
    global insurance_premium_entry, insurance_ex_v, road_expiry_vr, pco_number_entry, pco_expiry_vr
    global veh_reg_entry, veh_make_entry, veh_model_entry, veh_color_entry, veh_category_vr, veh_ownership_vr
    driver_first_name_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_first_name_entry.grid(row=0, column=1, pady=(5, 2), padx=5)
    # ______________
    driver_last_name_label.grid(row=0, column=2, pady=(5, 2), padx=5)
    driver_last_name_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_last_name_entry.grid(row=0, column=3, pady=(5, 2), padx=5)
    # --------------------------------
    driver_gender_label.grid(row=1, column=0, pady=2, padx=5)
    driver_gender_vr = StringVar()
    driver_gender_box = ttk.Combobox(driver_personal_info, width=13, textvariable=driver_gender_vr, font=("Arial", 12))
    driver_gender_box['values'] = ("Male", "Female")
    driver_gender_box.grid(row=1, column=1, pady=2, padx=5)
    driver_gender_box.current(0)
    # --------------------------------
    driver_birthday_label.grid(row=1, column=2, pady=2, padx=5)
    driver_birthday_vr = StringVar()
    driver_birthday_pick = DateEntry(driver_personal_info, width=13, selectmode="day", textvariable=driver_birthday_vr,
                                     font=("Arial", 12))
    driver_birthday_pick.grid(row=1, column=3, pady=2, padx=5)
    # ___________________________________
    driver_address_1.grid(row=2, column=0, pady=2, padx=5)
    driver_address_1_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_address_1_entry.grid(row=2, column=1, pady=2, padx=5)
    # --------------------------------
    driver_address_2.grid(row=2, column=2, pady=2, padx=5)
    driver_address_2_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_address_2_entry.grid(row=2, column=3, pady=5, padx=5)
    # --------------------------------
    driver_town.grid(row=3, column=0, pady=2, padx=5)
    driver_town_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_town_entry.grid(row=3, column=1, pady=2, padx=5)
    # --------------------------------
    driver_postcode.grid(row=3, column=2, pady=2, padx=5)
    driver_postcode_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_postcode_entry.grid(row=3, column=3, pady=2, padx=5)
    # --------------------------------
    driver_home_phone.grid(row=4, column=0, pady=2, padx=5)
    driver_home_phone_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_home_phone_entry.grid(row=4, column=1, pady=2, padx=5)
    driver_mobile.grid(row=4, column=2, pady=2, padx=5)
    driver_mobile_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_mobile_entry.grid(row=4, column=3, pady=2, padx=5)
    # ____________________________________
    driver_date_joined.grid(row=5, column=0, pady=2, padx=5)
    driver_date_joined_vr = StringVar()
    driver_date_joined_pick = DateEntry(driver_personal_info, width=13, selectmode="day",
                                        textvariable=driver_date_joined_vr, font=("Arial", 12))
    driver_date_joined_pick.grid(row=5, column=1, pady=2, padx=5)
    driver_date_left.grid(row=5, column=2, pady=2, padx=5)
    driver_date_left_vr = StringVar()
    driver_date_left_pick = DateEntry(driver_personal_info, width=13, selectmode="day",
                                      textvariable=driver_date_left_vr, font=("Arial", 12))
    driver_date_left_pick.grid(row=5, column=3, pady=2, padx=5)
    # ______________________________________
    driver_national_insurance.grid(row=6, column=0, pady=2, padx=5)
    driver_national_insurance_entry = Entry(driver_personal_info, width=15, font=("Arial", 12))
    driver_national_insurance_entry.grid(row=6, column=1, pady=2, padx=5)
    driver_license.grid(row=6, column=2, pady=2, padx=5)
    driver_license_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_license_entry.grid(row=6, column=3, pady=2, padx=5)
    # --------------------------
    driver_penalties.grid(row=7, column=0, pady=2, padx=5)
    driver_penalties_vr = IntVar()
    driver_penalties_spin = ttk.Spinbox(driver_personal_info, width=13, from_=0, to=5, textvariable=driver_penalties_vr,
                                        font=("Arial", 12))
    driver_penalties_spin.grid(row=7, column=1, pady=2, padx=5)
    driver_penalties_spin.set(0)
    # ____________________________
    driver_pco.grid(row=7, column=2, pady=2, padx=5)
    driver_pco_entry = Entry(driver_personal_info, font=("Arial", 12), width=15)
    driver_pco_entry.grid(row=7, column=3, pady=2, padx=5)
    driver_pco_exp.grid(row=8, column=0, pady=2, padx=5)
    driver_pco_exp_vr = StringVar()
    driver_pco_exp_pick = DateEntry(driver_personal_info, width=13, selectmode="day", textvariable=driver_pco_exp_vr,
                                    font=("Arial", 12))
    driver_pco_exp_pick.grid(row=8, column=1, pady=2, padx=5)

    # __________ Vehicle details___________
    vehicle_details = LabelFrame(add_new_driver_frame, text="Vehicle Details", bg="yellow")
    vehicle_details.place(x=frame_width * 0.47, y=frame_height * 0.013, height=frame_height * 0.4,
                          width=frame_width * 0.45)

    # _________________ label_______________
    veh_reg = Label(vehicle_details, text="Vehicle Registration", font=("Arial", 12))
    veh_make = Label(vehicle_details, text="Vehicle Make", font=("Arial", 12))
    veh_model = Label(vehicle_details, text="Vehicle Model", font=("Arial", 12))
    veh_color = Label(vehicle_details, text="Vehicle Color", font=("Arial", 12))
    veh_category = Label(vehicle_details, text="Category", font=("Arial", 12))
    veh_ownership = Label(vehicle_details, text="Ownership", font=("Arial", 12))
    # _______________Actions________

    veh_reg.grid(row=0, column=0, pady=2, padx=5)
    veh_reg_entry = Entry(vehicle_details, font=("Arial", 12), width=15)
    veh_reg_entry.grid(row=0, column=1, pady=2, padx=5)
    veh_make.grid(row=0, column=2, pady=2, padx=5)
    veh_make_entry = Entry(vehicle_details, font=("Arial", 12), width=15)
    veh_make_entry.grid(row=0, column=3, pady=2, padx=5)
    veh_model.grid(row=1, column=0, pady=2, padx=5)
    veh_model_entry = Entry(vehicle_details, font=("Arial", 12), width=15)
    veh_model_entry.grid(row=1, column=1, pady=2, padx=5)
    veh_color.grid(row=1, column=2, pady=2, padx=5)
    veh_color_entry = Entry(vehicle_details, font=("Arial", 12), width=15)
    veh_color_entry.grid(row=1, column=3, pady=2, padx=5)
    veh_category.grid(row=2, column=0, pady=2, padx=5)
    veh_category_vr = StringVar()
    veh_category_com = ttk.Combobox(vehicle_details, width=13, textvariable=veh_category_vr, font=("Arial", 12))
    veh_category_com['values'] = ("Any Car", "MPV5", "MPV6", "MPV7", "MPV8")
    veh_category_com.set("Any Car")
    veh_category_com.grid(row=2, column=1, pady=2, padx=5)
    veh_ownership.grid(row=2, column=2, pady=2, padx=5)
    veh_ownership_vr = StringVar()
    veh_ownership_com = ttk.Combobox(vehicle_details, width=13, textvariable=veh_ownership_vr, font=("Arial", 12))
    veh_ownership_com['values'] = ("Personal", "Company")
    veh_ownership_com.set("Personal")
    veh_ownership_com.grid(row=2, column=3, pady=2, padx=5)

    # __________ Driver expiry details___________
    expiry_details = LabelFrame(add_new_driver_frame, text="Expiry Details", bg="gray")
    expiry_details.place(x=frame_width * 0.47, y=frame_height * 0.15, height=frame_height * 0.3,
                         width=frame_width * 0.45)

    # _______label______________
    insurance_premium = Label(expiry_details, text="Insur. Premium", font=("Arial", 12))
    insurance_expiry = Label(expiry_details, text="Insur. Expiry", font=("Arial", 12))
    mot_expiry = Label(expiry_details, text="MOT Expiry", font=("Arial", 12))
    road_expiry = Label(expiry_details, text="Rd Tx Ex", font=("Arial", 12))
    pco_number = Label(expiry_details, text="PCO Num", font=("Arial", 12))
    pco_expiry = Label(expiry_details, text="PCO Exp Vehi", font=("Arial", 12))
    # _______________Actions_______________

    insurance_premium.grid(row=0, column=0, pady=2, padx=5)
    insurance_premium_entry = Entry(expiry_details, width=20)
    insurance_premium_entry.grid(row=0, column=1)
    # _____________________________________
    insurance_expiry.grid(row=0, column=2, pady=2, padx=5)
    insurance_ex_vr = StringVar()
    insurance_ex_picker = DateEntry(expiry_details, selectmode="day", textvariable=insurance_ex_vr, font=("Arial", 12),
                                    width=13)
    insurance_ex_picker.grid(row=0, column=3, pady=2, padx=5)
    # ______________________________________
    mot_expiry.grid(row=1, column=0, pady=2, padx=5)
    mot_expiry_vr = StringVar()
    mot_expiry_picker = DateEntry(expiry_details, selectmode="day", textvariable=mot_expiry_vr, font=("Arial", 12),
                                  width=13)
    mot_expiry_picker.grid(row=1, column=1, pady=2, padx=5)

    # _____________________________
    road_expiry.grid(row=1, column=2, pady=2, padx=5)
    road_expiry_vr = StringVar()
    road_expiry_picker = DateEntry(expiry_details, selectmode="day", textvariable=road_expiry_vr, font=("Arial", 12),
                                   width=13)
    road_expiry_picker.grid(row=1, column=3, pady=2, padx=5)
    # ______________________
    pco_number.grid(row=4, column=0, pady=2, padx=5)
    pco_number_entry = Entry(expiry_details, font=("Arial", 12), width=15)
    pco_number_entry.grid(row=4, column=1, pady=2, padx=5)
    pco_expiry.grid(row=4, column=2, pady=2, padx=5)
    pco_expiry_vr = StringVar()
    pco_expiry_picker = DateEntry(expiry_details, selectmode="day", textvariable=pco_expiry_vr, font=("Arial", 12),
                                  width=13)
    pco_expiry_picker.grid(row=4, column=3, pady=2, padx=5)
    # __________ Payment mode___________
    payment_mode = LabelFrame(add_new_driver_frame, text="Payment Mode", bg="orange")
    payment_mode.place(x=frame_width * 0.47, y=frame_height * 0.32, height=frame_height * 0.22,
                       width=frame_width * 0.45)
    # _________________Label_________________
    type_vehicle = Label(payment_mode, text=" Pay Type", font=("Arial", 12), )
    deposit = Label(payment_mode, text="Deposit", font=("Arial", 12))
    base = Label(payment_mode, text="BaseRent", font=("Arial", 12))
    radio = Label(payment_mode, text="PDA Rent", font=("Arial", 12))
    outstanding_b = Label(payment_mode, text="Out Balance", font=("Arial", 12))
    commission_rate = Label(payment_mode, text="Comm Rate", font=("Arial", 12))
    commission_rate_acc = Label(payment_mode, text=" Acc Comm Rate", font=("Arial", 12))
    rent = Label(payment_mode, text="Rent", font=("Arial", 12))
    salary = Label(payment_mode, text=" Daily Salary", font=("Arial", 12))
    # _________________Action___________________
    global type_vehicle_vr, deposit_entry, base_vr, radio_vr, outstanding_b_entry, commission_rate_vr, commission_rate_acc_vr
    global rent_entry, salary_entry
    type_vehicle.grid(row=0, column=0, pady=2, padx=5)
    type_vehicle_vr = StringVar()
    type_vehicle_com = ttk.Combobox(payment_mode, textvariable=type_vehicle_vr, font=("Arial", 12), width=13)
    type_vehicle_com["value"] = ("Rent", "Commission")
    type_vehicle_com.set("Commission")
    type_vehicle_com.grid(row=0, column=1, pady=2, padx=5)
    deposit.grid(row=0, column=2, pady=2, padx=5)
    deposit_entry = Entry(payment_mode, font=("Arial", 12), width=15)
    deposit_entry.grid(row=0, column=3, pady=2, padx=5)
    base.grid(row=1, column=0, pady=2, padx=5)
    base_vr = IntVar()
    base_spin = ttk.Spinbox(payment_mode, from_=0, to=100, textvariable=base_vr, font=("Arial", 12), width=13)
    base_spin.set(0)
    base_spin.grid(row=1, column=1, pady=2, padx=5)
    radio.grid(row=1, column=2, pady=2, padx=5)
    radio_vr = IntVar()
    radio_spin = ttk.Spinbox(payment_mode, from_=0, to=100, textvariable=radio_vr, font=("Arial", 12), width=13)
    radio_spin.set(0)
    radio_spin.grid(row=1, column=3, pady=2, padx=5)
    outstanding_b.grid(row=2, column=0, pady=2, padx=5)
    outstanding_b_entry = Entry(payment_mode, font=("Arial", 12), width=15)
    outstanding_b_entry.grid(row=2, column=1, pady=2, padx=5)
    commission_rate.grid(row=2, column=2, pady=2, padx=5)
    commission_rate_vr = IntVar()
    commission_rate_spin = ttk.Spinbox(payment_mode, from_=0, to=100, textvariable=commission_rate_vr,
                                       font=("Arial", 12), width=13)
    commission_rate_spin.set(0)
    commission_rate_spin.grid(row=2, column=3, pady=2, padx=5)
    commission_rate_acc.grid(row=3, column=0, pady=2, padx=5)
    commission_rate_acc_vr = IntVar()
    commission_rate_acc_spin = ttk.Spinbox(payment_mode, from_=0, to=100, textvariable=commission_rate_acc_vr,
                                           font=("Arial", 12), width=13)
    commission_rate_acc_spin.set(0)
    commission_rate_acc_spin.grid(row=3, column=1, pady=2, padx=5)
    rent.grid(row=3, column=2, pady=2, padx=5)
    rent_entry = Entry(payment_mode, font=("Arial", 12), width=15)
    rent_entry.grid(row=3, column=3, pady=2, padx=5)
    salary.grid(row=4, column=0, pady=2, padx=5)
    salary_entry = Entry(payment_mode, font=("Arial", 12), width=15)
    salary_entry.grid(row=4, column=1, pady=2, padx=5)
    # __________________ Button for drivers_____________
    add_driver_button = Frame(add_new_driver_frame, bg="purple")
    add_driver_button.place(x=frame_width * 0.055, y=frame_height * 0.55, height=frame_height * 0.22,
                            width=frame_width * 0.8)
    pda_settings = Button(add_driver_button, text="PDA settings")
    manage_vehicle = Button(add_driver_button, text="Manage Vehicle")
    manage_leave = Button(add_driver_button, text="Manage Leave")
    add_edit_vehicle = Button(add_driver_button, text="Add/Edit Vehicle")
    note_by_me = Label(add_driver_button, text="Note: Do not Put any Symbols in any field above",
                       font=("Comic Sans MS", 12, "bold"))
    pda_settings.place(x=20, y=15, width=100, height=30)
    manage_vehicle.place(x=140, y=15, width=100, height=30)
    manage_leave.place(x=260, y=15, width=100, height=30)
    add_edit_vehicle.place(x=380, y=15, width=100, height=30)
    note_by_me.place(x=500, y=15)
    # ______________________
    save_driver_btn = Button(add_driver_button, text="Save", command=saver)
    search_driver_btn = Button(add_driver_button, text="Search")
    clear_driver_btn = Button(add_driver_button, text="Clear")
    driver_list_btn = Button(add_driver_button, text="Driver List")
    vehicle_history_btn = Button(add_driver_button, text="Vehicl History")
    print_driver_btn = Button(add_driver_button, text="Print")
    delete_driver_btn = Button(add_driver_button, text="Delete Driver")
    close_driver_btn = Button(add_driver_button, text="Close")
    save_driver_btn.place(x=20, y=60, width=100)
    search_driver_btn.place(x=140, y=60, width=100)
    clear_driver_btn.place(x=260, y=60, width=100)
    driver_list_btn.place(x=380, y=60, width=100)
    vehicle_history_btn.place(x=500, y=60, width=100)
    print_driver_btn.place(x=620, y=60, width=100)
    delete_driver_btn.place(x=740, y=60, width=100)
    close_driver_btn.place(x=860, y=60, width=100)
    # _____________________Driver_________________
    # driver_image_frame = Frame(add_new_driver_frame, bg="white")
    # driver_image_frame.place(x=650, y=5, height=350, width=400)
    # add_image_driver = Button(driver_image_frame, text="Add Image of driver", width=10, height=5)
    # add_image_driver.pack(pady=100)

    # ___________________________Vehicle Image --------------------------------
    vehicle_image_frame = Frame(add_new_driver_frame, bg="white")
    # vehicle_image_frame.place(x=650, y=370, height=280, width=400)
    add_vehicle_image_driver = Button(vehicle_image_frame, text="Add Image of driver", width=10, height=5)
# add_vehicle_image_driver.pack(pady=100)
