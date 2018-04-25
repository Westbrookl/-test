import re 
import requests
from http import cookiejar
import json
import time
from PIL import Image
from urllib import parse
from urllib import request
from urllib import *
import urllib.request
#----------------------------------------------------------
# the value that post to the server when we login in ,so we should make a data like this
	# source: None
	# redir: https://www.douban.com/people/177798601/
	# form_email: 
	# form_password: 
	# captcha-solution: hearing
	# captcha-id: i6uIA1GL8KCn1CnoZdIdnwCv:en
def make_request():

	# headers ={
	# 	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
	# 	'(KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36', 
	# 	"Host":"www.douban.com",
	# 	"Referer":""
	# }
	session = requests.Session()
	url = "https://accounts.douban.com/login"
	response1 = session.get(url)
	html = response1.text
	return html

#----------------------------------------------------------
# headers ={
# 	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
# 	'(KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36', 
# 	"Host":"www.douban.com",
# 	"Referer":""
# }
# session = requests.Session()
# #-----------------------------
# #to obtain the response's text
# url = "https://accounts.douban.com/login"
# # with request.urlopen(url) as f:
# # 	response1 = f.read()

# response1 = session.get(url)
# html = response1.text

#----------------------------

# session.cookies = cookiejar.LWPCookieJar("cookie")

# opener = request.build_opener(request.HTTPCookieProcessor)

# try:
# 	session.cookies.load(ignored_discard = True)
# except:
# 	print('cookies aren\'t load')

# def get_captcha():
# response = session.get(url,headers)


#-----------------------------------------------
# to obtain the yanzhengma
def get_code(html):
	img_url = re.search(r'<img id="captcha_image" src=(.*) alt="captcha" class="captcha_image"/>',html)
	if(img_url == None):
		return None
	else:
		img = img_url.group(1)[1:-1]
		#这里的核心是用到了urllib.urlretrieve()方法，直接将远程数据下载到本地。
		req = request.urlretrieve(img, "1.jpg")##
		im = Image.open('1.jpg')
		im.show()
		yanzheng = input("input yanzhengma:")
		return yanzheng

	# # print(html)
	# # print (img_url)
	# img = img_url.group(1)[1:-1]
	# #这里的核心是用到了urllib.urlretrieve()方法，直接将远程数据下载到本地。
	# req = request.urlretrieve(img, "1.jpg")##
	# im = Image.open('1.jpg')
	# im.show()
	# yanzheng = input("input yanzhengma:")
	# return yanzheng
#-----------------------------------------------
#-----------------------------------------------
# to obtain the captche-id
def get_id(html):
	with open("1.text",'w') as f:
		f.write(html)
	##re.search(r'<input type="hidden" name ="" value=(.*)>',string)正则表达式获得我们想要的正则表达式得到的是带""一个字符串，我们需要把字符串去掉
	img_url = re.search(r'<input type="hidden" name="captcha-id" value=(.*)/>',html)
	if img_url == None:
		return None
	else:
		img = img_url.group(1)[1:-1]
		#re.search() 得到的值处理的三种方式：1 group（0）输出所有满足正则表达式的值。2：group（1）输出第一个满足正则表达式的值
		return img
	#  img = img_url.group(1)[1:-1]
	# #re.search() 得到的值处理的三种方式：1 group（0）输出所有满足正则表达式的值。2：group（1）输出第一个满足正则表达式的值
	# return img
#-----------------------------------------------

def login(yanzheng,img,username,password):
	#----------------------------------------------
	# url = "https://accounts.douban.com/login"
	# response1 = session.get(url)
	# html = response1.text
	# print(type(html))
	# print(html)
	# img_url1 = re.search(r'<input type="hidden" name="captcha-id" value=(.*)/>',html)
	
	# img = img_url1.group(1)[1:-1]
	#--------------------------------------------------
	#----------------------------------------------------
	# print(type(html))
	# print(html)
	# img_url = re.search(r'<img id="captcha_image" src=(.*) alt="captcha" class="captcha_image"/>',html)
	# img1 = img_url.group(1)[1:-1]
	# print(img1)
	# print(img)
	# response_q = session.get(img)
	# req = request.urlretrieve(img1, "1.jpg")
	# req = request.Request(parse.urlencode(img))
	# with request.urlopen(req) as f:
	# 	content_1 = f.read()
	# # img_content = session.get(img)
	# # print(img_content.text)
	# with open("yanzhengma.gif","wb") as f:
	# 	f.write(content_1)
	# im = Image.open('1.jpg')
	# im.show()
	# yanzheng = input("input yanzhengma:")
	#----------------------------------------------------
	# login: 登录
	#----------------------------------------------------
	#without yanzhengma
# 	source: None
# redir: https://www.douban.com/people/177798601/
# form_email: 
# form_password: 
# login: 登录
	#----------------------------------------------------
	opener = request.build_opener(request.HTTPCookieProcessor)
	data={}
	if(yanzheng == None and img == None):
		data["source"] = "None"
		data["redir"] = "https://www.douban.com/people/177798601/"
		data["form_email"]= username
		data["form_password"]=password
		data["login"] = "登录"
	else:
		data["source"] = "None"
		data["redir"] = "https://www.douban.com/people/177798601/"
		data["form_email"]= username
		data["form_password"]=password
		data["captcha-solution"] = yanzheng
		data["captcha-id"] = img
		data["login"] = "登录"
	# data["source"]= "index_nav"

	url = "https://accounts.douban.com/login"
	# response1 = session.get(url)
	# html = response1.read().decode('utf-8')
	# img_url = re.match(<img id="captcha_image" src="(.+?)"  class="captcha_image"/>)

	# if img_url:

	response = opener.open(url, parse.urlencode(data).encode("utf-8"))

	# print(response.status_code)
	print(response.geturl())
	# if response.geturl() == "https://accounts.douban.com/login":
	# 	print("login error")
	# url1 = "https://www.douban.com/people/177798601/"
	# login_code = session.get(url1)
	# # session.cookies.save(ignored_discard=True,ignored_expires=True)
	# return login_code
	
def is_login():
	url1 = "https://www.douban.com/people/177798601/"
	login_code = session.get(url1)
	if not (login_code.geturl() == url):
		print(login_code.text)
		return True
	else:
		return False
if __name__ == '__main__':
	# if is_login():
	# 	print("success")
	# else:
		html = make_request()
		username = input("please input your username:")
		password = input("please input your password:")
		code1 = get_code(html)
		id1 = get_id(html)
		login(id1,code1,username,password)
		# username = input("username:")
		# password = input("password:")
		# txt = login()
		# print(txt.text)
		# if():
		# 	print('login in success')