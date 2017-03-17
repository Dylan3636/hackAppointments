import database
from flask import Flask, render_template, request, redirect, url_for, abort, session, make_response
class Professional:
	title= ""
	name = ""
	lname = ""
	profession = ""
	phone = ""
	keywords = []

	def __init__(self, title, name, lname, profession, phone, keywords):
		self.title = title		
		self.name = name
		self.lname = lname
		self.profession = profession
		self.phone = phone
		self.keywords = keywords

profs = [] 
columns = ['title','fullName','lastName','profession', str('Professionals.phoneNo'), 'keyword']
for title,name,lname,profession,phone,keys in database.advQuery(['Professionals','keywords'],columns,{'Professionals.phoneNo':'keywords.phoneNo'}):
	profs.append(Professional(title,name, lname, profession, str(phone), keys));
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))
#profs.append(Professional("Miss", "Uvira", "Singh", "Orthodontist", "+8888888", ["asdf", "fdsa"]))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('front.html', docs = profs)

@app.route('/submit', methods=['GET','POST'])
def submit():
	print({'title': request.form['title'], 'lastName': request.form['lastname'], 'fullName': request.form['fullname'], 'profession': request.form['speciality'], 'phoneNo': request.form['phonenum']})
	basicAdd('Hackathon.Professionals', {'title': request.form['title'], 'lastName': request.form['lastname'], 'fullName': request.form['fullname'], 'profession': request.form['speciality'], 'phoneNo': request.form['phonenum']})
	#response = make_response(redirect(url_for('/')))
	#return response
	return 'asf';


if __name__ == '__main__':
	app.run(debug=True);
