#!/bin/bash

echo "===========Adding Dependecies============="
#seperate temp dependency script
touch dpndt.sh
cat <<EOF > dpndt.sh
apt install wkhtmltopdf python
pip install pdfkit requests
EOF

bash dpndt.sh 
rm dpndt.sh	
echo "Success"

echo "===========Configuration============="
#configuration
echo "Tip: Tweak configuration later by executing ./config.sh"
bash config.sh

echo "======Adding command to system======="
#adding command to system
dir=$(pwd)
cd /usr/bin
sudo rm webpage2kindle
ln -s $dir/webpage2kindle.py webpage2kindle
chmod +x webpage2kindle
cd $dir
echo "Done."

echo "command format: webpage2kindle http://link.xyz filename"
#Push successful notification
notify-send "webpage2kindle Installed!" \
            "$ webpage2kindle  http://  filename" \
            -i $dir/kindle.png


