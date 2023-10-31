from mysql.connector import Error

import mysql.connector

class DBConnection:
	def __init__(self):
		try:
			self.connection = mysql.connector.connect(user="{username}", 
														password="{password}", 
														host="{host}", 
														port=3306, 
														database="{database}", 
														ssl_ca="{ca-cert filename}", 
														ssl_disabled=False)
			self.cursor = self.connection.cursor()
		except mysql.connector.Error as err:
			print("Could not connect to the database: {}".format(err))

	def closeConnection(self):
		self.connection.close()

	def executeManyQuery(self, query, values):
		try:
			self.cursor.executemany(query, values)
			self.connection.commit()
			print(self.cursor.rowcount, "records was inserted.")
		except Error as err:
			print(err)