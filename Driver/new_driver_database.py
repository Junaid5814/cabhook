import mysql.connector
from Driver.add_new_driver import *
from datetime import datetime


def save():
    connection = mysql.connector.connect(
        host="sql12.freemysqlhosting.net",
        user="sql12595354",
        password="FhrtwRn45l",
        database="sql12595354",
        port=3306
    )
    cursor = connection.cursor()
    table_create = """
    CREATE TABLE IF NOT EXISTS bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        driver_no VARCHAR(255),
        pda_password VARCHAR(255),
        pda VARCHAR(255),
        mobile VARCHAR(255),
        driver_block VARCHAR(255),
        driver_first_name VARCHAR(255),
        driver_last_name VARCHAR(255),
        driver_gender VARCHAR(255),
        driver_birthday VARCHAR(255),
        driver_address_1 VARCHAR(255),
        driver_address_2 VARCHAR(255),
        driver_home_phone VARCHAR(255),
        driver_mobile VARCHAR(255),
        driver_date_joined VARCHAR(255),
        driver_date_left VARCHAR(255),
        driver_national_insurance VARCHAR(255),
        driver_license VARCHAR(255),
        driver_penalties VARCHAR(255),
        driver_pco VARCHAR(255),
        driver_pco_exp VARCHAR(255),
        driver_town VARCHAR(255),
        driver_postcode VARCHAR(255),
        insurance_premium VARCHAR(255),
        insurance_ex VARCHAR(255),
        road_expiry VARCHAR(255),
        pco_number VARCHAR(255),
        pco_expiry VARCHAR(255),
        veh_reg VARCHAR(255),
        veh_make VARCHAR(255),
        veh_model VARCHAR(255),
        veh_color VARCHAR(255),
        veh_category VARCHAR(255),
        veh_ownership VARCHAR(255),
        type_vehicle VARCHAR(255),
        deposit VARCHAR(255),
        base VARCHAR(255),
        radio VARCHAR(255),
        outstanding_b VARCHAR(255),
        commission_rate VARCHAR(255),
        commission_rate_acc VARCHAR(255),
        rent VARCHAR(255),
        salary VARCHAR(255)
    );
    """
    cursor.execute(table_create)

    cursor.execute(""" INSERT INTO bookings (driver_no, pda_password, pda, mobile, driver_block, driver_first_name,
     driver_last_name, driver_gender, driver_birthday, driver_address_1, driver_address_2, driver_home_phone,
     driver_mobile, driver_date_joined, driver_date_left, driver_national, driver_license, driver_penalties,
     driver_pco, driver_pco_exp, driver_town, driver_postcode, insurance_premium, insurance_ex,
     road_expiry, pco_number, pco_expiry, veh_reg, veh_make, veh_model, veh_color, veh_category,
     veh_ownership, type_vehicle, deposit, base, radio, outstanding_b, commission_rate, commission_rate_acc,
     rent, salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)""",
    (driver_no, pda_password, pda, mobile, driver_block, driver_first_name, driver_last_name, driver_gender,
       driver_birthday, driver_address_1, driver_address_2, driver_home_phone, driver_mobile,
       driver_date_joined, driver_date_left, driver_national_insurance, driver_license, driver_penalties,
       driver_pco, driver_pco_exp, driver_town, driver_postcode, insurance_premium, insurance_ex,
       road_expiry, pco_number, pco_expiry, veh_reg, veh_make, veh_model, veh_color, veh_category,
       veh_ownership, type_vehicle, deposit, base, radio, outstanding_b, commission_rate, commission_rate_acc,
       rent, salary))



    connection.commit()
    cursor.close()
    connection.close()




driver_no = driver_no_entry.get()
pda_password = pda_password_entry.get()
pda = pda_vr.get()
mobile = mobile_vr.get()
driver_block = driver_blocked_vr.get()
driver_first_name = driver_first_name_entry.get()
driver_last_name = driver_last_name_entry.get()
driver_gender = driver_gender_vr.get()
driver_birthday = driver_birthday_vr.get()
driver_address_1 = driver_address_1_entry.get()
driver_address_2 = driver_address_2_entry.get()
driver_home_phone = driver_home_phone_entry.get()
driver_mobile = driver_mobile_entry.get()
convert_j_date = driver_date_joined_vr.get()
driver_date_joined = datetime.strptime(convert_j_date, '%m/%d/%y').date()
convert_ll_date = driver_date_left_vr.get()
driver_date_left = datetime.strptime(convert_ll_date, '%m/%d/%y').date()
driver_national_insurance = driver_national_insurance_entry.get()
driver_license = driver_license_entry.get()
driver_penalties = driver_penalties_vr.get()
driver_pco = driver_pco_entry.get()
pco_expiry_convert = driver_pco_exp_vr.get()
driver_pco_exp = datetime.strptime(pco_expiry_convert, '%m/%d/%y').date()
driver_town = driver_town_entry.get()
driver_postcode = driver_postcode_entry.get()
insurance_premium = insurance_premium_entry.get()
insurance_ex_con = insurance_ex_vr.get()
insurance_ex = datetime.strptime(insurance_ex_con, '%m/%d/%y').date()
road_expiry_con = road_expiry_vr.get()
road_expiry = datetime.strptime(road_expiry_con, '%m/%d/%y').date()
pco_number = pco_number_entry.get()
pco_ex_con = pco_expiry_vr.get()
pco_expiry = datetime.strptime(pco_ex_con, '%m/%d/%y').date()
veh_reg = veh_reg_entry.get()
veh_make = veh_make_entry.get()
veh_model = veh_model_entry.get()
veh_color = veh_color_entry.get()
veh_category = veh_category_vr.get()
veh_ownership = veh_ownership_vr.get()
type_vehicle = type_vehicle_vr.get()
deposit = deposit_entry.get()
base = base_vr.get()
radio = radio_vr.get()
outstanding_b = outstanding_b_entry.get()
commission_rate = commission_rate_vr.get()
commission_rate_acc = commission_rate_acc_vr.get()
rent = rent_entry.get()
salary = salary_entry.get()

def renaming():
    connection = mysql.connector.connect(
        host="sql12.freemysqlhosting.net",
        user="sql12595354",
        password="FhrtwRn45l",
        database="sql12595354",
        port=3306
    )

    cursor = connection.cursor()

    old_table_name = "bookings"
    new_table_name = "Drivers"

    rename_table_query = "RENAME TABLE {0} TO {1};".format(old_table_name, new_table_name)

    cursor.execute(rename_table_query)

    connection.commit()

    cursor.close()
    connection.close()

def delete():
    connection = mysql.connector.connect(
        host="sql12.freemysqlhosting.net",
        user="sql12595354",
        password="FhrtwRn45l",
        database="sql12595354",
        port=3306
    )
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")

    for x in cursor:
        print(x)




