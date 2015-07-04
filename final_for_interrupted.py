# -*- coding: utf-8 -*-
import string
import requests
from bs4 import BeautifulSoup

#------------------------------
#輸入你想要的號碼，也就是要抓得那個號碼
start_from_no = 65
times = start_from_no/20
twenty_list = start_from_no%20

#輸入第二層的cookie
origin_cookie='ASP.NET_SessionId=0z1wsl55ao4pbifpuecdn255; lawbank=16df6c4cd8fe4b58ab3c8ca977f75c49-33; _ga=GA1.3.329735530.1434956986; _gat=1; JubFrm-pagebox=%5EcourtFullName%3DKMDV%60%5Ekw%3D%E8%BB%8A%5Ejcatagory%3D2%5Eissimple%3D-1%5Ejt%3D%E6%90%8D%E5%AE%B3%E8%B3%A0%E5%84%9F; x=j=KQ8PUNQkVDeVi1NA/IaHRM6ZF2IGUwF37WmqRzoiGo0lIyIpBoWGQHCA1pNHsOg/oxUC0PW5tbl0fVWAZM2kS/AJXQkYNbcyyDClGcrAEm5/BihyfO3X5ZK0LrvFe0z0FxZACoT4Er7ZiOotFQZZnzdWNNnv01tHLLIO1fqnhkilIC8sKrgyfV4wDWZihaY6L5bZjzFeX5A+g856uaKF57rkN7+7u58k5Ncsqzz6dJ8qJ/n2PfwMDvmRAB9gG/ys4eko1FfLgoo9piF/VZ6vKOa01genyil30Z3Da7Url9xs54hclIiWhcsiWP1nPnYI'
import string
if origin_cookie.find('y=p=') != -1:
    pos_yp = origin_cookie.split('y=p=')
    origin_cookie = pos_yp[0]+string.join(pos_yp[1].split(';')[1:],';')
#------------------------------

#cookie = 'ASP.NET_SessionId=xq3yfxucb122zjy2in5qunr0; lawbank=e83dafaa80234b35af3f1337bf1f5f83-33; y=p=ga6YQzTxtX4nbb%2fpDcqvILg2sSYKfSTHsTT6K2g%2bn2cpL5jR%2fdNhSIdktQsnj7Y8; _ga=GA1.3.1224627297.1434421447; _gat=1; JubFrm-pagebox=%5EcourtFullName%3DPCDV%60%5Ekw%3D%E8%BB%8A%5Ejcatagory%3D2%5Eissimple%3D-1%5Ejt%3D%E6%90%8D%E5%AE%B3%E8%B3%A0%E5%84%9F; x=j=yUm4L9fKJqyv+bvUjQeEuHlX2Uk1M6ZY+srNvIy39vuzWoh6eGOtto71u8OudzDz0CrH2GdHmjzEw0HcygOQAKKol52OCpWqcN/hWtAXH5wtK7YHkY+mqVnBI8nlomnlQ5AZovZs+0FOApcFFCI81Twziync+0q9lbAbc/AAMfDVKeUWCo75SIj6ZL4pjW1D2c1/x2pbv8XvUxO8jfmyFdlmLU3cFLkmTCT92LgODLdHWBY9RNmpc0czOtRWt0ci3B8iN3oB4mKKPeVozMR8R1Ds7Ez/RKcatvJjV8NRR8ZGNMCvkJpjDvtCp/nqyhea'
#catch y=p= whether exist

data = {'__EVENTTARGET':'lnkbtnOhmy1', \
        '__EVENTARGUMENT':'', \
        '__VIEWSTATE':'', \
        '__VIEWSTATEGENERATOR':'', \
        '__EVENTVALIDATION':'', \
        'FDLink':''
       }

uml = "http://fyjud.lawbank.com.tw/"
headers = {'Cookie' : origin_cookie}
res = requests.get('http://fyjud.lawbank.com.tw/listcontent5.aspx',\
                   headers = headers)
soup = BeautifulSoup(res.text)

#catch total_pages and this_page
this_page = soup.select('.page > tr > td')[0].text.replace(' ','')
pos_start = this_page.find(u'共')
pos_end = this_page.find(u'筆')
total_pages = int(this_page[pos_start+1:pos_end])
#print total_pages
print 'now',this_page

for i in range(0, times):
        data['__VIEWSTATE'] = soup.select('#__VIEWSTATE')[0]['value']
        data['__EVENTVALIDATION'] = soup.select('#__EVENTVALIDATION')[0]['value']
        data['__VIEWSTATEGENERATOR'] = soup.select('#__VIEWSTATEGENERATOR')[0]['value']

        res_post = requests.post('http://fyjud.lawbank.com.tw/listcontent5.aspx',\
                           headers = headers,\
                           data = data)
        soup = BeautifulSoup(res_post.text)
print 'after',soup.select('.page > tr > td')[0].text.replace(' ','')

target_element = soup.select('.Table-List > tbody > tr')[twenty_list].select('td > a')[0]
link = uml+target_element['href']

cookie_yp = '; y=p=%s'%(target_element['onclick'].split('\'')[1])
cookie = origin_cookie+cookie_yp

import requests
from bs4 import BeautifulSoup

filename_list={}
fl=int(start_from_no)
fin= fl
Request_URL=str(link)

#**********************************************************
print 'start from %d'%fl
print 'now start!!!!'

#catch y=p= whether exist

#if cookie.find('y=p=') != -1:
#    pos_yp = cookie.split('y=p=')
#    cookie = pos_yp[0]+string.join(pos_yp[1].split(';')[1:],';')

uml = "http://fyjud.lawbank.com.tw/"
headers = {'Cookie' : cookie}
res = requests.get(Request_URL,\
                   headers = headers)
soup = BeautifulSoup(res.text)

#抓location ----- def = get_place return place
#<eg台北>
def get_place(Beautiful):
    for h4 in soup.select('h4'):
        allname = str(h4).decode('utf-8')
        pos = allname.find('地方法院'.decode('utf-8'))
        place = allname[pos-2:pos].encode('utf-8')
    return place
place = get_place(soup)

#catch total_pages  
#def = get_total_pages return total_pages
def get_total_pages(Beautiful):
    state = soup.select('.page > tr > td')[0].text.replace(' ','')
    pos_start = state.find(u'共')
    pos_end = state.find(u'筆')
    total_pages = int(state[pos_start+1:pos_end])
    return total_pages
total_pages = get_total_pages(soup)

import string
save= soup.select('#FDLink')[0]['value'].encode('utf-8').split(',')
save_name = string.join(save[2:5],'_')
filename_list[fl]=(place+'_'+save_name+'.txt').decode('utf-8')
fl+=1

content = soup.select('.Table-List')[0].text
with open('project\%s' %(filename_list[fl-1]),'w') as f:#save-------------------------diraction
	f.write(content.encode('utf-8'))


#try to catch the rest of files
import time
data = {'__EVENTTARGET':'lnkbtnOhmy1', \
        '__EVENTARGUMENT':'', \
        '__VIEWSTATE':'', \
        '__VIEWSTATEGENERATOR':'', \
        '__EVENTVALIDATION':'', \
        'FDLink':''
       }
try:
    for i in range(fl, total_pages+1):
        data['__VIEWSTATE'] = soup.select('#__VIEWSTATE')[0]['value']
        data['__EVENTVALIDATION'] = soup.select('#__EVENTVALIDATION')[0]['value']
        data['__VIEWSTATEGENERATOR'] = soup.select('#__VIEWSTATEGENERATOR')[0]['value']

        res_post = requests.post(Request_URL,\
                           headers = headers,\
                           data = data)
        soup = BeautifulSoup(res_post.text)
        save= soup.select('#FDLink')[0]['value'].encode('utf-8').split(',')
        save_name = string.join(save[2:5],'_')
        save_dir = save[1]
        filename_list[fl]=(place+'_'+save_name+'.txt').decode('utf-8')
        fl+=1
		
        content = soup.select('.Table-List')[0].text
        with open('project\%s'%(filename_list[fl-1]),'w') as f:#---------------------------diraction
			f.write(content.encode('utf-8'))
        
        if i%100==0:
            print i,'-ok'
        time.sleep(1)
finally:
    total = len(filename_list)
	
    save_filename_list = ('project\%s.txt'%place).decode('utf-8')#-------------------diraction
    fn=open(save_filename_list,'a')
    
    for i in range(fin,total+fin):
        fn.write(str(i)+'-'+filename_list[i].encode('utf-8')+'\n')
    fn.close()
    print 'you have started from No. %d , and caught %d files'%(fin, total)
    print 'so total files should be %d , right?'%(fin+total-1)