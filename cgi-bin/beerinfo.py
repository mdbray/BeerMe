#!/usr/bin/python

import urllib2


homePage = '''


<!DOCTYPE html>
<head>
        <link rel="stylesheet" type="text/css" href="/styles.css">
        <meta charset = "UTF-8">
        <title>BeerMe</title>

</head>
<body>

    <table align ="center" width="800" cellspacing="0" cellpadding ="0" style="background-color: rgb(230,168,0); border-spacing: 0px">
		<tr>
			<td height="200" align="center"><a href="index.py"><img src="../images/foam.jpg" alt="banner" width="800" height="200" border="0" /></td>
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
        <table align="center" border="0" width="800" cellpadding="5"
		<tr valign ="top">
		<td>
        
        <h1>Welcome to <strong style="font-size: 30px; letter-spacing: -2px">BeerMe</strong></h1>

		<table>
		<td style="width: 750px; padding: 25px; background-color: rgb(225,225,225); border: 2px solid black; text-align: left; vertical-align: top;">
		<h2>QUICK!! Go Back!</h2>
		</td>
		</table>
		
		</td>
		</tr>
		</table>
		
</body>

'''
print homePage
