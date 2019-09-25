def Error_email(scriptname,timestamp,errorMsg):
	
	import linecache
	import sys

	
	exc_type, exc_obj, tb = sys.exc_info()
	f = tb.tb_frame
	lineno = tb.tb_lineno
	filename = f.f_code.co_filename
	linecache.checkcache(filename)
	line = linecache.getline(filename, lineno, f.f_globals)
	messageTwo = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
	
	import smtplib

	import Email_creds


	username = Email_creds.login['email_username']
	password = Email_creds.login['email_secret']
	delivery = Email_creds.login['to_email']

	subject = 'There was an error on script ' + str(scriptname)
	msg = 'There was an error on script ' + str(scriptname) + ' at ' + str(timestamp) + ' on with the error message ' + str(errorMsg) + '\n' + messageTwo
	content = 'Subject:{}\n\n{}'.format(subject, msg)

	mail = smtplib.SMTP('smtp.gmail.com',587)

	mail.ehlo()

	mail.starttls()



	mail.login(username,password)

	mail.sendmail(username,delivery,content)

	mail.close()

