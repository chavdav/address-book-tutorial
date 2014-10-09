__author__ = 'phrayezzen'

from flask import Flask, request, jsonify, redirect
import MySQLdb as mdb

app = Flask(__name__)
con = mdb.connect("localhost", "root", "root", "test") # edit w/ new db info
cur = con.cursor(mdb.cursors.DictCursor)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/getContacts")
def get_contacts():
    with con:
        cur.execute("""SELECT * FROM contact""")
        rows = {"result": cur.fetchall()}
        return jsonify(rows)
    return jsonify({})

@app.route("/addContact", methods = ["POST"])
def add_contact():
    f = request.form
    with con:
        cur.execute("""INSERT INTO contact (firstName, lastName, phone, address, city, state, zip)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                       (f['first'], f['last'], f['phone'], f['address'], f['city'], f['state'], f['zip']))
        con.commit()
        cur.execute("""SELECT * FROM contact WHERE contactId = """ + str(cur.lastrowid))
        contact = {"result": [cur.fetchone()]}
        return jsonify(contact)
    return jsonify({})

@app.route("/deleteContact/<int:contact_id>")
def delete_contact(contact_id):
    with con:
        cur.execute("""DELETE FROM contact WHERE contactId = """ + str(contact_id))
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)