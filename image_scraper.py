# from bs4 import BeautifulSoup
# from urllib.request import urlopen, Request
# import urllib.request
# # import urllib.errors
# # import requests

# # use this image scraper from the location that 
# #you want to save scraped images to

# def make_soup(url):
#     address = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
#     html = urlopen(address).read()
#     # html = htmlbyte.decode('utf-8')
#     return BeautifulSoup(html)

# def get_images(url):
#     soup = make_soup(url)
#     #this makes a list of bs4 element tags
#     images = [img for img in soup.findAll('img')]
#     print (str(len(images)) + "images found.")
#     print ('Downloading images to current working directory.')
#     #compile our unicode list of image links
#     image_links = [each.get('src') for each in images]
#     for each in image_links:
#         if(not bool(each)):
#             break
            
        
#         if(each[:4] == "http"):
#             filename=each.split('/')[-1]
#             print(each)
#             urllib.request.urlretrieve(each, filename)
#         else:
#             filename=each.split('/')[-1]
#             print(url+each)
#             urllib.request.urlretrieve(url + each, filename)
#         print(each)
#     return image_links

# #a standard call looks like this
# get_images('https://icons8.com/icons/set/play-button')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
f= open("ID.txt","r")
id = int(f.read())
f.close()


html = urlopen('https://www.iconfinder.com/search/?q=play+button&from=navbar')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.png')})
for image in images[1:-1]:
    print(id , image['src']+'\n')
    filename=str(id)+".png"
    r = requests.get(image['src'], allow_redirects=True)
    open(filename, 'wb').write(r.content)
    id = id+1
    if(id == 200):
        break
f = open('ID.txt', 'w')
f.write(str(id))
f.close()
