#Jacob C. Levine
#CSCI 3308, Spring 2015


import unittest
import MySQLdb

# connect to database
database = MySQLdb.connect("localhost","root","","BeerMeDB" )

# prepare cursor object for executing queries
cursor = database.cursor()

"""
# data base query example 
cursor.execute("SELECT * FROM Food")

# example of how to print all the first cell of all the rows
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
	
	def test_getColorUsingColorID(self):
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=1") 
		name = cursor.fetchone()[0]
		self.assertEqual(name,"Dark")
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=2")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Brown")
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=3")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Amber")
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=4")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Pale")
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=5")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Light")

if __name__ == '__main__':
	unittest.main()
