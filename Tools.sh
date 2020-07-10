clear
figlet "Tools"
echo "--------------------------------"
echo " Author : ĐɆĐ𝓲"
echo " Youtube: Seven Gaming"
echo " Github : Tai"
echo "--------------------------------"
echo
echo "Pilih Menu Tools Nya"
echo "[1] Dark Fb Premium"
echo "[2] MBF"
echo "[3] Dark Fb New"
echo "[4] Hack CCTV"
echo "[5] Spam Sms"
echo "[6] Panggilan Palsu"
echo "[7] Install Bahan Bahan"
read -p "[?] Pilih : " pil:

if [ $pil -1 ]
then
git clone https://github.com/TheMagizz/DarkPremium
cd DarkPremium
python2 DarkFB.py
fi

if [ $pil -2 ]
then
git clone https://github.com/pirmansx/mbf
cd mbf
python2 MBF.py
fi

if [ $pil -3 ]
then
git clone https://github.com/ARIYA-CYBER/NEW
cd NEW
python2 FbNew.py
fi

if [ $pil -4 ]
then
git clone https://github.com/AngelSecurityTeam/Cam-Hackers
cd Cam-Hackers
python2 cam-hackers.py
fi

if [ $pil -5 ]
then
git clone https://github.com/hekelpro/spammer
cd spammer
python2 spammer py
fi

if [ $pil -6 ]
then
git clone https://github.com/B4N954N2-ID/spam-call
cd spam-call
bash Call.sh
fi

if [ $pil -7 ]
then
apt update && apt upgrade
pkg install nano
pkg install python2
pkg install git
pip install requests mechanize
pip2 install requests mechanize
pkg install php
fi



