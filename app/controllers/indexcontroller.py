from flask import Flask, url_for, render_template, redirect, request, session
from app import app
# from app.models.user import User ## import kelas User dari model

# @app.route('/', methods = ['GET'])
# def index():
# 	user =  User() ## membuat objek dari kelas user
# 	nama = user.getName() ## memanggil method untuk mengambil nama
# 	return render_template('index.html', nama=nama)
app.secret_key="tes"
pengguna = None
cek = ''
@app.route('/')
def index():
	global cek
	cek=''
	if session:
		return render_template('index2.html', pengguna=session)
	else:
		return render_template('index2.html')

@app.route('/logout')
def logout():
	if session:
		session.pop("username")
		session.pop("password")
	return redirect(url_for("index"))	

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login', methods=["POST", "GET"])
def login():
	error = None
	session["username"] = "alex"
	session["password"] = "alex"
	if request.method == "POST":
		if cek=='ada':
			return render_template('gambar.html', pengguna=session)
		else:
			if request.form["nama_user"] != session["username"]:
				error = 'Username is not exist'
				return render_template('login.html', error=error)
			else:
				if request.form["kata_sandi"] == session["password"]:
					return render_template('index2.html', pengguna=session)	
				else:
					error = 'password is invalid'
					return render_template('login.html', error=error, pengguna=session)	
	else:
		return render_template('login.html')



@app.route('/gambar')
def gambar():
	if session:
		return render_template('gambar.html')
	else:
		global cek
		cek = 'ada'
		return redirect(url_for('login',cek=cek))
