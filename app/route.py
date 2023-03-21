from flask import render_template, request, session
from app import app
import sqlite3
from twilio.rest import Client


@app.route('/')
def index():
	return render_template("index.html")



@app.route('/message', methods=['POST'])
def index_2():

	reg_no = request.form.get('reg_no')
	password = request.form.get('pasword')
	level = request.form.get('lvl')
	semester = request.form.get('smester')



	#Connecting to sqlite
	conn = sqlite3.connect('results.db')
	#Creating a cursor object using the cursor() method
	cursor = conn.cursor()

	try:
		msg = ''
		#Retrieving specific records using the where clause
		cursor.execute("SELECT FIRST_NAME from STUDENT WHERE REG_NO LIKE ? AND PASSWORD LIKE ?", (reg_no, password, ))
		fn = cursor.fetchone()[0]

		cursor.execute("SELECT LAST_NAME from STUDENT WHERE REG_NO  LIKE ? AND PASSWORD LIKE ?", (reg_no, password, ))
		ln = cursor.fetchone()[0]

		cursor.execute("SELECT PHONE_NO from STUDENT WHERE REG_NO LIKE ? AND PASSWORD LIKE ?", (reg_no, password, ))
		pn = cursor.fetchone()[0]

		cursor.execute("SELECT SGPA from STUDENT WHERE REG_NO LIKE ? AND PASSWORD LIKE ? AND LEVEL LIKE ? AND SEMESTER LIKE ?", (reg_no, password, level, semester, ))
		sgpa = cursor.fetchone()[0]

		cursor.execute("SELECT CUMGPA from STUDENT WHERE REG_NO LIKE ? AND PASSWORD LIKE ? AND LEVEL LIKE ? AND SEMESTER LIKE ?", (reg_no, password, level, semester, ))
		cumgpa = cursor.fetchone()[0]

		cursor.execute("SELECT CUFAILED from STUDENT WHERE REG_NO LIKE ? AND PASSWORD LIKE ? AND LEVEL LIKE ? AND SEMESTER LIKE ?", (reg_no, password, level, semester, ))
		cufail = cursor.fetchone()[0]

		cursor.execute("SELECT REMARKS from STUDENT WHERE REG_NO LIKE ? AND PASSWORD LIKE ? AND LEVEL LIKE ? AND SEMESTER LIKE ?", (reg_no, password, level, semester, ))
		remark = cursor.fetchone()[0]
		print(f'{fn} {ln},\nYour result is: SGPA: {sgpa}, CUMGPA: {cumgpa}, CUFAILED: {cufail}, Remarks: {remark} ')	

		

		#Commit your changes in the database
		conn.commit()
		#Closing the connection
		conn.close()

		"""		
		#Your account Sid and auth token
		account_sid = 'ACXXXXXXXXXXXXXXXX'
		auth_token = 'your_auth_token'

		client = Client(account_sid, auth_token)

		message = client.messages.create(
			from_ = 'laklss',
			body = f'{fn} {ln},\nYour result is: SGPA: {sgpa}, CUMGPA: {cumgpa}, CUFAILED: {cufail}, Remarks: {remark} ',
			to == pn
			)
		
		print(message.sid)
		"""

		return render_template("index.html", msg = msg)

	except TypeError as e:
		msg = 'Insert Valid Matric Number and password'
		return render_template("index.html", msg = msg)




@app.route('/pg2')
def page2():
	return render_template("login.html")


@app.route('/login', methods=['POST'])
def logg():
	try:
		msg = ''
		password = request.form.get('admins')

		#Connecting to sqlite
		conn = sqlite3.connect('results.db')
		#Creating a cursor object using the cursor() method
		cursor = conn.cursor()

		#Retrieving specific records using the where clause
		cursor.execute("SELECT FIRST_NAME from ADMIN WHERE PASSWORD LIKE ?", (password, ))
		global fn
		fn = cursor.fetchone()[0]
		

		cursor.execute("SELECT LAST_NAME from ADMIN WHERE PASSWORD LIKE ?", (password, ))
		global ln
		ln = cursor.fetchone()[0]

		session['loggedin'] = True
		session['id'] = password + password
		session['username'] = fn
		return render_template("upload.html", name=f"{fn} {ln}")

	except TypeError as e:
		msg = 'Incorrect Password!'
		return render_template("login.html", msg = msg)



@app.route('/upload', methods=['POST'])
def uplod():
	try:
		reg_no = request.form.get('reg_no')
		level = request.form.get('lvl')
		semester = request.form.get('smester')
		sgpa = request.form.get('sgpa')
		cumgpa = request.form.get('cumgpa')
		cufail = request.form.get('cufail')
		remark = request.form.get('remark')
		#Connecting to sqlite
		conn = sqlite3.connect('results.db')
		#Creating a cursor object using the cursor() method
		cursor = conn.cursor()

		#put the update code hia
		cursor.execute("UPDATE STUDENT SET SGPA = ?, CUMGPA = ?, CUFAILED = ?, REMARKS = ? WHERE REG_NO LIKE ? AND LEVEL LIKE ? AND SEMESTER LIKE ?", (sgpa, cumgpa, cufail, remark, reg_no, level, semester, ))
		


		cursor.execute('''SELECT * from STUDENT''')

		#Fetching 1st row from the table
		result = cursor.fetchall();
		print(result)
		#Commit your changes in the database
		conn.commit()
		#Closing the connection
		conn.close()

		return render_template("upload.html", name=f"{fn} {ln}")

	except TypeError as e:
		return render_template("upload.html", name=f"{fn} {ln}")






	
	
	
	
	


"""
@app.route('/download', methods=['GET'])
def download():
	
	url = request.form['linkk']
	req = requests.get(url)
	soup = BeautifulSoup(req.text, "html.parser")
	imagen = soup.find("meta", attrs={"property": "og:image"})
	sourcee = imagen['content']
	return render_template("download.html")

"""