import sqlite3


class Sql:
	def __init__(self):
		self.connection = sqlite3.connect('bot.db')
		self.cursor = self.connection.cursor()

	def baza_create(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
    		id integer,
    		username varchar(60),
    		first_name varchar(60),
    		tel integer NULL,
    		kor1 bigint NULL,
    		kor2 bigint NULL
    		)""")

	def user_add(self,idi,username,first_name):
		self.cursor.execute("INSERT INTO user VALUES ({}, '{}','{}',NULL, NULL, NULL)".format(idi,username,first_name))
		return self.connection.commit()

	def id_user(self,idi):
		self.cursor.execute(f"SELECT id FROM user WHERE id = {idi}")
		data = self.cursor.fetchone()
		return data

	def contact_update(self,idi,raqam):
		self.cursor.execute(f"UPDATE user SET tel = {raqam} WHERE id = {idi}")
		return self.connection.commit()

	def location_update(self,idi,kor1,kor2):
		self.cursor.execute(f"UPDATE user SET kor1 = {kor1},kor2 = {kor2} WHERE id = {idi}")
		return self.connection.commit()

	def admin_send(self,idi):
		self.cursor.execute(f"SELECT * FROM user WHERE id = {idi}")
		data = self.cursor.fetchone()
		return data