# webpage2kindle
Send Webpages to your Kindle directly by one command.

#Pre-requisites:
<ul>
<li>Python2.7 installed on the system</li>
<li>Following Python modules installed (using pip): 
  <b>1.requests</b> 
  <b>2.pdfkit</b>
</li>
<li>A gmail account through which document is added to kindle</li>
<li>The kindle email address provided by Amazon</li>
<li>Permission to send documents via the gmail account in the Amazon Kindle settings</li>
</ul>

<h1>To USE the script make following <b>THREE</b> changes to the script:</h1>
<ul>
<li>Line 26: fromaddr = "YOUR_GMAIL_ADDRESS" => Change "YOUR_GMAIL_ADDRESS" to your gmail address (DO NOT REMOVE THE QUOTES)</li>

<li>Line 27: toaddr = "YOUR_KINDLE_EMAIL_ADDRESS" => Change "YOUR_KINDLE_EMAIL_ADDRESS" to your kindle email (DON'T REMOVE QUOTES)</li>

</ul>

# Usage :
<ul>
<li>Download the script and change to that directory Or Copy it to home directory for easy use</li>
<li><b>./webpage2kindle 'The_URL_Goes_Here' 'Filename_With_which_You_Want_to_save_webpage_in_kindle'</b></li>
<b>OR</b>
<li> <b>python webpage2kindle 'The_URL_Goes_Here' 'Filename_With_which_You_Want_to_save_webpage_in_kindle'</b></li>
<li> You will be prompted to enter your gmail password. Don't worry it will not be saved on the disk.</li>
</ul>

<b>Eg:</b>
./webpage2kindle 'https://indiegroundfilms.files.wordpress.com/2014/01/before-sunrise-numbered.pdf' 'Before Sunrise'
