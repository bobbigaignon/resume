import os
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def main():
	return render_template('main.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)
