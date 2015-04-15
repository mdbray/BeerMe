#!/usr/bin/python

import urllib2


homePage = '''


<!DOCTYPE html>
<html lang = "en">
<head>
	<link rel="stylesheet" type="text/css" href="/styles.css">
	<meta charset = "UTF-8">
	<title>BeerMe</title>
	
</head>
<body>


	<table align ="center" width="800" cellspacing="0" cellpadding ="0" style="background-color: rgb(230,168,0); border-spacing: 0px">
		<tr>
			<td height="200" align="center"><a href="index.py"><img src="../images/graphics-beer-249813.gif" alt="banner" width="780" height="200" border="0" /></td>
		</tr>
	</table>
	<table align ="center" border="0" width="800" cellspacing="0" cellpadding="0">
		<tr valign="center" style="border-spacing: 0px;">
			<td width="188" align="center"><div class ="nav" ><a href="index.py">Home</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="login.py">Login</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="beerinfo.py">Beer Info</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="resources.py">Other Resources</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="about.py">About Us</a></div></td>
		</tr>
	</table>
        

		<table align="center" border="0" width="800" cellpadding="5">
		<tr>
		<td align="center">

        <h1>Welcome to <strong style="font-size: 30px; letter-spacing: -2px">BeerMe</strong></h1>

		<h2>Here are some other beer resources you might find useful:</h2>
			
			<table align="center" border="0" width="750" cellpadding="5">
			<td style="width: 800px; padding: 25px; background-color: rgb(225,225,225); border: 2px solid black; text-align: left; vertical-align: top;">
			<a href="http://www.beeradvocate.com/" style="font-size: 22px; color: rgb(230,168,0); text-decoration: underline">beeradvocate.com</a>
			<br>
			<br>- Information on various beer
			<br>
			<br>- Ratings of every beer ever
			<br>
			<br>- Lists of highest rated beer
			<br>
			<br>- Forums
			
			<br>
			<br>
			<br>
			<a href="https://www.beermenus.com/" style="font-size: 22px; color: rgb(230,168,0); text-decoration: underline">beermenus.com</a>
			<br>
			<br>- Search for a specific beer
			<br>
			<br>- See the lists of various local establishments
			<br>
			<br>- In some cities like New York and San Francisco many establishments keep their beer menu's up-to-date here
			<br>
			<br>
			<a href="http://www.ratebeer.com/" style="font-size: 22px; color: rgb(230,168,0); text-decoration: underline">ratebeer.com</a>
			<br>
			<br>- Similar to beeradvocate

			<br>
			<br>
			<br>
			<a href="https://untappd.com/" style="font-size: 22px; color: rgb(230,168,0); text-decoration: underline">untappd.com</a>
			<br>
			<br>- Mobile app
			<br>
			<br>- Rate and comment on the beer you drink, brag to friends

			<br>
			<br>
			<br>
			<a href="http://nextglass.co/" style="font-size: 22px; color: rgb(230,168,0); text-decoration: underline">nextglass.com</a>
			<br>
			<br>- Mobile/Chrome app
			<br>
			<br>- Has review and scan feature

		</td>
		</tr>
		</table>
		
		</td>
		</tr>
		</table>
	
</body>
</html>
'''
print homePage
