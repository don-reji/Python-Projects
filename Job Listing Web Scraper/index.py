# python script to build a web scraper to scrape job listings from a fake job website using BeautifulSoup4
#  and requests library

import requests
from bs4 import BeautifulSoup   #importing necessary libraries 

# title_name=input('Enter the job role or any keyword: ')
url="https://realpython.github.io/fake-jobs/" #url to fake job listings website
response=requests.get(url)  #sending HTTP request to get response
response_parsed=BeautifulSoup(response.content,"html.parser")   #parsing the response data with html.parser
result=response_parsed.find_all('div',class_='card-content')    #variable storing all parent elements 
# containing all the child elements about job listing


for job_listing in result:  #looping each parent div element in variables

    # getting each title,company,location and link
    job_title=job_listing.find('h2')
    job_company=job_listing.find('h3')
    job_location=job_listing.find('p',class_='location')
    job_link=job_listing.find('a',class_="card-footer-item")
    

    # outputing each job,company and location. Using .text to display element text only and strip() to remove
    # unnecessary space
    print('Job Title:', job_title.text.strip())
    print('Company:', job_company.text.strip())
    print('Location:',job_location.text.strip())

    # outputing link only by targeting element link attribute href
    print("Job Link:",job_link['href'])
    print('\n')

print(input('Press enter to exit..'))


        



