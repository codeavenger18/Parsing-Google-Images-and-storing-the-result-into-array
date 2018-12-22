# Parsing-Google-Images-and-storing-the-result-into-array
This script will scrape google images and store link of Every image which we get from result in google image and store their link in form of array.

We have stored links which we want to scrap in link.txt.

Here for speeding our process we will use both type of multiprocessing i.e.. Pool and Process .

In f.py we are using Pool and it's scrapping 20 links and each link will generate 100 links that will be stored in final.txt and the whole process takes 70 sec where if you don't use multipocessing then it will take 20 sec for only one link

In n.py we are using Pool and it's scrapping 20 links and each link will generate 100 links that will be stored in final4.txt and the whole process takes 75 sec where if you don't use multipocessing then it will take 20 sec for only one link.

Pre-Requisite used :-

->BeautifulSoup

->multiprocessing

->urllib

->re

For Running this script you need Python 3.6 and write in your command prompt 

for f.py
 
 ->python f.py

for n.py
 
 ->python n.py
  
