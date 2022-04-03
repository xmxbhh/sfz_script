import numpy as np
import requests
import os
import time
from color import *
#area = '371324'
#year = '2002'
#moon = "9"
#zero = "0"
#day = "24"
sex = "woman"
name = "邢梦雪"
'''
area = "371324"
year = "2003"
moon = "8"
zero = "0"
day = "18"
sex = "man"
name = "张立豪"
'''
day_list =[]
moon_why=['01','02','03','04','05','06','07','08','09','10','11','12']
data1 = []
filenameyes='yes.txt'
filenameno='no.txt'
filenamenoscan='noscan.txt'
count = 0
ln_list=[]
sex_man = (1,3,5,7,9)  
sex_woman = ('0','2','4','6','8')
dlist=[]
facklist=[]
lln_list=[]
list1=[]
facks=[]
man_odd_number = []
woman_even_mumver =[]
def moon_day (year,moon):
	day_list =[]
	if_moon= moon
	Year = int(year)
	if if_moon == 'no':
		moon=moon_why=['01','02','03','04','05','06','07','08','09','10','11','12']
	else:
		moon = if_moon
	for i in moon:
		Month = int(i)
		#31天的情况判断
		if (Month == 1 or Month == 3 or Month ==5 or Month == 7 or Month == 8
		        or Month == 10 or Month == 12):
		    day_list.append(31+1)
		#30天的情况判断
		elif (Month == 4 or Month == 6 or Month ==9 or Month == 11):
		    day_list.append(30+1)
		#闰年2月判断
		elif Month ==2 and ((Year % 4 == 0 and Year % 100 !=0 ) or Year % 400 == 0):
		    day_list.append(29+1)
		#28天情况判断
		else:
		    day_list.append(28+1)
	#print(day_list)
	return day_list

def if_moon_why ():
	try:
	    moon
	except NameError:
	    moon_exists = False
	else:
	    moon_exists = True
	try:
	    day
	except NameError:
	    day_exists = False
	else:
	    day_exists = True

def del_to_file(m):
	txt=m
	list=[]
	for i in open(txt,"r",encoding='utf-8'):
		text = i.splitlines()
		list.append(text)
	return list
		 

def save_to_file(file_name, contents):
    fh = open(file_name, 'a')
    fh.write(contents)
    fh.write('\n')
    fh.close()
def new_if_verify(n,name,fliename):
    try:
        card = n
        name = name
        apikey='b1afcf59ad5a1589'
        url0 ='https://api.muxiaoguo.cn/api/checkIdCard'
        url1='?card=' + card
        url2='&name='+name
        url3='&api_key='+apikey
        url=url0+url1+url2+url3
        r = requests.get(url,timeout=10)
        req_jason = r.json() # 获取数据
        code_trunk = req_jason['code']
        if code_trunk==200:
            if code_trunk==3301:
                print('停止半小時')
                time.sleep(1900)
                r = requests.get(url)
            jason = r.json() # 获取数据
            code_trunk = jason['code']
            #print(req_jason)
            data_trunk = jason['data']
            #print(data_trunk)
            trunk = data_trunk['check']
            if trunk=="1":
                print(trunk,name,card)
                save_to_file('yes.txt', card)
            else:
                print(trunk,name,card)
                save_to_file(fliename,card)
        elif code_trunk==-3:
            save_to_file(fliename,card)
            print('fack:%s ' % card)
    except:
            print("报错了:%s" % card)
            save_to_file(fliename,card)
def get_checkcode(m):

	s = m
	#分组
	temp = zip(s[0:17], [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2])
	temp2 = map(lambda x:int(x[0])*x[1], temp)
	temp3 = sum(temp2)
	return '10X98765432'[temp3 % 11]
def fuck(area,year,moon,day,day1_list):
	ln_list=[]
	lln_list=[]
	day_list=[]
	day_list=day1_list
	if moon == 'no':
		k1_moon=moon_why=['01','02','03','04','05','06','07','08','09','10','11','12']
	else:
		moon=str(moon)
		k1_moon=moon
	for i in k1_moon:
		for k in day_list:
			for j in range(1,k):
				j=str(j)
				j=j.zfill(2)
				i=i.zfill(2)
				ssj=i+j
				lln_list.append(ssj)

	lln_list = np.unique(lln_list)
	lln_list = lln_list.tolist()
	for j in lln_list:
		sis=area+year+j
		ln_list.append(sis)
	return ln_list
def krange(list1):
	list=[]
	for j in list1:
		for i in range(1,100):
			i =str(i)
			i = i.zfill(2)
			jk=j+i
			list.append(jk)
	return list
def jjks(listk,sex):
	#global sex_man,sex_woman,dlist,list1,man_odd_number,woman_even_mumver,ln_list,facklist
	list=[]
	dlist=[]
	if sex=='man':
		if_sex=sex_man = (1,3,5,7,9)
	elif sex=='woman':
		if_sex=sex_woman = ('0','2','4','6','8')
	else:
		if_sex=sex_all =('0','1','2','3','4','5','6','7','8','9')
	for i in listk:
		for k in if_sex:
			k=str(k)
			jmp=i+k
			dlist.append(jmp)
	for m in dlist:
		glist=get_checkcode(m)
		list.append(m+glist)
	return list
def run(fliename,name,list1):
	fliename='lishi/'+fliename+'.txt'
	if os.path.exists(fliename):
		print(color.magenta("檢測到之前掃描進度，導入"))
	else:
		txt_file=open(fliename,'w')
	data1=del_to_file(fliename)
	data2=sum(data1,[])
	for x in data2:
		list1.remove(x)
	for n in list1:
		#new_if_verify(n,name,fliename)
		pass
def xingzuo(year,pd,area):
	sdate=[20,19,21,20,21,22,23,23,23,24,23,22]
	list=[]
	list1=[]
	if pd=='byz':
		moon=[3,4]
		danan=moon_day(year,moon)
		list=diaoyong(moon,danan)
		ss=danan[0]
		ss=ss-1
		ss=ss+sdate[1]
		list=list[:ss]
		list=list[sdate[1]:]
		#print(list)
		for i in list:
			sis=area+year+i
			list1.append(sis)
	elif pd=='tpz':
		moon=[9,10]
		danan=moon_day(year,moon)
		list=diaoyong(moon,danan)
		ss=danan[0]
		ss=ss+sdate[7]
		list=list[:ss]
		list=list[sdate[5]:]
		print(list)
		for i in list:
			sis=area+year+i
			list1.append(sis)
	else:
		print(pd)
	return list1
def diaoyong(moon,danan):
	list=[]
	for i in moon:
		for j in danan:
			for k in range(1,j):
				i=str(i)
				i=i.zfill(2)
				k=str(k)
				k=k.zfill(2)
				list.append(i+k)
	list = np.unique(list)
	list = list.tolist()
	return list
	
	
	
	
	
	
	
if __name__ == '__main__':
    man()
