import socket
import select
request = "GET / HTTP/1.1\nHost: "
url_list = ["campusinsight.in","gectcr.ac.in","watch8now.me","universityofcalicut.info","hyperboria.net"]
s = {}
s_ = {}
f = {}
requests = {}
for url in url_list:
	s[url] = (socket.socket(socket.AF_INET, socket.SOCK_STREAM))
	s[url].setblocking(False)
	s_[s[url]] = [0,url]
	f[s[url]] = open(url+'.html','w')
	requests[s[url]] = request+url+'\n\n'
	#s[url].connect((url,80))
	#s[url].send(requests[s[url]])
i = s.values()
i_ = i[:]
for url in url_list:
	try:
		s[url].connect((url,80))
	except:
		pass
while i != []:
	r = select.select(i,i_,[])
	#print r[0]
	for url in r[1]:
		if s_[url][0] == 0:
			print s_[url][1] , 'connected'
			s_[url][0] = 1
			i_.remove(url)
			url.send(requests[url])	
	for url in r[0]:
		if s_[url][0] == 1:
			result = url.recv(1024)
			if len(result) > 0:
				f[url].write(result)
			else:
				i.remove(url)
				print s_[url][1], 'finished'
				f[url].close()

	#print i
