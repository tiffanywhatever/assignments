username = raw_input("Enter a username: ")
password = raw_input("Enter a password: ")
allowed_user = "dean"
allowed_password = "pass"
if username.lower() == allowed_user and password == allowed_password:
	print ("Welcome %s" % (username.lower()))
else:
	print ("Access denied.")