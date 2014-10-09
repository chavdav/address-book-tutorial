__author__ = 'phrayezzen'

import MySQLdb as mdb

con = mdb.connect("localhost", "root", "root", "test") # edit w/ new db info
cur = con.cursor(mdb.cursors.DictCursor)

def get_contacts():
    with con:
        cur.execute("""SELECT * FROM contact""")
        rows = {"result": cur.fetchall()}
        return rows


def add_contact(f):
    with con:
        cur.execute("""INSERT INTO contact (firstName, lastName, phone, address, city, state, zip)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                       (f['first'], f['last'], f['phone'], f['address'], f['city'], f['state'], f['zip']))
        con.commit()
        cur.execute("""SELECT * FROM contact WHERE contactId = """ + str(contact_id))
        contact = {"result": cur.fetchone()}
        return contact

def delete_contact(contact_id):
    with con:
        cur.execute("""DELETE FROM contact WHERE contactId = """ + str(contact_id))

# add_contact({
#     'first':'Xilin',
#     'last':'Liu',
#     'phone':'9107280992',
#     'address':'1601 Rice Boulevard',
#     'city':'Houston',
#     'state':'TX',
#     'zip':'77005'
#     })

# print get_contacts()

# delete_contact(NUMBER)