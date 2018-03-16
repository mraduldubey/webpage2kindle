#!/bin/bash

#configuration
echo "Enter your trusted Gmail adress and press [ENTER]"
read gmail
echo "Enter your Kindle email address and press [ENTER]"
read kindle

sed -i "s/YOUR_TRUSTED_GMAIL/$gmail/" webpage2kindle.py
sed -i "s/YOUR_KINDLE_EMAIL/$kindle/" webpage2kindle.py

echo "Remember to add this Gmail address to trusted emails in Kindle settings."
