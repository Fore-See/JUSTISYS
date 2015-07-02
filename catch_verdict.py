# -*- coding: utf-8 -*-
#First Step @ second layer
import string
import requests
from bs4 import BeautifulSoup

cookie_1='ASP.NET_SessionId=pisqs455u2gvkm45yyjsy3bp; lawbank=03466c6cd0e24e29b6f38856110b3f37-33; _ga=GA1.3.329735530.1434956986; _gat=1; JubFrm-pagebox=%5EcourtFullName%3DILDV%60%5Ekw%3D%E8%BB%8A%5Ejcatagory%3D2%5Eissimple%3D-1%5Ejt%3D%E6%90%8D%E5%AE%B3%E8%B3%A0%E5%84%9F; x=j=csoRwOAahQP30doG2B84Jl6rT2X696guyiYjzyfERzlUq0jgk9RwqJTmSuWR4UjILyorQiMQl165XLbyYvaXKstjv6wGda6hDlfkPD2Q2sx62MsnOx/M4zJr6zvHqhKIxOZRS13PB0mKeJeyv1sHXL5Fp68lt5xZcbOf5hc25jKN/MvOt8N9RXw+RKLRJ2z+uLtoE+HNF8Hnl9HIFF5fJnn+v+3Dr8zL/FLiZWlgoHIx/pwmUmE6dckFGmUpeTPneMfGZp75QVmMEg/5lILjam1AHEoREIrvFLHs+Kvk8CpAfo12skJNrsViwOLZ+udi'

#cookie_2='ASP.NET_SessionId=f4zysqrd3mbrcgv5jul31155; _gat=1; _ga=GA1.3.1224946460.1434551693; JubFrm-pagebox=%5EcourtFullName%3DSLDV%60%5Ekw%3D%E8%BB%8A%5Ejcatagory%3D2%5Eissimple%3D-1%5Ejt%3D%E6%90%8D%E5%AE%B3%E8%B3%A0%E5%84%9F; x=j=MS75W8xcPQRONHRsik2vrEo62yf/Csi44AgRySnTAQmqQIX6L1PX6K4ZPckIKq03uUoYVN3hjZWJ0bgUm28vA4+9qDmiH0yQ4CxFjFvWOeg5IaBnd7qiUUs8jk/gdMYoacK6Y8RRP1Z4ro/Vr4y+3/+EXw2uz5kUvKgwOLp9NhLYM2RiZWKuG1XlWXcK2vgYg8DVj9B9ji7wLXefLWdehA9G9mzMGAL8zIjfFoHIR8nPjkldOvE+bUVBsIT8aBe932zj9bSQFOEXjCnTiedU8aF5R0mYLvdJJ9yoEQeFQbxTfot+g2tybWM47FLbSsFh'

#cookie_3='ASP.NET_SessionId=f4zysqrd3mbrcgv5jul31155; _gat=1; _ga=GA1.3.1224946460.1434551693; JubFrm-pagebox=%5EcourtFullName%3DPCDV%60%5Ekw%3D%E8%BB%8A%5Ejcatagory%3D2%5Eissimple%3D-1%5Ejt%3D%E6%90%8D%E5%AE%B3%E8%B3%A0%E5%84%9F; x=j=yUm4L9fKJqyv+bvUjQeEuHlX2Uk1M6ZY+srNvIy39vuzWoh6eGOtto71u8OudzDz0CrH2GdHmjzEw0HcygOQAKKol52OCpWqcN/hWtAXH5wtK7YHkY+mqVnBI8nlomnlQ5AZovZs+0FOApcFFCI81Twziync+0q9lbAbc/AAMfDVKeUWCo75SIj6ZL4pjW1D2c1/x2pbv8XvUxO8jfmyFdlmLU3cFLkmTCT92LgODLdHWBY9RNmpc0czOtRWt0ci3B8iN3oB4mKKPeVozMR8R1Ds7Ez/RKcatvJjV8NRR8ZkcEAPCFSG00o4/Eq1jAsY'

#cookie_4='ASP.NET_SessionId=f4zysqrd3mbrcgv5jul31155; _gat=1; _ga=GA1.3.1224946460.1434551693; JubFrm-pagebox=%5EcourtFullName%3DILDV%60%5Ekw%3D%E8%BB%8A%5Ejcatagory%3D2%5Eissimple%3D-1%5Ejt%3D%E6%90%8D%E5%AE%B3%E8%B3%A0%E5%84%9F; x=j=csoRwOAahQP30doG2B84Jl6rT2X696guyiYjzyfERzlUq0jgk9RwqJTmSuWR4UjILyorQiMQl165XLbyYvaXKstjv6wGda6hDlfkPD2Q2sxGnIFQ3+goRGQTuhJ0Y45PyMXedq8GG1mOTRW4Z9XwtX2BlW099bKBRKrr5a1+BHXj/yd/Vden4o2RiltTs1TTdvRFh3Zz8mYwN2KmQMuguTkuuUBcEnEs8dUMcybjhFCy1/mAkLW1fFeFAU/yk+DZ4sVF+9QOK3fzoa6Vc3nPslsOGb6DolNuKisXElW5+ZvHE9TkyWfJ1q8F9mJcU+jX'


def all(insert):
	filename_list={}
	fl=1

	cookie = str(insert)

	#catch y=p= whether exist
	if cookie.find('y=p=') != -1:
		pos_yp = cookie.split('y=p=')
		cookie = pos_yp[0]+string.join(pos_yp[1].split(';')[1:],';')

	uml = "http://fyjud.lawbank.com.tw/"
	headers = {'Cookie' : cookie}
	res = requests.get('http://fyjud.lawbank.com.tw/listcontent5.aspx',\
					   headers = headers)
	soup = BeautifulSoup(res.text)

	#抓location ----- place 
	#<eg台北>
	for h4 in soup.select('h4'):
		allname = str(h4).decode('utf-8')
		pos = allname.find('地方法院'.decode('utf-8'))
		place = allname[pos-2:pos].encode('utf-8')

	#catch total_pages
	state = soup.select('.page > tr > td')[0].text.replace(' ','')
	pos_start = state.find(u'共')
	pos_end = state.find(u'筆')
	total_pages = int(state[pos_start+1:pos_end])

	#進到第三層
	data = {'__EVENTTARGET':'lnkbtnOhmy1', \
			'__EVENTARGUMENT':'', \
			'__VIEWSTATE':'', \
			'__VIEWSTATEGENERATOR':'', \
			'__EVENTVALIDATION':'', \
			'FDLink':''
		   }
	a = soup.select('table > tbody > tr > td > a')[0]
	link = a['href']
	cookieId = a['onclick'].split('\'')[1]
	headers_3rd = {'Cookie': '%s;y=p=%s'%(cookie, cookieId)}
	res_3rd = requests.get('%s'%(uml+link), headers = headers_3rd)
	soup_3rd = BeautifulSoup(res_3rd.text)

	#each file name ----- save_name
	#eg. 士林_103_士簡_867
	import string
	save= soup_3rd.select('#FDLink')[0]['value'].encode('utf-8').split(',')
	save_name = string.join(save[2:5],'_')
	save_dir = save[1]
	filename_list[fl]=(place+'_'+save_name+'.txt').decode('utf-8')
	fl+=1

	#save first soup_3rd by get
	fid=open('project\%s'%(filename_list[fl-1]),'w')
	content = soup_3rd.select('.Table-List')[0].text
	fid.write(content.encode('utf-8'))
	fid.close()

	import time
	try:
		for i in range(1, total_pages):
			data['__VIEWSTATE'] = soup_3rd.select('#__VIEWSTATE')[0]['value']
			data['__EVENTVALIDATION'] = soup_3rd.select('#__EVENTVALIDATION')[0]['value']
			data['__VIEWSTATEGENERATOR'] = soup_3rd.select('#__VIEWSTATEGENERATOR')[0]['value']

			res_post = requests.post('http://fyjud.lawbank.com.tw/content3.aspx?p=lJE0csYFgzBIuZknAS%2f9cG4vHeoH7hup9KUMRu4jjlc%3d',\
							   headers = headers_3rd,\
							   data = data)
			soup_3rd = BeautifulSoup(res_post.text)
		
			#save_name
			save= soup_3rd.select('#FDLink')[0]['value'].encode('utf-8').split(',')
			save_name = string.join(save[2:5],'_')
			save_dir = save[1]
			filename_list[fl]=(place+'_'+save_name+'.txt').decode('utf-8')
			fl+=1
		
			fid=open('project\%s'%(filename_list[fl-1]),'w')

			content = soup_3rd.select('.Table-List')[0].text
			fid.write(content.encode('utf-8'))
			fid.close()
			if i%100==0:
				print i,'-ok'
			time.sleep(10)

	finally:
	#make an index by filename_list to a file
	#open() code must be 'unicode'
	#but write() code is 'utf-8'
		total = len(filename_list)
		save_filename_list = ('project\%s.txt'\
						%place).decode('utf-8')
		fn=open(save_filename_list,'w')
		for i in range(1,total+1):
			fn.write(str(i)+'-'+filename_list[i].encode('utf-8')+'\n')
		fn.close()
		if total==total_pages:
			print 'you did caught everything, there are %d files!'%total
		else:
			print 'FAIL!!!, there should be %d files!'%total_pages
			print 'but u only got %d files...'%total
			
print 'now start!!!'
all(cookie_1)
print 'the First one has done!!!!'
#time.sleep(60)
# print 'Now begin the Second one!'
# #all(cookie_2)
# print 'the Second one has done!!!!'
# #time.sleep(60)
# print 'Now begin the Third one!'
# #all(cookie_3)
# print 'the Third one has done!!!!'
# #time.sleep(60)
# print 'Now begin the Fourth one!'
# all(cookie_4)
# print 'the Fourth one has done!!!!'