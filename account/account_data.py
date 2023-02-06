import mysql.connector
from twilio.rest.api.v2010 import account

from create_new_account import *


def save():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Junaid.5814",
        database="Cabhook"
    )

    from create_new_account import new_account
    cursor = connection.cursor()
    account_name = account_name_entry.get()
    account_email = account_email_entry.get()
    account_telephone = account_tel_no_entry.get()
    account_contact_name = account_contact_name_entry.get()
    account_web_address = account_web_address_entry.get()
    account_address = account_address_entry.get()
    account_code = account_code_entry.get()
    account_mobile = account_mobile_entry.get()
    account_fax = account_fax_entry.get()
    account_password = account_password_entry.get()
    account_account_no = account_no_entry.get()
    account_note = account_notes_entry.get()
    account_type = account_type_vr.get()
    account_agent = account_agent_vr.get()
    account_commission = account_commission_entry.get()
    account_ccno = account_ccno_entry.get()
    account_payment = account_payment_vr.get()
    account_close = account_close_vr.get()
    account_invoice_fare = account_invoice_fare_deduction_vr.get()
    account_discount = account_discount_vr.get()
    account_admin_fee = account_admin_fee_vr.get()

    cursor.execute(
        "INSERT INTO accounts (account_name, email, tel_no, contact_name, web_address, address, code, mobile, "
        "fax, password, account_no, account_type, account_agent, commission, ccno, payment, close, "
        "fare_deduction, discount, admin_fee, note) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
        "%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (account_name, account_email, account_telephone, account_contact_name, account_web_address, account_address,
         account_code, account_mobile, account_fax, account_password, account_account_no, account_type, account_agent,
         account_commission, account_ccno, account_payment, account_close, account_invoice_fare, account_discount,
         account_admin_fee, account_note))

    connection.commit()
    cursor.close()
    connection.close()


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Junaid.5814",
    database="Cabhook"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM accounts")
data=cursor.fetchall()
print(data)



