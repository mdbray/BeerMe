CREATE TABLE IF NOT EXISTS `BeerCat` (
`Id` int(1) NOT NULL auto_increment,
`Name` varchar(20) NOT NULL,
PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=3;
INSERT INTO `BeerCat` (`Id`, `Name`) VALUES
	(1, 'American Ale'),
	(2, 'American Lager');

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
