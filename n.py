from bs4 import BeautifulSoup
#import requests
import re
import urllib
import json
import timeit
from multiprocessing import Pool
import multiprocessing

start = timeit.default_timer()

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

def parse(url):
    soup = get_soup(url,header)
    print(url+'\n\n')
    ActualImages=[]# contains the link for Large original images, type of  image

    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))


    print  ("there are total" , len(ActualImages),"images")

    file=open("final4.txt","a+")
    file.write(str(ActualImages)+'\n\n\n\n\n\n')
    file.close()

with open("link.txt","r") as f:
    data_links=f.readlines()
    
if __name__ == '__main__':
    processes = []
    for i in data_links:
        p = multiprocessing.Process(target=parse, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
stop = timeit.default_timer()
print('Time: ', stop - start)  
