from colorama import Fore
import argparse
import sys
from datetime import datetime
ctime=datetime.now().strftime("%H-%M-%S")
from argparse import RawTextHelpFormatter
print(Fore.RED+"""
      ,__                . .      __
     ------     _*=_      : .   __==__
      (``)     ,( ")>      .:.__ (~~)
____ /~::~\ ____'|~)__________`\\/;~\____________
    `|_::_|'    (` |             (~`\\._
      _||_      /__|_           _.||[___]

------------------------------------
    """)
helpc=Fore.GREEN+'You can use your gathered information to create target specific password lists.\n'
parser = argparse.ArgumentParser(description=Fore.GREEN+'Kracker is a tool developed and used by Kaleem ibn anwar to break the modern strong/week password encryption.'+helpc, formatter_class=RawTextHelpFormatter)
args = parser.parse_args()

cpasswds=open('common_passwords.txt','r')

try:
    fname=input("\033[0;32;10mFirstname: \033[0;33;10m")
    attempts=0
    while fname=='':
        attempts=1+attempts
        print("\033[0;31;10m Firstname is required.")
        if attempts==3:
            print("\033[0;31;10m Start it again.")
            exit()
        fname=input("\033[0;32;10mFirstname: \033[0;33;10m")    
    file=open(f"{fname}.txt",'w+')
    lname=input("\033[0;32;10mLastname: \033[0;33;10m")
    pname=input("\033[0;32;10mPartner's name: \033[0;33;10m")
    dob=input("\033[0;32;10mDate of birth dd/mm/yyyy: \033[0;33;10m")
    familyname=input('\033[0;32;10mFamily name or cast: \033[0;33;10m')
    extrawords=input('\033[0;32;10mAny Extra words: \033[0;33;10m')
    relgiouswords=input("\033[0;32;10mReligious words used on his profiles: \033[0;33;10m")
    trans=input("\033[0;32;10mDo you want to add character to digit translation like Aoi=401\n\t Enter 's' for short translation and 'l' for long tanslation: \033[0;33;10m")
    commonlist=input("\033[0;32;10mDo you want to include common word list(yes/no): \033[0;33;10m")

    cfname=fname.capitalize()
    ufname=fname.upper()
    sfname=fname.lower()
    clname=lname.capitalize()
    ulname=lname.upper()
    slname=lname.lower()
    passwords=[]
    transpass=[]
    sympass=[]
    symbs=['','!','@','$','#','&','*','-','+','.']
    symbsshort=['','!','@','#','&','+','.']
    day=dob[0:2]
    month=dob[3:5]
    year=dob[6:10]


    endnumric=[12,123,4321,1234,321,00,12345,2244,123,1122,'007',day+month,day,year,month]
    p=[pname.capitalize(),pname.upper(),pname.lower(),'']
    familynames=[familyname.capitalize(),familyname.upper(),familyname.lower(),'']

    a=['',sfname,ufname,cfname,'']
    b=['',slname,ulname,clname]

    passpattern=[]


    def wordls(extrawords):
        words=extrawords.split(',')
        return words

    def liner(file):
        lines=file.split('\n')
        return lines

    def shorttrans(passpattern):
        engc='eioa'
        numc='3104'
        for pattern in passpattern:
            tranc = pattern.maketrans(engc, numc)
            transpass.append(pattern.translate(tranc))

    def longtrans(passpattern):
        engc='EeiIoOaAs'
        numc='331100445'
        for pattern in passpattern:
            tranc = pattern.maketrans(engc, numc)
            transpass.append(pattern.translate(tranc))

    def sympas():
        for password in passwords:
            for i in endnumric:
                for sym in symbs:
                    if password == '' or password== ' ':
                        pass
                    else:
                        password1=password+sym+str(i)
                        sympass.append(password1)



    for word in wordls(extrawords):
        if word != "":
            passpattern.append(word)

    for firstname in a:
        for lastname in familynames:
            for sym in symbs:
                c=firstname+sym+lastname
                if firstname =="":
                    c=lastname
                    passpattern.append(str(c))
                    break
                if lastname =="":
                    c=firstname
                    passpattern.append(str(c))
                    break
                if c != '':
                    passpattern.append(str(c))

    for firstname in a:
        for lastname in b:
            for sym in symbs:
                c=firstname+sym+lastname
                if firstname =="":
                    c=lastname
                    passpattern.append(str(c))
                    break
                if lastname =="":
                    c=firstname
                    passpattern.append(str(c))
                    break
                if c != '':
                    passpattern.append(str(c))

    for pname in p:
        for firstname in a:
            for sym in symbs:
                c=pname+sym+firstname
                if pname == '':
                    break
                if firstname =="":
                    c=pname
                    passpattern.append(str(c))
                    break
                if c != '':
                    passpattern.append(str(c))



    if trans=='s':
        shorttrans(passpattern)
    elif trans=='l':
        longtrans(passpattern)
    else:
        pass

    for pattern in passpattern:
        passwords.append(pattern)
    for password in transpass:
        passwords.append(password)

    for word in wordls(relgiouswords):
        if word != "":
            passwords.append(word.capitalize())
            passwords.append(word.upper())
            passwords.append(word.lower())
    sympas()

    if commonlist.lower=='yes' or commonlist=='y':
        for line in cpasswds.readlines():
            line=line.replace('\n','')
            print('addd')

            if line != "" and line not in passwords:
                print('addddd')
                passwords.append(line)

    for password in sympass:
        if password=='':
            pass
        else:
            passwords.append(password)

    def writer():
        for line in passwords:
            line=line.replace('\n','')
            if line != '':
                file.write(line+'\n')
        file.close()

    writer()
    print(f"\033[0;33;10m \nA wordlist file ",end='')
    print(f"\033[0;35;10m{fname}-{ctime}.txt ",end='')
    print("\033[0;33;10mis successfully created.")
except KeyboardInterrupt:
    print(Fore.RED+'\nExiting')
    sys.exit()