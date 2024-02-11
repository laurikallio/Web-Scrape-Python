#!/usr/bin/env python
# coding: utf-8

# In[67]:


#import libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[92]:


#connect to website

url = 'https://www.amazon.de/Apple-iPhone-Pro-Max-256GB/dp/B0CHWZZM9M/ref=sr_1_1_sspa?crid=1CGOO97QK220L&keywords=iphone+15+pro+max&qid=1707636441&sprefix=iphpone%2Caps%2C356&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.find(id='productTitle').get_text()

price = soup2.find('span', {"class": "a-price-whole"}).get_text()

print(title)
print(price)





# In[97]:


#varovasti järjestyksen kanssa täällä!

price = price.strip()
price = price.strip(', ')
title = title.strip()
title = title.replace('(256 GB) - Titan Schwarz', 'a')
price = price.replace('.', '')

print(title)
print(price)


# In[ ]:





# In[ ]:





# In[ ]:





# In[70]:


today = datetime.date.today()

print(today)


# In[71]:


import csv

header = ['Title', 'Price', 'Date']

data = [title, price, today]

#type(data) varmista että vastaus on list

#with open('AmazonWSDataset.csv', 'w', newline='', encoding='UTF8') as f:
#    writer = csv.writer(f)
#    writer.writerow(header)
#    writer.writerow(data)


# In[76]:


import pandas as pd

df = pd.read_csv(r'C:\Users\lauri\AmazonWSDataset.csv')

print(df)


# In[75]:


#lisätään lisää dataa csv hen

with open('AmazonWSDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[99]:


def check_pric():
    url = 'https://www.amazon.de/Apple-iPhone-Pro-Max-256GB/dp/B0CHWZZM9M/ref=sr_1_1_sspa?crid=1CGOO97QK220L&keywords=iphone+15+pro+max&qid=1707636441&sprefix=iphpone%2Caps%2C356&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find('span', {"class": "a-price-whole"}).get_text()
    
    price = price.strip()
    price = price.strip(', ')
    title = title.strip()
    price = price.replace('.', '')
    
    import datetime
    
    today = datetime.date.today()
    
    import csv
    
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    with open('AmazonWSDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if(price < 1298):
        send_mail()


# In[95]:


while(True):
    check_pric()
    time.sleep(86400)


# In[96]:


import pandas as pd

df = pd.read_csv(r"C:\Users\lauri\AmazonWSDataset.csv")

print(df)


# In[100]:


def send_mail():
    server = smtplib.STMP_SSL('smtp.gmail.com', 465)
    server.ehlo()
#    server.starttls()
    server.ehlo()
    server.login('sahkoposti@gmail.com', 'xxxxxxx')
    
    subject = "The price of Iphone 15 pro max has dropped below 1299"
    body = "bla bla bla bla bal balaalfdslasaf"
    
    msg = f"subject: {subject}\n\n{body}"
    
    server.sendmail(
    'sahkoposti@gmail.com',
    msg)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




