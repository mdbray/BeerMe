## @package DBAutoTester
#  This document is designed to use automated testing to confirm that our database preforms
#  as expected.

import unittest;
import MySQLdb;

## A global variable
database = MySQLdb.connect("localhost","user","","BeerMeDB" );

## A global variable
cursor = database.cursor();

## Document class.
#  @param unittest.TestCase The Test Case pointer.
class Test_SQL_DB(unittest.TestCase):

	## A method
	#  @param self The object pointer
	def TestTetNameUsingBeerID(self): 
	
		## A method variable
		nameBeer1 = 0;
		
		## A method variable
		nameBeer2 = 0;
		
		cursor.execute("SELECT Name FROM BeerCat WHERE BeerCat.Id=1");
		nameBeer1 = cursor.fetchone()[0];
		self.assertEqual(nameBeer1,"American Ale");
		cursor.execute("SELECT Name FROM BeerCat WHERE BeerCat.Id=2");
		nameBeer2 = cursor.fetchone()[0];
		self.assertEqual(nameBeer2,"American Lager");

	## A method
	#  @param self The object pointer.
	def TestGetColorUsingColorID(self):
		
		## A method variable
		nameColor1 = 0;
		
		## A method variable
		nameColor2 = 0;
		
		## A method variable
		nameColor3 = 0;
		
		## A method variable
		nameColor4 = 0;
		
		## A method variable
		nameColor5 = 0;
		
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=1");
		nameColor1 = cursor.fetchone()[0];
		self.assertEqual(nameColor1,"Dark");
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=2");		
        nameColor2 = cursor.fetchone()[0];
        self.assertEqual(nameColor2,"Brown");
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=3");		
        nameColor3 = cursor.fetchone()[0];
        self.assertEqual(nameColor3,"Amber");     
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=4");		
        nameColor4 = cursor.fetchone()[0];
        self.assertEqual(nameColor4,"Pale");
		cursor.execute("SELECT Name FROM Color WHERE Color.Id=5");		
        nameColor5 = cursor.fetchone()[0];
        self.assertEqual(nameColor5,"Light");

	## A method
	#  @param self The object pointer.
	def TestGetFoodUsingFoodID(self):

		## A method variable
		nameFood1 = 0;
		
		## A method variable
		nameFood2 = 0;
		
		## A method variable
		nameFood3 = 0;
		
		## A method variable
		nameFood4 = 0;
		
		## A method variable
		nameFood5 = 0;
		
		## A method variable
		nameFood6 = 0;
		
		## A method variable
		nameFood7 = 0;
		
		## A method variable
		nameFood8 = 0;
		
		## A method variable
		nameFood9 = 0;
		
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=1");		
        nameFood1 = cursor.fetchone()[0];
        self.assertEqual(nameFood1,"Spicy");
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=2");
        nameFood2 = cursor.fetchone()[0];
        self.assertEqual(nameFood2,"Red Meat");
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=3");
        nameFood3 = cursor.fetchone()[0];
        self.assertEqual(nameFood3,"Pasta");
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=4");
        nameFood4 = cursor.fetchone()[0];
        self.assertEqual(nameFood4,"Sea Food");
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=5");
        nameFood5 = cursor.fetchone()[0];
        self.assertEqual(nameFood5,"Salad");
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=6");
        nameFood6 = cursor.fetchone()[0];
        self.assertEqual(nameFood6,"Chocolate");
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=7");
        nameFood7 = cursor.fetchone()[0];
        self.assertEqual(nameFood7,"Baked Good");
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=8");
        nameFood8 = cursor.fetchone()[0];
        self.assertEqual(nameFood8,"Poultry");
		cursor.execute("SELECT Name FROM Food WHERE Food.Id=9");
        nameFood9 = cursor.fetchone()[0];
        self.assertEqual(nameFood9,"Weiners");
        
	## A method
	#  @param self The object pointer.
	def TestGetBeerNameUsingFoodId(self):
	
	   ## A method variable
	   namesBeerBrandsByFood2 = 0;
	   
	   ## A method variable
	   namesBeerBrandsByFood5 = 0;
	   
	   ## A method variable
	   namesBeerBrandsByFood3 = 0;
	
		cursor.execute("SELECT Name FROM FoodPairing WHERE FoodPairing.FoodId=2");
        namesBeerBrandsByFood2 = cursor.fetchall();
        self.assertEqual(names[0][0],"Sierra Nevada");
		self.assertEqual(namesBeerBrandsByFood2[1][0],"Upslope");
		cursor.execute("SELECT Name FROM FoodPairing WHERE FoodPairing.FoodId=5");
        namesBeerBrandsByFoods5 = cursor.fetchall();
        self.assertEqual(namesBeerBrandsByFoods5[0][0],"Victory");
		cursor.execute("SELECT Name FROM FoodPairing WHERE FoodPairing.FoodId=3");
        namesBeerBrandsByFoods3 = cursor.fetchall();
        self.assertEqual(namesBeerBrandsByFoods3[0][0],"Coors Light");

	## Doc for method
	def TestGetReviewUsingFoodIdAndBeer(self):
	
	    ## A method variable
	    reviewOfFood2SierraNevadaPairing = 0; 
		
		cursor.execute("SELECT Review FROM FoodPairing WHERE FoodId=2 AND Name='Sierra Nevada'");
        reviewOfFood2SierraNevadaPairing = cursor.fetchone()[0];
        self.assertEqual(reviewOfFood2SierraNevadaPairing,"A very crisp and refreshing beer, this easy-to-drink pale ale is an excellent compliment to a delicious burger.  The heavier, meaty flavor of the burger pairs extraordinarily well with light, fresh taste of the beer.  You'll have a hard time finding a better brew than this to wash down your bites of");

if __name__ == '__main__':
	unittest.main();
