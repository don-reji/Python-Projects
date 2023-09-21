import requests

def main(url):
    response = requests.get(url)
    if response.status_code==200:
        print('Success!')
        print('Site is up and running')
    else:
        print('Failure!')
        print('Site is down')



# url='https://www.google.com'
url=input('Enter a Url: ')
main(url)