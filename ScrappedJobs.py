
'''A program to scrap jobs from indeed and extract the details to a csv file'''
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    '''A method to request the url '''
    headers= {'User-Agent':'YourSystem'}
    url= f'https://www.indeed.com/jobs?q=Application+Support+Analyst&l=Washington,+DC&radius={page}'
    r= requests.get(url,headers)
    soup= BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    '''Function for extracting the different job details and appending those details to a list'''
    all_div= soup.find_all('div', class_='jobsearch-SerpJobCard')
    for i in all_div:
        title= i.find('a').text.strip()
        company= i.find('span', class_='company').text.strip()
        #location= i.find('span', class_='location').text.strip()
        try:
            salary=i.find('span', class_='salaryText').text.strip()
        except:
            salary=''
        summary=i.find('div', class_='summary').text.strip()    
        
        job_details={
            'title': title,
            'company': company,
            #'location': location,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job_details) #appending job details
    return

joblist=[]

for i in range(0,40,10):
    print(f'Getting page,{i}') #for checking the process
    c= extract(0)
    transform(c)
    
df= pd.DataFrame(joblist)  
print(df.head())
df.to_csv('scrapped_jobs.csv') #transforming the extracted job details to a csv file

