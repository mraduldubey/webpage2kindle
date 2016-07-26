# webpage2kindle
Send Webpages to your Kindle directly by one command.

#Pre-requisites:
<ul>
<li>Python2.7 installed on the system</li>
<li>Following Python modules installed (using pip): 
  <b>1.requests</b> 
  <b>2.pdfkit</b>
</li>
<li>A gmail account through which document is added it kindle</li>
<li>The kindle email address</li>
<li>Permission to send documents via the gmail account in the Amazon Kindle settings</li>
</ul>

<h1>To USE the script make following <b>THREE</b> changes to the script:</h1>
<ul>
<li>Line 26: fromaddr = "YOUR_GMAIL_ADDRESS" => Change "YOUR_GMAIL_ADDRESS" to your gmail address (DO NOT REMOVE THE QUOTES)</li>

<li>Line 27: toaddr = "YOUR_KINDLE_EMAIL_ADDRESS" => Change "YOUR_KINDLE_EMAIL_ADDRESS" to your kindle email (DON'T REMOVE QUOTES)</li>

<li>Line 53: server.login(fromaddr, "YOUR_GMAIL_PASSWORD") => "YOUR_GMAIL_PASSWORD" to your gmail password</li>
</ul>

# Usage :
<ul>
<li>Download the script and change to that directory Or Copy it to home dirextory for easy use</li>
<li>./webpage2kindle 'The_URL_Goes_Here' 'Filename_With_which_You_Want_to_save_webpage_in_kindle'</li>
<b>OR</b>
<li> python webpage2kindle 'The_URL_Goes_Here' 'Filename_With_which_You_Want_to_save_webpage_in_kindle'</li>
</ul>
