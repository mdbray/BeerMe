CREATE TABLE IF NOT EXISTS `BeerCat` (
`Id` int(1) NOT NULL auto_increment,
`Name` varchar(20) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;
INSERT INTO `BeerCat` (`Id`, `Name`) VALUES
	(1, 'American Ale'),
	(2, 'American Lager'),
	(3, 'Amber Ale'),
	(4, 'American Stout');
	
CREATE TABLE IF NOT EXISTS `Source`(
`Id` int(1) NOT NULL auto_increment,
`Name` varchar(40) NOT NULL,
`SourceType` varchar (20) NOT NULL,
`Reference` varchar(50) NOT NULL,
PRIMARY KEY(`Id`)
) ENGINE = MyISAM DEFAULT CHARSET = utf8 auto_increment=3;
INSERT INTO `Source`(`Id`,`Name`,`SourceType`, `Reference`) VALUES
	(1, 'Beeradvocate', 'web', 'http://www.beeradvocate.com/beer/style/'),
	(2, 'BeerMe', 'primary source', 'from the people who brought you BeerMe');

CREATE TABLE IF NOT EXISTS `Beers` (
`Id` int(1) NOT NULL auto_increment,
`Name` varchar(30) NOT NULL,
`BeerCatId` int(1) NOT NULL,
`SourceId` int(1) NOT NULL,
`ABV` varchar(30) NOT NULL,
`Description` varchar(600) NOT NULL,
PRIMARY KEY(`Id`)
) ENGINE = MyISAM DEFAULT CHARSET = utf8 auto_increment = 4;
INSERT INTO `Beers` (`Id`,`Name`,`BeerCatId`,`SourceId`,`ABV`,`Description`) VALUES
	(1,'American Pale Ale (APA)', 1,1, '4.0-7.0%', 'Of British origin, this style is now popular worldwide and the use of local ingredients, or imported, produces variances in character from region to region. Generally, expect a good balance of malt and hops. Fruity esters and diacetyl can vary from none to moderate, and bitterness can range from lightly floral to pungent. American versions tend to be cleaner and hoppier, while British tend to be more malty, buttery, aromatic and balanced.'),
	(2,'Imperial Pilsner',2,1,'6.5-9.0%','Similar to a Pilsner in appearance, but expect a more pronounced malty backbone and an intense bitterness. Malt flavors tend to be quite sweet in many examples. Alcohol can be quite aggressive and lend some spicy notes to the flavor.'),
	(3,'Light Lager',2,1,'2.5-5.0%','The Light Lager is generally a lighter version of a breweries premium lager, some are lower in alcohol but all are lower in calories and carbohydrates compared to other beers. Typically a high amount of cereal adjuncts like rice or corn are used to help lighten the beer as much as possible. Very low in malt flavor with a light and dry body. The hop character is low and should only balance with no signs of flavor or aroma. European versions are about half the alcohol (2.5-3.5% abv) as their regular beer yet show more flavor (some use 100% malt) then the American counterparts. For the most part this style has the least amount of flavor than any other style of beer.'),
	(4,'Amber Ale',3,1,'4.0-7.0%','Primarily a catch all for any beer less than a Dark Ale in color, ranging from amber (duh) to deep red hues. This style of beer tends to focus on the malts, but hop character can range from low to high. Expect a balanced beer, with toasted malt characters and a light fruitiness in most examples. The range can run from a basic ale, to American brewers who brew faux-Oktoberfest style beers that are actually ales instead of lagers.'),
	(5,'American Stout',4,1,'4.0-7.0%','Inspired from English & Irish Stouts, the American Stout is the ingenuous creation from that. Thankfully with lots of innovation and originality American brewers have taken this style to a new level. Whether it is highly hopping the brew or adding coffee or chocolate to complement the roasted flavors associated with this style. Some are even barrel aged in Bourbon or whiskey barrels. The hop bitterness range is quite wide but most are balanced. Many are just easy drinking session stouts as well.');

CREATE TABLE IF NOT EXISTS `Color`(
`Id` int(1) NOT NULL auto_increment,
`Name` varchar(6) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET = utf8 AUTO_INCREMENT=6;
INSERT INTO `Color` (`Id`,`Name`) VALUES
	(1, 'Dark'),
	(2, 'Brown'),
	(3, 'Amber'),
	(4, 'Pale'),
	(5, 'Light');

CREATE TABLE IF NOT EXISTS `Food`(
`Id` int(1) NOT NULL auto_increment,
`Name`varchar(15) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET = utf8 AUTO_INCREMENT=10;
INSERT INTO `Food` (`Id`,`Name`) VALUES
	(1,'Spicy'),
	(2,'Red Meat'),
	(3,'Pasta'),
	(4,'Sea Food'),
	(5,'Salad'),
	(6,'Chocolate'),
	(7,'Baked Goods'),
	(8,'Poultry'),
	(9,'Weiners');

CREATE TABLE IF NOT EXISTS `FoodPairing`(
`Id` int(1) NOT NULL auto_increment,
`Name` varchar(20) NOT NULL,
`BeersId` int(1) NOT NULL,
`FoodId` int(1) NOT NULL,
`ColorId` int(1) NOT NULL,
`SourceId` int(1) NOT NULL,
`Review` varchar (400) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=11;
INSERT INTO `FoodPairing`(`Id`,`Name`,`BeersId`,`FoodId`,`ColorId`,`SourceId`,`Review`) VALUES
	(1,'Sierra Nevada',1,2,4,2,'A very crisp and refreshing beer, this easy-to-drink pale ale is an excellent compliment to a delicious burger.  The heavier, meaty flavor of the burger pairs extraordinarily well with light, fresh taste of the beer.  You will have a hard time finding a better brew than this to wash down your bites of juicy burger!'),
	(2,'Upslope',1,2,4,2,'This beer is full of flavor and matches up nicely with your favorite burger.  This pale ale has a hoppy bite to it which complements the rich, earthy taste of the burger quite well.  If you like pale ales, you’ll love this combination! '),
	(3,'Victory',2,5,4,2,'Slightly sweet and very refreshing beer that’s smooth and is perfect for a nice salad. The vegetables in the salad paired with this refreshing (yet tasteful) beer quenches any thirst. The flavors of the lettuce and other veggies meshes perfectly with the slightly sweet and fruity notes. '),
	(4,'Coors Light',3,3,5,2,'While I am not usually one to reach for a ‘light’ beer, it does a fantastic job washing down the greasy, doughy pizza. Very light hop profile and slight maltiness makes this beer seem like (and go down like) water.'),
	(5,'Censored',4,1,3,1,'Clear amber with a frothy light team head leaving a good lacing. Nice cereal grain aroma, hints of cinnamon and orange. Medium sweetness with lots of cereal grain flavor, transitions to a long herby hop linger. Medium-light body with a slick mouthfeel and average carbonation and some cloying sugars linger . Overall, nice for the style. Decent malt character and balance.'),
	(6,'Upslope',1,4,4,1,'Pours a clear, copper color with a tight, white that leaves chunks of lacing. Smells of earthy and floral hops with some pine on the backend with some toasted notes. Tastes of the floral and earthy hops with a fairly big malt backbone. Malts lead off with toasted notes leading to some caramel sweetness and syrupy notes. This leads into a bit of citrus and pine, but then bigger earthy and floral notes come in. Leans toward the sweet side and finishes that way. Mouthfeel is medium with a crisp amount of carbonation. Overall, this is a good IPA, however, it is malt heavy for the style.'),
	(7,'Rogue Chocolate Stout',5,6,1,1,'A great gift brought by guests to a dinner party. Ads stouts are her favorite beer style, my wife got to contribute to this review....a rarity. Pours a deep black licorice with a pretty coffee brown bubbly head that dissipates, but returns with a gentle swirl of the glass. The scent is of toasted malt and leaves a reminder of chocolate milk. The taste is of bitter dark chocolate, a hint of coffee, and a faint caramel aftertaste. Some creaminess, but also a nice carbonation. Slightly sweet, especially late. We have had chocolatier stouts, but this was nicely balanced and really quite well done. I hope to get this again, but I will likely have to share it.'),
	(8,'Rogue Chocolate Stout',5,7,1,1,'A great gift brought by guests to a dinner party. Ads stouts are her favorite beer style, my wife got to contribute to this review....a rarity. Pours a deep black licorice with a pretty coffee brown bubbly head that dissipates, but returns with a gentle swirl of the glass. The scent is of toasted malt and leaves a reminder of chocolate milk. The taste is of bitter dark chocolate, a hint of coffee, and a faint caramel aftertaste. Some creaminess, but also a nice carbonation. Slightly sweet, especially late. We have had chocolatier stouts, but this was nicely balanced and really quite well done. I hope to get this again, but I will likely have to share it.'),
	(9,'Upslope',1,8,4,1,'Pours a clear, copper color with a tight, white that leaves chunks of lacing. Smells of earthy and floral hops with some pine on the backend with some toasted notes. Tastes of the floral and earthy hops with a fairly big malt backbone. Malts lead off with toasted notes leading to some caramel sweetness and syrupy notes. This leads into a bit of citrus and pine, but then bigger earthy and floral notes come in. Leans toward the sweet side and finishes that way. Mouthfeel is medium with a crisp amount of carbonation. Overall, this is a good IPA, however, it is malt heavy for the style.'),
	(10,'Victory',2,9,4,1,'Slightly sweet and very refreshing beer that’s smooth and is perfect for a nice salad. The vegetables in the salad paired with this refreshing (yet tasteful) beer quenches any thirst. The flavors of the lettuce and other veggies meshes perfectly with the slightly sweet and fruity notes. Slightly sweet and very refreshing beer that’s smooth and is perfect for a nice salad. The vegetables in the salad paired with this refreshing (yet tasteful) beer quenches any thirst. The flavors of the lettuce and other veggies meshes perfectly with the slightly sweet and fruity notes.');
	(10,'Victory',2,9,4,1,'Pours a clear golden hue with a pure white head and lots of bubbles. The aroma is full of spicy and fruity hop scents with cracker and biscuit goodness backing it up. What a tasty pils. Follows the aroma with nice, spicy hops, sweet cracker, a little bit of citrus and a nice, slightly bitter finish. Mouthfeel is medium and well-carbonated. Overall, just a really tasty, crisp and refreshing beer.');

CREATE TABLE IF NOT EXISTS `Users`(
`Id` int(1) NOT NULL auto_increment,
`UsrName` varchar(20) NOT NULL,
`Pass` varchar(20) NOT NULL,
`Email` varchar(32) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `Likes`(
`Id` int(1) NOT NULL auto_increment,
`UsersId` varchar(20) NOT NULL,
`BeerId` varchar(20) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `Dislikes`(
`Id` int(1) NOT NULL auto_increment,
`UsersId` varchar(20) NOT NULL,
`BeerId` varchar(20) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
