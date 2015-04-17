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
	
	<h1 align="center">Join our beer community today!</h1>
	<h2 align="center">Sign in or create an account for personalized beer recommendations. </h2>

	<table style="border-spacing: 100px 5px;">
	<td style="width: 500px; padding: 25px; background-color: rgb(225,225,225); border: 2px solid black; text-align: left; vertical-align: top;">
	<section id="loginBox">
	<h3 style="text-align:center; font-size: 25px; letter-spacing: -2px">Login:</h3>
	<form method="post" class="minimal">
		<label for="username">
			Username:
			<input type="text" name="username" id="username" placeholder="Username" pattern="^[a-zA-Z][a-zA-Z0-9-_\.]{8,20}$" required="required" />
		<p style="font-size: 10px;">Username must be between 8 and 20 characters</p>
		</label>
		
		<br>
		<label for="password">
			Password:
			<input type="password" name="password" id="password" placeholder="Password" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required" />
		<p style="font-size: 10px;">Password must contain 1 uppercase, lowercase and a number</p>
		</label>
		
		<br><br>
		<button type="submit" class="btn-minimal">Sign in</button>
	</form>
	</section>
	</td>
	
	<td style=" width: 500px; padding: 25px; background-color: rgb(225,225,225); border: 2px solid black; text-align: left; vertical-align: top;">
        <section id="signupBox">
        <h3 style="text-align:center; font-size: 25px; letter-spacing: -2px">Sign up:</h3>
        <form method="post" class="minimal">
                <label for="email">
                        E-mail:
                        <br>
                        <input type="text" name="email" id="email" placeholder="youremail@xyz.com" pattern="[a-zA-Z0-9_-.]+@[a-zA-Z0-9_-.]+\." required="required" />
                </label>
		
		<br><br>
		<label for="username">
                        Username:
                        <input type="text" name="username" id="username" placeholder="Username" pattern="^[a-zA-Z][a-zA-Z0-9-_\.]{8,20}$" required="required" />
                <p style="font-size: 10px;">Username must be between 8 and 20 characters</p>
                </label>
                
		<br>
		<label for="password">
                        Password:
                        <input type="password" name="password" id="password" placeholder="Password" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required" />
                <p style="font-size: 10px;">Password must contain 1 uppercase, lowercase and a number</p>
                </label>

		<br>
                <label for="password">
                        Confirm Password:
                        <input type="password" name="password" id="password" placeholder="Confirm password" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required" />
                <p style="font-size: 10px;">Passwords must match</p>
                </label>

		<br>
                <button type="submit" class="btn-primary">Create Account!</button>
        </form>
	</section>
	</td>
	</table>

	</td>
	</tr>
	</table>

</body>
</html>
'''
print homePage
