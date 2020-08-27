from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'Jariel'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'toor' #enter your password here 
app.config['MYSQL_DB'] = 'contact' #database name

mysql = MySQL(app)
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM CONTACT")
    data = cur.fetchall()
    cur.execute("SELECT  * FROM ADDRESS")
    data1 = cur.fetchall()
    cur.execute("SELECT  * FROM PHONE")
    data2 = cur.fetchall()
    cur.execute("SELECT  * FROM DATE")
    data3 = cur.fetchall()
    cur.close()
    return render_template('index2.html', contacts=data ,address=data1 ,phone=data2 ,date=data3)

@app.route('/search', methods = ['POST'])
def search():
    if request.method == "POST":
        search_key = request.form['search_key']
        search_key=("%' OR '".join(search_key.split()))
        cur = mysql.connection.cursor()
        query1="SELECT  * FROM CONTACT WHERE Fname LIKE '"+str(search_key)+"%' OR Mname LIKE '"+str(search_key)+"%' OR Lname LIKE '"+str(search_key)+"%' OR Contact_id LIKE '"+str(search_key)+"%';"
        query2="SELECT  COUNT(*) AS Hits FROM CONTACT WHERE Fname LIKE '"+str(search_key)+"%' OR Mname LIKE '"+str(search_key)+"%' OR Lname LIKE '"+str(search_key)+"%' OR Contact_id LIKE '"+str(search_key)+"%';"
        cur.execute(query1)
        data = cur.fetchall()
        cur.execute(query2)
        data1 = cur.fetchall()
        cur.close()
    return render_template('index2.html', contacts=data, count=data1 )
@app.route('/searchglobal', methods = ['POST'])
def searchglobal():
    if request.method == "POST":
        search_key = request.form['search_key']
        search_key=("%' OR '".join(search_key.split()))
        cur = mysql.connection.cursor()
        query1="Select * from CONTACT WHERE Contact_id in (select P.Contact_id from ADDRESS AS A JOIN CONTACT AS C ON A.Contact_id=C.Contact_id JOIN DATE AS D ON C.Contact_id=D.Contact_id JOIN PHONE AS P ON D.Contact_id=P.Contact_id WHERE Address LIKE '"+str(search_key)+"%' OR Address_type LIKE '"+str(search_key)+"%' OR Zip LIKE '"+str(search_key)+"%' OR State LIKE '"+str(search_key)+"%' OR City LIKE '"+str(search_key)+"%' OR Address_id LIKE '"+str(search_key)+"%' OR Fname LIKE '"+str(search_key)+"%' OR Mname LIKE '"+str(search_key)+"%' OR Lname LIKE '"+str(search_key)+"%' OR C.Contact_id LIKE '"+str(search_key)+"%' OR Phone_id LIKE '"+str(search_key)+"%' OR Number LIKE '"+str(search_key)+"%' OR Phone_type LIKE '"+str(search_key)+"%' OR Area_code LIKE '"+str(search_key)+"%' OR Date_id LIKE '"+str(search_key)+"%' OR Date_type LIKE '"+str(search_key)+"%' OR Date LIKE '"+str(search_key)+"%' );"
        query2="SELECT  COUNT(*) AS Hits from CONTACT WHERE Contact_id in (select P.Contact_id from ADDRESS AS A JOIN CONTACT AS C ON A.Contact_id=C.Contact_id JOIN DATE AS D ON C.Contact_id=D.Contact_id JOIN PHONE AS P ON D.Contact_id=P.Contact_id WHERE Address LIKE '"+str(search_key)+"%' OR Address_type LIKE '"+str(search_key)+"%' OR Zip LIKE '"+str(search_key)+"%' OR State LIKE '"+str(search_key)+"%' OR City LIKE '"+str(search_key)+"%' OR Address_id LIKE '"+str(search_key)+"%' OR Fname LIKE '"+str(search_key)+"%' OR Mname LIKE '"+str(search_key)+"%' OR Lname LIKE '"+str(search_key)+"%' OR C.Contact_id LIKE '"+str(search_key)+"%' OR Phone_id LIKE '"+str(search_key)+"%' OR Number LIKE '"+str(search_key)+"%' OR Phone_type LIKE '"+str(search_key)+"%' OR Area_code LIKE '"+str(search_key)+"%' OR Date_id LIKE '"+str(search_key)+"%' OR Date_type LIKE '"+str(search_key)+"%' OR Date LIKE '"+str(search_key)+"%' );"
        cur.execute(query1)
        data = cur.fetchall()
        cur.execute(query2)
        data1 = cur.fetchall()
        cur.close()
    return render_template('index2.html', globalsearch=data, globalcount=data1 )
@app.route('/searchaddress', methods = ['POST'])
def searchaddress():
    if request.method == "POST":
        search_key = request.form['search_key']
        search_key=("%' OR '".join(search_key.split()))
        cur = mysql.connection.cursor()
        query1="SELECT  * FROM ADDRESS WHERE Address LIKE '"+str(search_key)+"%' OR Address_type LIKE '"+str(search_key)+"%' OR Zip LIKE '"+str(search_key)+"%' OR State LIKE '"+str(search_key)+"%' OR City LIKE '"+str(search_key)+"%' OR Address_id LIKE '"+str(search_key)+"%' OR Contact_id LIKE '"+str(search_key)+"%';"
        query2="SELECT  COUNT(*) AS Hits FROM ADDRESS WHERE Address LIKE '"+str(search_key)+"%' OR Address_type LIKE '"+str(search_key)+"%' OR Zip LIKE '"+str(search_key)+"%' OR State LIKE '"+str(search_key)+"%' OR City LIKE '"+str(search_key)+"%' OR Address_id LIKE '"+str(search_key)+"%' OR Contact_id LIKE '"+str(search_key)+"%';"
        cur.execute(query1)
        data = cur.fetchall()
        cur.execute(query2)
        data1 = cur.fetchall()
        cur.close()
    return render_template('index2.html', address=data, countaddress=data1 )

@app.route('/searchphone', methods = ['POST'])
def searchphone():
    if request.method == "POST":
        search_key = request.form['search_key']
        search_key=("%' OR '".join(search_key.split()))
        cur = mysql.connection.cursor()
        query1="SELECT  *  FROM PHONE WHERE Phone_id LIKE '"+str(search_key)+"%' OR Number LIKE '"+str(search_key)+"%' OR Phone_type LIKE '"+str(search_key)+"%' OR Area_code LIKE '"+str(search_key)+"%' OR Contact_id LIKE '"+str(search_key)+"%';"
        query2="SELECT  COUNT(*) AS Hits FROM PHONE WHERE Phone_id LIKE '"+str(search_key)+"%' OR Number LIKE '"+str(search_key)+"%' OR Phone_type LIKE '"+str(search_key)+"%' OR Area_code LIKE '"+str(search_key)+"%' OR Contact_id LIKE '"+str(search_key)+"%';"
        cur.execute(query1)
        data = cur.fetchall()
        cur.execute(query2)
        data1 = cur.fetchall()
        cur.close()
    return render_template('index2.html', phone=data, countphone=data1 )

@app.route('/searchdate', methods = ['POST'])
def searchdate():
    if request.method == "POST":
        search_key = request.form['search_key']
        search_key=("%' OR '".join(search_key.split()))
        cur = mysql.connection.cursor()
        query1="SELECT  *  FROM DATE WHERE Date_id LIKE '"+str(search_key)+"%' OR Date_type LIKE '"+str(search_key)+"%' OR Date LIKE '"+str(search_key)+"%' OR Contact_id LIKE '"+str(search_key)+"%';"
        query2="SELECT  COUNT(*) AS Hits FROM DATE WHERE Date_id LIKE '"+str(search_key)+"%' OR Date_type LIKE '"+str(search_key)+"%' OR Date LIKE '"+str(search_key)+"%' OR Contact_id LIKE '"+str(search_key)+"%';"
        cur.execute(query1)
        data = cur.fetchall()
        cur.execute(query2)
        data1 = cur.fetchall()
        cur.close()
    return render_template('index2.html', date=data, countdate=data1 )


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        Contact_id = request.form['Contact_id']
        Fname = request.form['Fname']
        Mname = request.form['Mname']
        Lname = request.form['Lname']
        cur = mysql.connection.cursor()
        if(Contact_id==""):
            cur.execute("INSERT INTO CONTACT (Fname,Mname,Lname) VALUES (%s, %s, %s)", (Fname,Mname,Lname))
        else:
            cur.execute("INSERT INTO CONTACT (Contact_id,Fname,Mname,Lname) VALUES (%s, %s, %s, %s)", (Contact_id,Fname,Mname,Lname))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/insertaddress', methods = ['POST'])
def insertaddress():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        Contact_id = request.form['Contact_id']
        Address = request.form['Address']
        Address_id = request.form['Address_id']
        Address_type = request.form['Address_type']
        City = request.form['City']
        State = request.form['State']
        Zip = request.form['Zip']
        cur = mysql.connection.cursor()
        if(Address_id==""):
            cur.execute("INSERT INTO ADDRESS (Contact_id,Address,Address_type,City,State,Zip) VALUES (%s, %s, %s, %s, %s, %s)", (Contact_id,Address,Address_type,City,State,Zip))
        else:
            cur.execute("INSERT INTO ADDRESS (Address_id,Contact_id,Address,Address_type,City,State,Zip) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Address_id,Contact_id,Address,Address_type,City,State,Zip))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/insertphone', methods = ['POST'])
def insertphone():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        Contact_id = request.form['Contact_id']
        Phone_id = request.form['Phone_id']
        Phone_type = request.form['Phone_type']
        Area_code = request.form['Area_code']
        Number = request.form['Number']
        cur = mysql.connection.cursor()
        if(Phone_id==""):
            cur.execute("INSERT INTO PHONE (Phone_type,Area_code,Contact_id,Number) VALUES (%s, %s, %s, %s)", (Phone_type,Area_code,Contact_id,Number))
        else:
            cur.execute("INSERT INTO PHONE (Phone_id,Phone_type,Area_code,Contact_id,Number) VALUES (%s, %s, %s, %s, %s)", (Phone_id,Phone_type,Area_code,Contact_id,Number))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/insertdate', methods = ['POST'])
def insertdate():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        Contact_id = request.form['Contact_id']
        Date_id = request.form['Date_id']
        Date_type = request.form['Date_type']
        Date = request.form['Date']
        cur = mysql.connection.cursor()
        if(Date_id==""):
            cur.execute("INSERT INTO DATE (Date,Contact_id,Date_type) VALUES (%s, %s, %s)", (Date,Contact_id,Date_type))
        else:
            cur.execute("INSERT INTO DATE (Date_id,Date,Contact_id,Date_type) VALUES (%s,%s, %s, %s)", (Date_id,Date,Contact_id,Date_type))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM CONTACT WHERE Contact_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))
@app.route('/deleteaddress/<string:id_data>', methods = ['GET'])
def deleteaddress(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM ADDRESS WHERE Address_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))
@app.route('/deletephone/<string:id_data>', methods = ['GET'])
def deletephone(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM PHONE WHERE Phone_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))
@app.route('/deletedate/<string:id_data>', methods = ['GET'])
def deletedate(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM DATE WHERE Date_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))



@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        Contact_id = request.form['Contact_id']
        Fname = request.form['Fname']
        Mname = request.form['Mname']
        Lname = request.form['Lname']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE CONTACT
               SET Contact_id=%s, Fname=%s, Mname=%s, Lname=%s
               WHERE Contact_id=%s
            """, (Contact_id,Fname,Mname,Lname,Contact_id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/updateaddress',methods=['POST','GET'])
def updateaddress():
    if request.method == 'POST':
        Contact_id = request.form['Contact_id']
        Address = request.form['Address']
        Address_id = request.form['Address_id']
        Address_type = request.form['Address_type']
        City = request.form['City']
        State = request.form['State']
        Zip = request.form['Zip']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE ADDRESS
               SET Address_id=%s,Contact_id=%s,Address_type=%s, Address=%s, City=%s, State=%s, Zip=%s
               WHERE Address_id=%s
            """, (Address_id,Contact_id,Address_type,Address,City,State,Zip,Address_id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/updatephone',methods=['POST','GET'])
def updatephone():
    if request.method == 'POST':
        Contact_id = request.form['Contact_id']
        Phone_id = request.form['Phone_id']
        Phone_type = request.form['Phone_type']
        Area_code = request.form['Area_code']
        Number = request.form['Number']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE PHONE
               SET Phone_id=%s, Contact_id=%s, Phone_type=%s, Area_code=%s, Number=%s
               WHERE Phone_id=%s
            """, (Phone_id,Contact_id,Phone_type,Area_code,Number,Phone_id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/updatedate',methods=['POST','GET'])
def updatedate():
    if request.method == 'POST':
        Contact_id = request.form['Contact_id']
        Date_id = request.form['Date_id']
        Date_type = request.form['Date_type']
        Date = request.form['Date']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE DATE
               SET Date_id=%s, Contact_id=%s, Date_type=%s, Date=%s
               WHERE Date_id=%s
            """, (Date_id,Contact_id,Date_type,Date,Date_id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
