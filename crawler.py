from selenium import webdriver as wd
from bs4 import BeautifulSoup
import os
import re

#driver=wd.PhantomJS('/home/tk/phantom/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver=wd.Chrome('./chromedriver')
driver.implicitly_wait(3)
#url login
def login():
    driver.get("https://oslab.ssu.ac.kr/main/index.php/login/")
    driver.find_element_by_id('username-63').send_keys('USERNAME')
    driver.find_element_by_id('user_password-63').send_keys('PASSWORD')
    driver.find_element_by_class_name('um-left').click()
login()

#driver.implicitly_wait(3)
#menu button click

num = 0

for i in range(1,55):
    driver.get("https://oslab.ssu.ac.kr/main/index.php/oslab-main/2017-os/qa/?pageid="+str(i)+"&mod=list")
    elements=driver.find_elements_by_class_name('kboard-default-cut-strings')

    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    notices = soup.select('div[class=kboard-default-cut-strings]')

    '''for notice in notices:
        num += 1
        a=notice.find_parent('a').get
        fileName = './file/ ' + notice.text.strip()[:-5].strip() +  str(num) + ".txt"
        print(notice.text.strip()[:-5].strip())
        f = open(fileName, 'w')


    for element in elements:
        num+=1
        fileName = './file/ ' + element.text.strip()[:-5].strip().replace('/', '_') + str(num) + ".txt"
        print(element.text.strip()[:-5].strip())
        f=open(fileName, 'w')'''

    for link in soup.find_all('a'):
        tag = str(link.get('href'))

        if re.match('/main/index.php/oslab-main/2017-os/qa/*', tag):
            if re.match('.*mod=editor', tag):
                continue
            else:
                num += 1
                #fileName = './file/ ' + element.text.strip()[:-5].strip().replace('/', '_') + str(num) + ".txt"
                #print(element.text.strip()[:-5].strip())
                #f = open(fileName, 'w')

                tag = "https://oslab.ssu.ac.kr"+tag
                #login()
                driver.get(tag)
                html1 = driver.page_source
                soup1 = BeautifulSoup(html1, 'lxml')
                #print(soup.text)

                #Check if this page is secret or not.
                if soup1.select_one('div[class=kboard-title]') == None :
                    continue
                else:

                #제목
                    title = './file/' + soup1.select_one('div[class=kboard-title]').getText().replace('/', '_').strip() + str(num) + ".txt"
                    f = open(title, 'w')

                #본문
                    notices1 = soup1.select('div[class=content-view]')
                    for i in notices1:
                        f.write("==============Content================\n")
                        f.write(i.getText().strip())
                        f.write("\n\n\n\n")
                    comment=soup1.select('div[class=comments-list-content]')

                    if comment != None :
                        f.write("==============Comment================\n")
                        for i in comment:
                            f.write(i.getText().strip() + '\n\n')
                    f.close()
