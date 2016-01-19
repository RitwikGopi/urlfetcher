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
	s_[s[url]] = url
	s[url].connect((url,80))
	f[s[url]] = open(url+'.html','w')
	requests[url] = request+url+'\n\n'
	s[url].send(requests[url])
i = s.values()
while i != []:
	r = select.select(i,[],[])
	#print r[0]
	for url in r[0]:
		result = url.recv(1024)
		if len(result) > 0:
			f[url].write(result)
		else:
			i.remove(url)
	#print i
