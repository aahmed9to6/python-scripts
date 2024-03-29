import sys
import re
from urllib2 import urlopen as uo
from bs4 import BeautifulSoup as soup
import os.path

if len(sys.argv) > 1:
	my_url = sys.argv[1]
else:
	my_url = "https://gaana.com/playlist/abdullahahmed-bxhwz-todo-jkrmd4wjb6"
print my_url
uclient = uo(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"lastend-container details-list-paddingnone content-container artworkload"})
contain = containers[0]
song = contain.findAll("div",{"class":"track_npqitemdetail"})

playlist = page_soup.findAll("div",{"class":"_d_t_det _d_tp_det"})
playlist[0].h1.text
try:
	os.mkdir(playlist[0].h1.text)
except Exception:
	pass
os.chdir(playlist[0].h1.text)

filename = playlist[0].h1.text + ".csv"
fcsv = open(filename, "w")
headers = "name, searchLink, url, status\n"
fcsv.write(headers)
for s in song:
	try:
		title = s.h2.text.replace(","," and ").strip()
		artist = s.p.text.split("-")[1].strip()
		movie = s.p.text.split("-")[0].strip()
		name = movie + " - " + title
		link = "http://mymp3song.site/files/search/sort/download/find/" + title.replace(" ",'+')
		uclient = uo(link)
		page_html = uclient.read()
		uclient.close()
		mymp3 = soup(page_html, "html.parser")
		maindiv = mymp3.findAll("div",{"id":"mainDiv"})
		md = maindiv[0]
		song_list = md.findAll("a",{"class":"fileName"})
		for ss in song_list:
			p = ss.findAll(text=re.compile(title,re.IGNORECASE))
			if p:
				d_page = "http://mymp3song.site" + ss['href']
				#print "d_page is " + d_page
				break
		uclient = uo(d_page)
		page_html = uclient.read()
		uclient.close()
		dl_page = soup(page_html, "html.parser")

		dl = dl_page.findAll("div",{"class":"fi"})
		url = "http://mymp3song.site" + dl[0].a['href']
		url = url.replace("type/128",'type/320')		
		fcsv.write(name + "," + link + "," + url)
		file_name = name + ".mp3"
		u = uo(url)
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		print "Downloading: %s Bytes: %s" % (file_name, file_size)

		# file_size_dl = 0
		# block_sz = 8192
		# while True:
		#     buffer = u.read(block_sz)
		#     if not buffer:
		#         break

		#     file_size_dl += len(buffer)
		#     f.write(buffer)
		#     # status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		#     # status = status + chr(8)*(len(status)+1)
		# print "Downloaded" + "\n"
		fcsv.write(",Downloaded\n")
		del d_page
	except Exception:
		fcsv.write("\n")
		pass
fcsv.close()
