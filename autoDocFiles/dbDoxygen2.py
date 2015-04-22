## dbTests.py
# Documentation for this module
# 
# this document is designed to use automated testing to confirm that our database preforms
# as expected.
# 
# It is our only code script, which is why we are using it for the autodoc assignment.
# data base query example 
# cursor.execute("SELECT * FROM Food")
# 
# example of how to print all the first cell of all the rows
# for row in cursor.fetchall() :
#     print row[0],row[1]

import unittest
import MySQLdb

## a global variable
database = MySQLdb.connect("localhost","user","","BeerMeDB" )


## a global variable prepare cursor object for executing queries
cursor = database.cursor()


## \brief    Test class for testing database.
#  \details   This class tests that SELECT statements return desired results.
#  \authors	Jacob C. Levine, Spencer Wilson, Matt Geckle
class TestSQLdb(unittest.TestCase):
        
 	## \brief    Confirms that beer category ID's are linked to proper beer category names in BeerCat table. 
	#  \details    Test format: SELECT Name FROM BeerCat Where BeerCat.Id = <ID number>
	#  \functionality	Returns false if a self.assert fails
	#  @param self The object pointer	
	def test_getNameUsingBeerID(self): 
		
		cursor.execute("SELECT Name FROM BeerCat WHERE BeerCat.Id=1") # query database for beer with ID 1
		name = cursor.fetchone()[0] # get name associated with beer ID 1
		self.assertEqual(name,"American Ale") # check to see if name is correct
		
		# same steps for checking name of beer ID 2
		cursor.execute("SELECT Name FROM BeerCat WHERE BeerCat.Id=2")
		name = cursor.fetchone()[0]
		self.assertEqual(name,"American Lager")
		
	## \brief    Confirms that beer color ID's are linked to the proper beer color in Color table. 
	#  \details    Test format: SELECT Name FROM Color Where Color.Id = <ID number>
	#  \functionality	Returns false if a self.assert fails
	#  @param self The object pointer.
	def test_getColorUsingColorID(self):
		
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=1") # query database for color with ID 1
		name = cursor.fetchone()[0] # get name associated with color ID 1
		self.assertEqual(name,"Dark") # check to see if name is corrrect
		
		# repeat steps for color with ID 2, 3, 4, etc
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
	## \brief    Confirms that food ID's are linked to proper food name in Food table. 
	#  \details    Test format: SELECT Name FROM Food Where Food.Id = <ID number>
	#  \functionality	Returns false if a self.assert fails
	#  @param self The object pointer.
	def test_getFoodUsingFoodID(self):

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=1")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Spicy")

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=2")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Red Meat")

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=3")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Pasta")

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=4")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Sea Food")

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=5")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Salad")

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=6")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Chocolate")

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=7")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Baked Good")

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=8")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Poultry")

		cursor.execute("SELECT Name FROM Food WHERE Food.Id=9")
                name = cursor.fetchone()[0]
                self.assertEqual(name,"Weiners")
                
	## \brief    Confirms that food ID's are linked to proper beer matches in the FoodPairing table. 
	#  \details    Test format: SELECT Name FROM FoodPairing WHERE FoodPairing.FoodId = <ID number>
	#  \functionality	Returns false if a self.assert fails
	#  @param self The object pointer.
	def test_getBeerNameUsingFoodId(self):

		cursor.execute("SELECT Name FROM FoodPairing WHERE FoodPairing.FoodId=2")
                names = cursor.fetchall()
                self.assertEqual(names[0][0],"Sierra Nevada")
		self.assertEqual(names[1][0],"Upslope")

		cursor.execute("SELECT Name FROM FoodPairing WHERE FoodPairing.FoodId=5")
                names = cursor.fetchall()
                self.assertEqual(names[0][0],"Victory")


		cursor.execute("SELECT Name FROM FoodPairing WHERE FoodPairing.FoodId=3")
                names = cursor.fetchall()
                self.assertEqual(names[0][0],"Coors Light")

	def test_getReviewUsingFoodIdAndBeer(self):
		
		cursor.execute("SELECT Review FROM FoodPairing WHERE FoodId=2 AND Name='Sierra Nevada'")
                review = cursor.fetchone()[0]
                self.assertEqual(review,"A very crisp and refreshing beer, this easy-to-drink pale ale is an excellent compliment to a delicious burger.  The heavier, meaty flavor of the burger pairs extraordinarily well with light, fresh taste of the beer.  You'll have a hard time finding a better brew than this to wash down your bites of")

if __name__ == '__main__':
	unittest.main()
