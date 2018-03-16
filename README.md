# webpage2kindle
Send Webpages to your Kindle directly by one command.
## 1 Step Setup
Dowload this repo. Go to the downloaded directory and run:

` sudo ./install.sh `

![Installation](working.png?raw=true "Installation Screenshot")

That's it. You are good to go. It will prompt you to give your Gmail and the Kindle email while Installation.

**Tip :** If, however, **any mistake occurs during the email configuration part**, run this command: ` ./config.sh ` and you will be prompted to configure the emails again.

**Do Your Homeowork :**
Though you still need to "allow less secure apps" in Gmail settings and add this Gmail to trusted email in Kindle settings.

## Usage
One command without thinking about the repository you currently are in:

` webpage2kindle http://www.link.xyz filename.pdf `

![Command](sample.png?raw=true "Working Screenshot")


#Technical details

## Installation Pre-requisites:
Pre-requisites are being handled by the installer script. User need not explicitly install it.
- python
- pdfkit
- requests
- wkhtmltopdf

## Configuration Pre-Requisites:
<ul>
<li>A gmail account through which document is added to kindle.</li>
<li>The kindle email address provided by Amazon.</li>
<li>Permission to send documents via the gmail account in the Amazon Kindle settings.</li>
<li> Access to "less secure apps" in your Gmail settings. </li>
</ul>

## Authors

* **Mradul Dubey** - *webpage2kindle* - [MradulDubey](https://github.com/mraduldubey)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the [LICENSE.md](LICENSE?raw=true "LICENSE") file for details.
