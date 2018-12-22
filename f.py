from bs4 import BeautifulSoup
#import requests
import re
import urllib
import json
import timeit
from multiprocessing import Pool



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

    file=open("final.txt","a+")
    file.write(str(ActualImages)+'\n\n\n\n\n\n')
    file.close()
    return ','.join(str(ActualImages))

if __name__ ==  '__main__':
    start = timeit.default_timer()
    with open("link.txt","r") as f:
        data_links=f.readlines()
        
    with Pool(7) as p:
        records = p.map(parse, data_links)
        
    if len(records) > 0:
        with open('data_parallel.csv', 'a+') as f:
            f.write('\n'.join(records))
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
