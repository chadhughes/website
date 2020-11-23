import os, binascii
from flask import Flask, render_template, request, redirect, session, jsonify
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
#from flask_wtf.csrf import CsrfProtect
from flask_wtf.csrf import CSRFProtect
from flask_sslify import SSLify
from faker import Faker

WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')
APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY')

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SSL_DISABLE'] = False
#app.config['SSL_DISABLE'] = bool(os.environ.get('SSL_DISABLE'))
app.secret_key = APP_SECRET_KEY

### SSL HTTPS ###
if not app.debug and not app.testing and not app.config['SSL_DISABLE'] is True:
	sslify = SSLify(app)
	
@app.route('/')
def index():
	fake = Faker('la')
	fake_sent = fake.sentences(nb=10)
	fake_para = fake.paragraphs(nb=10)
	#return render_template('index.html', fake_sent=fake_sent, fake_para=fake_para)
	return render_template('home.html', fake_sent=fake_sent, fake_para=fake_para)
	
@app.route("/hello")
def hello():
	fake = Faker('la')
	fake_sent = fake.sentences(nb=10)
	fake_para = fake.paragraphs(nb=10)
	# return "Hello World!"
	return render_template('hello.html', fake_sent=fake_sent, fake_para=fake_para)

@csrf.exempt
@app.route("/.well-known/keybase.txt")
def keybase():
	return render_template('keybase.txt')

'''
@csrf.exempt
@app.route('/api_v1', methods=['POST'])
def api01():
	#if request.method == 'POST':
	#plaintext = b"foo foo foo bar"
	#passphrase = b'super secret phrase'
	plaintext = request.form['plaintext'].encode('utf-8')
	passphrase = request.form['passphrase'].encode('utf-8')
	## ENCRYPT
	enc = triplesec.encrypt(plaintext, passphrase)
	ciphertext = binascii.hexlify(enc)
	## DECRYPT
	enc = binascii.unhexlify(ciphertext)
	decryptedtext = triplesec.decrypt(enc, passphrase).decode()
	## jsonify
	jout = [
		{'plaintext': decryptedtext, 'ciphertext': ciphertext.decode()}
	]
	return jsonify(results=jout)
	#return render_template('api_v1.html', plaintext=plaintext, ciphertext=ciphertext.decode(), decryptedtext=decryptedtext)
'''

@app.route('/getMyIP', methods=['GET'])
def get_ipaddr():
    if request.access_route:
        return request.access_route[0]
    else:
        return request.remote_addr or '127.0.0.1'
	
@app.route('/tumblr/')
def tumblr_redir():
	return redirect("https://tumblr.chadhughes.com/", code=302)
	
@app.route('/blog1/')
def blog_redir():
	return redirect("https://tumblr.chadhughes.com/", code=302)
	
@app.route('/blog2/')
def blogger_redir():
	return redirect("https://blog.chadhughes.com/", code=302)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)


