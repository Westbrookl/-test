from urllib import request
with request.urlopen('http://tieba.baidu.com/p/741081023') as f:
	s = f.read()
	print(s)
