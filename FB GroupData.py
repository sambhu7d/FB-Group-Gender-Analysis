#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 03:30:31 2020
@author: sambhu7d
"""

from sys import platform
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
        time.sleep(30)
                    
import bs4
import pandas as pd
from selenium import webdriver
import chromedriver_autoinstaller as cd
from selenium.webdriver.common.keys import Keys
    
class fb_backend(object):
    pass
class fb_frontend(fb_backend):
    pass
    
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
        
        user=input('Input Your Facebook Username ')
        pswd=input('Input Your Facebook Password ')
           
        print("Paste The Facebook Group Link who\'s data you want")
        print("Make Sure The Group is Either Public or you are the member in the group")
        print('Example')
        print('https://www.facebook.com/groups/group_name_or_id')
        url=input("Paste The Facebook Group Link here :\n")
        confirm=input('Please Confirm The input Y ')
        if confirm=='Y':
            break
        
    url+='/members/'

    return user,pswd,url
           
def Auth():
    
    while True:
        # print('Do you use 2 step Authentication ')
        g=input('Do you use Google Authentication Y or N \n')
        if g=="Y" :
            ga=input("Input Google Authentication \n")
            return  ga
        elif g=="N":
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
            # driver.fullscreen_window()
            
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
        
        c=0
        print('Please Wait')
        while True:
            
            # Scroll down to the bottom.
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.implicitly_wait(2)
        
            ps=driver.page_source
            soup=bs4.BeautifulSoup(ps,'html.parser')
            offline=soup.find("div", {"aria-busy":"true"})
            
            if offline==None:
                break
            
            c+=1
            
        print('Total Scroll =' + str(c))
              
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
            
                bt=driver.find_element_by_id("u_0_3")
                bt.click()
                bt.send_keys(Keys.RETURN)
                
            break
                
        except:
            print('Network Down ')
            time.sleep(10)
        
    while True:
        
        driver.refresh()
        driver.fullscreen_window()
        title=driver.title
        ps=driver.page_source
        soup=bs4.BeautifulSoup(ps,'html.parser')
        m=soup.find("strong")
        print(m)
        
        if not m==None:
            members=m.get_text()
            total=''
            for i in members:
                try:
                    int(i)
                    total+=i
                except:
                    continue
            
            total=int(total)
            print('\n')
            print('Total Member in '+ title + ' is ' + str(total))
            break
        
        print("No Internet Connection")
        print("Retrying in 10 second")
        time.sleep(10)

    scroll_to_end()      
    ps=driver.page_source
    soup=bs4.BeautifulSoup(ps,'html.parser')
    data=soup.select('a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.oo9gr5id.gpro0wi8.lrazzd5p')
    print('\n\n')    
    print('We have Total Data of '+str(len(data)))
    print('\n\n\n')
    
    return title,data
                
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
    while i < len(links):
        driver.implicitly_wait(1)
        driver.get(links[i])
        time.sleep(2)
        
        try:# Add Friend | Follow | Message | Page
            try: # Add Friend | Follow | Message             
                try:
                    t=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div/div/div[1]/div/div[2]/span') 
                except:
                    t=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/span')            
                
                text=t.text
                if ' him ' in text or ' his ' in text:
                    print(names[i] +'\t'+'M')
                    file.append([names[i],links[i],'M',True,1]) 
                    gfile.append(1)
                elif ' her ' in text :
                    print(names[i] +'\t'+'F')
                    file.append([names[i],links[i],'F',False,0])
                    gfile.append(0)
                else:
                    print(names[i] +'\t'+'T') 
                    file.append([names[i],links[i],'T','NONE',2])
                    gfile.append(2)                    
            except: #Page
                # driver.implicitly_wait(1)
                g=driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.l9j0dhe7.dp1hu0rb.cbu4d94t.j83agx80 > div.rq0escxv.lpgh02oy.du4w35lb.rek2kq2y > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.o8rfisnq > div > div > div.oajrlxb2.tdjehn4e.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.nhd2j8a9.j83agx80.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.tkv8g59h.qt6c0cv9.fl8dtwsd.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.l9j0dhe7.abiwlrkh.p8dawk7l.beltcj47.p86d2i9g.aot14ch1.kzx2olss.cbu4d94t.taijpn5t.ni8dbmo4.stjgntxs.k4urcfbm.tv7at329 > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.taijpn5t.bp9cbjyn.owycx6da.btwxx1t3.c4xchbtz.by2jbhx6 > div:nth-child(2) > span')
                print('Its a Page')
                # print()
            
            i+=1
                
        except: #Friend
            driver.implicitly_wait(1)
            driver.get(links[i]+'/about_contact_and_basic_info')
            time.sleep(2)
            ps=driver.page_source
            soup=bs4.BeautifulSoup(ps,'html.parser')
            j=soup.select('div.j83agx80.cbu4d94t.ew0dbk1b.irj2b8pg')
            bool_=False
            if len(j)>0:
                for g in j:
                    if 'Gender' in g.text:
                        if 'Male' in g.text:
                            print(names[i] +'\t'+'M')
                            file.append([names[i],links[i],'M',True,1]) 
                            gfile.append(1)
                        elif 'Female' in g.text :
                            print(names[i] +'\t'+'F') 
                            file.append([names[i],links[i],'F',False,0])        
                            gfile.append(0)
                        else:
                            print(names[i] +'\t'+'T') 
                            file.append([names[i],links[i],'T','NONE',2])        
                            gfile.append(2)
                        bool_=True
                        break
                    
                if not bool_:
                    print(names[i] +'\t'+'N')
                    file.append([names[i],links[i],'N','----','3'])
                    gfile.append(3)
                        
                i+=1             
            else: #check Internet
                try:
                    # time.sleep(1)
                    no=driver.find_element_by_css_selector('#main-message > h1 > span')
                    print(no.text)
                    print()
                    time.sleep(20)
                except:
                   print('Oops! Something Went Wrong')
                                                               
    driver.close()
    return file,gfile
           
def save_file():
    df=pd.DataFrame(f, columns =['Name', 'Link','Gender','Boolean','Binary']) 
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
 
t,data=automation(driver)
names,links=check_dup()
f,g=gender(driver)

print('Offline Work')

cwd =os.getcwd()

t=t.replace('Facebook','')
t=t.replace(' | ','')

if OS=='M':
    file_path= cwd + '/' + t + '/'
if OS=='W':
    file_path= cwd + '\\' + t + '\\'
  
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
