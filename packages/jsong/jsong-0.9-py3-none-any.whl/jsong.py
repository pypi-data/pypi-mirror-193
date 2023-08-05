#!/usr/bin/env python
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
import xlsxwriter
from colorama import Fore, Back, Style

artist = "artist0"

def newCollection():
    if not os.path.exists('collection'):
        print("\n\nCreated new Collection File\n\t* Excel files will be labeled 'artist#' according to how many albums you retrieve\n\t* JSON files will be simply labeled 'artist', and will contain all the information you retrieved\n")
        os.mkdir('collection')
    redirect("into","collection")
    with open('numOf.txt', 'w') as w:
        w.write('1')
    print("\n\033[4mData collection may slow down your computer or cause some lagging, especially when parsing larger albums or discographies\033[0m\n\n")

def getWhichOne():
    with open('numOf.txt','r') as r:
        return r.read()

def changeNum(newNum):
    with open('numOf.txt', 'w') as w:
        w.write(str(newNum))

def convertToSoup(link):
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(5)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    return soup

def writeSongstoFileExcel(trs):
    databook = xlsxwriter.Workbook('album.xlsx')
    datasheet = databook.add_worksheet()
    headers = ["Title/Composer","Performer","Duration","Stream on"]
    row = 0
    column = 0
    for header in headers :
        datasheet.write(row, column, header)
        column += 1
    column = 0
    for tr in trs:
        column=0
        title_composer = tr.find('td',{'class': 'title-composer'})
        title = title_composer.find('div',{'class': 'title'})
        performer = tr.find('td',{'class': 'performer'})
        time = tr.find('td',{'class': 'time'})
        stream = tr.find('td',{'class': 'stream'})
        data = [title.text.strip(),performer.text.strip(),time.text.strip(),stream.text.strip()]
        row+=1
        for y in range(0, len(data)):
            datasheet.write(row, column, data[y])
            column+=1
    databook.close()

def writeSongstoFileExcel(trs,albumNum):
    databook = xlsxwriter.Workbook('album'+str(albumNum)+'.xlsx')
    datasheet = databook.add_worksheet()
    headers = ["Title/Composer","Performer","Duration","Stream on"]
    row = 0
    column = 0
    for header in headers :
        datasheet.write(row, column, header)
        column += 1
    column = 0
    for tr in trs:
        column=0
        title_composer = tr.find('td',{'class': 'title-composer'})
        title = title_composer.find('div',{'class': 'title'})
        performer = tr.find('td',{'class': 'performer'})
        time = tr.find('td',{'class': 'time'})
        stream = tr.find('td',{'class': 'stream'})
        data = [title.text.strip(),performer.text.strip(),time.text.strip(),stream.text.strip()]
        row+=1
        for y in range(0, len(data)):
            datasheet.write(row, column, data[y])
            column+=1
    databook.close()

def writeSongstoFileJson(trs):
    dataHeaders = ["Title/Composer","Performer","Duration","Stream on"]
    with open(artist+getWhichOne()+'.json', 'a') as f: 
        x = 0
        for tr in trs:
            finalComma = ",\n"
            if((x+1)==len(trs)):
                finalComma = ""
            title_composer = tr.find('td',{'class': 'title-composer'})
            title = title_composer.find('div',{'class': 'title'})
            performer = tr.find('td',{'class': 'performer'})
            time = tr.find('td',{'class': 'time'})
            stream = tr.find('td',{'class': 'stream'})
            data = [title.text.strip(),performer.text.strip(),time.text.strip(),stream.text.strip()]
            f.write("\t{")
            for y in range(0, len(dataHeaders)):
                end = ","
                if((y+1)==(len(dataHeaders))):
                    end = ""
                f.write('\n\t\t"'+dataHeaders[y]+'": '+'"'+data[y]+'"'+end)
            f.write("\n\t}"+finalComma)
            x+=1

def returnSongData(soup):
    body = soup.find('body')
    albumContainer = body.find('div',{'class','overflow-container album'})
    cmn_wrap = albumContainer.find('div',{'id': 'cmn_wrap'})
    content_container = cmn_wrap.find('div',{'class': 'content-container'})
    content = content_container.find('div',{'class': 'content'})
    track_listing = content.find('section',{'class': 'track-listing'})
    disc = track_listing.find('div',{'class': 'disc'})
    table = disc.find('table')
    tbody = table.find('tbody')
    trs = tbody.find_all('tr',{'class': 'track'})
    return trs

def finishingTouch(fileType):
    with open(artist+getWhichOne()+'.'+fileType, 'r') as f:
        allData = f.read()
    with open(artist+getWhichOne()+'.'+fileType, 'w') as w:
        w.write("[\n"+str(allData)+"\n]")

def redirect(whichWay,dest):
    if(whichWay=="into"):
        if os.path.exists(dest):
            os.chdir(dest)
    else:
        os.chdir(dest)
    
def getAlbum(link, fileType):
    orig = os. getcwd()
    newCollection()
    toPrint = "| Creating data file for link: \t"+'\033[1m'+Back.CYAN+link+Style.RESET_ALL+'\033[0m'
    line = "-"*(len(toPrint)-17)
    print(line)
    print(toPrint+"\n| Of type: \t"+'\033[1m'+Back.YELLOW+fileType+Style.RESET_ALL+'\033[0m')
    soup = convertToSoup(link)
    trs = returnSongData(soup)
    redirect("into","collection")
    if(fileType=="json"):
        writeSongstoFileJson(trs)
        finishingTouch(fileType)
    elif(fileType=="xlsx"):
        writeSongstoFileExcel(trs,0)
    else:
        raise Exception("| We didn't recognize that filetype -- please try again! |")
    googleForm()
    print(line)
    changeNum(int(getWhichOne())+1)
    beautify()    
    redirect("outof",orig)

def getDiscography(link, fileType):
    orig = os. getcwd()
    newCollection()
    albumNum = int(getWhichOne())
    toPrint = "| Creating data file for link: \t"+'\033[1m'+Back.CYAN+link+Style.RESET_ALL+'\033[0m'
    line = "-"*(len(toPrint)-17)
    print(line)
    print(toPrint+"\n| Of type: \t"+'\033[1m'+Back.YELLOW+fileType+Style.RESET_ALL+'\033[0m')
    soup = convertToSoup(link)
    body = soup.find('body')
    artistContainer = body.find('div',{'class','overflow-container artist'})
    cmn_wrap = artistContainer.find('div',{'id': 'cmn_wrap'})
    content_container = cmn_wrap.find('div',{'class': 'content-container'})
    content = content_container.find('div',{'class': 'content'})
    discography = content.find('section',{'class': 'discography'})
    table = discography.find('table')
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    x = 0
    trsLength = len(trs)
    redirect("into","collection")
    for tr in trs:
        title = tr.find('td',{'class': 'title'})
        a = title.find('a')
        newLink = a.get('href')
        print("| Perusing data in link: \t"+'\033[1m'+Back.GREEN+newLink+Style.RESET_ALL+'\033[0m')
        newDriver = webdriver.Chrome()
        newDriver.get(newLink)
        time.sleep(3)
        newContent = newDriver.page_source.encode('utf-8').strip()
        newSoup = BeautifulSoup(newContent,"html.parser")
        newTrs = returnSongData(newSoup)
        if(fileType=="json"):
            writeSongstoFileJson(newTrs)
            if((x+1)!=trsLength):
                with open(artist+getWhichOne()+'.'+fileType, 'a') as f:
                    f.write(',\n')
            finishingTouch(fileType)
        elif(fileType=="xlsx"):
            writeSongstoFileExcel(newTrs,albumNum)
            albumNum+=1
        else:
            raise Exception("We didn't recognize that filetype -- please try again!")
        x+=1
        newDriver.quit()
    googleForm()
    print(line)
    changeNum(int(getWhichOne())+1)
    beautify()
    redirect("outof",orig)

def googleForm():
    print('|\n| Submit suggestions to --> https://forms.gle/BPuNi3DzqLFHEc8N9\t\tThank you! :)')

def beautify():
    if os.path.exists('geckodriver.log'):
        os.remove("geckodriver.log")