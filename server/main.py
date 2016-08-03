import os
import sqlite3
from flask import Flask, request
from count_cars import get_cars


app = Flask(__name__)

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


@app.route('/')
def index():
	return 'Flask server is working!'


@app.route('/api/set/<int:id>', methods=['GET', 'POST'])
def set(id):

	if (request.method != 'POST'):
		return 'only POST method'
	
	request.files['parking'].save('img/parking.jpg')
	request.files['background'].save('img/background.jpg')
	
	cnt = len(get_cars('img/parking.jpg', 'img/background.jpg'))

	cursor.execute('UPDATE `parking` SET `available`=(`all`-' + str(cnt) + ')  WHERE `id`=' + str(id))
	conn.commit()
	return 'ok'


@app.route('/api/get/<int:id>')
def get(id):
	
	cursor.execute('SELECT `available` FROM `parking` WHERE `id`=' + str(id))
	return str(cursor.fetchone()[0])


def main():
	app.run()


if __name__ == '__main__':
	main()