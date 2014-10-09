__author__ = 'phrayezzen'

from flask import Flask, request, jsonify, redirect
import MySQLdb as mdb

app = Flask(__name__)
con = mdb.connect("localhost", "root", "root", "test") # edit w/ new db info
cur = con.cursor(mdb.cursors.DictCursor)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/contact", methods=["GET", "POST", ""])
def contact():
    if request.method == "GET":
        with con:
            cur.execute("""SELECT * FROM contact""")
            rows = {"result": cur.fetchall()}
            return jsonify(rows)
        return jsonify({})
    elif request.method == "POST":
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

@app.route("/contact/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    with con:
        cur.execute("""DELETE FROM contact WHERE contactId = """ + str(contact_id))
    return "deleted " + str(contact_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0")