#!/usr/bin/python
#encoding:utf-8

import urllib2
import requests


def scan(url):
    mulu= ['/dump','/trace','/logfile','/env','/actuator/','/jolokia/list','/robots.txt', '/.htaccess', '/admin', '/WEB-INF/web.xml', '/.svn/entries', '/cms', '/FCKeditor', '/fck', '/console/login/LoginForm.jsp', '/jenkins/','/%c0%ae/WEB-INF/web.xml', '/em/', '/isqlplus/', '/ws_utc/config.do', '/ws_utc/begin.do', '/jmx-console/', '/install/', '/uddiexplorer/SearchPublicRegistries.jsp', '/crossdomain.xml', '/WS_FTP.LOG', '/console/', '/fckeditor/editor/filemanager/connectors/test.html', '/.svn/all-wcprops', '/manage', '/script', '/_nodes', '/_river', '/_config', '/containers/json', '/index.jsp', '/index.html', '/Admin', '/Admin/login.jsp', '/Admin/Login.jsp', '/system', '/home','/wp-admin/includes/admin.php',
           '/wp-settings.php',
           '/phpinfo.php',
           '/admin.jsp',
           '/login.php',
           '/login.jsp',
           '/index.action',
           '/_plugin/head/',
           '/logs',
           '/solr/#/',
           '/script',
           '/info.php',
           '/phpmyadmin',
           '/phpMyAdmin',
           '/Main.aspx',
           '/login.aspx',
           '/jmx-console',
           '/web-console',
           '/zh-CN/app/Callat/home',
           '/webalizer',
		   '/ws/services',
		   '/ws/services/HelloServices?wsdl'
           ]
    header = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://'+url,
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
    print(1)
    if 'http' in url:
        url2 = url
    else:
        url2= 'http://'+url

    print(url2)
    for m in mulu:


        file = r"result.txt"
        with open(file, 'a+') as f:
            print(3)


            try:
                reponse2 = requests.get(url2+m, timeout=3, headers=header)
                print(url2+m)

                code2 = reponse2.status_code


                if 100< code2 < 305 or 400 < code2 < 403 or code2 > 499:
                    print(url2+m+'*************************'+'存活')
                    html = reponse2.text

                    f.write(url2+m+'*************'+str(html.__len__())+'\n')
                    f.close()
                else:
                    f.close()
            except:
                pass



if __name__ == "__main__":
    file1 = open('result.txt','w')
    file1.close()

    urls = open('url.txt', 'r')
    lines = urls.readlines()
    for line in lines:
        scan(line.replace('\n', ''))

    urls.close()
