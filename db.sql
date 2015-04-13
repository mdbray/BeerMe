CREATE TABLE IF NOT EXISTS `BeerCat` (
`Id` int(1) NOT NULL auto_increment,
`Name` varchar(20) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;
INSERT INTO `BeerCat` (`Id`, `Name`) VALUES
	(1, 'American Ale'),
	(2, 'American Lager');
	
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
`abv` varchar(30) NOT NULL,
`description` varchar(600) NOT NULL,
PRIMARY KEY(`Id`)
) ENGINE = MyISAM DEFAULT CHARSET = utf8 auto_increment = 4;
INSERT INTO `Beers` (`Id`,`Name`,`BeerCatId`,`SourceId`,`abv`,`description`) VALUES
	(1,'American Pale Ale (APA)', 1,1, '4.0-7.0%', 'Of British origin, this style is now popular worldwide and the use of local ingredients, or imported, produces variances in character from region to region. Generally, expect a good balance of malt and hops. Fruity esters and diacetyl can vary from none to moderate, and bitterness can range from lightly floral to pungent. American versions tend to be cleaner and hoppier, while British tend to be more malty, buttery, aromatic and balanced.'),
	(2,'Imperial Pilsner',2,1,'6.5-9.0%','Similar to a Pilsner in appearance, but expect a more pronounced malty backbone and an intense bitterness. Malt flavors tend to be quite sweet in many examples. Alcohol can be quite aggressive and lend some spicy notes to the flavor.'),
	(3,'Light Lager',2,1,'2.5-5.0%','The Light Lager is generally a lighter version of a breweries premium lager, some are lower in alcohol but all are lower in calories and carbohydrates compared to other beers. Typically a high amount of cereal adjuncts like rice or corn are used to help lighten the beer as much as possible. Very low in malt flavor with a light and dry body. The hop character is low and should only balance with no signs of flavor or aroma. European versions are about half the alcohol (2.5-3.5% abv) as their regular beer yet show more flavor (some use 100% malt) then the American counterparts. For the most part this style has the least amount of flavor than any other style of beer.');

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
	(7,'Backed Good'),
	(8,'Poultry'),
	(9,'Weiners');

CREATE TABLE IF NOT EXISTS `FoodPairing`(
`Id` int(1) NOT NULL auto_increment,
`Name` varchar(20) NOT NULL,
`BeerId` int(1) NOT NULL,
`FoodId` int(1) NOT NULL,
`ColorId` int(1) NOT NULL,
`SourceId` int(1) NOT NULL,
`Review` varchar (400) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=5;
INSERT INTO `FoodPairing`(`Id`,`Name`,`BeerId`,`FoodId`,`ColorId`,`SourceId`,`Review`) VALUES
	(1,'Sierra Nevada',1,2,4,2,'A very crisp and refreshing beer, this easy-to-drink pale ale is an excellent compliment to a delicious burger.  The heavier, meaty flavor of the burger pairs extraordinarily well with light, fresh taste of the beer.  You will have a hard time finding a better brew than this to wash down your bites of juicy burger!'),
	(2,'Upslope',1,2,4,2,'This beer is full of flavor and matches up nicely with your favorite burger.  This pale ale has a hoppy bite to it which complements the rich, earthy taste of the burger quite well.  If you like pale ales, you’ll love this combination! '),
	(3,'Victory',2,5,4,2,'Slightly sweet and very refreshing beer that’s smooth and is perfect for a nice salad. The vegetables in the salad paired with this refreshing (yet tasteful) beer quenches any thirst. The flavors of the lettuce and other veggies meshes perfectly with the slightly sweet and fruity notes. '),
	(4,'Coors Light',3,3,5,2,'While I am not usually one to reach for a ‘light’ beer, it does a fantastic job washing down the greasy, doughy pizza. Very light hop profile and slight maltiness makes this beer seem like (and go down like) water.');

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
