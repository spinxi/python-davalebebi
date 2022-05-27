
import urllib.request, os
import requests 
from bs4 import BeautifulSoup 
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("http://www.heraldika.ge/index.php?m=85&p_news=1") 
soup = BeautifulSoup(htmldata, 'html.parser') 
select = soup.select("#trueContainer ul li a img")
download_url = 'http://www.heraldika.ge/'
for item in select:
    img_real_name = item.get('src')
    download_img_link = download_url + img_real_name
    img_replaced = item.get('src').replace('.', '/')
    img_format = str(img_replaced.split('/')[-1])
    img_name = str(img_replaced.split('/')[-2])
    print("downloading {}".format(img_name))
    urllib.request.urlretrieve(download_img_link, img_name+'.'+img_format)