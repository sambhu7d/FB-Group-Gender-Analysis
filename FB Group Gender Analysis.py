# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 03:30:31 2020
@author: sambhu7d
"""

from sys import platform
import unicodedata
import time
import pip
import os
import matplotlib.pyplot as plt

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

while True:
    
    try:
        modules=['bs4','selenium','chromedriver-autoinstaller','pandas']
        for module in modules:
            install(module)   
        break
    except:
        print('Bad Internet Connection')
        time.sleep(5)
                    
import bs4
import pandas as pd
from selenium import webdriver
import chromedriver_autoinstaller as cd
from selenium.webdriver.common.keys import Keys
    

def OS_():
    if platform == "linux" or platform == "linux2":
        OS='L'
    elif platform == "darwin":
        OS='M'
    elif platform == "win32":
        OS='W'
    
    return OS
        
def fb():
    
    while True:
        
        user=input('Input Your Facebook Username/email/phone ')
        pswd=input('Input Your Facebook Password ')
           
        print("Paste The Facebook Group Link who\'s data you want")
        print("Make Sure The Group is Either Public or you are the member in the group")
        print('Example')
        print('https://www.facebook.com/groups/group_name_or_id')
        url=input("Paste The Facebook Group Link here :\n")
        confirm=input('Please Confirm The input by pressing Y or y \n ')
        if confirm=='Y' or confirm=='y':
            break
    
    url+='/members/'

    return user,pswd,url
           
def Auth():
    
    while True:
        # print('Do you use 2 step Authentication ')
        g=input('Do you use 2 Step Verfication Y/y or N/n \n')
        if g=="Y" or g=='y' :
            while True:
                try:
                    ga=int(input("Input Google Authentication \n"))
                    return  ga
                except:
                    print('Only numbers Buddy')
        elif g=="N" or g=='n':
            return None          
        else:
            print('Oops wrong Input')

def chrome_driver(cd):
    while True:
        try:
            path=cd.install()  
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 1}
            options.add_experimental_option("prefs",prefs)
            driver = webdriver.Chrome(executable_path=path,options=options,keep_alive=False)
            driver.implicitly_wait(2)
            driver.fullscreen_window()
            
            break
        except :  
            print("No Internet Connection")
            print("Retrying in 10 second")
            print('\n\n\n')
            time.sleep(10)
    return driver

def automation(driver):
    
    def scroll_to_end():
        """A method for scrolling the page."""
        
        # Get scroll height.
        driver.maximize_window()
        # driver.execute_script("return document.body.scrollHeight")
        print('Please Wait')
        
        while True:
            pre_height = driver.execute_script("return document.documentElement.scrollHeight")
            t_end = time.time() + 15    
            while time.time() < t_end:

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
            print('break\n\n\n')
            height = driver.execute_script("return document.documentElement.scrollHeight")
            if pre_height==height:
                print('\n\n')
                print('Noting left to scroll')
                break
            else:
                print("Previous Height =",pre_height)
                print("Present Height=",height)
                
                
                
        driver.implicitly_wait(2)
        ps=driver.page_source
                
        return ps
           
    while True:
        
        try:
            
            driver.get(url)
            e=driver.find_element_by_id("email") #//*[@id="email"]
            p=driver.find_element_by_id("pass")
            l=driver.find_element_by_id("loginbutton")
            
            e.send_keys(user)
            p.send_keys(pswd)
            l.click()
            
            if pin != None :
                gu=driver.find_element_by_id("approvals_code")
                gu.send_keys(pin)
                gu.send_keys(Keys.RETURN)
            
                try:
                    driver.implicitly_wait(1)
                    bt=driver.find_element_by_id("checkpointSubmitButton")
                    bt.click()
                    # bt.send_keys(Keys.RETURN)
                    
                except:
                    print('Error detected')
                
                
            break
        
        except:
            print('Network Down ')
            time.sleep(10)
        
    while True:
        
        
        driver.refresh()
        time.sleep(5)
        driver.fullscreen_window()
        ps=driver.page_source
        soup=bs4.BeautifulSoup(ps,'html.parser')
        group=soup.select("span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ojkyduve")
        # title=' '
        gt=[]
        # tot=' '
        for g in group:
            gt.append(g.get_text())
        
        print(gt)
        
        for g in gt:
            if 'Members' in g:
                tot=g.split('·')[1]
                title=gt[gt.index(g)-1]
                break
        
        
        print('\n')
        print('Total Member in '+ title + ' is '+ tot) 
        
         #+ str(ml[0]))
           
        break
    
    ps=scroll_to_end() 
    soup=bs4.BeautifulSoup(ps,'html.parser')
    data=soup.select('a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.oo9gr5id.gpro0wi8.lrazzd5p')
    print('\n\n')    
    print('We have Total Data of '+str(len(data)))
    print('\n\n\n')
    
    return title,tot,data
               
def check_dup():
    print('Duplicate Data')
    names,links=[],[]
    for d in data:
        if not d['href'] in links:
            names.append(d.get_text())
            links.append(d['href'])
        else:
            print(d.get_text()+'\t'+d['href'])
            print()
        
    names.remove(names[0])
    links.remove(links[0])


    return names,links

def gender(driver): 
    print('\n')
    print('Gender Data')
    print()
    file=[]
    gfile=[]
    i=0
    # prfL=[]
    while i < len(links):
        driver.implicitly_wait(1)
        driver.get('https://www.facebook.com'+links[i])
        time.sleep(1)
        
        #update
        ps=driver.page_source
        soup=bs4.BeautifulSoup(ps,'html.parser')
  
        
        data=soup.select('a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.pq6dq46d.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.l9j0dhe7.abiwlrkh.p8dawk7l.cbu4d94t.taijpn5t.k4urcfbm')
        link=data[0]['href']
        if '?id' in link:
            driver.get(link)
            prf=driver.current_url  
            try :
                lnk=prf.split('/?show')[0]
            except:
                lnk=prf
                
        else:
            print(link)
            print("Its a Page\n\n\n")
            i+=1
            
        try:
            driver.get(lnk)
            ps=driver.page_source
            soup=bs4.BeautifulSoup(ps,'html.parser')
            txt=soup.select('span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.fe6kdd0r.mau55g9w.c8b282yb.mdeji52x.a5q79mjw.g1cxx5fr.knj5qynh.m9osqain.hzawbc8m')
            text_=txt[0].get_text()
            text=text_
                     
        except:
            
            driver.get(lnk+'/about_contact_and_basic_info')
            ps=driver.page_source
            soup=bs4.BeautifulSoup(ps,'html.parser')
            txt=soup.select('span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.fe6kdd0r.mau55g9w.c8b282yb.iv3no6db.jq4qci2q.a3bd9o3v.knj5qynh.oo9gr5id.hzawbc8m')
            txtL=[t.get_text() for t in txt]
            for t in txtL:
                if 'Male' in t or 'Female' in t:
                    text=t
                    break

            
        if ' him ' in text or ' his ' in text or 'Male' in text:
            print('M'+ '\t'+ names[i]) 
            file.append(['M',lnk,names[i]]) #[names[i],lnk,'M',True,1]') 
            gfile.append(1)
        elif 'she' in text or' her ' in text or 'Female' in text :
            print('F'+'\t'+ names[i]) 
            file.append(['F',lnk,names[i]]) #[names[i],lnk,'M',True,1]') 
            gfile.append(0)               
        elif 'they' or 'them':
            print('T' +'\t'+ names[i]) 
            file.append(['T',lnk,names[i]]) #[names[i],lnk,'M',True,1]') 
            gfile.append(2)       
        else:    
            print('N'+'\t'+ names[i]) 
            file.append(['N',lnk,names[i]]) #[names[i],lnk,'M',True,1]') 
            gfile.append(3)
            
        i+=1
                                                             
    driver.close()
    return file,gfile
           
def save_file():
    df=pd.DataFrame(f, columns =['Gender', 'Link','Name']) #,'Boolean','Binary']) 
    df=df.sort_values(by=['Gender','Name'],ascending=True)
    df = df.reset_index(drop=True)
    df.index+= 1  
    
    df.to_csv(file_path+ 'Data.csv', index_label='Event_id')
    
def save_gFile():
    df=pd.DataFrame(g, columns =['Gender']) 
    df=df.sort_values(by=['Gender'],ascending=True)
    df = df.reset_index(drop=True)
    df.index+= 1    
    df.to_csv(file_path + 'Gender.csv',index_label='Event_id')
    
def piePlot():
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Female','Trans', 'Male',  'No Data'
    sizes = [g.count(0),g.count(2),g.count(1),g.count(3)]
    explode = (0.1, 0.1, 0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(file_path+'Pie Chart')
    plt.show()
   
OS=OS_()

user,pswd,url=fb()
pin=Auth()
driver=chrome_driver(cd)

print('\n')       
 
page,num, data=automation(driver)
names,links=check_dup()

f,g=gender(driver)


print('Offline Work')

cwd =os.getcwd()


if OS=='M':
    file_path= cwd + '/' + page+ '/'
if OS=='W':
    file_path= cwd + '\\' + page + '\\'
  
try:  
    os.mkdir(file_path)  
except OSError as error:  
    print(error)   

save_file()
save_gFile()
piePlot()

print()
print('File Saved')
print(file_path)
print('\n'+'Godd Bye!!!')