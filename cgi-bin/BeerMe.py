#!/usr/bin/python

import urllib2


homePage = '''



<!DOCTYPE html>
<html>
	<head>
	<link rel="stylesheet" href="styles.css">
	<meta charset = "UTF-8">
	<title>BeerMe</title>

</head>
<body>
	<table align ="center" width="800" cellspacing="0" cellpadding ="0" style="background-color: rgb(230,168,0); border-spacing: 0px">
		<tr>
			<td height="200" align="center"><a href="index.html"><img src="images/foam.jpg" alt="banner" width="800" height="200" border="0" /></td>
		</tr>
	</table>
	<table align ="center" border="0" width="800" cellspacing="0" cellpadding="0">
		<tr valign="center" style="border-spacing: 0px;">
			<td width="188" align="center"><div class ="nav" ><a href="index.html">Home</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="login.html">Login</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="beerinfo.html">Beer Info</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="resources.html">Other Resources</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="about.html">About Us</a></div></td>
		</tr>
	</table>
	
	<table align="center" border="0" width="800" cellpadding="5">
	<td>
	<br>
	<h1>Welcome to <strong style="font-size: 30px; letter-spacing: -2px">BeerMe</strong></h1>

	<table align="center">
		<td>

		<table align="center">
						
						<td style="width: 400px; padding: 25px; background-color: rgb(225,225,225); border: 2px solid black; text-align: center; vertical-align: center;">
						<strong style="font-size: 25px; color: rgb(230,168,0)">Search by Food:</strong>
						<br>
						<p style="font-size: 22px; color: rgb(50,50,50)">
						<br>
						Red Meat
						<br>
						<br>
						Poultry
						<br>
						<br>
						Pasta
						<br>
						<br>
						Dessert
						<br>
						<br>
						Sausage
						<br>
						<br>
						Spicy
						<br>
						<br>
						</td>
		</table>
		<br>
		<table align="center">
						<td style="width: 400px; padding: 25px; background-color: rgb(225,225,225); border: 2px solid black; text-align: center; vertical-align: center;">
						<strong style="font-size: 25px; color: rgb(230,168,0)">Search by Color:</strong>
						<br>
						<p style="font-size: 22px">
						<br>
						Dark
						<br>
						<br>
						Brown
						<br>
						<br>
						Amber
						<br>
						<br>
						Pale
						<br>
						<br>
						Light
						<br>
						<br>
						</p>
		</table>
	
	</td>
	</table>
	
</body>
</html>
'''
print homePage
