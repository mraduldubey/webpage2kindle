#!/usr/bin/python
import os,sys,pdfkit,requests,re
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


#IMPORTANT--Make sure your gmail settings' access to 'less-secure apps' is allowed.
#IMPORTANT--Make sure that the email you use here is added as trusted address in amazon kindle settings

def URL_to_PDF( URL, filename, pdfobj ):
	'''Convert to pdf if URL given is not the direct link to pdf. Save on disk.'''

	res = requests.get(URL)

	#Validating URL
	res.raise_for_status()        

	#If URL is a direct Link to a pdf file, then save directly on DISK.
	if pdfobj.search(URL):

		with open(filename,'wb') as f:
			f.write(res.content)
		
		f.close()

	#Convert to pdf and save on DISK using pdfkit.
	else:

		pdfkit.from_url( URL, filename ) 



def email_to_kindle( URL, filename, from_address, to_address ):
	'''Sending the saved PDF on disk, to the configured kindle email address.'''

	#Do not want to configure password in a unencrypted file.
	print "Enter your password for account:", from_address, " (Will not be saved)"
	password = raw_input()

	print 'Adding webpage to kindle...'

	msg = MIMEMultipart()
	 
	msg['From'] = from_address
	msg['To'] = to_address
	msg['Subject'] = "Kindle Document by Webpage2Kindle."
	 
	body = "The document named" + filename + "from" + URL + "has been added to this Kindle account:" + to_address + "."
	
	#Text added to email body. 
	msg.attach(MIMEText(body, 'plain'))

	#PDF Object. 
	attachment = open(filename, "rb")
	 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)

	#Add PDF to email header.
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	
	#Attach the header to email.
	msg.attach(part)

	#Starting Gmail server.
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()

	#LogIn Attempt to the from_address email.
	server.login(from_address, password)

	text = msg.as_string()
	
	#Push the email.
	server.sendmail(from_address, to_address, text)
	
	#Quit the server after sending email.
	server.quit()

	#Deleting the saved PDF file from DISK.
	os.remove(filename)

	return True


if __name__ == '__main__':

	filename = sys.argv[2]
	URL = sys.argv[1]

	#The email added to trusted email in Kindle settings.
	from_address = "YOUR GMAIL ADDRESS."

	#The Kindle email.
	to_address = "YOUR KINDLE EMAIL ADDRESS."

	pdfobj = re.compile('.pdf$')

	httpobj = re.compile('^http//:')

	#Add '.pdf' to file at the end, if not supplied as cmd line arguments e.g. 'thefirstbook' to 'thefirstbook.pdf'
	if not pdfobj.search(filename):

		filename += '.pdf'

	#Add connection adapter to the URL if not present in cmd line argument e.g. 'www.google.com' to 'http://www.google.com'.
	if not httpobj.search( URL ):

		URL = 'http://' + URL

	URL_to_PDF( URL, filename, pdfobj )

	if email_to_kindle( URL, filename, from_address, to_address ):

		os.system( "notify-send 'Webpage added to Kindle Documents.' ")
