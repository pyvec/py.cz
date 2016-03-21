# -*- coding: utf-8 -*- 
# for python 2.x


u"""Na konci tohoto scriptu budete mít stažené jednotlivé archívy *.txt z mailmanovských
archívačních webů a jeden celkový souhrnný. Tyto pak již stačí nakopírovat do příslušné složky vašeho 
emailového klienta, a budete tak moci offline, se všemi funkcemi pro vyhledávání, 
které váš emailový klient podporuje, prohledávat kompletní archívy poštovních konferencí. 
Funguje pro stahování všude, kde používají program Mailman na správu 
poštovních konferencí včetně archivace.

Zpracovává txt i gzip archivy.
"""

import urllib, os, gzip, StringIO, re

def rozbal(obsah):
    handle=StringIO.StringIO(obsah)
    handleGzip=gzip.GzipFile("", "r" ,9 , handle) 
    return handleGzip.read()

def nactiOdkazy(www, reHledat):
    fp = urllib.urlopen(www)
    data = fp.read()
    fp.close()
    
    # vytvorime seznam jmen *.gz a *.txt na webu
    odkazy=re.findall(reHledat, data)      
    #odkazy.reverse()
   
    return odkazy

def stahniJedenArchiv(archiv):
    print "Stahuji", archiv, "  ",
    
    #stahneme po castech, abychom mohli vypisovat "."
    fp = urllib.urlopen(archiv)
        
    data=""
    dataNew=fp.read(dataFraction)
    while dataNew:
        data=data+dataNew
        dataNew=fp.read(dataFraction)
        print "\b.",
    if archiv[-3:]==".gz":
        data=rozbal(data)
        archiv=archiv[:-3]

    return data

def uloz(soubor, ulozitAll, data):
    #ulozime
    ulozit=file(os.path.join(cilovyAdresar, soubor), 'w')
    ulozit.write(data)
    ulozitAll.write(data)
    ulozitAll.flush()
    ulozit.close()
    
    velikost= "%.2f" % (len(data)/1024.0/1024.0)
    print u"\n     soubor", soubor, ", velikosti", velikost, u"MB, uložen do", cilovyAdresar
    

def stahniVse(odkazy):
    
    print u"\nZačínám stahovat", len(odkazy), u"poštovních archívů z konference", archivyNaWebu
    allInOne=file(os.path.join(cilovyAdresar, archivFull),"w")
    
    #stahovani a ukladani
    for soubor in odkazy:
        
        archiv=os.path.join(archivyNaWebu, soubor)
        data=stahniJedenArchiv(archiv)
        uloz(soubor, allInOne, data)        
        
    allInOne.close()
    print u"Soubor", archivFull , u"uložen do", cilovyAdresar

if __name__=="__main__":
    
    archivyNaWebu='http://www.py.cz/pipermail/python/'
    archivFull="MailArchive.txt"
    cilovyAdresar=os.getcwd()
    
    
    dataFraction=1024*10
    reHledat="(20\d.-.*(?:\.gz|\.txt))"   # vsechny 2000 a výše s příponou gz nebo txt

    print u"Zjišťuji odkazy na", archivyNaWebu
    odkazy=nactiOdkazy(archivyNaWebu, reHledat)
    print odkazy
    stahniVse(odkazy)

    print u"""\nVše staženo, stačí nakopírovat MailArchive.txt nebo jednotlivé txt
do příslušné složky emailového klienta, a máte k dispozici lokálně plně 
prohledávatelný archiv poštovní konference.
    
    Happy Pythoning!"""
