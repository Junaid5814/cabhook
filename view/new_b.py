from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime
import googlemaps
import tkintermapview
from PIL import ImageTk, Image
import polyline as polyline
from time import time
from test import *

global address_search_entry, search_list
global pickup_p, destination_p, pick, needed_code, pickup_postcode
global total_price_entry, destination_postcode
global milage_price_entry, total_miles_entry, area_surge_entry, cc_surcharge_entry, cong_charges_entry
global wait_vr, agent_entry, cong_charges_entry, total_price_entry, drivers_price_entry

global payment_mode_vr, payment_status_vr
global company_vr, driver_no_entry, airline_entry, flight_no_entry, coming_from_entry
global accounts_vr, jobtype_vr, vehicle_vr, number_of_vehicles_vr, returnbox_vr, reference_entry, max_vr, luggage_vr
global return_job_vr, regular_booking_vr, message_vr, email_vr
global address_label, address_entry, destination_list

global date_entry, time_entry, auto_vr
global name_entry, phone_entry, catagory_vr, email_entry, notes_entry, black_check_vr


def save_booking():
    # from new_booking_database import saveed
    # saveed()
    pass


def validate_time(time_string):
    if not time_string:  # the field is being cleared
        return True
    try:
        datetime.strptime(time_string, '%H:%M')
        return True
    except ValueError:
        return False


def transfer_to_pickup():
    global pick, pickup_lang_long
    address_entry.delete(0, END)
    selected_index = search_list.curselection()
    if selected_index:
        selected_item = search_list.get(selected_index[0])
        address_entry.insert(0, selected_item)


def transfer_to_destination():
    selected_index = search_list.curselection()
    if selected_index:
        selected_item = search_list.get(selected_index[0])
        destination_list.insert(END, selected_item)

    distance_request()


global pickup_lan_long

global top


def show_map_n():
    global pickup_lan_long, destination_postcode, pickup_postcode

    destination_addresses = [destination_list.get(index) for index in range(destination_list.size())]
    gmaps = googlemaps.Client(key)
    root = Toplevel(top)
    root.geometry("800x700")
    root.title("mapview")

    map_frame = LabelFrame(root, text="Map")
    map_frame.pack()
    map_view = tkintermapview.TkinterMapView(root, width=780, height=680, corner_radius=0)
    map_view.set_position(51.5125, -0.5908)
    map_view.set_zoom(15)
    icon_1 = ImageTk.PhotoImage(Image.open("../marker_ico.png"))
    parts = address_entry.get().split(',')

    if address_entry.get() != "":
        pickup_lan_long = f"{parts[-2]}, {parts[-1]}"
        pickup_postcode = parts[-3]
        marker_1 = map_view.set_address(pickup_lan_long, marker=True, icon=icon_1, text="Pickup")
        destination_addresses = [destination_list.get(index) for index in range(destination_list.size())]
        abc_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        count = 0

        if len(destination_addresses) != 0:
            all_lat_lng = []
            for destination in destination_addresses:
                destination_part = destination.split(',')
                destination_lan_long = f"{destination_part[-2]}, {destination_part[-1]}"
                destination_postcode = destination_part[-3]
                marker_2 = map_view.set_address(destination_lan_long, marker=True, icon=icon_1,
                                                text=f"drop off {abc_list[count].upper()}")

                # Get the route between the pickup and destination locations
                directions_result = gmaps.directions(pickup_lan_long, destination_lan_long, mode="driving",
                                                     avoid="tolls", alternatives=True, optimize_waypoints=True)

                # Get the encoded polyline from the first route
                encoded_polyline = directions_result[0]['overview_polyline']['points']

                # Decode the polyline
                decoded_polyline = polyline.decode(encoded_polyline)

                # Use the set_path method to draw the line
                map_view.set_path(decoded_polyline)

    map_view.pack()
    root.mainloop()


def distance_request():
    global destination_addresses, current_location
    total_miles_entry.delete(0, END)
    destination_addresses = [destination_list.get(index) for index in range(destination_list.size())]
    gmaps = googlemaps.Client(key="AIzaSyD6UkyqYlTztvNgVp2BbMxhq4T-F2FXqSg")

    total_distance = 0
    current_location = address_entry.get()
    for destination in destination_addresses:
        distance = gmaps.distance_matrix(str(current_location), str(destination))["rows"][0]["elements"][0]["distance"][
            "value"]
        total_distance += distance
        current_location = destination

    total_miles_entry.insert(0, total_distance / 1000)
    top.after(1, price)


# ________________________map  related  ________________________


def get_location_suggestions(typed, API_KEY):
    global needed_code
    gmaps = googlemaps.Client(key=API_KEY)
    result = gmaps.places_autocomplete(typed + ', Slough, UK')
    data = []
    for item in result:
        door_number = None
        street = None
        postcode = None
        address = item['description']
        place_id = item['place_id']
        details = gmaps.place(place_id)
        for component in details['result']['address_components']:
            if 'postal_code' in component['types']:
                postcode = component['long_name']
            if 'street_number' in component['types']:
                door_number = component['long_name']
            if 'route' in component['types']:
                street = component['long_name']

        # Check if door_number, street, or postcode is None
        if door_number is None:
            door_number = ''
        if street is None:
            street = ''
        if postcode is None:
            postcode = ''

        location = gmaps.geocode(door_number + ' ' + street + ', ' + address + ', ' + postcode)
        latitude = location[0]["geometry"]["location"]["lat"]
        longitude = location[0]["geometry"]["location"]["lng"]
        data.append(f"{door_number} {street}, {address}, {postcode}, {latitude}, {longitude}")

    return data


def update(data):
    search_list.delete(0, END)
    for item in data:
        search_list.insert(END, item)


def check(e):
    import threading
    typed = address_search_entry.get()
    if len(typed) >= 3:
        thread = threading.Thread(target=run_api_request, args=(typed,))
        thread.start()


def run_api_request(typed):
    gmaps = googlemaps.Client(key="AIzaSyD6UkyqYlTztvNgVp2BbMxhq4T-F2FXqSg")
    location_suggestions = get_location_suggestions(typed, "AIzaSyD6UkyqYlTztvNgVp2BbMxhq4T-F2FXqSg")
    update(location_suggestions)


key = 'AIzaSyD6UkyqYlTztvNgVp2BbMxhq4T-F2FXqSg'

# latitude and longitude for Slough
SLOUGH_LAT = 51.5125
SLOUGH_LNG = -0.5908


# _________________________# buttton Fuctoins ________________________________

def delete_pickup():
    address_entry.delete(0, END)


def clear_0search():
    address_search_entry.delete(0, END)
    search_list.delete(0, END)


def move_up1():
    try:
        idxs = destination_list.curselection()
        if not idxs:
            return
        for pos in idxs:
            if pos == 0:
                continue
            text = destination_list.get(pos)
            destination_list.delete(pos)
            destination_list.insert(pos - 1, text)
            destination_list.pop(pos)
            destination_list.insert(pos - 1, text)
            destination_list.selection_set(pos - 1)
    except:
        pass


def move_down1():
    try:
        idxs = destination_list.curselection()
        if not idxs:
            return
        for pos in idxs:
            if pos == 0:
                continue
            text = destination_list.get(pos)
            destination_list.delete(pos)
            destination_list.insert(pos + 1, text)
            destination_list.pop(pos)
            destination_list.insert(pos + 1, text)
            destination_list.selection_set(pos + 1)
    except:
        pass


def delete_list():
    destination_list.delete(ANCHOR)


def price():
    global area_surge_entry, cc_surcharge_entry

    price1 = float(total_miles_entry.get())
    round_price = round(price1) * 2.00
    pricetotal = f"£{round_price}"
    total_price_entry.delete(0, END)
    total_price_entry.insert(0, pricetotal)
    drivers_price_entry.delete(0, END)
    drivers_price_entry.insert(0, total_price_entry.get())
    milage_price_entry.delete(0, END)
    milage_price_entry.insert(0, total_price_entry.get())

    cong_charges_entry.insert(0, "£00.00")
    cong_charges_entry.delete(0, END)
    pick_parts = address_entry.get().split(',')
    pick_partss = pick_parts[-3]
    pick_partss_split = pick_partss.split(' ')
    pick_postcode = pick_partss_split[1]
    if pick_postcode in postcodes:
        cong_charges_entry.delete(0, END)
        cong_charges_entry.insert(0, "£15.00")
    else:
        cong_charges_entry.delete(0, END)
        cong_charges_entry.insert(0, "£00.00")

    if len(destination_addresses) != 0:
        all_lat_lng = []
        for destination in destination_addresses:
            destination_part = destination.split(',')
            destination_postcode = destination_part[-3]
            destination_s = destination_postcode.split(' ')
            destination_postcode = (destination_s[1])
            if destination_postcode in postcodes:
                cong_charges_entry.delete(0, END)
                cong_charges_entry.insert(0, "£15.00")
                break


# ___________________ programe _____________________________________________________
def newbookings(notebook, screen_width, screen_height, root):
    global top

    top = Frame(notebook, width=screen_width, height=screen_height)
    notebook.add(top, text="New Booking")
    top.config(bg="sky blue")
    top.update()
    parent_width = top.winfo_width()
    parent_height = top.winfo_height()
    customer_info_frame = Frame(top, bg="yellow")
    customer_info_frame.place(x=0, y=0, height=screen_width * 0.04, width=(screen_width))
    customer_info_frame_height = customer_info_frame.winfo_height()
    customer_info_frame_width = customer_info_frame.winfo_width()
    # ____________ Customer details ____________
    global name_entry, phone_entry, catagory_vr, email_entry, notes_entry, black_check_vr
    name = Label(customer_info_frame, text="Name", borderwidth=0,padx=30)
    name.grid(row=1, column=0, padx=2, pady=2, )
    name_entry = Entry(customer_info_frame, borderwidth=2)
    name_entry.grid(row=1, column=1, padx=2, pady=5, )
    phone = Label(customer_info_frame, text="Phone",padx=30)
    phone.grid(row=1, column=2, padx=2, pady=5, )
    phone_entry = Entry(customer_info_frame, borderwidth=2)
    phone_entry.grid(row=1, column=3, padx=2, pady=5, )
    history_button = Button(customer_info_frame, text="History",padx=30)
    history_button.grid(row=1, column=4, padx=2, pady=5, )
    catagory_vr = StringVar()
    catagory = ttk.Spinbox(customer_info_frame, values=("Diamond", "Gold", "Silver"), textvariable=catagory_vr)
    catagory.grid(row=1, column=5, padx=2, pady=2, )
    catagory.set("Silver")
    email = Label(customer_info_frame, text="Email")
    email.grid(row=1, column=6, padx=2, pady=2, )
    email_entry = Entry(customer_info_frame, borderwidth=2)
    email_entry.grid(row=1, column=7, padx=2, pady=5, )
    notes = Label(customer_info_frame, text="Notes")
    notes.grid(row=1, column=8, padx=2, pady=5, )
    notes_entry = Entry(customer_info_frame, borderwidth=2)
    notes_entry.grid(row=1, column=9, padx=2, pady=5, )
    black_check_vr = IntVar()
    black_check_box = Checkbutton(customer_info_frame, text="Black list", onvalue=1, offvalue=0,
                                  variable=black_check_vr)
    black_check_box.deselect()
    black_check_box.grid(row=1, column=10, padx=2, pady=5, )
    # __________________________booking_address frame___________
    global date_entry, time_entry, auto_vr
    address_Frame = Frame(top, bg="red", bd=3, )
    address_Frame.place(x=0, y=screen_height * 0.04, width=screen_width * 0.75, height=screen_height * 0.59)
    booking_date = Label(address_Frame, text="Date", )
    booking_date.grid(row=0, column=0, padx=5, pady=(5, 0))
    date_entry_vr = StringVar()
    date_entry = DateEntry(address_Frame, selectmode="day", textvariable=date_entry_vr)
    date_entry.grid(row=0, column=1, padx=5, pady=(5, 0))
    time_label = Label(address_Frame, text="Time")
    time_label.grid(row=0, column=2, padx=5, pady=(5, 0))
    # Get the current time
    current_time = datetime.now().strftime("%H:%M")
    # Create the time picker
    # Get the current time
    current_time = datetime.now().strftime("%H:%M")
    # Create the time picker
    reg = root.register(validate_time)
    time_entry = ttk.Combobox(address_Frame, width=5, font="Arial 10", validate='key', validatecommand=(reg, '%P'),
                              values=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00",
                                      "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
                                      "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"])
    time_entry.set(current_time)
    time_entry.grid(row=0, column=3, padx=5, pady=(5, 0))

    auto_vr = IntVar()
    auto = Checkbutton(address_Frame, text="Auto Dispatch", onvalue=1, offvalue=0, variable=auto_vr)
    auto.deselect()
    auto.grid(row=0, column=4, padx=5, pady=(5, 0))
    # ------------------ Search box and shortcuts buttons-------
    global address_search_entry, search_list
    address_search_label = Label(address_Frame, text="Search address")
    address_search_label.grid(row=1, column=0, padx=5,pady=(2, 0))
    address_search_entry = Entry(address_Frame, width=50, font="Helvetica 12")
    address_search_entry.bind("<KeyRelease>", check)
    address_search_entry.grid(row=1, column=1, columnspan=5, padx=5,pady=(2, 0))
    go_btn = Button(address_Frame, text="Clear", padx=20, command=clear_0search)
    go_btn.grid(row=1, column=6, padx=(2,0),pady=(2, 0))
    airport_btn = Button(address_Frame, text="Airport", padx=10)
    stations_btn = Button(address_Frame, text="Stations", padx=3)
    school_btn = Button(address_Frame, text="Schools")
    hotel_btn = Button(address_Frame, text="Hotels")
    hospital_btn = Button(address_Frame, text="Hospitals")
    shop_btn = Button(address_Frame, text="Shops")
    airport_btn.grid(row=1, column=8, padx=(2,0), pady=(1, 0))
    stations_btn.grid(row=1, column=9, padx=(2,0), pady=(1, 0))
    school_btn.grid(row=1, column=10, padx=(2,0), pady=(1, 0))
    hotel_btn.grid(row=1, column=11, padx=(2,0), pady=(1, 0))
    hospital_btn.grid(row=1, column=12, padx=(2,0), pady=(1, 0))
    shop_btn.grid(row=1, column=13, padx=(2,0), pady=(1, 0))
    suggestion_box = Frame(address_Frame, bg="#ffffff", relief=SUNKEN, bd=2)
    suggestion_box.place(x=screen_width*0.01, y=screen_height*0.08, height=200, width=screen_width*0.55)
    search_list = Listbox(suggestion_box, bg="red")
    search_list.place(x=0, y=0, height=190, width=500)
    pick_button = Button(address_Frame, text="Pick", command=transfer_to_pickup)
    destination_btn = Button(address_Frame, text="Destination", command=transfer_to_destination)
    pick_button.place(x=screen_width*0.62, y=screen_height*0.11, height=screen_height*0.10, width=screen_width*0.080)
    destination_btn.place(x=screen_width*0.62, y=screen_height*0.23, height=screen_height*0.10, width=screen_width*0.080)

    # _____________pickup entry____________________
    global address_label, address_entry, destination_list
    pick_up_label = Label(address_Frame, text="Pick UP")
    pick_up_label.place(x=screen_width*0.01, y=screen_height*0.345)
    address_label = Label(address_Frame, text="Address")
    address_label.place(x=10, y=330)
    address_entry = Entry(address_Frame)
    address_entry.place(x=screen_width*0.05, y=screen_height*0.345, width=screen_width*0.51)
    delete_pickup_btn = Button(address_Frame, text="Delete", command=delete_pickup)
    delete_pickup_btn.place(x=screen_width*0.62, y=screen_height*0.345,width=screen_width*0.08)

    # _______destination buttons____________________________
    move_up_btn = Button(address_Frame, text="Move Up", command=move_up1)
    move_down_btn = Button(address_Frame, text="Move Down", command=move_down1)
    delete_selected_btn = Button(address_Frame, text="Delete Selected", command=delete_list)
    move_up_btn.place(x=screen_width*0.62, y=screen_height*0.40, width=screen_width*0.08)
    move_down_btn.place(x=screen_width*0.62, y=screen_height*0.450, width=screen_width*0.08)
    delete_selected_btn.place(x=screen_width*0.62, y=screen_height*0.5, width=screen_width*0.08)
    # ___________ destination jobs ttk.tree________________

    destination_frame = Frame(address_Frame, bg="yellow", relief=SUNKEN, bd=3)
    destination_frame.place(x=screen_width*0.05, y=screen_height*0.38, width=screen_width*0.51,height=screen_height*0.2)
    destination_list = Listbox(destination_frame, bg="green", )
    destination_list.place(x=0, y=0, height=170, width=560)
    # ___________________ job Info box  Labels _________
    job_info_frame = Frame(top, bg="gray")
    job_info_frame.place(x=screen_width * 0.75, y=screen_height * 0.04, height=screen_height * 0.60,
                         width=screen_width * 0.24)
    job_info_frame.update()
    job_info_w=job_info_frame.winfo_width()
    job_info_h=job_info_frame.winfo_height()
    account_label = Label(job_info_frame, text="Accounts",font=("Arial", 12))
    job_type_label = Label(job_info_frame, text="Job Type",font=("Arial", 12))
    vehicle_label = Label(job_info_frame, text="Vehicle",font=("Arial", 12))
    no_of_vehicle_label = Label(job_info_frame, text="No of Vehicle",font=("Arial", 12))
    reference_label = Label(job_info_frame, text="Reference",font=("Arial", 12))
    max_passenger_label = Label(job_info_frame, text="Max Pass",font=("Arial", 12))
    return_booking_label = Label(job_info_frame, text="Return booking",font=("Arial", 12))
    booking_label = Label(job_info_frame, text="Booking",font=("Arial", 12))
    company_label = Label(job_info_frame, text="Company",font=("Arial", 12))
    driver_no_label = Label(job_info_frame, text="Driver No",font=("Arial", 12))
    authorised_label = Label(job_info_frame, text="Authorised",font=("Arial", 12))
    airline_label = Label(job_info_frame, text="Airline",font=("Arial", 12))
    flight_no_label = Label(job_info_frame, text="Flight No",font=("Arial", 12))
    coming_label = Label(job_info_frame, text="Coming From",font=("Arial", 12))
    account_label.grid(row=1,column=0,pady=(5,5))
    job_type_label.grid(row=2,column=0,pady=(0,5))
    vehicle_label.grid(row=3,column=0,pady=(0,5))
    no_of_vehicle_label.grid(row=4,column=0,pady=(0,5))
    reference_label.grid(row=5,column=0,pady=(0,5))
    max_passenger_label.grid(row=6,column=0,pady=(0,5))
    return_booking_label.grid(row=7,column=0,pady=(0,5))
    booking_label.grid(row=8,column=0,pady=(0,5))
    company_label.grid(row=9,column=0,pady=(0,5))
    driver_no_label.grid(row=10,column=0,pady=(0,5))
    authorised_label.grid(row=11,column=0,pady=(0,5))
    airline_label.grid(row=12,column=0,pady=(0,5))
    flight_no_label.grid(row=13,column=0,pady=(0,5))
    coming_label.grid(row=14,column=0,pady=(0,5))
    # ______________ job info data__________entry box,dropdown,combobox and check buttons
    # ______________ job info data__________entry box,dropdown,combobox and check buttons
    global accounts_vr, jobtype_vr, vehicle_vr, number_of_vehicles_vr, returnbox_vr, reference_entry, max_vr, luggage_vr
    global return_job_vr, regular_booking_vr, message_vr, email_vr

    # Account combobox___________________
    accounts_vr = StringVar()
    accounts_combo = ttk.Combobox(job_info_frame, width=27, textvariable=accounts_vr,font=("Arial", 12))
    # Adding combobox drop down list
    accounts_combo['values'] = ("NONE", 'Account 1', "Account 2", "Account 3", "Account 4", "Account 5")
    accounts_combo.current(0)
    accounts_combo.place(x=job_info_w*0.40, y=job_info_h*0.01, width=100)

    # job type_______________________
    jobtype_vr = StringVar()
    jobtype_combo = ttk.Combobox(job_info_frame, width=27, textvariable=jobtype_vr,font=("Arial", 12))
    jobtype_combo['values'] = ("Local", "Long job", 'School run', "Airport", "Account")
    jobtype_combo.current(0)
    jobtype_combo.place(x=job_info_w*0.40, y=job_info_h*0.07, width=100)

    # ___________________Vehicle_________________________
    vehicle_vr = StringVar()
    vehicle_combo = ttk.Combobox(job_info_frame, width=27, textvariable=vehicle_vr,font=("Arial", 12))
    vehicle_combo['values'] = ("ANY CAR", "SALOON", 'ESTATE', "MPV 5", "MPV 6", "MPV 7", "MPV 8")
    vehicle_combo.place(x=job_info_w*0.40, y=job_info_h*0.13, width=100)
    vehicle_combo.current(0)
    # ________________number of vehicles____________________________
    number_of_vehicles_vr = IntVar()
    number_of_vehicles_spin = ttk.Spinbox(job_info_frame, from_=1, to=10, textvariable=number_of_vehicles_vr,font=("Arial", 12))
    number_of_vehicles_spin.set(1)
    number_of_vehicles_spin.place(x=job_info_w*0.40, y=job_info_h*0.20, width=40)
    returnbox_vr = IntVar()
    return_checkbox = Checkbutton(job_info_frame, onvalue=0, offvalue=1, variable=returnbox_vr)
    return_checkbox.deselect()
    return_checkbox.place(x=job_info_w*0.8, y=job_info_h*0.20)
    return_label = Label(job_info_frame, text="W.Return",font=("Arial", 12))
    return_label.place(x=job_info_w*0.55, y=job_info_h*0.20)
    # __________Reference______________
    reference_entry = Entry(job_info_frame, bd=3, relief=SUNKEN,font=("Arial", 12))
    reference_entry.get()
    reference_entry.place(x=job_info_w*0.40, y=job_info_h*0.26,width=100)
    # ___________max pass
    max_vr = IntVar()
    max_pass = ttk.Spinbox(job_info_frame, from_=1, to=8, textvariable=max_vr,font=("Arial", 12))
    max_pass.set(1)
    max_pass.place(x=job_info_w*0.40, y=job_info_h*0.33, width=40)
    luggage_label = Label(job_info_frame, text="Luggage",font=("Arial", 12))
    luggage_label.place(x=job_info_w*0.55, y=job_info_h*0.33)
    luggage_vr = IntVar()
    luggage_spin = ttk.Spinbox(job_info_frame, from_=1, to=10, textvariable=luggage_vr,font=("Arial", 12))
    luggage_spin.set(1)
    luggage_spin.place(x=job_info_w*0.80, y=job_info_h*0.33, width=40)
    # _______________return__________
    return_job_vr = IntVar()
    return_job_checkbox = Checkbutton(job_info_frame, onvalue=0, offvalue=1, variable=return_job_vr,font=("Arial", 12))
    return_job_checkbox.deselect()
    return_job_checkbox.place(x=job_info_w*0.40, y=job_info_h*0.39)
    regular_booking_label = Label(job_info_frame, text="Regular",font=("Arial", 12))
    regular_booking_label.place(x=job_info_w*0.55, y=job_info_h*0.39)
    regular_booking_vr = IntVar()
    regular_booking_check = Checkbutton(job_info_frame, onvalue=0, offvalue=1, variable=regular_booking_vr,font=("Arial", 12))
    regular_booking_check.deselect()
    regular_booking_check.place(x=job_info_w*0.80, y=job_info_h*0.39)
    # ______________________text and mail sent _______________check
    sms_label = Label(job_info_frame, text="SMS")
    sms_label.place(x=job_info_w*0.40, y=job_info_h*0.46)
    message_vr = IntVar()
    message_checkbox = Checkbutton(job_info_frame, onvalue=0, offvalue=1, variable=message_vr)
    message_checkbox.deselect()
    message_checkbox.place(x=job_info_w*0.55, y=job_info_h*0.46)
    email_label = Label(job_info_frame, text="Email")
    email_label.place(x=job_info_w*0.65, y=job_info_h*0.46)
    email_vr = IntVar()
    email_check = Checkbutton(job_info_frame, onvalue=0, offvalue=1, variable=email_vr)
    email_check.deselect()
    email_check.place(x=job_info_w*0.80, y=job_info_h*0.46)
    # _____________ company_______________
    global company_vr, driver_no_entry, airline_entry, flight_no_entry, coming_from_entry
    company_vr = StringVar()
    company_combo = ttk.Combobox(job_info_frame, width=27, textvariable=company_vr,font=("Arial", 12))
    company_combo['values'] = ("511", "711", 'Cabco')
    company_combo.place(x=job_info_w*0.40, y=job_info_h*0.52,width=100)
    company_combo.current(0)
    # -------------------Driver no_____________
    driver_no_entry = Entry(job_info_frame, bd=2, relief=SUNKEN,font=("Arial", 12))
    driver_no_entry.place(x=job_info_w*0.40, y=job_info_h*0.58,width=40)
    # ____________  authority___
    aut = Label(job_info_frame, text="_______________")
    aut.place(x=job_info_w*0.40, y=job_info_h*0.64)
    # __________________ flight Info entries _______________
    airline_entry = Entry(job_info_frame, bd=2, relief=SUNKEN, font="Arial 12")
    flight_no_entry = Entry(job_info_frame, bd=2, relief=SUNKEN, font="Arial 12")
    coming_from_entry = Entry(job_info_frame, bd=2, relief=SUNKEN, font="Arial 12")
    airline_entry.place(x=job_info_w*0.40, y=job_info_h*0.71,width=100)
    flight_no_entry.place(x=job_info_w*0.40, y=job_info_h*0.77,width=100)
    coming_from_entry.place(x=job_info_w*0.40, y=job_info_h*0.83,width=100)
    # _______________ Payment and Pricing section___________
    pricing_frame = Frame(top, bg="blue")
    pricing_frame.place(x=screen_width * 0.01, y=screen_height * 0.63, height=screen_height * 0.20,
                         width=screen_width)
    payment = Label(pricing_frame, text="Payment and Charges Details", font="Arial 12")
    payment.place(x=0, y=0)

    # ___________ payment mode----------------
    global payment_mode_vr, payment_status_vr
    payment_mode_label = Label(pricing_frame, text="Payment Mode")
    payment_status_label = Label(pricing_frame, text="Payment Status")
    payment_mode_label.place(x=15, y=25)
    payment_status_label.place(x=15, y=55)
    payment_mode_vr = StringVar()
    payment_mode_combobox = ttk.Combobox(pricing_frame, width=27, textvariable=payment_mode_vr)
    payment_mode_combobox['values'] = ("Cash", "Credit Card Payed", 'Credit Card', "Account")
    payment_mode_combobox.place(x=110, y=25, width=75)
    payment_mode_combobox.current(0)
    payment_status_vr = StringVar()
    payment_status_combobox = ttk.Combobox(pricing_frame, width=27, textvariable=payment_status_vr)
    payment_status_combobox['values'] = ("Unpaid", "Payed")
    payment_status_combobox.place(x=110, y=55, width=75)
    payment_status_combobox.current(0)
    # ____________ miles________________
    global total_miles_entry, milage_price_entry, area_surge_entry, cc_surcharge_entry
    total_miles_label = Label(pricing_frame, text="Total miles")
    area_surge_label = Label(pricing_frame, text="Area Surge")
    total_miles_label.place(x=200, y=25)
    area_surge_label.place(x=200, y=55)
    total_miles_entry = Entry(pricing_frame)
    total_miles_entry.place(x=280, y=25, width=50)
    area_surge_entry = Entry(pricing_frame)
    area_surge_entry.place(x=280, y=55, width=50)
    area_surge_entry.insert(0, "00.00")
    milage_price_label = Label(pricing_frame, text="Milage Price")
    cc_surcharge_label = Label(pricing_frame, text="CC Surcharge")
    milage_price_label.place(x=340, y=25)
    cc_surcharge_label.place(x=340, y=55)
    milage_price_entry = Entry(pricing_frame)
    cc_surcharge_entry = Entry(pricing_frame)
    milage_price_entry.place(x=430, y=25, width=50)
    cc_surcharge_entry.place(x=430, y=55, width=50)
    cc_surcharge_entry.insert(0, "00.00")
    # ___________wait tiem________________
    global wait_vr, agent_entry, cong_charges_entry, total_price_entry, drivers_price_entry

    wait_time_label = Label(pricing_frame, text="Wait Time")
    agent_label = Label(pricing_frame, text="Agent Fee")
    wait_time_label.place(x=490, y=25)
    agent_label.place(x=490, y=55)
    wait_vr = IntVar()
    wait_spin = ttk.Spinbox(pricing_frame, from_=0, to=99999, textvariable=wait_vr)
    wait_spin.set(0)
    wait_spin.place(x=550, y=25, width=50)
    agent_entry = Entry(pricing_frame)
    agent_entry.place(x=550, y=55, width=50)
    agent_entry.insert(0, "00.00")
    cong_charges_label = Label(pricing_frame, text=" Cong Charges")
    total_cost_label = Label(pricing_frame, text="Total Price")
    cong_charges_label.place(x=610, y=25)
    total_cost_label.place(x=610, y=55)
    cong_charges_entry = Entry(pricing_frame)
    cong_charges_entry.place(x=710, y=25)
    total_price_entry = Entry(pricing_frame)
    total_price_entry.place(x=710, y=55)
    drivers_price_label = Label(pricing_frame, text="Driver Price")
    drivers_price_label.place(x=840, y=55)
    drivers_price_entry = Entry(pricing_frame)
    drivers_price_entry.place(x=920, y=55)

    # ________________________job buttons____________________
    job_button_frame = Frame(top, bg="purple")
    job_button_frame.place(x=screen_width * 0.01, y=screen_height * 0.75, height=screen_height * 0.20,
                         width=screen_width)
    save_job_button = Button(job_button_frame, text="Save", command=save_booking)
    save_and_button = Button(job_button_frame, text="Save & Dispatch")
    show_map_button = Button(job_button_frame, text="Show Map", command=show_map_n)
    print_job_button = Button(job_button_frame, text="Print Job")
    clear_job_button = Button(job_button_frame, text="Clear")
    close_job_button = Button(job_button_frame, text="Close", command=lambda: top.destroy())
    save_job_button.place(x=40, y=10, width=120)
    save_and_button.place(x=170, y=10, width=120)
    show_map_button.place(x=300, y=10, width=120)
    print_job_button.place(x=430, y=10, width=120)
    clear_job_button.place(x=570, y=10, width=120)
    close_job_button.place(x=700, y=10, width=120)

    top.mainloop()
