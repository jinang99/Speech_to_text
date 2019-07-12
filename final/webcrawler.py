import mechanize
from bs4 import BeautifulSoup
import requests
import os


#Webcrawler to upload the .txt file to the LM Tool and download the necessary files required for the model.
br = mechanize.Browser()
flag = 0
br.set_handle_robots(False)
filename = './etc/final.txt'
br.addheaders = [('User-agent','Chrome')]
while True:
	try:
		br.open('http://www.speech.cs.cmu.edu/tools/lmtool-new.html')
		break
	except:
		print("Connection not established")

	
for f in br.forms():
	    print(f)
br.select_form(nr=0)
br.form.add_file(open(filename), 'text/plain', filename)

data = br.submit()
print(data)


soup = BeautifulSoup(data.read(),'html.parser')


urls_list = soup.find_all('a')
print(urls_list)

link = urls_list[0]['href']
link = link[:-11]
link    

new_url_list = []
new_url_list.append(link+urls_list[4]['href'])
new_url_list.append(link+urls_list[5]['href'])
new_url_list.append(link+urls_list[7]['href'])
print(new_url_list)

file = requests.get(new_url_list[0])
with open('./etc/final.dic','wb') as f:
	    f.write(file.content)

file = requests.get(new_url_list[1])
with open('./etc/final.lm.DMP','wb') as f:
	    f.write(file.content)

file = requests.get(new_url_list[2])
with open('./etc/final.transcription','wb') as f:
	    f.write(file.content)

	    






