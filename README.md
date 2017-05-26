# webpage2kindle
Send Webpages to your Kindle directly by one command. Currently working on the browser-extention for the same on a seperate branch.

## Installation Pre-requisites:
<ul>
<li>Python2.7</li>
<li>Following Python modules: 
  <b>1.requests</b> 
  <b>2.pdfkit</b>
</li>
</ul>

## Settings Pre-Requisites:
<ul>
<li>A gmail account through which document is added to kindle.</li>
<li>The kindle email address provided by Amazon.</li>
<li>Permission to send documents via the gmail account in the Amazon Kindle settings.</li>
<li> Access to "less secure apps" in your Gmail settings. </li>
</ul>

## Make following changes to the script [webpage2kindle.py](webpage2kindle.py?raw=true "webpage2kindle.py")
<ul>
<li> Line 96: from_address = "YOUR GMAIL ADDRESS." Change "YOUR GMAIL ADDRESS." to your gmail address (Don't Remove Quotes).</li>
<li> Line 99: to_address = "YOUR KINDLE EMAIL ADDRESS." to your Kindle email (Do Not Remove Quotes). </li>
</ul>

<b> Example: </b>
```
from_address = "mraduldubeymd19@gmail.com"
```
```
to_address = "mradul@kindle.com"
```

## Usage:
<ul>
<li>Download the script and change to that directory Or Copy it to home directory for easy use</li>
<li><b>./webpage2kindle 'The_URL_Goes_Here' 'Filename_With_which_You_Want_to_save_webpage_in_kindle'</b></li>
<b>OR</b>
<li> <b>python webpage2kindle 'The_URL_Goes_Here' 'Filename_With_which_You_Want_to_save_webpage_in_kindle'</b></li>
<li> You will be prompted to enter your gmail password. The script has been updated to avoid 'over the shoulder' attack. Don't worry it will not be saved on the disk.</li>
</ul>

<b>Example:</b>
```
chmod +x wepage2kindle.py #Need to run only once.

./webpage2kindle.py https://indiegroundfilms.files.wordpress.com/2014/01/before-sunrise-numbered.pdf Before Sunrise
```
<b>OR</b>

```
python webpage2kindle.py https://indiegroundfilms.files.wordpress.com/2014/01/before-sunrise-numbered.pdf Before Sunrise
```

## Screenshot
![Screenshot](sample.png?raw=true "Working Screenshot")


## Authors

* **Mradul Dubey** - *webpage2kindle* - [MradulDubey](https://github.com/mraduldubey)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the [LICENSE.md](LICENSE?raw=true "LICENSE") file for details.

