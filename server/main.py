import os
import sqlite3
from flask import Flask, request

from count_cars import get_cars
import config

app = Flask(__name__)

conn = sqlite3.connect(config.db_name)
cursor = conn.cursor()


@app.route('/')
def index():
	return 'Flask server is working!'


@app.route('/api/set/<int:id>', methods=['GET', 'POST'])
def set(id):

	if (request.method != 'POST'):
		return 'only POST method'
	
	request.files['parking'].save(config.p_img_dir)
	request.files['background'].save(config.b_img_dir)
	
	cnt = len(get_cars(config.p_img_dir, config.b_img_dir))

	cursor.execute('UPDATE `parking` SET `available`=(`all`-' + str(cnt) + ')  WHERE `id`=' + str(id))
	conn.commit()
	return 'ok'


@app.route('/api/get/all')
def get_all():

	cursor.execute('SELECT `available` FROM `parking`')
	return ' '.join([str(x[0]) for x in cursor.fetchall()])
	# return str(cursor.fetchall())


@app.route('/api/get/<int:id>')
def get(id):
	
	cursor.execute('SELECT `available` FROM `parking` WHERE `id`=' + str(id))
	return str(cursor.fetchone()[0])


def main():
	app.run()


if __name__ == '__main__':
	main()