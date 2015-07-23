# -*- coding:utf-8 -*-
ls = [u'臺北',u'士林',u'新北',u'宜蘭'\
     ,u'基隆',u'桃園',u'新竹',u'苗栗'\
     ,u'臺中',u'彰化',u'南投',u'雲林'\
     ,u'嘉義',u'臺南',u'高雄',u'花蓮'\
     ,u'臺東',u'屏東',u'澎湖',u'金門'\
     ,u'連江']


cut = [u'最高法院：',u'歷審裁判',u'相關法條']
def find(content):
    stop =0
    for c in cut:
        if c in content:

            if stop ==0:
                stop = content.find(c)
#                 print c,stop
            if content.find(c) < stop:
                stop = content.find(c)
#                 print c,stop
    return stop
        
import os 
import codecs
def cut_useless(pos):
#     pos = u'金門'
    location = 'project\\%s'%pos
    all_files = os.path.abspath(location)
    for x in os.listdir(all_files):
        if x[0]!=u'c' and x[0]!=u'W':
            print x
            with codecs.open(os.path.join(location,x),'r+b','utf-8') as f:
                content = f.read()
                stop = find(content)
                f.write(content[:stop])
                f.truncate()
for pos in ls:
    print pos
    cut_useless(pos)
print 'done'