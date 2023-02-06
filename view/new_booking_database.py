from view.new_b import *
import mysql.connector
from Driver.add_new_driver import *


def create_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Junaid.5814",
        database="Cabhook"
    )
    cursor = connection.cursor()

    # Create table for storing the form data
    create_table_query = """
        CREATE TABLE IF NOT EXISTS form_data (
            customer_name VARCHAR(255),
            phone VARCHAR(255),
            category VARCHAR(255),
            customer_email VARCHAR(255),
            note VARCHAR(255),
            black VARCHAR(255),
            date VARCHAR(255),
            time VARCHAR(255),
            auto VARCHAR(255),
            pickup VARCHAR(255),
            destination_list VARCHAR(255),
            return_job VARCHAR(255),
            regular VARCHAR(255),
            text VARCHAR(255),
            email VARCHAR(255),
            account VARCHAR(255),
            job_type VARCHAR(255),
            vehicle VARCHAR(255),
            number_of_vehicle VARCHAR(255),
            wait_return VARCHAR(255),
            reference VARCHAR(255),
            max_passenger VARCHAR(255),
            luggage VARCHAR(255),
            company_booked VARCHAR(255),
            driver_no VARCHAR(255),
            airline VARCHAR(255),
            flight VARCHAR(255),
            coming_from VARCHAR(255),
            payment_mode VARCHAR(255),
            payment_status VARCHAR(255),
            miles VARCHAR(255),
            miles_price VARCHAR(255),
            area_surge VARCHAR(255),
            cc_surcharge VARCHAR(255),
            wait VARCHAR(255),
            agent VARCHAR(255),
            cong_charges VARCHAR(255),
            total_price VARCHAR(255),
            drivers_price VARCHAR(255)
        );
        """
    cursor.execute(create_table_query)

    cursor.execute("""INSERT INTO form_data (customer_name, phone, category, customer_email, note,
    black, date, time, auto, pickup, destination_list, return_job, regular, text, email, account,
    job_type, vehicle, number_of_vehicle, wait_return, reference, max)""")
    connection.commit()
    cursor.close()
    connection.close()


create_table()
def check1():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Junaid.5814",
        database="Cabhook"
    )
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    for table in tables:
        print(table)




def droped():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Junaid.5814",
        database="Cabhook"
    )
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS drivers")


check1()

def mainii():
    customer_name = name_entry.get()
    phone = phone_entry.get()
    category = catagory_vr.get()
    customer_email = email_entry.get()
    note = notes_entry.get()
    black = black_check_vr.get()
    date = date_entry.get()
    time = time_entry.get()
    auto = auto_vr.get()
    pickup = address_entry.get()
    destination = destination_list.get()
    return_job = return_job_vr.get()
    regular = regular_booking_vr.get()
    text = message_vr.get()
    email = email_vr.get()
    account = accounts_vr.get()
    job_type = jobtype_vr.get()
    vehicle = vehicle_vr.get()
    number_of_vehicle = number_of_vehicles_vr.get()
    wait_return = returnbox_vr.get()
    reference = reference_entry.get()
    max_passenger = max_vr.get()
    luggage = luggage_vr.get()
    company_booked = company_vr.get()
    driver_no = driver_no_entry.get()
    airline = airline_entry.get()
    flight = flight_no_entry.get()
    coming_from = coming_from_entry.get()
    payment_mode = payment_mode_vr.get()
    payment_status = payment_status_vr.get()
    miles = total_miles_entry.get()
    miles_price = milage_price_entry.get()
    area_surge = area_surge_entry.get()
    cc_surcharge = cc_surcharge_entry.get()
    wait = wait_vr.get()
    agent = agent_entry.get()
    cong_charges = cong_charges_entry.get()
    total_price = total_price_entry.get()
    drivers_price = drivers_price_entry.get()
