import sys,os,re
from color import *
from lib.cmdline import *
from lib.fuck import *
######################################################################
#得到输入的参数进行判断
def getparameter():
    # 获取命令行所有参数
    Command = sys.argv
    # print(Command)
    Command_dict = {}
    #判断互斥参数:
    if "-xz" in Command and  "-moon" in Command :
        print(color.red("[E]Error:参数值设置错误！"))
        print(color.magenta("星座欲月不可同調用"))
        sys.exit(1)
    if "-q6" in Command and  "-fq6" in Command :
        print(color.red("[E]Error:参数值设置错误！"))
        print(color.magenta("批量當個不可同調用"))
        sys.exit(1)
    #帮助信息
    if  len(sys.argv) ==1 or "-h" in Command:
        # 输出帮助信息
        logo()
        total_menu()
        sys.exit(1)
    elif  len(sys.argv) ==1 or "-sl" in Command:
        logo()
        scan_menu()
        sys.exit(1)
    elif  len(sys.argv) ==1 or "-eh" in Command:
        # 列出所有漏洞
        help_menu()
        sys.exit(1)
    try:
        #列表每次取兩个元素
        for i in range(1, len(Command), 2):
            # print(Command[i])
            Command_dict[Command[i]] = Command[i + 1]
            #转化为字典
        return(Command_dict)
    except:
        logo()
        print(color.red("[E]Error:参数值设置错误！"))
        sys.exit(1)
    #如果参数字典为空  输出帮助
    if not Command_dict:
        logo()
        total_menu()
        sys.exit(1)
    #否则返回参数
    else:
        return Command_dict
######################################################################   
def Judgement_parameter(Command_dict):
##########################
	if "-q6" in Command_dict:
		qliu=Command_dict['-q6']
	elif "-fq6" in Command_dict:
		fqliu=Command_dict['-fq6']
	else:
		print(color.red('未获取到前六!  退出'))
		q6 = None
		sys.exit(1)
	if "-year" in Command_dict:
		year =Command_dict['-year']
	else:
		print(color.red('未获取到年!  退出'))
		year = None
		sys.exit(1)
	if "-xz" in Command_dict:
		xz =Command_dict['-xz']
		a1=xingzuo(year,xz,qliu)
		a2=krange(a1)
	else:
		print(color.red('未获取到星座!'))
		print(color.magenta("自動取消星座"))
		xz = 'no'
	if "-moon" in Command_dict:
		moon =Command_dict['-moon']
		s1=moon_day(year,moon)
	else:
		print(color.red('未获取到月!'))
		print(color.magenta("自動本年所有月"))
		moon = 'no'
		s1=moon_day(year,moon)
	if "-day" in Command_dict:
		day =Command_dict['-day']
		s2=fuck(qliu,year,moon,day,s1)
		s3=krange(s2)
	else:
		print(color.red('未获取到日!'))
		print(color.magenta("自動本月所有日"))
		day = 'all'
		s2=fuck(qliu,year,moon,day,s1)
		s3=krange(s2)
	if "-sex" in Command_dict:
		sex =Command_dict['-sex']
		if xz=='no':
			s4=jjks(s3,sex)
		else:
			s4=jjks(a2,sex)
	else:
		print(color.red('未获取到性別!'))
		print(color.magenta("自動男女全選"))
		sex = all
	fliename=qliu+year+moon+day
	if "-name" in Command_dict:
		name =Command_dict['-name']
		s5=run(fliename,name,s4)
		print(s5)
	else:
		print(color.red('未获取到名字! 退出'))
		name = None
		sys.exit(1)	

######################################################################

