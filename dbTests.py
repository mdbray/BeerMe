#Jacob C. Levine
#CSCI 3308, Spring 2015


import unittest
import MySQLdb

# connect to database
database = MySQLdb.connect("localhost","root","","jakesdb" )

# prepare cursor object for executing queries
cursor = database.cursor()

"""
# data base query 
cursor.execute("SELECT * FROM Food")

# print all the first cell of all the rows
for row in cursor.fetchall() :
    print row[0],row[1]
"""

class TestSQLdb(unittest.TestCase):

	def test_getNameUsingBeerID(self): 
		cursor.execute("SELECT Name FROM BeerCat WHERE BeerCat.Id=1") # query data base for beer ID = 1
		name = cursor.fetchone()[0] # get name associated with beer ID = 1
		self.assertEqual(name,"American Ale") # check to see if name is correct
		# same steps for checking name of beer ID = 2
		cursor.execute("SELECT Name FROM BeerCat WHERE BeerCat.Id=2")
		name = cursor.fetchone()[0]
		self.assertEqual(name,"American Lager")


if __name__ == '__main__':
	unittest.main()
