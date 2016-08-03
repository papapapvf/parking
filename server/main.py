import sqlite3
from flask import Flask

app = Flask(__name__)

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

@app.route('/')
def index():
	return 'Flask server is working!'

@app.route('/api/set/<int:id>&<int:available>')
def send(id, available):
	cursor.execute('UPDATE `parking` SET `available`=' + str(available) + '  WHERE `id`=' + str(id))
	conn.commit()
	return 'ok'
	# return str(id) + str(available)

@app.route('/api/get/<int:id>')
def get(id):
	cursor.execute('SELECT `available` FROM `parking` WHERE `id`=' + str(id))
	return str(cursor.fetchone()[0])

def main():
	app.run()

if __name__ == '__main__':
	main()