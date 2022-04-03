import sys
from color import *

def total_menu():
	usage = '''
    All:  
    POC Mode:
	-xz                      選擇星座
	-year                    選擇年
	-moon                    選擇月
	-day                     選擇天
	-sex                     選擇性別
	-name                    選擇名字
	-q6                      身份證前六位
	-fq6                     批量身份證前六位
    Example:
        python3 control.py -u http://example.com -e thinkphp
        python3 control.py -u http://example.com -s all
        python3 control.py -f list.txt -txt results.txt
    --------------------------------------------------------------
    tolerance  %s         Blog:xxxx
    ''' 
	print(color.purple(usage))
def help_menu():
    help_menu='''
    sdfasfadsf
    '''
    print(color.purple(help_menu))
    
def scan_menu():
    scan_menu='''
    -s:
        all         All POC tests            所有部件掃描(默认)
        C           Use poc name             C段掃描
        icp                                  备案查詢
        ip                                   ip地址所在地
        os                                   操作系統識別
        port                                 端口掃描
        shoulu                               網站收錄情況
        web                                  web信息識別
        whois                                whois信息查詢
        whatcms                              指纹识别
        webside                              旁站查询
        record                               备案查询
        CDN                                  CDN查询

    '''
    print(color.purple(scan_menu))
    
def logo():
	logo = ('''
                             ██                    ██
                            ░██                   ░██
  █████   ██████  ███████  ██████ ██████  ██████  ░██
 ██░░░██ ██░░░░██░░██░░░██░░░██░ ░░██░░█ ██░░░░██ ░██
░██  ░░ ░██   ░██ ░██  ░██  ░██   ░██ ░ ░██   ░██ ░██
░██   ██░██   ░██ ░██  ░██  ░██   ░██   ░██   ░██ ░██
░░█████ ░░██████  ███  ░██  ░░██ ░███   ░░██████  ███
 ░░░░░   ░░░░░░  ░░░   ░░    ░░  ░░░     ░░░░░░  ░░░                                                            
''')  
	print(color.ccyan(logo))
    
    
    
    
    
